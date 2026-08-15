---
title: "Am I Meant To Be Impressed?"
date: 2026-05-07T08:02:46Z
category: reading
description: "Big Tech 的 AI 收入叙事最危险处不是 ROI 差，而是需求被高度集中在 OpenAI / Anthropic 两个持续烧钱主体上；云厂商和 VC 给它们融资，它们再把钱付回云厂商，形成看似增长、实则高度循环的资本化采购链。"
source: "https://www.wheresyoured.at/am-i-meant-to-be-impressed/"
---

## TL;DR
Big Tech 的 AI 收入叙事最危险处不是 ROI 差，而是需求被高度集中在 OpenAI / Anthropic 两个持续烧钱主体上；云厂商和 VC 给它们融资，它们再把钱付回云厂商，形成看似增长、实则高度循环的资本化采购链。

## 核心主张拆解
作者的核心判断：Microsoft、Google、Amazon、Meta 用近万亿美元级 capex 制造了一个“AI 需求很旺”的叙事，但目前可见的真实收入既小、又集中、又不透明。

**收入规模与 capex 不匹配**
- Microsoft 披露 AI revenue run rate 约 $37B，Amazon 约 $15B；这只是收入，不是利润，也不是清晰季度分部收入。
- 对比投入极其难看：Microsoft 已花约 $293.8B AI capex，Amazon 约 $298.3B；Amazon 的 AI run-rate 月收入约 $1.25B，只相当于其累计 AI capex 的约 0.419%。
- Google 和 Meta 更糟：它们反复说 AI 带动业务，却不披露可核验的 AI 收入行项目；如果 AI 真的贡献巨大且盈利，最直接的做法应是单列数字。

**客户集中度是整篇文章的硬核风险点**
Microsoft 的 AI 收入很大一部分来自 OpenAI。作者基于 Azure 账单来源估算，OpenAI 在 Q3 FY2025 的推理支出约占 Microsoft AI run rate 的 71%，Q2 FY2025 也约 63.8%；叠加 CoreWeave / Microsoft 为 OpenAI 提供的训练算力，OpenAI 可能占 Microsoft AI 收入约 70%、占 AI GPU 容量 80% 左右。Amazon 的结构类似：Anthropic 可能贡献 AWS AI 收入约 80%，并吃掉 Amazon AI GPU 容量 75% 以上。Google Cloud 的增长也可能被 Anthropic 的 TPU / Cloud 承诺大幅放大，The Information 称 Anthropic 对 Google 有约 $200B 五年支出承诺，约占 Google 披露 backlog 的 40%。

**循环融资让“需求”看起来比实际更健康**
作者最重的指控是：这不是自然需求，而是 hyperscaler 自己喂出来的需求。Amazon、Google 向 Anthropic 投资，Anthropic 再向 Amazon / Google 采购云和 TPU；Google 还可能通过 TPU 销售、SPV 融资、数据中心租赁，把硬件销售和云租赁叠成多层收入。OpenAI / Anthropic 对 Microsoft、Google、Amazon 的承诺合计被描述为超过 $718B，但它们自身都没有靠经营现金流支付这些承诺的能力，只能继续融资。

**ARR 与 run rate 的可操作空间很大**
作者质疑 Anthropic 的 ARR 口径：API 收入用最近四周乘以 13，订阅收入用某一天活跃订阅乘以 12；企业预付 API credit 也可能让短期收入看起来暴涨。若 Anthropic 真在两个月内新增接近其历史累计收入的规模，同时又声称容量紧张，就需要解释：这些收入来自哪些客户、消耗了多少 token、为什么容量不足没有压制营收增长。

**Meta 是另一个问题：没有清晰 AI 商业模型**
Meta 自 2023 年以来 capex 约 $158B，并可能在 2026 年继续烧到 $145B 级别，但对 AI 如何转化为广告收入没有给出可验证桥梁。所谓 GEM 带来 Instagram / Facebook conversion lift，并未对应到广告主 ROI 或 Meta 实际收入；如果转化提升真的重要，Meta 应能给出 dollar impact。

## 反驳或薄弱处
- 作者大量估算依赖自有信源、公开披露拼接和容量推断，OpenAI / Anthropic 占用比例、Azure 账单结构、Google TPU 回流链条都不是完整公开数据。
- 文章把“未披露利润”强烈推向“经济性不存在”，这一步方向上合理，但证据仍不足以证明所有 AI 收入都不可盈利。
- 语气过于战斗，容易让读者忽略最重要的问题：不是 AI 有没有使用需求，而是当前需求能否支撑 $2T 级 capex、折旧、融资和客户集中风险。

## 投资判断含义
真正该盯的不是“AI 用户增长”或“模型更强”，而是五个硬指标：AI 收入是否单列、AI 收入毛利率、capex 与折旧压力、RPO / backlog 的客户集中度、OpenAI / Anthropic 能否不靠下一轮融资支付云账单。若 Microsoft 的 Copilot token-based billing、Anthropic / OpenAI 涨价、AI startup 倒闭潮、NVIDIA 出货与数据中心上线错配同时出现，说明补贴式需求开始退潮。

## 最后一层意思
这篇文章最有价值的提醒不是“AI 没用”，而是：一个技术可以有真实使用价值，同时仍然被资本市场用错误价格、错误期限、错误会计叙事包装成史上最大 capex 泡沫。泡沫破裂点未必是技术失败，而是某个巨头先承认循环收入不能等同于外部需求。
