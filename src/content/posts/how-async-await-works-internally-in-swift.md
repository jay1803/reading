---
title: "How async/await works internally in Swift"
date: 2025-06-24T10:44:51Z
category: reading
description: "结论先说：这篇文章的核心不是教你“怎么用” async/await，而是拆解它如何通过编译器 + 运行时 + 执行器体系，从根上重构 Swift 的并发模型，把“内存安全”扩展到“并发安全”，但同时引入了新的复杂性与思维负担。"
source: "https://swiftrocks.com/how-async-await-works-internally-in-swift"
---

## TL;DR
结论先说：这篇文章的核心不是教你“怎么用” async/await，而是拆解它如何通过编译器 + 运行时 + 执行器体系，从根上重构 Swift 的并发模型，把“内存安全”扩展到“并发安全”，但同时引入了新的复杂性与思维负担。

第一部分：为什么 Swift 必须引入 async/await

Swift 的初心是消灭 undefined behavior。数组越界会 crash，但行为可预测，这是“受控失败”。
问题在于——并发长期是 Swift 的盲区。

GCD 是 C 库，不在编译器控制范围内。
因此数据竞争、死锁、优先级反转、线程爆炸，编译器无能为力。

Chris Lattner 在 2017 年的 Swift Concurrency Manifesto 中明确目标：
让并发成为语言级能力，而不是库级能力。

引入 async/await 的根本目的并不是语法优雅，而是：

- 编译器可理解执行上下文
- 可追踪任务结构
- 可在编译期阻止数据竞争

第二部分：底层核心机制

1）Cooperative Thread Pool（协作线程池）

async/await 仍然基于 libdispatch，但不再使用传统 DispatchQueue。

使用的是固定线程数（等于 CPU 核数）的协作线程池。
目的是：

- 避免线程爆炸
- 保证 forward progress
- 提高调度效率

这意味着：线程是稀缺资源。阻塞会饿死线程池。

Gotcha：
你不能在 async 中做长时间阻塞操作。

2）Executors（执行器）

线程池只是“执行者”。
真正管理任务的是 Executor。

Swift 内置两种：

- Global Concurrent Executor（默认，全局并发）
- Default Actor Executor（串行）

Executor 的职责：

- 接收 Job
- 将 Job 投递到线程池

重点理解：

async 并不是“开新线程”。
它只是把任务交给 executor。

3）Execution Context & hop_to_executor

编译后 SIL 中会出现 hop_to_executor。

它的作用：

- 检查当前执行上下文
- 若目标 executor 不同 → 创建 suspension point
- 当前函数释放线程
- 任务变成 Job
- 投递给目标 executor

核心洞察：

await 只是“潜在挂起点”。

如果当前就在目标 executor 上，就不会真正挂起。

这比 GCD 更智能。

第三部分：Suspension & Reentrancy

async 函数可以：

- 释放线程
- 保存自身状态
- 等待完成
- 再恢复执行

这解决了死锁问题。
因为线程不会被阻塞。

但代价是 Reentrancy。

在 await 期间：

- 当前 executor 可能去执行其他任务
- Actor 状态可能发生变化
- 恢复时世界已不同

所以：

不要跨 suspension point 假设状态不变。

这是 Swift 并发最大的思维陷阱。

第四部分：Task 与 Structured Concurrency

async 的入口是 Task。

Task 会：

- 创建 AsyncTask
- 继承父任务上下文
- 提交给 executor

Swift 运行时维护一个任务树结构：

- 父子关系
- 优先级传播
- 取消传播

这叫 Structured Concurrency。

Gotcha：

Task {} 默认是“子任务”，会继承：

- executor
- 优先级
- task local values

如果你想完全独立，必须用 Task.detached。

第五部分：Actors —— 数据竞争的解决方案

Actor 是语言级隔离机制。

本质：

- 每个 actor 绑定一个串行 executor
- 外部访问必须 await
- 编译器阻止共享可变状态泄漏

底层：

actor 编译成 class + SerialExecutor。

访问 actor 方法时：

hop_to_executor 指向 actor 的 executor。

效果：

同一 actor 的任务串行执行。

这防止数据竞争。

但不防逻辑错误。

Actor Reentrancy：

在 await 期间，其他任务可插队执行。

状态可能被改变。

因此：

actor ≠ 自动线程安全逻辑
你仍然必须设计状态流。

第六部分：Sendable 与 nonisolated

因为 actor 隔离：

必须定义什么可以“离开 actor”。

Sendable：

- value type
- final immutable class
- actor
- @Sendable closure

它是编译器标记机制。

Gotcha：

Sendable 具有“传染性”。

一旦某个 API 需要 Sendable，整个调用链可能都要改。

nonisolated：

允许跳过 actor 隔离。

但只能用于 Sendable 类型。

第七部分：MainActor

UI 必须在主线程。

MainActor 是一个特殊 global actor。

它的 executor 会：

将 job 投递到 dispatch_get_main_queue()

@MainActor 本质是：

编译期插入 hop_to_executor(MainActor.shared)

并且如果已经在主线程，不会真的 dispatch。

总结：async/await 改变了什么？

它解决了：

- 线程爆炸
- 优先级反转
- 数据竞争（通过 actor）
- 死锁（通过挂起而非阻塞）

但它引入了：

- Reentrancy 复杂性
- Task 继承陷阱
- Sendable 污染
- Actor 状态设计难题

最终结论

Swift 的 async/await 让并发“更简单”，
但没有让并发“更容易”。

它把错误从“运行时灾难”变成“设计阶段错误”。

如果你写的是 Dot 这种强调状态一致性与数据流正确性的产品（尤其是你已经在用 SwiftUI + async 数据流），你真正需要思考的是：

- 哪些状态属于 actor
- 哪些 API 需要 MainActor
- 是否跨 suspension point 持有旧状态
- Task 是否无意继承执行上下文

async/await 是安全系统。
但安全系统从来不会替你思考架构。

如果你愿意，我可以帮你画一张“Swift 并发运行时完整心智模型图”，用系统图形式把 thread pool、executor、task、actor 全部串起来。
