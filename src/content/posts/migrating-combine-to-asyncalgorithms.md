---
title: "Migrating Combine to AsyncAlgorithms"
date: 2025-05-12T13:48:58Z
category: reading
author: "Jacob Bartlett"
description: "这篇文章的核心判断是：如果你还在用 Combine，最值得迁移的不是一次性清空实现细节，而是先把公开接口换成 Swift Concurrency / AsyncAlgorithms 能直接消费的 AsyncSequence 语义。这样既能保留存量 Combine 代码作为仓库内部实现，又能让上层 view mod..."
source: "https://blog.jacobstechtavern.com/p/migrating-combine-to-asyncalgorithms"
---

## TL;DR
这篇文章的核心判断是：如果你还在用 Combine，最值得迁移的不是一次性清空实现细节，而是先把公开接口换成 Swift Concurrency / AsyncAlgorithms 能直接消费的 AsyncSequence 语义。这样既能保留存量 Combine 代码作为仓库内部实现，又能让上层 view model 用更直观的 for-await-in、@MainActor 和 async task 组织数据流，减少心智负担与未来维护成本。

## 关键洞察
作者用三个典型场景说明迁移方法。第一类是多数据源合并通知数：仓库层先把 CurrentValueSubject 私有化，再通过 publisher.values 暴露成 AsyncPublisher，让 Combine 退到实现细节；消费层把 combineLatest 从 publisher 操作改成对两个 AsyncSequence 做 combineLatest(...) 后再 map，原本的 .receive(on: RunLoop.main) 则直接由 @MainActor 吸收。迁移后的关键变化不是功能，而是值流的处理模型：从 sink 回调转成顺序化的异步迭代，代码读起来更像普通控制流。

第二类是高频进度更新：原来用 PassthroughSubject 承接回调式下载进度，再 throttle 后喂给 UI；迁移后仓库层直接用 AsyncStream 包装回调 API，把 subject.send(value) 改成 continuation.yield(value)，view model 再对 stream 做 ._throttle(...) 并在 for-await-in 中更新状态。这里最重要的不是 API 名字几乎一一对应，而是 AsyncStream 让“把 callback 桥接成可组合的异步序列”成为一等做法，下载、传感器、delegate 回调之类场景都能沿这个思路处理。

第三类是单对象加载与错误传播：原来的 CurrentValueSubject<User?, Error> 被换成 AsyncThrowingChannel，send(completion: .failure(error)) 变成更直接的 fail(error)，消费端则从 sink(receiveCompletion:receiveValue:) 变成 do/catch 包裹的 for try await。作者顺手指出 compactMap 的迁移并不神秘，直接用 .compacted() 即可。更大的价值在于错误流、主线程约束与值处理都回到 Swift Concurrency 自己的语法体系里，不再被 Combine 的专用操作符语法切开。

但作者也没有把 AsyncAlgorithms 神化。AsyncChannel 更像 PassthroughSubject，不像 CurrentValueSubject 那样天然缓存最新值；因此如果你依赖“后来订阅者立刻拿到最近状态”的语义，迁移后会失去这层便利。更关键的是，当前 AsyncSequence / AsyncStream 不适合天然广播给多个并发消费者：多个 for-await-in 共享同一序列会遇到迭代器层面的限制，做共享仓库时这是实打实的架构约束。作者因此给出的真实建议不是“马上把 Combine 全删掉”，而是优先迁移公开接口，让新代码建立在未来仍会演进的并发模型上，把旧 Combine 留在仓库内部，等生态补上缓存与广播能力后再进一步收缩。

## 一句话总结
最稳妥的迁移路径不是把 Combine 逐操作符翻译成 AsyncAlgorithms，而是先把系统边界改成 AsyncSequence，让并发模型先统一，存量 Combine 再慢慢退居内部实现。
