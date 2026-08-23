---
title: "Impressions from visiting OpenAI, Anthropic, & Cursor"
date: 2026-07-01T08:03:04Z
category: reading
author: "Gergely Orosz"
description: "三家公司——OpenAI、Anthropic、Cursor——各自从不同的痛点出发，独立得出同一结论：本地机器是运行 AI Agent 的错误基础设施。这是文章最核心的观察，而非关于 Slack 集成的技术细节。"
source: "https://newsletter.pragmaticengineer.com/p/impressions-from-visiting-openai"
---

## Agent 上云是 2026 年最大的行业收敛信号

三家公司——OpenAI、Anthropic、Cursor——各自从不同的痛点出发，独立得出同一结论：本地机器是运行 AI Agent 的错误基础设施。这是文章最核心的观察，而非关于 Slack 集成的技术细节。

Karpathy 对 Claude Tag（在 Slack 中 @ Claude 触发任务）喊出"新范式"，社交媒体的反驳是"不就是个 Slack 集成"。但 Anthropic Applied AI 的 David Hershey 给出了真正的解释：真正的价值不在 Slack，而在于 Agent 不再跑在本地机器上——无需额外配置 MCP servers，无需切换工具，任何人随手发一条消息就能踢开一个长跑任务。

### 三家公司的具体动作

- *Anthropic*：Claude Managed Agents 是 Katelyn Lesse（Claude Platform 工程负责人）团队花六个月建设的托管服务，把长时间运行的 Agent 跑在各家云厂商上。这是内部核心项目，不是附加功能。

- *OpenAI*：收购 Ona（前身 Gitpod，云端开发环境领导者）。官方表态直接："Codex 最有价值的工作正在从分钟级演变为小时乃至数天级。我们相信人们应该能够委托更宏大的工作，而不需要被任务开始时的那台机器绑定。"Cloud Agents 团队正在招聘，岗位要求 Python/Rust/分布式系统背景。

- *Cursor*：年底已上线 Cloud Agents，CPO Sualeh Asif 披露了两个真实工程挑战：① 云端 Agent 无法"抱怨"——本地 Agent 遇到报错会反馈给人，云端长任务没有这个反馈回路，Cursor 的解决方案是让模型定期"confession"（坦白）并汇总给 infra 团队；② 节点中途宕机时，Agent 执行如何迁移到另一节点。6 月 29 日刚上线的 iOS app 本质上是构建在 Cloud Agents 之上的产物。

### 为什么是现在

四个条件同时成熟：Opus 4.5 / GPT-5.4 出现之前模型自主编码能力不够，长任务没有意义；MCP 和 Skills 等 Agent infra 进入主流；context window 扩大到百万 token 级别；各家云厂商 GPU 产能终于足够。

### 付费墙后三节（仅摘要标题）

文章第 2-4 节在付费墙后，内容未可得：OpenAI 内部 95% 以上非工程师使用 Codex 而非 ChatGPT；工程师主要工作将转向提升 Agent 执行效率；企业正大力压缩每 token 成本（Coinbase 案例）。
