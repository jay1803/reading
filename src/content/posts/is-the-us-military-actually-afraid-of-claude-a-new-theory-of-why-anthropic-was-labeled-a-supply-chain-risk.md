---
title: "Is the US military actually afraid of Claude? A new theory of why Anthropic was labeled a supply chain risk."
date: 2026-03-27T08:01:53Z
category: reading
author: "Gary Marcus"
description: "国防部将 Anthropic 列为\"供应链风险\"的官方理由——Claude 有\"灵魂\"、有宪法、会\"焦虑\"、Anthropic 认为它有 20% 概率有意识——每一条都经不起逻辑检验，且全部同样适用于所有 LLM，包括 OpenAI。"
source: "https://garymarcus.substack.com/p/is-the-us-military-actually-afraid"
---

## TL;DR
国防部将 Anthropic 列为"供应链风险"的官方理由——Claude 有"灵魂"、有宪法、会"焦虑"、Anthropic 认为它有 20% 概率有意识——每一条都经不起逻辑检验，且全部同样适用于所有 LLM，包括 OpenAI。

## 核心主张拆解
DoD CTO Emil Michael 的四项指控，Gary Marcus 逐条解包：

- **"Claude 说自己焦虑"** ≠ Claude 真的焦虑。LLM 模仿人类语言，包括"我有孩子""我周末出去玩"，这些都不是内部状态的真实描述，是 next-word prediction 的产物。
- **"Anthropic 认为 Claude 有 20% 的意识概率"**：这句话是 Claude Opus 4.6 自己在特定 prompt 下说的，不是 Anthropic 官方立场；Amodei 本人在采访中明确拒绝认真对待这个数字。
- **"Claude 有非美国宪法的'宪法'"**：OpenAI 同样有 guardrails，只是叫法不同。整个行业都依赖内置约束，否则 LLM 根本无法安全部署。
- **幻觉问题**：确实是风险，但这是所有 LLM 的共性，而非 Anthropic 专有问题。

逻辑结论：如果上述任何一条成立，那么所有 LLM 都是供应链风险——正确决策是停用所有 LLM，而不是选择性打压 Anthropic。Marcus 还指出，早在 LaMDA 争议（Blake Lemoine 事件）时，同样的"意识指控"就针对 Google 的模型出现过；任何 LLM 训练数据中都包含意识话语，这不能作为单一公司的罪证。

## 反驳或薄弱处
Marcus 承认 DoD 在采访早段提出的另一部分担忧（具体未展开）有一定合理性——承包商关系的考量本身是正当的。但"供应链污染"这条论证链他认为根本站不住脚。

文章开头暗示的"真实原因"（OpenAI Brockman 给 Trump 捐了 2500 万美元，Anthropic 没有）在正文中没有正面展开，属于暗示而非论证，是全文最薄弱的环节。

## 要么全是风险，要么全不是
这套逻辑只能把 Anthropic 单独列出来——说明 DoD 的论证框架本身不是技术判断，要么是政治决策，要么是对 LLM 工作原理的根本性误解。两种解释对 AI 政策方向的含义都很糟糕。
