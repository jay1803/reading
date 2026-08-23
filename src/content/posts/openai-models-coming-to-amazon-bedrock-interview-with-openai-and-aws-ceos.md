---
title: "OpenAI models coming to Amazon Bedrock: Interview with OpenAI and AWS CEOs"
date: 2026-04-30T08:02:48Z
category: reading
author: "Ben Thompson"
description: "Sam Altman：OpenAI CEO；对话中代表 OpenAI 解释与 AWS 共建 Bedrock Managed Agents、Codex/agent runtime、模型供给与定价方向。"
source: "https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/"
---

## 嘉宾背景
- Sam Altman：OpenAI CEO；对话中代表 OpenAI 解释与 AWS 共建 Bedrock Managed Agents、Codex/agent runtime、模型供给与定价方向。
- Matt Garman：AWS CEO；从 AWS 云计算、AgentCore、Bedrock、Trainium、企业安全与合作伙伴生态角度解释这次合作。
- Ben Thompson：Stratechery 作者/主持人；核心追问是 OpenAI-AWS 合作是否只是分销，还是新的企业 agent 平台控制点。

## TL;DR
OpenAI 进 AWS 的关键不只是“多一个云渠道”，而是企业 AI 的价值重心正在从模型 API 迁移到“模型 + harness + 身份/权限/状态/审计 + 企业数据边界”的托管 agent runtime；谁能把这个复杂层做成可信基础设施，谁就可能掌握下一代企业软件的集成点。

## Microsoft 放松独占是在保护 OpenAI 投资，而不是单纯削弱 Azure
微软新协议保留了 OpenAI 产品优先上 Azure、OpenAI IP 授权到 2032、微软继续作为大股东等核心利益，但 OpenAI 可把产品服务到任意云，微软对 OpenAI IP 的授权转为非独占，微软也不再向 OpenAI 支付 revenue share。Thompson 的判断是：Azure 独占曾是差异化优势，但当企业更在意“在现有云里用模型”时，独占反而限制 OpenAI 增长，并让 Anthropic 在多云企业市场获得机会。微软接受稀释 Azure 差异化，是为了让自己持有的 OpenAI 股权资产继续扩张。

## Bedrock Managed Agents 的差异点是托管 agent，而不是裸模型入口
这次产品不是简单把 OpenAI API 放进 Bedrock，而是“Bedrock Managed Agents, powered by OpenAI”：OpenAI frontier models 被封装进 AWS-native agent runtime，包含身份、权限、状态、日志、治理、部署与 VPC 内数据边界。Garman 说它复用了 AgentCore 的记忆、安全执行环境、permissioning 等原语，但把这些原语与 OpenAI 模型共同产品化；Altman 明确说这是 AWS 独家合作，并且客户数据留在 AWS/Bedrock 环境中，AWS 是一线支持入口。

## 模型与 harness 会越来越不可分，企业 agent 的控制点就在这里
Altman 认为 model 和 harness 已经很难完全分开：Codex 的效果来自模型能力、工具调用、状态、提示、post-training 与运行环境的共同作用。早期需要靠系统提示硬挤出的行为，会随着模型变强被吸收到模型能力里；但在当下，真正让 agent 可用的是 harness 把模型接入工具、记忆、权限和企业环境。非直觉点是：企业买的不是“更聪明的文本补全”，而是一个可以在组织内部安全执行工作的虚拟同事系统。

## 本地 Codex 是过渡形态，云端企业 agent 需要重做身份与权限原语
Altman 承认 Codex 先回到本地，是因为本地环境天然拥有代码、文件、凭证与上下文，短期更容易跑通；但长期 agent 需要在云端运行，才能扩展、协作、持久执行并纳入企业治理。对话中最尖锐的问题是身份模型：agent 该直接使用员工账号，还是拥有独立账号，还是“以 Ben 身份登录但标记为 agent”？Altman 说行业甚至还没有合适原语。Garman 的回答是 AWS 能用 VPC、IAM、网关、角色和审计等 20 年企业安全积累，把 agent 放进可控边界里。

## AWS 的“不全栈拥有”在推理时代反而可能是平台优势
Google Cloud 的叙事是从芯片、模型到 agent 层的全栈整合；AWS 的叙事是基础设施和平台层开放，向上拥抱合作伙伴。Garman 说 AWS 从一开始就把合作伙伴成功视为自己成功，Bedrock 也延续多模型、多能力的策略。这里的战略含义是：当训练时代偏向垂直整合时，AWS 似乎缺少 frontier model；但当企业推理和 agent 部署成为主战场，AWS 的客户关系、数据驻留、权限体系和中立平台位置可能让它更容易“在中间接住”OpenAI。

## AI 定价会从 token 走向“完成工作的智能单位”
Altman 把 OpenAI 描述为 intelligence factory，而不是 token factory：客户真正关心的是以最低价格获得最好、最多的智能，不关心背后是更大模型少 token、小模型多 token、GPU、Trainium 还是其他路径。他还指出 GPT-5.5 的单 token 成本更高，但完成同等任务需要少得多的 token，所以 token pricing 长期并不自然。更重要的是，OpenAI 目前听到更多的是“无论价格给我更多容量”，而不是压价，说明 frontier intelligence 的需求仍由能力和供给约束主导。

## 真正待建的是企业 agent 管理层和数据中间层
Thompson 提出企业内部可能需要一个 middleware：向下连接数据库、SaaS、文件系统和权限系统，向上支撑用户面对的 agent workspace。Altman 同意客户需求正在收敛成三件事：agent runtime、连接企业数据并管理 token/支出的管理层、员工使用的 workspace。非直觉推断是：短期会出现多层 agent 架构，甚至有 agent 维护中间层；长期若模型足够强，现有架构可能被重新设计，今天的中间件只是过渡。

## 值得质疑
- OpenAI 与 AWS 都强调这不是单纯分销，但对产品具体能力、落地时间、可靠性边界和责任划分细节仍偏概念化。
- “客户数据留在 AWS”解决了数据驻留叙事，但没有完全回答 OpenAI 在模型运行、调试、质量改进中能看到什么级别的元数据或错误上下文。
- “智能需求几乎无限”成立于能力持续快速提升和价格快速下降的前提；一旦企业 ROI、合规或流程重构成本成为瓶颈，需求弹性可能低于 Altman 的表述。

## 收束
这场对话最值得盯的不是 OpenAI 是否终于进入 AWS，而是企业软件可能出现一个新基础层：agent 不再是应用里的功能，而是需要身份、权限、状态、审计、预算和数据通道共同支撑的运行环境。
