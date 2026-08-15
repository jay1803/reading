---
title: "A Tool To Automatically Detect Memory Leaks"
date: 2026-03-22T02:00:30Z
category: reading
description: "检测内存泄漏的有效性反转：与其在 deinit 监听\"某对象消失了没有\"（检测缺席），不如在 init 检测\"同类实例是否超额存活\"（检测过剩）——前者在日常工作流里极易漏掉，后者自动触发、无法回避。"
source: "https://blog.jacobstechtavern.com/p/automatically-detect-memory-leaks"
---

## TL;DR
检测内存泄漏的有效性反转：与其在 `deinit` 监听"某对象消失了没有"（检测缺席），不如在 `init` 检测"同类实例是否超额存活"（检测过剩）——前者在日常工作流里极易漏掉，后者自动触发、无法回避。

## 核心洞见
Retain cycle 的结构决定了泄漏会以"实例数量堆积"而非"单次 deinit 缺失"的方式暴露。用弱引用记录每个类的存活实例数，`init` 时一旦超过 `maxInstances` 就 `assert` 崩溃——比在 `deinit` 里手写 `print` 可靠一个量级。弱引用的关键特性：它能观察对象生命周期，但不影响生命周期。

## 具体机制
三层结构：

- **`WeakRef`**：包裹 `weak var ref: AnyObject?`，提供 `isDeallocated: Bool`。
- **`WeakRefStore`**：持有 `[WeakRef]` 数组，每次调用 `numberOfLiveInstances(including:)` 时：追加新引用 → 过滤已释放条目 → 返回存活数量。自清理设计无需外部维护。
- **`LeakDetector` 单例**：以 `String(describing: instance)`（即类名）为键，维护 `[String: WeakRefStore]` 字典。`BaseViewModel.init()` 调用 `LeakDetector.shared.check(self)`，所有继承屏自动获得检测，零侵入。
- 触发方式：超过 `maxInstances` 时 `assert` 崩溃（仅 `#if DEBUG`）；Swift 6 下将字典替换为 `Mutex` 保证线程安全。

## 隐藏限制
仅覆盖继承自 `BaseViewModel`（UIKit 下为 `BaseViewController`）的页面级对象。Services、models、navigation 逻辑、并发闭包中的泄漏一概不受保护。检测范围边界完全取决于开发者手动扩展 `LeakDetectable` 协议——文章将此留为"读者练习"，但这意味着最常见的跨层引用泄漏实际上未被捕获。

## 一把锁锁不住所有门
最简洁的调试工具往往建立在最朴素的原语上：计数 + 弱引用。但"朴素"也是边界——它只在你已经知道该在哪里放探针时才有效。
