---
title: "No, it doesn't cost Anthropic $5k per Claude Code user"
date: 2026-03-27T08:01:53Z
category: reading
description: "Claude Code Max 用户\"消耗 $5000 算力\"说的是 Anthropic 零售 API 定价折算的价值，不是实际推理成本——真实计算成本约是这个数字的 1/10，平均用户对 Anthropic 很可能是盈利的。"
source: "https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## TL;DR
Claude Code Max 用户"消耗 $5000 算力"说的是 Anthropic 零售 API 定价折算的价值，不是实际推理成本——真实计算成本约是这个数字的 1/10，平均用户对 Anthropic 很可能是盈利的。

## 核心主张拆解
- Forbes 引用的 $5,000 数字来自 Cursor 的内部分析：Cursor 要按 Anthropic 零售 API 价格付费，所以对 Cursor 这个数字是真实的。但对 Anthropic 自身而言，"服务这些 token 的成本"远低于零售定价。
- 对比基准：OpenRouter 上参数规模相近的开权重 MoE 模型（Qwen 3.5 397B-A17B 输入 $0.39/MTok、输出 $2.34；Kimi K2.5 输入 $0.45、输出 $2.25）vs. Anthropic Opus 4.6 API（$5/$25）——约 10 倍差距。这些 OpenRouter 供应商都是盈利企业，必须覆盖 GPU 成本和利润率，因此差价不可能全部是亏损。
- 实际测算：重度用户 API 折算 $5,000 → 实际算力成本约 $500 → 月亏损约 $300，不是 $4,800。Anthropic 自己说 <5% 订阅者会触及每周上限，普通用量折算下来很可能盈亏平衡甚至盈利。

## 值得质疑
OpenRouter 开权重模型定价能否准确代理 Anthropic 闭源前沿模型的推理成本并非确定——两者在硬件、架构开销、SLA 上存在差异，文章对这一代理假设的成立条件没有充分讨论。

## 收束行
"推理成本是无底洞"这个叙事，客观上在帮前沿实验室维护护城河——没人质疑 10 倍溢价，竞争就更难形成；而这个叙事的传播者，很多并不意识到自己在替 Anthropic 站台。
