---
title: "Paged Out Issue #8 [pdf]"
date: 2026-02-24T10:55:40Z
category: reading
description: "Paged Out! #8 是迄今最大一期（90+ 页，逾百万次下载里程碑），但它最反直觉的地方是：全书没有一篇文章超过一页，却有多篇在那一页里推翻了你对已熟悉事物的基本假设——包括 x86 调试寄存器、C/C++ 未定义行为、浏览器暂停下载，以及 Signal 是否算自由软件。"
source: "https://pagedout.institute/download/PagedOut_008.pdf"
---

## TL;DR

Paged Out! #8 是迄今最大一期（90+ 页，逾百万次下载里程碑），但它最反直觉的地方是：全书没有一篇文章超过一页，却有多篇在那一页里推翻了你对已熟悉事物的基本假设——包括 x86 调试寄存器、C/C++ 未定义行为、浏览器暂停下载，以及 Signal 是否算自由软件。

## 核心内容拆解

**x86 只读断点从来不存在（Xusheng Li）**：DR7 调试寄存器自 80386（1985 年）起的 R/W 字段只有四种编码：执行 / 写入 / IO端口 / 读写，从来没有"只读"。GDB 的 ~rwatch~ 用"读写断点 + 值未变即判定为读"模拟，当连续写入相同值时会误触发——这是已知已久的限制。ARM/AArch64 原生支持真正的只读断点。

**未定义行为永远不会发生（Michał Nazarewicz）**：这不是哲学命题，是编译器的操作公理。一旦代码路径触发 UB，编译器将整条路径视为逻辑不可达并直接消除：Linux tun/tap 驱动曾因此删掉了一个空指针检查，导致内核漏洞。MSVC 通过 ~-fno-delete-null-pointer-checks~ 等扩展明确允许部分 UB 场景（如 ~CWnd::GetSafeHwnd~），但这不可移植，GCC/Clang 默认不遵循。

**浏览器暂停下载的两种实现（Xusheng Li）**：Firefox 点暂停 = TCP RST 断连 + 记录字节数 + 恢复时用 Range 头重连；Chrome 点暂停 = 停止从 socket 读取 → 内核缓冲区满 → TCP 零窗口广播 → 服务端停发但连接保持。Chrome 的方案恢复瞬间但会持续占用一个并发连接配额（HTTP/1.1 下每主机 6 个连接中的一个）。

**Signal 是自由软件吗？（Frank Seifferth）**：源码用 AGPLv3 发布，但服务条款将"Services"定义为包含客户端 app，并禁止"批量消息、自动化账号创建、未授权收集用户信息"。这与自由软件第 0 条自由（"按你的意愿运行程序，用于任何目的"）存在张力。作者没有给出答案，只是把问题摆出来。

**AI 安全代码审查基准（Adrian Sroka）**：23 段代码、30 个隐藏漏洞，人类准确率 92%，最佳 AI（Claude 3.5 Sonnet 87%、Perplexity DeepSeek 83%）仍有差距；AI 对过时加密算法和敏感数据暴露接近满分，但对依赖验证和特性标志上下文分析几乎为 0。推荐模式：AI 扫显而易见的问题，人工专注复杂逻辑。

**Gemini CLI + MITRE ATT&CK（Jakub Kowalski）**：相比上篇（GPT-5 提示词工程准确率 50-80%），Gemini CLI 通过 GEMINI.md 配置文件 + 加载 MITRE relationship 文件到上下文，TTP 识别准确率跃升至 72-94%，且能正确输出子技术和流程级别映射。核心变量是可检索的结构化上下文，而非模型本身。

**B 树序列化：零复制格式（Elias de Jong）**：JSON 反序列化必须先构建 DOM 树，Protobuf 需要 schema——两者本质上都是在把数据转换成树形结构。Lite³ 直接把 B 树编码进消息缓冲区，读取时原地遍历，无需解析步骤。基准测试：比 simdjson DOM 快 30x，比 Google Flatbuffers 快 225x；9.3 kB，零依赖。

**AWK 声学调制解调器（Nicolas Seriot）**：在无网络、无编译器、无安装权限的锁定 Unix 系统上，5 行 AWK 可实现 Bell 103（300 波特，1270/1070 Hz）音频数据外泄；改用 15-17.5 kHz 超声频段可静默传输，iOS Voice Memo 可无声录制。

**个人工作 Agent（Rene Schallner）**：一个有意思的架构案例——自建 agentic loop（而非用框架），原因是上下文窗口控制：每次 LLM 调用传什么、传多少完全由代码决定，而非框架自动注入；工具调用结果用 SDK 留在 Python 内存而非序列化给 LLM，大幅节省 token。支持 YOLO 模式（跳过每步审批）。

## 收束行

Paged Out! 用结构性约束（一页纸）做到了大多数长文做不到的事：每篇文章都被迫暴露自己的核心论点——没地方藏废话，也没地方留给"我大概懂了"的安全着陆。
