---
title: "Local Qwen isn't a worse Opus, it's a different tool"
date: 2026-06-19T08:02:20Z
category: reading
description: "作者是 OpenFaaS/Actuated/Inlets 的 bootstrapped 创始人，花了约 12000 美元买了一张 RTX 6000 Pro Blackwell（96GB VRAM），并且这张卡已经通过一次商业事件回本：把客户的计费遥测数据跑过本地模型，发现该客户少报许可证数量 4-5 倍、持续 1..."
source: "https://blog.alexellis.io/local-ai-is-not-opus/"
---

## 本地 27B 模型的商业价值来自数据主权，不来自性能平价

作者是 OpenFaaS/Actuated/Inlets 的 bootstrapped 创始人，花了约 12000 美元买了一张 RTX 6000 Pro Blackwell（96GB VRAM），并且这张卡已经通过一次商业事件回本：把客户的计费遥测数据跑过本地模型，发现该客户少报许可证数量 4-5 倍、持续 12 个月以上。这笔数据合规上绝无可能走任何云端 API。

主权不是情怀，是真实约束。企业客户的诊断 dump（OpenFaaS "diag" CLI 输出）、遥测数据库，走云端 API 违反客户合同，无论是 ChatGPT Pro 还是 Claude Max，即使配置 30 天留存也不够。本地 airgapped 模型是唯一合规路径。厂商风险同理：Anthropic Fable 5 一夜从某些地区下架，这不是假设而是已发生的事实。

## Benchmark 分数差 12% 不等于能力差 12%

Qwen 3.6 27B 在 SWE-Bench Verified 拿到 77.2，Opus 4.8 拿到 88.6。但 SWE-Bench 是 Python 同步代码，而作者团队写的是 Go 分布式系统——channels、contexts、structs 跨越大型执行域。这个领域的差距在实测中被显著放大：Qwen 在自动代码审查时会无视"简洁"指令、虚报并发问题和 race condition，最终被弃用，换成了当时速度更快、更便宜的 Grok Coder Fast 1。

量化进一步拉大差距。一张 3090 装不下全精度 27B 模型，必须压缩权重和 KV cache。Q4_0 的 keys 被认为会导致质量明显下滑，作者测试到的最激进配置是 Q8_0 keys + Q4_0 values。

## 关键失效模式：无限循环，砸钱也买不掉

本地模型在长 horizon 任务中有两种循环：一是无意义重复输出（让 Qwen 列出 faas-cli 命令建议，列到第 58 条后开始循环，烧了半小时 600W 电）；二是模型知道自己卡住但既不放弃也不求助，越跑越偏（写 --json flag 时遇到无法解决的问题，不停尝试直到损坏文件）。团队两位成员各自独立复现了这两种情况。

$12,000 的 RTX 6000 Pro 没有解决这个问题。这是模型层面的限制，不是算力问题。类比：像钢刀回火时错过颜色，没有修复方式，只能断电重启。

## 可用场景：三个有边界的商业场景

1. **客服支持**：把客户的 diag dump 跑过 airgapped 本地模型，0 数据泄露风险，已规模化。
2. **营收追回**：分析计费遥测，发现欠报 license——回本了整张卡。
3. **代码库解读**：本地模型读懂并解释代码库是"超能力"，但写 Go 不行。

不适合的场景：长 horizon、无监督 agentic 任务。"我不会把一把刀的回火工序留给机器自己完成。"

## 技术配置

RTX 6000 Pro 96GB，跑两个独立 llama.cpp 实例（各持完整 context，避免共享实例时 KV cache thrashing）。speculative decoding 用 MTP 草稿，93% 接受率，生成速度从 67 tok/s 提升到 130-200 tok/s。

还在并行测试 Qwopus fine-tune（Jack Rong 在 Qwen 上叠加 Chain of Thought 训练数据）：thinking 关闭、temperature 0.85-1.0 时效果最好。Team 用自建的 "Toilgate" opencode provider 管理多个模型实例，加了两个 Shelly Plus 插座监控实际用电成本。
