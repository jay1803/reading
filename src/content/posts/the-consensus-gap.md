---
title: "The Consensus Gap"
date: 2026-05-12T08:01:38Z
category: reading
author: "Kevin Indig"
description: "AI 搜索可见度的关键误区不是“谁排名更高”，而是把 ChatGPT、Perplexity、Google AI Overviews 当成同一套分发系统。Omnia 对 3.7M 次 URL citation 的数据表明，只有约 2.37% 的 cited URL 会在三个引擎里同时出现，约 91.07% 只出现在..."
source: "https://www.growth-memo.com/p/the-consensus-gap"
---

## TL;DR
AI 搜索可见度的关键误区不是“谁排名更高”，而是把 ChatGPT、Perplexity、Google AI Overviews 当成同一套分发系统。Omnia 对 3.7M 次 URL citation 的数据表明，只有约 2.37% 的 cited URL 会在三个引擎里同时出现，约 91.07% 只出现在一个引擎；所以单一 blended AEO score 会把真正的风险——引擎集中度与不可迁移性——压扁掉。

## 发现
- 跨引擎共识极低且稳定：多组样本里 universal overlap 基本在 2.35%–2.45% 之间，engine-exclusive citation 约 91%。Q3 2025 到 Q4 2025 / Q1 2026 有轻微收敛，universal overlap 从 2.2% 升到 2.7%，exclusive citation 从 90.1% 降到约 88%，但碎片化仍是主结构。
- 商业意图并没有显著提高共识：commercial prompt 的 universal overlap 为 2.4%，informational prompt 为 2.0%。即使“best CRM / best project management software”这类高意图问题看似答案池更窄，各引擎仍主要按自己的 retrieval logic、信任源和格式偏好取材。
- 页面类型只带来很小差异：guides/tutorials 的 cross-engine overlap 最高，也只有 2.3%；blogs 1.8%，category pages 1.6%，product pages 1.2%，homepages 1.1%。解释型、教学型内容相对更能迁移，但绝对水平仍很低。
- 高频引用不等于可迁移：Wikipedia 在数据集中出现 16,073 次，但 universal overlap 只有 1.3%；Reddit 出现 14,267 次，只有 0.1%；Reuters 出现 1,202 次，仍是 0.0%。LinkedIn、TikTok、Facebook、Quora 等 UGC / social 平台也几乎没有跨引擎可迁移性。

## 为什么重要
- 一个品牌可以在 aggregate dashboard 上看起来很强，同时在 2/3 的引擎里几乎不可见。平均分会掩盖“可见度到底来自哪个引擎”的事实。
- AEO 不应被当成 SEO 的单榜单版本；它更像三个并行、低重叠的分发系统。策略单位应从“整体 AI visibility”下沉到 engine-level visibility、asset portability 和 citation concentration。
- 这会改变诊断方式：homepage 表现弱未必是 homepage 问题，而可能是 AI 引擎整体偏好“有用来源”而非“官方来源”。品牌中心页和交易页天然不如解释、比较、教学型资产容易被引用。

## 破坏了什么常识
- “被一个 AI 引擎引用，就有机会被其他引擎引用”基本不成立；多数 cited URL 只活在单一引擎里。
- “商业查询更容易形成共识”也不成立；高意图没有带来明显更高的 source consensus。
- “大站 / 高频来源更稳”不成立；citation frequency 衡量 presence，portability 才衡量 visibility 是否有韧性。

## 应该怎么测
1. Presence：你的 domain 在多少 tracked prompts 中被任一引擎引用，用来判断是否可见。
2. Portability：你的 cited URLs 中有多少能同时出现在三个引擎，用来判断可见度是否能跨系统迁移。
3. Concentration：你的 citations 有多少来自单一引擎，用来判断当前 dashboard 是否被某个平台的偏好“伪装成整体优势”。

## 证据边界
- 样本来自 Omnia 的 live prompt monitoring pool，偏欧洲，尤其 Spain-heavy，并覆盖 fintech / insurtech、travel、SaaS、B2B services 等客户结构；结论更适合作为方向性判断，不应直接外推到所有市场。
- Intent 与 page type 用 regex 分类，速度足够支撑百万级 URL 分析，但边界会粗糙，Other 类别也因此偏大。
- 本地缓存正文在 “Then there is YouTube...” 后出现 paywall；以上总结基于可访问正文与缓存内容，不包含 premium 部分里的 YouTube exception data、universal-winners domain list 和 operator guidance。

## 收束
AEO 的核心问题应从“我们在 AI 里排名如何”改成“哪些资产能穿过不同引擎的 retrieval 偏好并保持可见”。
