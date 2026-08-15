---
title: "Managed agents are the new Lambda"
date: 2026-05-15T08:01:24Z
category: reading
description: "托管智能体的核心诱惑是“把 agent 从本机搬进云端”，但真正的战略风险是把 agent primitive、工作流状态、权限模型和计费路径一起交给前沿模型厂商；短期像 Lambda 一样省事，长期可能像 Lambda 一样难迁移。"
source: "https://martinalderson.com/posts/managed-agents-are-the-new-lambda/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## TL;DR
托管智能体的核心诱惑是“把 agent 从本机搬进云端”，但真正的战略风险是把 agent primitive、工作流状态、权限模型和计费路径一起交给前沿模型厂商；短期像 Lambda 一样省事，长期可能像 Lambda 一样难迁移。

## 核心主张拆解
云端托管 agent 的价值很实在：它可以 24/7 后台运行、接收 webhook/email 等外部事件、由供应商负责系统补丁与运行环境，并通过沙箱只暴露被授权资源。对已经把 Claude Code、Codex、OpenCode 跑在服务器 Docker 里的团队来说，这不是全新范式，而是 frontier labs 把已有工程模式产品化。

作者认为 agent harness 本身并不难替换：本质都是“prompt + context + tools + logs/output”的执行外壳。真正难迁移的是托管平台周边沉淀的数据、权限、工作流、触发器、运行假设和组织习惯。类比 AWS：容器工作负载跨云迁移相对直接，Lambda 迁移却常常要花数月拆解代码与平台假设。

Anthropic 的 Claude plan 调整强化了这个判断：非交互式 Claude Code，包括绝大多数云端 agent 用法，不再消耗订阅 token allowance，而是进入新 credit/API token 计费路径；作者估计重度非交互使用者可能面对 5–20 倍成本上升。价格规则一变，托管 agent 的“方便”就暴露出供应商定价权。

## 可行方案
最稳妥的短期方案是自建托管基础设施：用 Docker 运行 agent harness，例如 OpenCode，并保持模型供应商可替换。这样团队能把 agent 放进现有安全边界内，同时积累对 agent primitives 的组织能力，而不是过早外包掉关键知识。

第二条路是使用中立或多模型托管平台，例如 Cloudflare Agents、Vercel、AWS AgentCore、Azure AI Foundry、GCP Vertex AI Agent Engine 等。问题是市场变化太快，质量、抽象边界和长期锁定风险还没有稳定结论。

## 值得质疑
作者的判断依赖一个前提：agent harness 的核心能力会继续保持可替换。如果 frontier labs 把新模型能力、专属工具、上下文管理、权限系统或多 agent 编排只放在自家托管平台里，迁移成本就不只是工作流问题，而会变成能力差距问题。

另一个薄弱点是自建方案对非工程团队并不便宜。Docker 化 agent 对开发者“并不难”，但安全隔离、审计、密钥管理、权限最小化、队列与失败恢复都需要真实运维能力；自建不是免费选项，只是把锁定风险换成组织能力建设成本。

## 收束
这篇文章最有用的提醒不是“不要用托管 agent”，而是：现在还太早把 agent 运行层当成普通 SaaS 外包；在平台边界未稳定前，保留可替换性本身就是战略资产。
