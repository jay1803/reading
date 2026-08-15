---
title: "Handle Deep Links with Async Algorithms"
date: 2025-05-12T13:44:17Z
category: reading
description: "用 AsyncChannel 的 back pressure 特性做深链路由，每个路由独享一个 channel——看似绕路，实则直接暴露了 Async Algorithms 至今无法广播的根本缺陷；这个框架在深链场景上恰好够用，但设计天花板清晰可见。"
source: "https://blog.jacobstechtavern.com/p/deep-links-with-async-algorithms"
---

## TL;DR
用 AsyncChannel 的 back pressure 特性做深链路由，每个路由独享一个 channel——看似绕路，实则直接暴露了 Async Algorithms 至今无法广播的根本缺陷；这个框架在深链场景上恰好够用，但设计天花板清晰可见。

## 核心洞见
深链的核心张力：SceneDelegate 是入口，各 Coordinator 才是消费者，两者跨越生命周期边界。AsyncChannel 的 back pressure（消费者调用 next() 前不推送下一个值）保证路由事件不会丢失；用 `merge()` 将同一 Coordinator 的多个 channel 合并进单个 `for-await-in`，比 withTaskGroup 线性得多。

## 具体机制
- `DeepLink` 枚举用 NSRegularExpression 把 URL 字符串映射为 case（自定义 `~=` infix operator）。
- `DeepLinkHandlerImpl` 为每个 case 维护一个私有 `AsyncChannel<DeepLink>`；`open(url:)` 解析后向对应 channel 发值，`stream(link:)` 返回该 channel 供 Coordinator 订阅。
- 每个 Coordinator 在 `init` 中启动 `Task { await handleDeepLinks() }`；用 `merge(stream(.a), stream(.b))` 合并同属该 Coordinator 的多条路由，导航调用加 `await` 确保切回主线程。
- 三条入口：冷启动走 `willConnectTo` 的 `connectionOptions.urlContexts`；已活跃走 `openURLContexts`；Universal Link 走 `continue userActivity`；纯 SwiftUI 用 `.onOpenURL` modifier。

## 隐藏限制
AsyncChannel 的迭代器不支持多消费者并发调用 `next()`——无广播能力。同一 channel 若在两处 for-await-in，只有最后启动的监听者能收到值；这意味着每个路由只能有单一消费者，"多模块同时响应同一深链"在 Async Algorithms 现有设计下无法实现。最难 debug 的陷阱：Factory 依赖注入未设 `.scope(.singleton)`，SceneDelegate 和 Coordinator 拿到不同实例，open() 和 stream() 完全断连——表现为"只有最后一个 tab 的深链有效"，修复只需半行代码。

## 收束
Combine 的 PassthroughSubject 广播对 Async Algorithms 至今是奢望。这个框架的选择是"安全的单消费者"而非"灵活的多订阅"——深链场景恰好合适，但不要对它有更多期待。
