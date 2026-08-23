---
title: "Tasks vs Threads"
date: 2025-05-12T13:43:58Z
category: reading
author: "Jacob Bartlett"
description: "Thread 与 Task 的 API 设计高度镜像——sleep / cancel / priority / 本地存储都有对应物——但它们运行在完全不同的抽象层：Thread 是内核级实体，每个占 512kB 调用栈，切换代价高；Task 是 Swift Runtime 管理的轻量执行单元，状态存在 conti..."
source: "https://blog.jacobstechtavern.com/p/tasks-vs-threads"
---

## TL;DR
Thread 与 Task 的 API 设计高度镜像——sleep / cancel / priority / 本地存储都有对应物——但它们运行在完全不同的抽象层：Thread 是内核级实体，每个占 512kB 调用栈，切换代价高；Task 是 Swift Runtime 管理的轻量执行单元，状态存在 continuation 里，调度在 Cooperative Thread Pool 上，目标是 1 线程/CPU 核。

## 核心洞见
Thread 和 Task 的核心差距不是功能，而是代价模型。Thread 的 sleep 阻塞线程，OS 做上下文切换，开销不可避免；Task 的 sleep 让出执行权但不阻塞线程，Runtime 可以在同一线程上继续调度其他 Task。优先级在 Thread 上是 0.0–1.0 的浮点数映射到内核整数（Darwin 上是 0–63）；Task 的 priority 是给 executor 的"建议"，且 executor 会自动提升优先级（priority elevation）来避免低优先级任务堵塞高优先级任务（priority inversion）。

## 具体机制
- **Thread 需要手动 `start()`**，底层会创建 pthread 并执行 `main()`；Task 创建即调度，但调度≠立即执行。
- **取消语义不同**：`thread.cancel()` 是外部信号，不保证停止；Task 的取消是 cooperative 的——必须主动检查 `Task.isCancelled` 或 `Task.checkCancellation()`，否则代码照跑。这是故意设计，防止中间状态损坏。
- **Task-local values** 比 `threadDictionary` 更结构化：通过 `@TaskLocal` 声明，用 `.withValue` 作用域绑定，子 Task 自动继承，退出 scope 后恢复旧值。
- **跳主线程**：Thread 没有内置机制，必须借 GCD（`DispatchQueue.main.async`）；Task 用 `await MainActor.run` 或 `Task { @MainActor in … }`。

## 隐藏限制
- Task 的 priority 映射与 GCD 的 QoS 并不直觉对应（`.userInitiated` = `.high`，`.utility` = `.low`，无 `.medium` 别名），迁移代码时易踩坑。
- 子 Task 不自动继承父 Task 的取消——"嵌套 Task" 不等于结构化并发，需要用 `async let` 或 TaskGroup 才能保证传播。文章提到这点但没给具体示例。**值得质疑**：文章在这个关键点上点到即止，建议另查 SE-0304。
- Thread 独有的 `callStackSymbols` 在 Swift Concurrency 没有对等物——这正是 Crashlytics 等工具底层仍用 Thread 的原因之一。

## 低级 API 不是天才专属
真正的门槛不是理解难度，而是认知错位：用"低级=危险"的直觉屏蔽了可以直接对照学习的知识。Task 的设计几乎照搬了 Thread API 的形状，只是把调度代价从 OS 转移到了 Runtime。
