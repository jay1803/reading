---
title: "Advanced Swift Actors: Re-entrancy & Interleaving"
date: 2025-05-12T13:49:57Z
category: reading
author: "Jacob Bartlett"
description: "Actor 的\"可重入性\"（re-entrancy）不是 bug，而是可以主动利用的机制：在 ~await~ 挂起点期间，其他调用可以插入同一 actor，从而让多个并发调用共享同一个底层任务结果，而无需任何锁。"
source: "https://blog.jacobstechtavern.com/p/advanced-swift-actors-re-entrancy"
---

## TL;DR
Actor 的"可重入性"（re-entrancy）不是 bug，而是可以主动利用的机制：在 ~await~ 挂起点期间，其他调用可以插入同一 actor，从而让多个并发调用共享同一个底层任务结果，而无需任何锁。

## 核心洞见
Actor 的 ~SerialExecutor~ 保证同一时刻只有一段代码在执行，但 ~async~ 方法的 ~await~ 点会释放执行权，允许其他工作入队。这意味着"actor 内部绝对没有并发"的直觉是错的——准确说法是"actor 内部没有同步并发"，异步交叉（interleaving）仍然会发生。

## 具体机制
将一个 ~Task~ 存为 actor 的属性，是解决重复网络请求的关键模式：
- 第一个调用发现 ~tokenTask == nil~，创建 Task 并 ~await~ 其 ~.value~（挂起点）。
- 后续并发调用进入时，发现 ~tokenTask~ 已存在，直接跳过创建，同样 ~await~ 同一个 Task 的 ~.value~。
- 所有调用共享同一次网络刷新，Task 完成后其 ~.value~ 可被反复读取而不重新执行。
- ~defer { tokenTask = nil }~ 在函数退出时重置，让下一轮请求可以新建 Task，但并发持有者已通过挂起点缓存了 Task 引用，因此不会 crash。

## 隐藏限制
这个模式假设"刷新一次 token 对所有并发调用都有效"——若 token 在刷新过程中被第三方 revoke，第二个挂起的调用拿到的仍然是同一个失败结果。另外，~defer~ 在 ~async~ 上下文中执行时序依赖 actor 的 re-entrancy 行为，若对 Swift 并发模型不熟悉，维护者很容易误改。

## 边缘判断
这篇文章真正有价值的地方不是 "actor 防数据竞争"（这是显然的），而是展示了如何利用 re-entrancy **消除重复异步工作**——这个用法在文档里几乎看不到。
