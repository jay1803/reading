---
title: "The dire state of B2B marketing attribution"
date: 2025-05-08T10:33:32Z
category: reading
description: "Touch-based归因的根基正被法律主动拆除：GDPR/CCPA要求用户主动授权追踪，Chrome/Safari/ATT已系统封锁第三方Cookie与跨app数据，可能让70%的流量永久不可追踪。B2B还在争论last-touch vs multi-touch，其实是在赌一套正在消失的基础设施。"
source: "https://www.elenaverna.com/p/the-dire-state-of-b2b-marketing-attribution"
---

## TL;DR
Touch-based归因的根基正被法律主动拆除：GDPR/CCPA要求用户主动授权追踪，Chrome/Safari/ATT已系统封锁第三方Cookie与跨app数据，可能让70%的流量永久不可追踪。B2B还在争论last-touch vs multi-touch，其实是在赌一套正在消失的基础设施。

## 核心主张拆解
B2B归因的现状大致分五级：无归因（标"直接"敷衍了事）→ 线索层级归因（Hubspot/Marketo源报告）→ last-click → 自报调查（"您从哪得知我们？"）→ 手动主观分配。结构性原因：数据量少（难做统计）、购买旅程复杂（$10万软件决策 vs $10外卖）、涉及采购委员会（用户/影响者/决策者各有权重）、还要同时追踪多种获客目标（新品牌用户、存量客户扩展、企业买家）。

Touch-based归因有两个根本问题：一是天生偏向"产生数字触点"的渠道（SEM/SEO），间接渠道和线下渠道完全隐形，而实际上95%的潜在买家当前并不在市场中；二是被法规系统性终结——Cookie死亡、ATT、Android Privacy Sandbox已让移动端触点归因实际作废，GDPR/CCPA则让70%的流量面临不可追踪的法律风险。

MMM通过聚合时间序列数据（而非用户级追踪）建立回归模型，将总销售额分解为各渠道增量贡献、季节性、品牌资产等因子，进而做场景预测和预算优化。优势：覆盖线下和间接数字渠道；不依赖第三方数据；无渠道偏见。Asana案例：增加YouTube投入后注册量上升的相关性即可确认渠道价值，无需点击归因。

## 值得质疑
MMM同样有数据量门槛——B2B数据量少是全文反复强调的痛点，但MMM在稀少数据下如何保证统计显著性，文章没有正面解答。作者明确注明投资了 Paramark（文章主要推荐的工具），存在利益冲突。

## Google 这笔账
Google默默发布MMM方法论、开源代码，却从不主动推广——因为普及MMM意味着稀释SEM/SEO的垄断价值。这个动机冲突，是整篇文章最值得记住的一笔。
