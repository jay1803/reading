---
title: "Your traffic data is lying to you"
date: 2026-05-13T08:01:53Z
category: reading
description: "流量已经变成滞后指标；真正该追的是品牌在买家“形成考虑名单”时出现了多少次。AI Overview、LLM 回答、Reddit 讨论、评测站和传统搜索都会影响购买决策，但很多触点不会回到 GA 里，Share of Voice 才能把这些不可见曝光纳入同一张竞争地图。"
source: "https://newsletters.feedbinusercontent.com/3ea/3ea6fa8e64e22f2c986f77f670e6bc37dc34d9ec.html"
---

## TL;DR
流量已经变成滞后指标；真正该追的是品牌在买家“形成考虑名单”时出现了多少次。AI Overview、LLM 回答、Reddit 讨论、评测站和传统搜索都会影响购买决策，但很多触点不会回到 GA 里，Share of Voice 才能把这些不可见曝光纳入同一张竞争地图。

## 核心洞见
- SoV 衡量的是品牌相对竞争对手占据多少“类别对话”。传统上它用于广告声量，现在更适合衡量搜索、AI、社区、评测站、PR、社媒等买家研究触点。
- 搜索 SoV 是起点，因为它同时具备购买意图强、可度量、可按竞争对手拆解这三个条件；文章重点放在 organic search 与 AI search。
- “好”的 SoV 没有统一阈值：20+ 竞争者的碎片市场里 8% 可能已进前五；三玩家市场里低于 30% 可能意味着落后于领导者。
- 高 SoV 如果发生在萎缩品类里可能只是虚荣指标；更重要的是在增长品类中提升份额，并把声量移到能影响收入的漏斗阶段。

## 具体机制
### 1. 先定义竞争边界
- 追踪对象要按收入相关 topic cluster 划分，而不是只按搜索量排序。
- 示例 cluster：category fundamentals、use cases、industry-specific。
- 每个 cluster 继续映射到漏斗阶段：awareness、consideration、decision。
- 如果品牌只在 awareness 可见，却在 decision 阶段缺席，它其实是在教育市场，但没有进入购买比较场景。
- 竞争对手要同时包含 direct competitors（同类产品）与 indirect competitors（G2、行业媒体、HubSpot/Zoho 这类占据关键词但不直接卖同类产品的站点）。

### 2. 建立 keyword + prompt library
- 文章建议整理 200–500 个 queries，覆盖 SEO keywords 与 AI prompts。
- SEO 侧从 Google Search Console impressions、Google Ads 高转化/高 CTR 词、Semrush Position Tracking 等来源导出。
- 竞争侧用 Keyword Gap 找 competitors 已验证、自己缺席的机会词。
- AI 侧从 Reddit、Facebook groups、Slack communities、G2/Capterra alternatives 等地提取更口语化的问题，例如“适合小型创意 agency、不要太 corporate 的 project management tool”。
- 每条 query 需要记录 metadata：Keyword/Prompt、Topic Cluster、Funnel Stage、Source（SEO/AI）。这些字段会成为后续资源分配的分析维度。

### 3. 分别计算 SEO SoV 与 AI SoV
- SEO SoV 公式：自己的 estimated traffic ÷ 所有追踪品牌的 total estimated traffic × 100。
- 单个关键词的 estimated traffic = monthly search volume × 当前排名位置的平均 CTR；再对所有关键词加总。
- 位置、设备、地区会改变排名与 CTR，所以 tracking location 必须贴近真实客户市场。
- AI SoV 目前没有标准化手工算法；近似做法是把 prompt library 分别跑过 ChatGPT、Claude、Google AI Mode、Perplexity 等目标平台，记录每个回答里出现的品牌、引用来源、情绪倾向。
- 简化 AI SoV = 某品牌出现次数 ÷ 总 prompt 数 × 100；更成熟的工具会对 mentions、citations、context 加权。
- SEO SoV 与 AI SoV 可能背离：SEO 强但 AI 弱，说明内容排名好却不被 LLM 视为可信引用；AI 强但 SEO 弱，说明内容可信度够，但 SEO 基础和关键词覆盖不足。

### 4. 建 baseline，而不是追日噪音
- Dashboard 至少拆三层：overall metrics、topic cluster performance、funnel stage breakdown。
- 月度跟踪适合看趋势，季度 deep dive 用来关联 campaign、分析 cluster 变化、调整资源。
- 可设置阈值提醒，例如核心 cluster 的 SoV 跌破某个幅度时触发。

## 如何提升 SoV
- 低于 10% SoV 的 cluster 基本等于不可见，尤其是 decision-stage queries；优先补 comparison pages、buyer guides、case studies、ROI calculators。
- 如果某 cluster SoV 高但转化率只有 1%，说明声量占在低价值受众上；预算应从泛 awareness 内容转到 bottom-of-funnel 内容。
- 如果竞争对手在你的强 cluster 中提升超过 5% SoV，这是进入你地盘的早期信号；需要检查它们是否在 review sites、community platforms、organic search 或新内容格式上抢占入口。
- 优先级排序要用 effort vs impact：先做高影响低成本动作，例如优化 #5–10 排名内容、认领 review/directory profiles、更新 comparison pages；再投资 Reddit/forums 权威建设、核心 cluster hub、AI 可引用来源与行业 thought leadership。

## 证据薄弱处
- 文章大量依赖 Semrush 工作流和工具截图，方法论有实操价值，但也带有明显工具营销倾向。
- AI SoV 的手工测量仍然粗糙：LLM 输出会受 session、prompt wording、location、平台版本影响，单次测量更像 directional read，不能当作稳定市场份额。
- CTR benchmark 在 AI answers 吃掉点击后会持续漂移；用固定排名 CTR 估算 SEO SoV，可能高估传统 organic 的真实价值。
- “SoV 作为北极星”容易把团队推向追可见度；如果没有同时绑定 pipeline、conversion 和 revenue quality，声量仍可能变成高级版 vanity metric。

## 最后一层判断
这篇的关键价值不在“多追一个营销指标”，而在把买家注意力从点击日志里解放出来：未来的品牌竞争会越来越发生在用户还没访问你网站之前。谁能持续进入 AI、搜索、社区和评测场景里的候选名单，谁才真正拥有类别需求。
