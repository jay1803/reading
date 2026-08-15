---
title: "the end of tokenmaxxing"
date: 2026-06-27T08:04:38Z
category: reading
description: "对话者 Augusto Marietti 是 Kong 的联合创始人兼 CEO。Kong 有约 1000 人，运营于 28 个国家，80% 是全球 2000 强企业客户。公司起点是 API 市场（GitHub for APIs），2015 年转型为开源 API 网关，目前演进为企业级 AI 网关。"
source: "https://newsletters.feedbinusercontent.com/734/734aa140c53937e078e7768e1eb1e74b19a783e2.html"
---

## AI 网关是三个不同市场，Kong 做的是最不性感但最值钱的那个

对话者 Augusto Marietti 是 Kong 的联合创始人兼 CEO。Kong 有约 1000 人，运营于 28 个国家，80% 是全球 2000 强企业客户。公司起点是 API 市场（GitHub for APIs），2015 年转型为开源 API 网关，目前演进为企业级 AI 网关。

## "模型路由"一词掩盖了三个本质不同的生意

- *Costco/仲裁层*：OpenRouter，对 LLM 批发定价进行仲裁，抽 5% 经纪费。Grok 等模型在 OpenRouter 上以折扣价上架是为了走量。Cloudflare/Vercel 的公共网关本质相同，都是仲裁利润，而非代理本身。
- *防火墙后的企业网关*：Kong 的市场。60% 的企业现在使用 7 个以上 LLM，管理这个蔓延是核心需求。不上社交媒体，但非常赚钱，接近 Palantir 式的大企业生意。
- *LiteLLM/Portkey*：Python 框架起家，日均调用量超过 10 亿后误码率和延迟开始恶化。LiteLLM 安全事件后，一周内 50 家企业主动来找 Kong。

## Token 成本反而成为企业 AI 网关的最佳推销员

2022 年以来顶级前沿模型的 token 成本下降了 25%，但总支出上涨了 700 倍——原因是 agent 每个任务消耗的 token 是 chatbot 时代的 10 倍（大 context window + reasoning chain + 多步 tool loop）。10,000 名员工发送中等复杂度的 prompt，通过网关将其语义路由至更便宜的模型，可帮企业节省数千万美元。没有路由层的结果：所有请求默认打到最贵的模型。

## MCP 是 AI 网关的杀手级用例

Kong 的 MCP 网关在 11 个月内增长了 11 倍。Marietti 把 MCP 描述为"API 的 Duolingo"——让 API 说自然语言。机器对机器的场景不需要 MCP，直接用 API 或 SDK；只要有自然语言介入就需要 MCP。Kong 做的是 MCP 服务器群的托管层，提供认证、治理、日志和分析能力，让 CIO/CISO/CTO 对 AI 流量有控制权。A2A 协议更新，未来还会有更多协议涌现，但 GUI→程序化接口的转向是主线。

## Anthropic 收购 Stainless 背后的逻辑不是 SDK 收入

Stainless SDK 本身营收可能只有几百万，不是重点。Marietti 的判断：Stainless 被 OpenAI、Grok 等广泛使用，收购的真正目的是获取 SDK 使用元数据——这些数据可以直接反哺 Claude Code 等 agentic coding 工具的改进。

## 未来 AI 货币化是计量问题，不是计费问题

Marietti 认为"AI 货币化的核心不是 billing，是 metering"：token/毫秒、token/瓦特。Kong 收购 OpenMeter 正是为此。OpenMeter 一半的客户根本不做 API 业务，只是需要计量层。最终他认为所有收入都会直接或间接变成 token 收入；outcome-based pricing 仍需 5~10 年才能在复杂场景成熟。

## 企业 agent 真正落地还需 3 年

原因不是模型智能不够（benchmark 分数在快速提升），而是多步 API tool calling 的准确率仍只有 17%，两三年来几乎没有改进。每个 SaaS 系统各自封闭，没有统一认证/授权/系统记录。Forward-deployed engineering 正在爆火，正因为企业内部复杂性（55,000 个办公室、75 个数据仓库）无法靠一个聪明模型自动消解。垂直 agent（Ashby for 招聘、Pigment for FP&A）各自为阵，跨职能的真正 agent 工作流仍不存在。

## 长期愿景："API 和 Agent 的 eBay"

Kong 的路径：从代理流量（API 网关→AI 网关）→ 积累足够多 API 供给形成系统记录 → 把这个供给变成面向 agent 需求的市场。届时 agent 只需一个钱包，Kong 在底层处理 API 密钥、计费和配置。先建供给再开市场，这是为什么过去几年要先做基础设施的原因。从 Kong 网关流量的匿名数据来看，Anthropic 在企业使用中明显领先于其他模型。
