---
title: "snyk vs endor labs"
date: 2026-03-11T01:01:07Z
category: reading
description: "Snyk 的旧核心业务（开源依赖扫描）正在下滑，靠 Snyk Code 的 AI 代码扫描掩盖了这一事实；同样的转型压力还会再来一次——这次是由 AI 编程工具本身带来的，而 Snyk 并非这波浪潮的原生选手。"
source: "https://newsletters.feedbinusercontent.com/6d8/6d83595fe6dc10da20bb1062420cbf161b1d79ce.html"
---

## TL;DR
Snyk 的旧核心业务（开源依赖扫描）正在下滑，靠 Snyk Code 的 AI 代码扫描掩盖了这一事实；同样的转型压力还会再来一次——这次是由 AI 编程工具本身带来的，而 Snyk 并非这波浪潮的原生选手。

## 数据与现状
- 2023 年底 $250M ARR → 2024 年底 $300M ARR，增长来自 Snyk Code（AI 代码扫描），已超 $100M ARR，主要推动力是 GitHub Copilot 和 Cursor 的企业级采用。
- 同期，Snyk 传统的开源漏洞扫描（SCA）业务出现下滑——这是增长的结构性代价，而非暂时性波动。

## 战略动作与竞争格局
- 2025 年 6 月收购 Invariant Labs（专注 AI agent 安全）；2026 年 2 月换帅，引入 AI-native 背景的新 CEO。
- 推出 Snyk Evo（beta）：面向 MCP 安全扫描、LLM 注入监控、自然语言安全策略的 agent 套件。
- 对手：Semgrep（2017 年，$93M，Lightspeed）与 Endor Labs（2021 年，$95M，Lightspeed），二者均被认为比 Snyk 更 AI-native。

## 结构性判断
Snyk 的历史成功建立在"应用安全的执行主体从安全团队转移到开发者"这一断层上。下一个断层是"从开发者转移到 AI agent / MCP 工作流"，但这次 Snyk 站在了防守方：它的产品底座不是为 agentic 工作流设计的，而 Endor Labs 等公司从零开始构建，没有遗留包袱。
