---
title: "2025: The Year in LLMs"
date: 2026-02-14T20:36:35Z
category: reading
author: "Simon Willison"
description: "2025 最反常识的事实：Claude Code 以\"博客第二条子弹点\"的方式发布，最终做到 10 亿美元年化营收；而开源模型排行榜前五，全是中国实验室的模型（GLM-4.7、Kimi K2、DeepSeek V3.2 等），最高排名的非中国模型来自 OpenAI，位列第六。这两件事都没被任何人预测到。"
source: "https://simonwillison.net/2025/Dec/31/the-year-in-llms/"
---

## TL;DR

2025 最反常识的事实：Claude Code 以"博客第二条子弹点"的方式发布，最终做到 10 亿美元年化营收；而开源模型排行榜前五，全是中国实验室的模型（GLM-4.7、Kimi K2、DeepSeek V3.2 等），最高排名的非中国模型来自 OpenAI，位列第六。这两件事都没被任何人预测到。

## 一个推理技巧引爆了全年

RLVR（从可验证奖励中强化学习）是 2025 年几乎所有重要进展的起点。用数学/代码题目训练的模型自发出现"推理行为"——分解步骤、反复验证——这个技巧的真正价值不在解谜题，在于**驱动工具调用**：reasoning model + 工具 = 能规划、能纠错的 agent，AI 辅助搜索和 coding agent 都由此变得真正可用。

DeepSeek 在 2024 年圣诞节发布 V3（据称训练成本 555 万美元），随后 R1 于 2025 年 1 月上线，直接引发 NVIDIA 单日市值蒸发 5930 亿美元——投资者第一次意识到 AI 算力不是美国垄断的。

## 几个具体数据点

- Claude Code 在 Anthropic 公告中仅作第二子弹点出现；截至 12 月 2 日，年化营收达 10 亿美元。CLI 工具做到这个数字，Simon 本人也没预料到。
- GPT-4o 图像编辑功能上线后，单周带来 1 亿 ChatGPT 新注册用户，峰值每小时 100 万注册。
- METR 数据：AI 能独立完成"人类需数小时"任务的能力，每 7 个月翻倍（2025 年最好的模型已覆盖 2-5 小时任务）。
- MCP 爆火后正被 coding agent 架空：既然 agent 能直接跑 bash，专门的 MCP server 反而成了冗余层。

## 值得质疑

Llama 4 的失败被一笔带过——Scout 和 Maverick 分别是 109B 和 400B，无法在 64GB Mac 上运行，实际上 Meta 把开源生态的最大优势（可本地运行）完全抛弃了。文章对此批评较轻。另外，"RLVR 每 7 个月翻倍"的外推 Simon 自己也标注了存疑，但读者很容易被这个数字带走。

## 边缘判断

最值得警惕的不是 AI 变强，而是"规范化偏差"（Normalization of Deviance）：反复在 YOLO 模式下运行 agent 却没出事，正在让整个开发者社区把高风险行为当成默认配置——NASA 当年也是因为 O 形圈"一直没出事"才酿成挑战者号灾难。
