---
title: "Softcore Debugging"
date: 2025-05-12T13:46:39Z
category: reading
author: "Jacob Bartlett"
description: "~po~ 慢的根本原因是它内嵌了整个 Swift 编译器：每次调用都在编译表达式、注入运行进程、执行——换用 ~v~ 可直接读栈帧内存，绕过所有编译，速度\"戏剧性地\"更快。"
source: "https://blog.jacobstechtavern.com/p/softcore-debugging"
---

## TL;DR
~po~ 慢的根本原因是它内嵌了整个 Swift 编译器：每次调用都在编译表达式、注入运行进程、执行——换用 ~v~ 可直接读栈帧内存，绕过所有编译，速度"戏剧性地"更快。

## 核心洞见
三条 LLDB 命令的性能阶梯：~po~（编译＋注入＋执行＋描述）→ ~p~（编译＋执行，无描述）→ ~v~（零编译，直读内存）。日常打印局部变量时默认用 ~v~，只在需要完整对象描述时才升级到 ~po~。

条件断点比在代码里手写日志更优雅：可在第 N 次循环迭代、特定字符串长度、泛型函数命中特定类型时才暂停，且不需要重新编译。

## 具体机制
- ~po~ 本质是 ~expr --O --~：LLDB 调用内嵌 Swift 编译器编译表达式→注入进程→执行→调 ~CustomStringConvertible~ / ~CustomDebugStringConvertible~；两者都未实现则打印十六进制堆地址（如 ~0x6000002498a0~）
- ~p~ = ~expr --~，省去对象描述请求，稍快
- ~v~ = ~frame variable~，直接访问当前栈帧内存，不编译任何代码

Memory Graph Debugger：可视化堆上所有引用类型及其关系图，内存泄漏定位从"猜"变成"在图上看到多出来的那个实例"。

## Debug 层级的隐形陷阱
Thread Navigator 展示的是 pthread 快照，和 Swift Concurrency 的 Task 层级是两个不同抽象——用 async/await 写的并发代码，Task 和线程之间没有直接映射关系，这是 async 代码调试中最容易迷失的地方。
