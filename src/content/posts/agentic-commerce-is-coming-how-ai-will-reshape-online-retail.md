---
title: "Agentic Commerce is Coming: How AI Will Reshape Online Retail"
date: 2025-06-18T22:09:26Z
category: reading
author: "Tanay Jaipuria"
description: "AI 接管购物漏斗的每一环（发现→比价→谈判→下单），不只是 UX 升级——它让整套现有基础设施的前提假设（买家是人类）失效，从商品目录格式到支付管道到售后支持，都需要从底层重建。"
source: "https://www.tanayj.com/p/agentic-commerce-is-coming-how-ai"
---

## TL;DR
AI 接管购物漏斗的每一环（发现→比价→谈判→下单），不只是 UX 升级——它让整套现有基础设施的前提假设（买家是人类）失效，从商品目录格式到支付管道到售后支持，都需要从底层重建。

## 核心主张拆解
电商已占全球零售约 20%（约 6 万亿美元），其发现渠道从 Google → Amazon → TikTok 每隔几年完成一次迁移，Agentic Commerce 是下一次迁移，且覆盖整个漏斗而非仅发现环节。

作者给出了一个六层 stack 的机会地图：
- **宽口 Agentic 平台**（ChatGPT、Claude、Perplexity、Meta AI）：作为消费者购物意图的聚合入口，最终可能直接向商家要求 agent-ready 目录标准；
- **垂直商业平台**（Amazon Rufus、Daydream、Phia）：在特定品类提供更深度的推荐与专业知识；
- **商品目录基础设施**（Zinc、Velou、Shopify Catalog）：向 agent 提供结构化、实时、可机读的 SKU 数据，目前尚不清楚最终是第三方聚合商还是平台自定义标准胜出；
- **交易与支付**（Stripe Order Intents API、Visa Intelligent Commerce、Firmly、Skyfire）：Bot 历来是支付反欺诈系统的打击对象，现在需要区分"被授权的 agent"与恶意 bot；
- **商家可见性与优化**（Profound、Bluefish、Evertune）：类比 SEO，帮助品牌在 AI 引擎的推荐结果中提升排名；
- **售后体验**（Loop、Aftership、Gorgias）：退换货、物流追踪、客服支持将在 AI 对话界面内发生，而非商家自有网站。

当前各平台（OpenAI Shopping、Google Agentic Checkout、Perplexity Buy with Pro）均处于极早期，支持的 SKU 数量有限，尚未形成完整闭环。

## 反驳或薄弱处
文章对六层机会的描述停留在"哪类公司在做"层面，缺乏对竞争动态的深入分析——尤其是：宽口平台（ChatGPT 等）本身就有动机向下游延伸吞并商品目录、支付、可见性等层，对初创公司而言，哪些层是平台不愿自建或无法做好的"剩余空间"，文章没有给出答案。

## 当 Bot 变成合法买家
支付系统把 bot 当欺诈信号是持续了几十年的铁律；Agentic Commerce 要求在不开放欺诈漏洞的前提下，将"被授权的 agent 身份"嵌入信用/支付协议——这比重写结账页面难得多，也是整个 stack 中技术摩擦最大的一层。
