---
title: "Anthropic's Method to Losing Goodwill in a Few Easy Steps"
date: 2026-07-07T08:02:31Z
category: reading
description: "Dario 需要资本的根本原因是模型训练（AGI 竞赛），而非推理——推理本身已经有利可图。订阅分池、锁定生态、额外收费，这些对用户的所有损耗，本质是在用订阅者为下一代模型训练买单，而不是改善现有产品。"
source: "https://raheeljunaid.com/blog/anthropics-method-to-losing-goodwill-in-a-few-easy-steps/"
---

### Anthropic 的价格压榨是 AGI 训练融资，而非商业盈亏平衡

Dario 需要资本的根本原因是模型训练（AGI 竞赛），而非推理——推理本身已经有利可图。订阅分池、锁定生态、额外收费，这些对用户的所有损耗，本质是在用订阅者为下一代模型训练买单，而不是改善现有产品。

### 计费分割：影响比公告更大

2026 年 6 月 15 日起，Anthropic 将订阅用量拆成两个池：一方工具（claude.ai、Claude Code CLI）与三方 Agent/SDK 工具。新的"Agent SDK 信用"按 API 全价计费：Pro $20/月，Max 5x $100，Max 20x $200。订阅此前以 15–30 倍差价补贴了 Agent 用量，这一补贴现已取消。

有两个细节比公告本身更值得注意：其一，这件事不是因为服务中断被发现，而是用户主动查账单才发觉。其二，=claude -p=——Anthropic 自己的一方工具——也被划入"额外用量"池，在用户达到速率限制前就开始扣钱。

### 两次更早的诚信透支

Anthropic 曾通过检测会话目录内的特定文件名来判断用户是否使用三方工具——即使用户并未使用，也会被收取额外费用。同期修改 API 合约后，代理工具（如 meridian）在没有改变自身请求机制的情况下，一夜之间触发了额外收费。

### 生态锁定的实际边界

Claude 订阅只能用于 Anthropic 一方界面（Claude Code CLI/Desktop、CoWork、Slack 的 @Claude）。Vertex AI、AWS Bedrock、Azure 仅售更贵的 Anthropic API 点数，不支持订阅池。Claude Code 目前有 9100+ 个未解决 GitHub Issue，包括持续 6 个月以上的完全冻结问题。

### Vibe Coding 才是主市场

Anthropic 的实际目标用户不是开发者，而是无法写代码、愿意付 $200/月"自动化掉工程师"的管理层和 vibe coder。这部分市场越大，被锁定的人越多，Anthropic 的议价能力越强。作者指出，过度依赖 Agent 驱动开发导致了自身技能退化，已切换回"autocomplete 辅助"模式，并将 Sonnet 从工作流中移除。

### 开源替代的可行性

Qwen 3.7 Max 和 GLM 5.2 的编码能力已接近 Sonnet 5，且成本大幅更低。通过 OpenRouter、Requesty、Portkey 等 AI 网关，可动态路由至最便宜的供应商，同时支持零数据保留和敏感词过滤。
