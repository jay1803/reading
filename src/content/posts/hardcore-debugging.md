---
title: "Hardcore Debugging"
date: 2025-05-12T13:46:56Z
category: reading
description: "当崩溃栈指向内核内存管理层、调试器拒绝报告真正的责任方时，两个\"极端\"工具——git bisect 二分法定位提交时间轴、atos 手动符号化崩溃日志定位代码空间——可以绕开调试器，直接把几千行代码缩窄到一个函数。"
source: "https://blog.jacobstechtavern.com/p/hardcore-debugging"
---

## TL;DR
当崩溃栈指向内核内存管理层、调试器拒绝报告真正的责任方时，两个"极端"工具——`git bisect` 二分法定位提交时间轴、`atos` 手动符号化崩溃日志定位代码空间——可以绕开调试器，直接把几千行代码缩窄到一个函数。

## 核心洞见

**`git bisect` 在时间轴上二分**：把崩溃出现前后的已知 good/bad commit 喂给 `git bisect`，它自动 checkout 中间点，你只需判断好/坏，10 步左右可以从数百个提交中定位到单一 guilty commit 及对应 diff。`git bisect run <script>` 可全自动化——命令返回 exit 0 代表 good，非 0 代表 bad。陷阱：漏标一个 good/bad 结果全废，每步都要 clean build 并重复验证。

**手动符号化在代码空间里定位**：适用调试器不可用的场景（只发布构建崩溃、没有 crash SDK 的 App Extension、dSYM 上传管道断掉）。核心步骤：
1. 用 `xcrun dwarfdump --uuid` 确认 `.app` / `.dSYM` 与 `.ips` 崩溃报告的 UUID 一致，否则结果无意义。
2. 从崩溃报告的 Binary Images 段取出 **load address**（模块加载进进程的内存基址）。
3. 把 load address 和崩溃栈里的各地址一起喂给 `atos -o Bev.app.dSYM -l <load_addr> <addr1> <addr2> …`，输出变成可读函数名 + 源文件行号。
4. 若 `atos` 失败，可直接在 `dSYM/Contents/Resources/Relocations/aarch64/*.yml` 中按内存地址前缀局部搜索，用 locality 推断所在类/方法。

## 隐藏限制

文中实际找到的根因是一个经典的 `@MainActor deinit` 陷阱：属性标注为 `@MainActor`，在 `deinit` 里用 `Task { @MainActor in }` 做清理，但 Task 是**异步调度**到主 actor executor 的——`deinit` 先执行完、属性内存已被回收，Task 才真正运行，触发 `EXC_BAD_ACCESS`。修复只需去掉不必要的 `Task` 包装（`SequenceListener` 自身的 deinit 已自动 cancel）。文章花大篇幅讲定位过程，顺带证明了：能找到 culprit commit 只是起点，理解 Swift 并发所有权模型才是真正的门槛。

## 两个工具都是"最后手段"
`git bisect` 耗时按小时计，只在无其他线索时值得。`atos` 手动符号化的大前提是你手头有匹配 UUID 的 dSYM——CI 流水线要保留 artifacts，不然这条路也走不通。
