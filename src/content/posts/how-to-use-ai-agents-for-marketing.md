---
title: "How to use AI agents for marketing"
date: 2025-11-19T08:34:44Z
category: reading
author: "Kate Syuma"
description: "SafetyCulture 最大的 AI 成果来自数据聚合，而非 AI 自动化本身：把五个第三方 enrichment 平台并行调用、AI 事实核查后，覆盖率接近 100%——这个底座没打好，所有下游个性化都是对错误数据的精准操作。"
source: "https://www.growthunhinged.com/p/how-to-use-ai-agents-for-marketing"
---

## TL;DR
SafetyCulture 最大的 AI 成果来自数据聚合，而非 AI 自动化本身：把五个第三方 enrichment 平台并行调用、AI 事实核查后，覆盖率接近 100%——这个底座没打好，所有下游个性化都是对错误数据的精准操作。

## 核心洞见
四个 workflow 底层逻辑一致：先喂给 AI 足够多的上下文，再让它生成个性化输出。

- **Waterfall Enrichment**：串行调用 5 个 provider 直到数据充分，另一个 agent 对照官网、LinkedIn、OSHA API 做事实核查 → enrichment 覆盖近 100%，消除数百小时手工研究
- **AI Inbound BDR**：从 Salesforce 拉基础信息 + HubSpot 页面行为 + ZoomInfo 就职历史 + Redshift 同行业历史客户案例 → 生成个性化邮件加入 Gong Engage flow → 会议预约率 3x，机会创建 2x
- **Feature Recommender**：Databricks 上用 RAG 建立 300+ 使用场景，每日跑分存入 Redshift，生成 2500+ 文案变体动态插入生命周期邮件 → 新功能采用率 +10%
- **AI Copilot Layer**：Retool 在现有 SaaS 系统上叠一层统一界面，自动生成 SPICED 销售框架、AE 可直接查账户所有数据 → 线索转机会率 +25%，每次交接节省 30 分钟

## 具体机制
Enrichment、序列化外联、lifecycle 个性化、销售 copilot 工具市面上都有现成品。SafetyCulture 的差异在于自建 orchestration 层把碎片化 SaaS 数据打通——换的不是工具，是工具之间的胶水层。

## 隐藏限制
- 早期 hallucination 问题真实存在；靠缩小 AI 输出类别（scope）而非升级模型来提高一致性
- 每次 reply 都触发 AI enrichment 成本过高 → 只对高潜力客户优先跑 AI query
- 实时调用偶发超时 → 改为批量运行 + 缓存结果，下游营销平台直接查映射表

这套 workflow 的真正起点不是 AI，是数据治理。data hygiene 做不好，AI 只是更快地联系到错误的人。
