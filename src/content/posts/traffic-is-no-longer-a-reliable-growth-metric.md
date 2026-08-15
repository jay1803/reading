---
title: "Traffic is no longer a reliable growth metric"
date: 2025-11-04T11:14:00Z
category: reading
description: "ChatGPT 引荐流量的转化率是 Google 的 6 倍——这意味着流量总量下降反而可能是一个健康信号：低意图流量在减少，高意图流量在增加。用总流量衡量增长，已经误导你了。"
source: "https://www.growthunhinged.com/p/traffic-is-no-longer-reliable"
---

## TL;DR
ChatGPT 引荐流量的转化率是 Google 的 6 倍——这意味着流量总量下降反而可能是一个健康信号：低意图流量在减少，高意图流量在增加。用总流量衡量增长，已经误导你了。

## 核心洞见
Webflow 10% 的注册来自 AI 发现渠道，ChatGPT 引荐占 LLM 来源的 91%，转化率 24%（Google 转化率的 6 倍），且 2/3 在 7 天内完成转化。Josh Grant 的结论：非品牌自然注册（AI chatbot + 非品牌 SEO）才是衡量整体内容健康度的正确指标，而非原始流量。

## 具体机制
Webflow 围绕三个新维度建立度量体系：
- **Visibility**（每周几次）：AI 搜索中被引用的频率与内容类型，用 Profound 监测。
- **Comprehension**（每周）：AI 如何描述 Webflow vs 竞品，叙述偏差指向需优化的信任信号。
- **Conversion**（每天）：LLM 来源的注册与新客，以及 time-to-conversion。

实操层面的三个有数据支撑的动作：
1. Reddit 深度运营：以真人方式参与，用 Gumloop 挖掘竞争情绪，Profound 追踪帖子是否被 AI 引用 → 内容刷新速度 5x，被刷新页面流量 +40%。
2. Webinar 内容自动化再利用：AirOps 提取转写 + 主题聚类 → 24 小时内产出博客摘要、FAQ schema、社交片段 → SEO impressions +24%，新增 AI 引用 +331。
3. FAQ + schema 自动化：从 Google PAA 和 Reddit 抓取真实用户问题，批量生成结构化 FAQ 并注入 schema markup，再用 Profound 迭代。

## 隐藏限制
LLM 排名每次查询都是全新计算（"every query is a fresh model run"），没有 Google 式的稳定排名——赢得引用需要持续维护，而非一次性优化。另：llms.txt 文件 Webflow 实测无显著效果，目前无任何 LLM 确认在使用它。

## 留下的问题
ChatGPT 占 91% 的 LLM 引荐——这个极度集中的依赖本身就是风险。当 OpenAI 更新模型或调整引用逻辑时，整套 AEO 打法可能一夜重构。SEO 花了 20 年才稳定，AEO 的"规则"现在仍是移动靶。
