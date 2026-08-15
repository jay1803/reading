---
title: "The Synchronization Framework in Swift 6"
date: 2025-05-12T13:47:13Z
category: reading
description: "Mutex 的实际性能比 Actor 快 25%（在高竞争的缓存场景），比 Atomic 快约一倍——而 Mutex 底层就是 ~os_unfair_lock~，和 ~OSAllocatedUnfairLock~ 几乎一致；所谓\"新原语更快\"的直觉在 10M 操作量级下基本不成立。"
source: "https://blog.jacobstechtavern.com/p/the-synchronisation-framework"
---

## TL;DR
Mutex 的实际性能比 Actor 快 25%（在高竞争的缓存场景），比 Atomic 快约一倍——而 Mutex 底层就是 ~os_unfair_lock~，和 ~OSAllocatedUnfairLock~ 几乎一致；所谓"新原语更快"的直觉在 10M 操作量级下基本不成立。

## 核心洞见
- ~Mutex~ 与 ~Atomic~ 之所以到 Swift 6 才能引入，依赖的是 *generic ownership*（~Value: ~Copyable~ 的负约束）：~Mutex~ 允许包裹任意可/不可复制类型，~Atomic~ 要求 ~AtomicRepresentable~。
- ~Mutex~ 的关键 API 是 ~withLock~ 闭包（不支持递归调用，否则 crash）；~withLockIfAvailable~ 则在已锁定时返回 ~nil~ 而不阻塞。
- ~Atomic~ 的 ~ordering~ 参数（relaxed → acquiring → releasing → acq-rel → seq-cst）控制内存同步强度，但在简单算术场景下，五种 ordering 之间的速度差可忽略不计。

## 具体机制
基准测试（10M 操作，多核 taskGroup，Apple 硬件）：

| 场景         | Mutex  | Actor  | Lock (OSAllocatedUnfairLock) | Atomic (relaxed) |
|--------------+--------+--------+------------------------------+------------------|
| 缓存写入     | 6.33s  | 8.32s  | 4.42s                        | —                |
| 计数器递增   | 3.65s  | 7.51s  | —                            | 7.77s            |

~OSAllocatedUnfairLock~ 在缓存场景中比 ~Mutex~ 更快，原因是 Mutex 底层即为 ~os_unfair_lock~，但多了 Swift 封装层开销。

## 隐藏限制
Actor 是"安全默认"：Swift Concurrency 保证所有线程前向推进（无死锁），而 Mutex 会阻塞线程；Actor 的 ~await~ 挂起点也可能成为重入陷阱（re-entrancy mines）。Atomic 的适用场景被官方明确定位为"系统级代码与库作者"——日常 app 开发中几乎不需要直接使用。

## 留下的想法
benchmark 的可信度本身就是个问题：原版测试用了 10M 个独立 taskGroup task，大量运行时耗在并发调度开销而非锁上；修正后结果才更可信。文章建议"profile your damn code"，但自身的基准设计缺陷到修正前都没被捕捉到——这恰好说明并发性能测试比写并发代码本身更难。
