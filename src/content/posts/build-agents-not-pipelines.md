---
title: "Build agents, not pipelines"
date: 2026-06-01T08:01:18Z
category: reading
description: "当任务难点在“事前不知道该收集哪些上下文”或“必须根据中间结果继续行动”时，pipeline 的可控性会变成认知天花板；agent 的不确定成本是它购买额外智能的价格，coding agent 已经证明这笔价格在高难任务上常常划算。"
source: "https://seangoedecke.com/build-agents-not-pipelines/"
---

## TL;DR
当任务难点在“事前不知道该收集哪些上下文”或“必须根据中间结果继续行动”时，pipeline 的可控性会变成认知天花板；agent 的不确定成本是它购买额外智能的价格，coding agent 已经证明这笔价格在高难任务上常常划算。

## 核心主张拆解
- 作者把 LLM 程序分成两类：pipeline 由代码掌控控制流，LLM 只是其中一步；agent 则给模型工具，让模型自己决定下一步。这个区别类似 library 与 framework：前者可控、显式、维护样板多，后者上手快、能力更完整，但会把部分结构权交给框架。
- 简单任务里两者差异会消失。若上下文很小、动作路径固定，一个带 `gather_context` 和 `email_me` 工具的 agent 很可能复刻 pipeline 的步骤。
- 差异在复杂任务里扩大：上下文超过单次 prompt、需要先行动再观察结果、或者无法提前确定信息需求时，agent 能循环、搜索、读取、修正；pipeline 只能吃到工程师预先塞进去的上下文。
- pipeline 的优势是真实的：延迟、成本、推理量更容易控制，尤其适合大规模批处理、本地模型、小 context window、GPU 成本必须封顶的场景。agent 的风险也真实：一次任务可能几轮结束，也可能跑到上百轮，成本和延迟可轻易翻倍。

## 关键机制
- 作者认为 context-gathering 是 pipeline 最脆弱的环节。很多系统把难题伪装成 RAG、AST walk、embedding 检索，但“找出什么信息与当前问题相关”本身往往接近原问题难度；agent 反而可以用 grep/read file 这类普通工具，像人一样边想边找。
- 多模型 pipeline 看似灵活，可以让便宜模型做整理、让强模型做判断；作者对此怀疑，因为信号常在原始数据里，先让弱模型压缩上下文可能已经损伤了决策材料。若真要分工，也可把便宜模型藏进 agent 的工具内部，例如让 web_search 工具自行摘要网页。
- agent 更 future-proof：模型训练正在显式优化 tool use 与长程任务，agent 把更多决策委托给模型，因此会更直接吃到新模型能力提升。pipeline 也会变好，但提升更像局部替换；agent 可能因为模型变强而跨过原本不可解的任务门槛。
- 安全问题没有被 pipeline 消除。prompt injection 来自输入内容本身，不管内容是工具调用拿到的，还是 pipeline 直接拼进 prompt，模型都会读到。真正需要的是内容隔离、动作审批、敏感工具约束，而不是把系统命名为 workflow。

## 值得质疑
- 作者对 RAG 的批评方向成立，但略显一刀切。很多生产系统的目标不是“解决开放问题”，而是高召回地把候选证据送到固定判断器；在这些场景，RAG 的上限低于 agent，不等于它没有工程价值。
- “when in doubt, use agents”适合探索和高难任务，但对可规模化产品可能过于乐观。若任务量巨大、输出价值低、SLA 明确，先用 agent 找到可行行为，再蒸馏成 pipeline，可能比长期保留 agent loop 更经济。
- NSA 例子把两者组合得更清楚：海量邮件先用低成本 pipeline 打标，再由 agent fleet 深挖高价值线索。这个混合结构也许才是大多数严肃系统的最终形态，而不是纯 agent 或纯 pipeline。

## 收束
这篇文章最有用的判断标准不是“agent 更聪明”，而是把问题拆成两层：若难点是执行固定流程，选 pipeline；若难点是发现流程本身，选 agent。控制流交给谁，本质上是在成本可预测性和上下文自发现能力之间下注。
