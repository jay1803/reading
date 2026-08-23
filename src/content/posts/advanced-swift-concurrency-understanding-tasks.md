---
title: "Advanced Swift Concurrency: Understanding Tasks"
date: 2025-05-12T13:48:41Z
category: reading
author: "Jacob Bartlett"
description: "Task 优先级映射与直觉相反（.background 低于 .low，.userInitiated 才等于 .high），Swift 协作式取消（cooperative cancellation）不会立即停止工作，必须手动检查 Task.isCancelled——这两点是大多数并发 bug 的根源。"
source: "https://blog.jacobstechtavern.com/p/advanced-swift-concurrency"
---

## TL;DR
Task 优先级映射与直觉相反（`.background` 低于 `.low`，`.userInitiated` 才等于 `.high`），Swift 协作式取消（cooperative cancellation）不会立即停止工作，必须手动检查 `Task.isCancelled`——这两点是大多数并发 bug 的根源。

## 核心机制

**优先级陷阱：** `.userInitiated = .high`，`.utility = .low`，`.background` 甚至低于 `.low`；`.medium` 没有别名。直接用 `rawValue` 构造优先级会崩溃。

**协作式取消的含义：** `.cancel()` 只是设置标志，不中断执行流。代码必须在循环或异步点主动调用 `guard !Task.isCancelled else { return }`，否则 cancel 形同虚设。

**存储 Task 引用用于可控取消：** 把 `Task<Void, Never>` 存为实例属性，每次重新触发时先 `.cancel()` 旧任务再创建新任务——文中的 `coolModelCacheTask` 模式（5分钟无使用后清理 ML 模型缓存）是这个模式的典型应用。

**`Task.yield()`：** 在大量同步 CPU 密集工作（如批量图像分类）中插入 `await Task.yield()`，把主 actor 执行权让给其他任务，防止 UI 卡顿。注意它只在主 actor 上下文或长同步循环中有意义。

**`withThrowingTaskGroup` 实现超时：** 用两个子任务竞速——一个执行真实请求，一个 `Task.sleep` 到超时后 throw——`group.next()` 取第一个完成的结果，然后 `group.cancelAll()` 清理另一个。

## 值得质疑
文章断言"模型缓存 + 定时清理"是记忆与计算的最优平衡，但未给出 benchmark 数据；实际阈值（5 分钟）是经验值，并非推导结论。

## 留下的那个想法
协作式取消要求在每个"可取消点"手动检查标志——这意味着并发安全的责任从运行时转移到了开发者身上，Swift Concurrency 并没有替你消除竞态，只是让竞态更可见。
