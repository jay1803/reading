---
title: "What's new in Claude Sonnet 5"
date: 2026-07-01T08:03:04Z
category: reading
description: "Sonnet 5 标价与 Sonnet 4.6 完全一致（$3/$15 per million tokens，折扣期至 8 月 31 日降至 $2/$10），但新 tokenizer 对同一文本产生的 token 数比 4.6 多约 30%。Simon Willison 的实测数据：英文 ×1.42、西班牙文 ×..."
source: "https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything"
---

## 隐性涨价：同价 tokenizer 让英文成本实增 30–40%

Sonnet 5 标价与 Sonnet 4.6 完全一致（$3/$15 per million tokens，折扣期至 8 月 31 日降至 $2/$10），但新 tokenizer 对同一文本产生的 token 数比 4.6 多约 30%。Simon Willison 的实测数据：英文 ×1.42、西班牙文 ×1.33、Python 代码 ×1.28；简体中文几乎不变（×1.01）。实际跑英文 / 代码工作负载的成本等效于涨价 30–40%。

## 关键 API 变化

- 不再支持 temperature、top_p、top_k 参数。
- 上下文窗口 100 万 token，最大输出 128K token。
- 自适应思考（adaptive thinking）默认开启；关闭需显式传 ~"thinking": {"type": "disabled"}~。
- 工具和平台特性与 Sonnet 4.6 一致。

## 能力定位与监管理由

性能接近 Opus 4.8，售价低于 Opus。System Card 明确说明 Sonnet 5 在 cyber 任务上的能力"显著弱于 Mythos 5"（Anthropic 内部旗舰模型），安全风险等级与现有 Opus 4.7/4.8 相当——这是它能不被美国政府阻拦的核心依据。
