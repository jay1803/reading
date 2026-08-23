---
title: "Uber Caps Usage of AI Tools Like Claude Code to Manage Costs"
date: 2026-06-04T08:02:07Z
category: reading
author: "Simon Willison"
description: "Uber 将每位员工每个 AI 编程工具的月花费上限设为 $1,500，这个数字事实上是在公开为 AI coding agent 定价：假设每人同时使用两个工具，全年上限 $36,000，约为美国 Uber 工程师中位薪酬包（$330,000）的 11%。"
source: "https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything"
---

## TL;DR
Uber 将每位员工每个 AI 编程工具的月花费上限设为 $1,500，这个数字事实上是在公开为 AI coding agent 定价：假设每人同时使用两个工具，全年上限 $36,000，约为美国 Uber 工程师中位薪酬包（$330,000）的 11%。

## 关键时刻
- Uber 2026 年 AI 预算在四个月内耗尽。根本原因是预算于 2025 年制定，彼时无人预测到 agentic coding 工具会爆发性普及。
- 新限额：$1,500/月/工具，仅针对 Cursor、Claude Code 等 agentic coding 软件；不同工具的预算彼此独立，不相互抵扣。

## 背后逻辑
- 该限额实际上内嵌了一个隐性定价信号：Uber 认为每个工具每月的合理价值上限即在此附近。Simon Willison 自己的使用量约为每家 provider $1,000/月，在此限额下尚余 $500 的空间。
- 个人订阅用户可享受 Anthropic 和 OpenAI 的补贴计划（实付 $100），大企业则须按 API 价格全额支付——两者成本结构根本不同，是 Uber 相对成本远高于个人用户的直接原因。

## 更大意义
用 $1,500 定额取代"tokenmaxxing 排行榜"（鼓励员工竞争最高使用量），是对超支问题的理性政策回应。更深层的问题在于：这个 11% 阈值，可能将成为行业其他公司测算 AI coding agent ROI 时的隐性基准。
