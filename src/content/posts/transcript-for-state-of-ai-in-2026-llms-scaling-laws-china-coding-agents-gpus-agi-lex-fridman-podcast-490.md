---
title: "Transcript for State of AI in 2026: LLMs, Scaling Laws, China, Coding, Agents, GPUs, AGI | Lex Fridman Podcast #490"
date: 2026-02-14T20:39:06Z
category: reading
description: "RLVR（可验证奖励强化学习）已成为后训练的核心驱动力，其关键特性是\"可无限加码\"——RLHF 存在信号饱和上限，而 RLVR 遵循对数-线性 scaling law，多投入10×算力仍有线性收益；这一差异正在重塑 AI 研究的资源分配逻辑。"
source: "https://lexfridman.com/ai-sota-2026-transcript/?utm_source=rss&utm_medium=rss&utm_campaign=ai-sota-2026-transcript"
---

## TL;DR
RLVR（可验证奖励强化学习）已成为后训练的核心驱动力，其关键特性是"可无限加码"——RLHF 存在信号饱和上限，而 RLVR 遵循对数-线性 scaling law，多投入10×算力仍有线性收益；这一差异正在重塑 AI 研究的资源分配逻辑。

## RLVR 的机制与边界

DeepSeek 通过让模型反复尝试数学/代码题并以正确答案作为奖励信号，解锁了"模型自我纠错"（aha moment）——不是新能力，而是放大了预训练中已有的行为模式。Nathan Lambert 指出 RLVR 与 RLHF 的本质分叉：RLHF 优化的是平均偏好（有上限、有哲学缺陷），RLVR 优化的是可验证的对错（可持续 scaling）。

当前 RLVR 面临的核心问题：随模型能力提升，简单问题不再提供梯度信号，需要持续寻找更难的验证域——科学实验、复杂软件工程、形式化数学（Lean）。下一阶段（RLVR 2.0）的候选方向是 Process Reward Models 或 Value Functions，对中间推理步骤而非仅最终答案给分。

**值得质疑**：Qwen 系列在 MATH-500 上"50步从15%跳到50%"的案例，被怀疑是预训练数据污染而非真正的数学学习——模型记住了与测试集几乎相同的问题，而非习得推理能力。如何区分"解锁已有知识"与"真正学到新东西"，目前无法干净地分离。

## 开源 vs 闭源：结构性裂变

Meta/Llama 的退场（Llama 4 基准过拟合、内部政治内耗）在 2025 年留下空白，被中国开源模型（Qwen、DeepSeek 系列）填充。Nathan Lambert 的 Adam Project（美国真正开源模型）核心论点是：开源模型是 AI 研究的起点，谁控制开源生态谁就控制下游研究话语权；用 100M 美元建出半代领先的开源模型比打 AGI 军备竞赛更具杠杆。

Cursor 的案例揭示了闭源与开源的一条新裂缝：每90分钟用真实用户反馈更新模型权重，这是目前最接近"生产环境实时 RL"的公开案例，而开源模型因缺乏统一工具调用集成，在 agentic 任务上仍系统性落后。

## AGI 时间线："超人程序员"是个伪命题

AI 2027 报告将"超人程序员"设为 AGI 的代理指标，Nathan 的反驳是：模型能力是"锯齿形"的（jagged）——在传统 ML 和前端代码上接近超人，在大规模分布式系统上仍很弱。不存在一个整体意义上的"超人程序员"，只有在特定代码类型上局部超人。

对经济影响的诚实评估：到目前为止，LLM 尚未产生可观测的 GDP 跳跃。真正的大规模经济冲击依赖 computer use（让 AI 自主操作界面）——而 2025 年所有演示的 computer use 都"很烂"。

## 留下的那个想法
Lex 说的那句话值得单独记住："我们正在溺于 slop，但也许这种溺死本身会让社会自我清醒。" 真实性溢价（in-person 体验、人类手工制品、可验证来源的信任）可能是 AI 大量普及后的自然反弹——不是因为人们变聪明了，而是因为信噪比的崩塌让人本能地退回到更贵的信号。
