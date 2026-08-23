---
title: "DeepSeek V4–almost on the frontier, a fraction of the price"
date: 2026-05-03T08:01:45Z
category: reading
author: "Simon Willison"
description: "DeepSeek V4 的真正冲击不是“最大开源模型”本身，而是把接近前沿的 1M 上下文 MoE 能力压到极低价格：Flash 进入小模型最低价带，Pro 在大模型/前沿候选里也显著便宜，竞争重心正在从参数规模转向长上下文效率与单位推理成本。"
source: "https://simonwillison.net/2026/Apr/24/deepseek-v4/"
---

## TL;DR
DeepSeek V4 的真正冲击不是“最大开源模型”本身，而是把接近前沿的 1M 上下文 MoE 能力压到极低价格：Flash 进入小模型最低价带，Pro 在大模型/前沿候选里也显著便宜，竞争重心正在从参数规模转向长上下文效率与单位推理成本。

## 核心主张拆解
- DeepSeek V4 首批是两个预览模型：DeepSeek-V4-Pro 与 DeepSeek-V4-Flash；二者都是 1M token context 的 MoE，采用 MIT license。
- Pro 为 1.6T 总参数、49B 激活参数，作者判断它可能是新的最大 open weights model，超过 Kimi K2.6 的 1.1T、GLM-5.1 的 754B，也超过两倍 DeepSeek V3.2 的 685B。
- Flash 为 284B 总参数、13B 激活参数；模型体积上，Pro 在 Hugging Face 上约 865GB，Flash 约 160GB。
- 作者用 OpenRouter 简单测试了 SVG pelican riding a bicycle，结果“pretty good”，但文章真正强调的不是能力 demo，而是价格曲线。

## 成本优势
- DeepSeek-V4-Flash 定价为每百万 input $0.14、output $0.28，低于 GPT-5.4 Nano 的 $0.20/$1.25，也低于 Gemini 3.1 Flash-Lite 的 $0.25/$1.50。
- DeepSeek-V4-Pro 定价为 $1.74/$3.48；相比 Gemini 3.1 Pro $2/$12、GPT-5.4 $2.50/$15、Claude Sonnet 4.6 $3/$15、GPT-5.5 $5/$30，尤其在 output token 上差距很大。
- 如果质量真的接近前沿，这会直接改变高 token 量、长上下文、批量推理场景的经济账：模型选择不只是“谁最强”，而是谁能在可接受质量下把边际成本打穿。

## 效率机制
- DeepSeek 论文给出的解释是长上下文效率：在 1M-token context 下，V4-Pro 的单 token FLOPs 只有 V3.2 的 27%，KV cache 只有 10%。
- V4-Flash 更激进：同样 1M context 下，单 token FLOPs 只有 V3.2 的 10%，KV cache 只有 7%。
- 这意味着低价不一定只是补贴或营销，至少按论文说法，它来自架构和推理效率的系统性改进，尤其适合长上下文成本敏感场景。

## 前沿位置
- DeepSeek 自报 benchmark 认为 V4-Pro-Max 通过扩展 reasoning tokens，在标准 reasoning benchmark 上超过 GPT-5.2 和 Gemini-3.0-Pro。
- 但论文也承认它仍略低于 GPT-5.4 与 Gemini-3.1-Pro，约落后当前 SOTA 前沿 3–6 个月。
- 所以标题里的 “almost on the frontier” 很精确：它不是宣称绝对领先，而是用低得多的价格逼近前沿质量区间。

## 证据薄弱处
- benchmark 主要来自 DeepSeek 自报，需要第三方评测和真实工作负载验证。
- SVG pelican 测试只是轻量 anecdote，不能证明复杂推理、长任务可靠性或 agentic 表现。
- 本地运行仍不确定：Flash 160GB 可能等量化版；Pro 865GB 即使只流式加载 active experts，也需要实际工程验证。
- 文章没有展开延迟、吞吐、稳定性、API 限额、生态工具链等生产部署关键因素。

## 最后一层
如果量化后的 Flash 真能在高端个人机器上可用，DeepSeek V4 的意义会从“便宜 API”升级为“个人/小团队可拥有的接近前沿长上下文基础设施”。这比单次 benchmark 排名更值得盯。
