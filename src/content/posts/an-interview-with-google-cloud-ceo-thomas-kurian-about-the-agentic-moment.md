---
title: "An Interview with Google Cloud CEO Thomas Kurian About the Agentic Moment"
date: 2026-04-24T08:01:56Z
category: reading
description: "Thomas Kurian 是 Google Cloud CEO，2018 年加入 Google；此前在 Oracle 工作 22 年，曾任产品开发总裁。本次访谈由 Stratechery 的 Ben Thompson 主持，发生在 Google Cloud Next 2026 keynote 前，核心讨论 Go..."
source: "https://stratechery.com/2026/an-interview-with-google-cloud-ceo-thomas-kurian-about-the-agentic-moment/"
---

# BEGIN_OPENCLAW_SUMMARY
## 嘉宾背景
Thomas Kurian 是 Google Cloud CEO，2018 年加入 Google；此前在 Oracle 工作 22 年，曾任产品开发总裁。本次访谈由 Stratechery 的 Ben Thompson 主持，发生在 Google Cloud Next 2026 keynote 前，核心讨论 Google Cloud 如何理解“agentic moment”、Gemini 企业化、TPU 供给、跨云数据与生态伙伴。

## TL;DR
Kurian 的核心叙事不是“Gemini 单点赢过所有模型”，而是 Google Cloud 已经把模型、企业流程、数据语义、安全、TPU 经济性和客户反馈环打成一个闭环。真正的赌注是：企业 agent 的难点会从 demo 能力转向身份、权限、审计、数据上下文、成本和流程变体；如果这个判断成立，Google 的大公司复杂性反而会变成训练与产品化优势。

## 企业 agent 的门槛从聊天能力转向可控执行
Kurian 认为 2026 年的变化来自三件事同时成熟：Gemini 推理能力增强、长流程记忆变强、工具 / skill / MCP 等外部交互抽象成熟。企业客户不只是要 chatbot，而是要让模型自动化多步骤业务流程，例如 Citi 的财富顾问、Comcast 的维修排期与技师派单。

这里最关键的非直觉点是：约束多并不会让 agent 更简单，反而要求模型更强。企业流程里存在大量无法预先穷举的异常分支，模型必须能围绕目标生成临时代码、调用工具、维护状态，并在库存、日历、工单、权限等系统之间完成闭环。

## Google 的优势被定义为“从客户流程到 DeepMind 的反馈环”
Kurian 反复强调 Google Cloud 与 DeepMind 的关系非常紧：客户流程会进入 Gemini 的 harness 和强化改进循环，Google 内部产品也在同一天、同一小时使用同一版本 Gemini 与同一 harness。他用这个回应 Ben 对“大公司会不会被 50 个方向拉散”的质疑。

这套说法把 Google 的全栈优势拆成四层：模型改进循环、经典计算与 TPU 基础设施、面向企业数据的 Knowledge Catalog、以及 cyber / Wiz 体系。Google Cloud 想证明的不是“我们也有模型”，而是“企业 agent 每一步需要的上下文、安全和算力都在同一平台里”。

## TPU 不是 Gemini 的附属品，而是独立利润与供给杠杆
Kurian 明确表示 Anthropic 等实验室使用 Google TPU 并不与 Gemini 零和。Google 可以在不同层变现：卖 TPU 训练 / 推理能力、卖 Gemini、卖 cyber 保护、卖完整平台。更大的 TPU 规模还能平滑消费业务的日内波动，提高利用率，并通过供应链规模降低成本。

访谈里披露的硬信息包括：Gemini 当前生成 160 亿 tokens/min，比上一季度增长 40%；Gemini Enterprise 环比增长 40%；Google 将推出 TPU 8t（训练优化，单 pod 9600 芯片，性能约 3 倍于上一代）和 TPU 8i（推理优化，1152 芯片，3 倍 SRAM，引入 Collectives Engine）。Google 还准备把 TPU 放到客户或第三方场地，服务资本市场、HPC、能源建模等低延迟或数据不可迁移场景。

## 跨云策略承认企业现实：数据不会因为 AI 全部搬家
Google 的 cross-cloud lakehouse 不是要求客户把 AWS、Azure、SaaS 里的数据搬到 GCP，而是让 BigQuery / Gemini 能在数据原地进行分析。Kurian 把问题定义为 custody 与 egress cost：企业要跨云分析，但不想复制全部数据，也不想为每个云买一套安全和分析工具。

Knowledge Catalog 的角色是把“数据在哪里、字段是什么意思、API 如何对应业务概念”变成 Gemini 可引用的语义层。Kurian 声称这不等同于 Palantir 式人工 ontology 项目，而是利用 Gemini 读取文档、API specs 和数据库结构来自动建立映射。这个判断如果成立，会显著降低 enterprise AI 落地成本；如果不成立，Google 仍会遇到大量现场集成与语义清洗工作。

## Google 对生态的回答是“卖 agent 平台，不吃掉所有 ISV”
Ben 提出一个关键问题：模型会不会吞掉所有 SaaS，让其他公司只剩系统记录层？Kurian 的回答是否定的。他说 Google 会让第三方 SaaS / ISV 嵌入 Gemini 模型和 agent platform，因为这些公司需要身份、策略、审计、registry、数据出境防护和低成本推理，而不一定要自己重建底层 plumbing。

这也是 Google 与 OpenAI / Anthropic 叙事的差异：Google Cloud 不只卖一个面向终端用户的智能入口，而是试图成为企业 agent 生态的基础设施层。其可信度来自企业级控制能力与 TPU 成本结构，而不是单纯来自模型体验。

## 值得质疑
Kurian 对 Gemini agent 能力的证明主要依赖客户案例、token 用量和财务结果，缺少与 Claude / Codex / OpenAI agent 体系的独立横向比较。Knowledge Catalog 的自动化程度也可能被乐观化：真实企业数据命名混乱、权限复杂、历史系统割裂，未必能仅靠 Gemini 快速完成高质量语义映射。

另一个未完全展开的问题是算力分配。Kurian 说 Google 在 Gemini、内部产品、外部 TPU 客户之间做 balanced portfolio，并认为这不是简单零和；但在 compute 长期短缺环境下，资本、芯片、数据中心和顶尖工程注意力仍会形成真实取舍。

## 收束
这场访谈最有边缘感的一点是：Google Cloud 的关键资产可能不只是 TPU 或 Gemini，而是 Kurian 过去几年把它改造成真正 enterprise company 的组织能力；AI 时代会奖励能把企业混乱转化为模型反馈、平台控制面和基础设施收入的公司。
# END_OPENCLAW_SUMMARY
