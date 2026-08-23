---
title: "Subagents"
date: 2026-03-24T08:01:26Z
category: reading
author: "Simon Willison"
description: "过去两年 LLM 能力大幅提升，但上下文窗口几乎原地踏步（上限约 100 万 token，实测最佳质量通常在 20 万以内）。Subagent 的本质是用\"新鲜上下文\"来保护主 agent 的 token 余量——它是 token 预算管理策略，而非单纯的并行加速手段。"
source: "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/#atom-everything"
---

## TL;DR
过去两年 LLM 能力大幅提升，但上下文窗口几乎原地踏步（上限约 100 万 token，实测最佳质量通常在 20 万以内）。Subagent 的本质是用"新鲜上下文"来保护主 agent 的 token 余量——它是 token 预算管理策略，而非单纯的并行加速手段。

## 核心洞见
Coding agent 把特定子任务（代码库探索、测试运行、专项调试）分派给 subagent，后者以全新上下文窗口独立完成，压缩结果后返回给父 agent；父 agent 只消耗"摘要"而非"过程"，根上下文因此得以延续更长时间。

## 具体机制
Claude Code 的标准流程示范了这一模式：开新任务时先派 Explore subagent 读目录、找相关文件、返回结构摘要，父 agent 拿到摘要再动手修改。Subagent 也可并发运行（适合多个互不依赖的文件改动），还可搭配更快更便宜的模型（如 Claude Haiku）进一步降低成本。专用角色包括：代码审查 agent、测试运行 agent、调试 agent。

## 隐藏限制
过度拆分适得其反：把每个环节都塞进专门 subagent 会增加协调成本，并不一定带来更好的结果。主 agent 完全能胜任调试和审查——前提是它还有足够的 token 余量。专用 subagent 的价值判断标准只有一个：省下的上下文是否比拆分引入的协调代价更值钱。

## 收束行
Subagent 让模型学会"给自己写提示词"——父 agent 构造子任务目标，子 agent 的返回结果成为下一步的输入上下文。整个模式本质上是在用架构手段对抗上下文稀缺性，而不是靠等待模型厂商把窗口再翻一倍。
