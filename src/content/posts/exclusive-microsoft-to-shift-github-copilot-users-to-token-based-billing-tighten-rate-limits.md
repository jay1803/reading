---
title: "Exclusive: Microsoft To Shift GitHub Copilot Users To Token-Based Billing, Tighten Rate Limits"
date: 2026-04-22T08:01:29Z
category: reading
description: "GitHub Copilot 的核心转向不是“多收一点钱”，而是微软承认 AI 编程助手已经无法继续靠统一订阅价掩盖算力差异：Copilot 正从 SaaS 订阅品，变成按 token 计量的算力转售业务，低价用户补贴时代正在结束。"
source: "https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/"
---

## TL;DR
GitHub Copilot 的核心转向不是“多收一点钱”，而是微软承认 AI 编程助手已经无法继续靠统一订阅价掩盖算力差异：Copilot 正从 SaaS 订阅品，变成按 token 计量的算力转售业务，低价用户补贴时代正在结束。

## 关键变化
- 微软计划暂停 GitHub Copilot Student 与个人付费层的新注册，并暂停个人付费试用。
- Pro、Pro+、Business、Enterprise 都会继续收紧 rate limits；最便宜的 Pro 套餐将移除 Anthropic Opus 家族模型。
- 内部文件称 GitHub Copilot 的周运行成本自今年 1 月以来几乎翻倍，token-based billing 因此从长期方向变成紧急优先级。
- Opus 4.7 虽然上线，但 7.5x request multiplier 的本质是把昂贵模型的真实成本显性化，用户会更快耗尽额度。

## 背后逻辑
- 现有的“request”体系本质上已经是伪装后的成本分层：不同模型通过不同 multiplier 消耗不同额度，只是还没把 token 成本直接摊到用户账单上。
- 一旦改成 token 计费，prompt 长度、输出长度、推理链开销就会直接决定价格，微软等于把模型成本重新绑定到用户行为本身。
- 这和 Anthropic 把企业客户推向 token billing 是同一条线：前沿模型公司不想再做无限补贴的订阅生意，而要把 compute 成本尽可能传导给终端客户。

## 更大意义
- AI coding 产品的竞争会从“谁功能更多”转向“谁能压低单位算力成本、控制滥用、设计更细颗粒的定价层级”。
- 便宜套餐会越来越像入口层，只保留轻量模型和更严的配额；真正高端能力会被重新定价，而不是继续塞进统一月费。
- 最近行业里频繁出现的模型下架、倍率调整、限额收紧，本质不是产品小修小补，而是商业模式开始对不上账。

## 值得质疑
- 报道基于泄露的内部文件，正式生效时间、最终 token 定价方案、各层级限额细节都还没有公开。
- 文章把 Copilot 的成本压力上升推演成“补贴时代结束”的行业拐点，这个方向大概率对，但微软会走多快、走多彻底，仍取决于竞争压力和用户流失风险。

## 收束行
当 AI 产品开始把“每次调用烧掉多少算力”明码标价时，所谓 AI SaaS 就会越来越像电力计费：订阅还会存在，但真正定义毛利、用户分层和产品边界的，将是每一个 token 的成本。

## 模型
GPT-5.4
