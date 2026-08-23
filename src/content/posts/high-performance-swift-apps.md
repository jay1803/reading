---
title: "High Performance Swift Apps"
date: 2025-05-12T13:49:41Z
category: reading
author: "Jacob Bartlett"
description: "在这个 2FA app 的性能调优中，比密码学 TOTP 计算更慢的是一个检测重复数字的 regex，替换成 Set 查找后提速 30x——瓶颈在哪里，优化的价值就在哪里，其余所有改动都是幻觉。"
source: "https://blog.jacobstechtavern.com/p/high-performance-swift-apps"
---

## TL;DR
在这个 2FA app 的性能调优中，比密码学 TOTP 计算更慢的是一个检测重复数字的 regex，替换成 Set 查找后提速 30x——瓶颈在哪里，优化的价值就在哪里，其余所有改动都是幻觉。

## 核心洞见
- Instruments 定位出真正的热路径：~checkThoseSexts()~ 里的一个 regex 占用了总计算时间的大多数，远超 TOTP 密码学运算本身。把它替换成硬编码 ~Set<String>~ 的 ~contains()~ 调用（O(1)，无堆分配），该函数从累计 27.54s 降到 899ms，总处理时间减半。
- 并行化正确姿势是 ~processorCount - 1~，而非"能开几个开几个"——直接使用全部 6 核导致 UI 卡死，留一个核给主线程后恢复正常。Actor 协调（而非按偏移量分块）进一步把最慢线程从 15.37s 压到 6.74s，整体提速 47%，因为 actor 的 serial executor 确保每个线程总是计算"下一个未处理"的时间步，消除了分块方式下线程间的计算不均衡。
- 启动慢的根源是把 TOTP 生成绑在视图生命周期上（~onAppear~ + 1 秒 Timer）。把账户获取和代码生成移入 ViewModel ~init()~，启动到代码显示从 1.764s 降到 0.400s。

## 具体机制
1. **Time Profiler 三步清洁**：开启 Separate by Thread + Invert Call Tree + Hide System Libraries，才能从系统调用的噪音中看到自己的代码。
2. **Regex → Set 替换**：硬编码 10 个字符串的集合（~"000000"~ 到 ~"999999"~），消除每次调用时动态创建 10 个堆字符串的开销；对 counting sequence 同理处理。
3. **~actor CodeIncrementor~**：单一原子计数器保证各并发任务不重复、不遗漏地认领下一个时间步，代价是 actor serial executor 的调度开销，但换来更均衡的 CPU 利用率。

## 隐藏限制
文中提到了一个更彻底的方案：预计算全部 100 万个 6 位数的 interestingness 状态，存成 O(1) 字典，彻底免去运行时判断。被搁置的理由是"TOTP 生成本身才是移位后的新瓶颈"。这个取舍准确，但也意味着该优化在用户升级设备后的某一天可能变得必要——只要 TOTP 速度持续提升，这个被跳过的方案就会迟早重新登场。

## 留下的那个问题
整套方法论的隐性前提是：Instruments 采样场景必须贴近真实用户行为。文中最极端的 ultra-rare GETs 是手动构造的压力用例——若绝大多数用户只启用 common GETs（处理时间本就不超过 1 秒），那 47% 并行化提速对他们几乎不可见，值得测量的是中位用户路径，而不只是最坏情况。
