---
title: "AI Is Too Expensive"
date: 2026-05-21T05:49:55Z
category: reading
description: "这篇文章的核心判断不是“AI 成本偏高”，而是整条生成式 AI 经济链条仍靠资本补贴、云厂商循环交易和企业端 token 狂欢维持表面增长。一旦企业开始认真压缩 token 预算，OpenAI/Anthropic 的收入增长、hyperscaler 的 RPO 叙事、GPU/data center capex 的..."
source: "https://www.wheresyoured.at/ai-is-too-expensive/"
---

## TL;DR
这篇文章的核心判断不是“AI 成本偏高”，而是整条生成式 AI 经济链条仍靠资本补贴、云厂商循环交易和企业端 token 狂欢维持表面增长。一旦企业开始认真压缩 token 预算，OpenAI/Anthropic 的收入增长、hyperscaler 的 RPO 叙事、GPU/data center capex 的回收逻辑会同时承压。

## 核心主张拆解
作者认为 hyperscaler 的 AI 投资已经进入无法用现有收入解释的量级。微软、Google、Amazon、Meta 过去三年投入超过 8000 亿美元，2026 年还计划增加约 7000 亿美元，2027 年可能再增加 1 万亿美元；这意味着 AI 专属收入至少要达到 3 万亿美元才能回本，若要产生像样回报，可能需要 6 万亿美元以上。

微软是文章的主要样本：庭审证词显示微软与 OpenAI 相关投入约 1000 亿美元；自 FY2023 起微软 capex 总额约 2938 亿美元，其中约 30% 可能用于 OpenAI 基础设施。作者估算微软 FY2025 AI 收入约 179 亿美元，只相当于当年 capex 的不到五分之一，而且还没计入电力、维护、税费、保险和融资成本。

文章反复强调“run rate 不是收入”。微软宣称 AI revenue run rate 为 370 亿美元、Amazon 宣称 150 亿美元，但这些是把单月数据年化后的表达，无法证明实际累计收入、毛利率、留存或现金流。若 AI 业务真的强，厂商会披露收入与利润；现在的沉默本身就是信息。

## 算力需求的循环结构
作者最强的结构性论点是：hyperscaler 的 AI backlog 很大一部分来自 OpenAI 和 Anthropic，而这两家公司本身又依赖 hyperscaler、NVIDIA 和 VC 资金续命。微软 RPO 从 3920 亿美元跳到 6250 亿美元，主要由 OpenAI 的 2500 亿美元 Azure 承诺和 Anthropic 的 300 亿美元承诺推动；Amazon RPO 从 2440 亿美元到 3640 亿美元，包含 OpenAI 1000 亿美元扩展承诺；Google RPO 从 2428 亿美元到 4676 亿美元，核心驱动是 Anthropic 据称 2000 亿美元 TPU/compute 承诺。

这意味着真实的外部需求可能远弱于表面数字。若 AI compute 需求真的来自广泛企业市场，RPO 应该出现多个 OpenAI/Anthropic 级别客户，而不是集中在两个持续亏损、持续融资的 AI lab 上。作者因此判断：Amazon 需要再造一个 AWS，微软需要再造一个 Azure，Google 需要至少半个 Search 体量的新业务，才可能覆盖当前 capex。

AI lab 端也没有更好的答案。作者引用 OpenAI 预计到 2030 年累计烧钱 8520 亿美元、Anthropic 截至 2026 年 3 月收入超过 50 亿美元但 inference/training 花费 100 亿美元、Anthropic 未来数年对 Google/Amazon/Microsoft 的云承诺约 3300 亿美元。若再加 xAI、CoreWeave 等 compute 交易，Anthropic 四年内可能需要 3800 亿美元以上才能履约。

## 客户侧压力
企业 token 支出正在从“试验成本”变成失控的 operating expense。ServiceNow、Uber 等公司几个月就烧穿年度 API token 预算；Salesforce 计划 2026 年花 3 亿美元买 Anthropic tokens；Stripe 约 5000 名技术人员平均每天烧 9.4 万美元、每月 280 万美元，年化约 3360 万美元。Goldman Sachs 口径下，AI 成本已经接近 headcount 成本的 10%，并可能继续上升。

Zillow 是文章中的极端案例：2026 Q1 AI 服务花费超过 100 万美元，4 月在 Cursor、Anthropic 和 AWS Bedrock 上花了 74.9 万美元，年底可能达到 700 万到 1000 万美元；这相当于其 2025 年 2300 万美元净利润的相当大比例。更糟的是，AI 没有减少工程负担，反而让需人工 review 的输出增加近 50%，PR 与部署增加 39%，每月多出 2.9 万小时 review 负担，约等于每名工程师多 19 小时。

作者把这解释为企业管理层把“使用 AI”当成指标，而非把产出质量、成本或 ROI 当成指标。token 预算难以管理，因为同一任务在不同模型、不同上下文、不同用户下消耗不稳定；“每天用 AI”“多烧 token”“多开 PR”这类 KPI 又天然可被员工或团队 gaming。

## 更深层批判
文章后半段的判断更社会学：生成式 AI 之所以能扩散，不是因为它已经证明了经济性，而是因为它非常适合被不理解具体工作的管理层误读为“工作本身”。LLM 会给出看似积极、可执行、不会拒绝的回应，能生成 PRD、demo、deck 和代码片段，正好满足管理层对“速度”和“服从”的想象。

因此，作者认为 AI 不是单纯的技术泡沫，而是管理层无知、资本过剩、媒体叙事和平台补贴共同制造的泡沫。它把成本外部化给企业预算、工程 review、云基础设施、电力系统和最终投资人，同时把“必须采用，否则落后”的语言包装成必然性。

## 值得质疑
文章证据密度高，但大量关键数字来自作者估算、匿名来源、媒体报道和公司披露的再解释，需要单独核验。尤其是 AI revenue run rate、RPO 归因、Anthropic/OpenAI cash burn、企业 token 支出等数据，方向上有参考价值，但不能直接当作 audited financials。

文章也有明显的总括风险：它把消费级 LLM 订阅、企业 coding agent、云 compute、模型训练、inference、传统 AI automation 混成一个“大 AI 经济性”问题。若存在更窄、更低成本、更可计量的 AI workflow，它们不一定被同一套泡沫逻辑完全覆盖。

## 最后留下的判断
判断 AI 泡沫是否破裂，关键不是看模型能力继续进步多少，而是看三件事：hyperscaler 是否开始披露 AI 收入和毛利，企业是否削减 token 预算，OpenAI/Anthropic 是否必须以越来越高频率融资或签更大的 compute 承诺。能力叙事可以继续膨胀，但现金流会先说真话。
