---
title: "Why we changed pricing 3 times in 1 year"
date: 2025-05-28T10:58:38Z
category: reading
description: "Equals 公司通过六个版本的迭代，探索并找到了适合其当前产品的定价市场契合点（pricing-market fit）。这个过程强调了主动实验的重要性，并揭示了关于使用限制、捆绑销售、实验幅度以及早期分销策略的关键经验。"
source: "https://wrap-text.equals.com/p/why-we-changed-pricing-3-times-in-1-year"
---

## TL;DR
Equals 公司通过六个版本的迭代，探索并找到了适合其当前产品的定价市场契合点（pricing-market fit）。这个过程强调了主动实验的重要性，并揭示了关于使用限制、捆绑销售、实验幅度以及早期分销策略的关键经验。
### 主题
#### 寻找定价市场契合点 (Finding pricing-market fit)
定价是SaaS业务增长的关键杠杆，但没有万能公式。需要通过不断测试来找到最适合产品、发展阶段和市场的定价策略。随着客户增多，定价调整会愈发困难，因此主动实验至关重要。Equals 公司在三年内迭代了六个版本的定价模型，最终找到了当前的定价市场契合点。
#### 关键经验教训
- 使用限制损害了用户接纳度 (Usage limits harmed adoption)
在Equals的早期定价模型中，对查询次数或查询返回行数的限制，即使是为了驱动用户升级，也实际损害了用户接纳度，甚至可能导致用户流失，特别是没有超额使用缓冲（rollover into overages）而直接强制升级到下一层级。最新的定价模型取消了这些使用限制，让每个人都能无限制地使用Equals的所有功能。
“Usage limits harmed adoption” 指的是在产品或服务的定价策略中设置使用量上限（例如，每月可运行的查询次数、查询可返回的数据行数等），这种做法反而对用户接受和广泛使用产品造成了负面影响。
- 用户不喜欢购买尚不需要的功能 (People didn’t like having to buy things they didn’t need (yet))
多次尝试将固定数量的席位捆绑到起始价格中以提高年度合同价值（Annual Contract Values, ACVs），但用户反感被迫购买他们当时不需要的席位。这反映了早期定价模型与交付价值未对齐。当定价模型调整为主要基于连接的数据源后，就不再需要强制用户购买固定数量的席位，用户可以根据自身需求从1个或20个席位开始。
- 大胆的实验带来更深刻的认知 (Bigger swings resulted in bigger learnings)
大幅度的定价实验，如取消免费增值模式（freemium）或关闭自助服务业务，带来了最深刻的认知。对于尚未找到合适模式的早期公司，尝试差异巨大的方案（如10倍价格、改变打包结构）比小幅调整（如20%）能学到更多。
you'll learn a lot more by trying wildly different things, e.g., 10x prices, changing the packaging structure, etc. Go big or go home.
- 早期分销比最大化收益更重要 (Distribution was more important than maximization)
公司过早地尝试最大化价格点，而实际上应该优先考虑提高交易量和交易质量。在拥有高度满意的客户和产品价值随时间与使用持续增长的基础上，后续再提高价格是可行的。Equals 因此专注于[频繁发布产品更新](https://updates.equals.com/changelog)。
#### 定价模型的演变
##### v1 → v2: 引入免费增值模式 (Going freemium)
Equals 的第一个版本 (v1) 是经典的分层套餐和基于席位的定价，起步价为 $250/月。在 [Series A 融资](https://wrap-text.equals.com/p/equals-raises-16m-series-a-from-a16z)后，认为产品已准备好面向大众，因此引入了免费计划并调整了付费计划的席位定价，形成了 v2 版本。然而，免费增值模式最终对业务造成了负面影响（[freemium tanked our business](https://wrap-text.equals.com/p/the-fallacy-of-freemium-in-saas)）。
##### v3: 取消免费增值并提高年度合同价值 (ACVs) (Killing freemium and increasing ACVs)
六个月后，取消免费增值模式，带来了收入的再次加速增长。为了提高 ACVs，v3 版本开始对基础价格之外的额外 *Connectors*（如 Postgres, Stripe）收费（$100/月/连接）。但这导致了需要最高级别套餐 (*Enterprise*) 的潜在客户，其心理价位被中等级别 (*Professional* $149/月) 所锚定，限制了他们的支付意愿。
##### v4: 进一步提高年度合同价值 (ACVs) (Further increase ACVs)
v4 版本的调整目标是：
1. 使最高级别套餐更具吸引力，给予销售更多可售卖点，并鼓励更多潜在客户与销售沟通以开始使用；
2. 将期望获得最佳版本的潜在客户锚定在更高的价格点。

具体变更包括：
1. 套餐重命名：*Starter* → *Good*, *Professional* → *Better*, *Enterprise* → *Best*。
2. 为 *Best* 套餐引入标价：$499/月（按年计费），包含5个席位，额外席位$49/月，无月度付费选项。
3. 提高 *Better* 套餐的额外席位价格。
4. 在 *Better* 套餐中引入 *Queries* 限制（500次/月），此前为无限制。
5. 引入新的 *Rows returned* 限制 (*Good* → 50k, *Better* → 100k, *Best* → 200k)。

鼓励用户与销售沟通（[Not all friction is bad](https://wrap-text.equals.com/p/why-you-should-add-friction-to-your-onboarding)）是因为数据显示，那些在使用产品前与团队互动的客户（基于产品参与度和支出）通常是最好的客户。引入使用限制是为了增加基于使用量的扩展维度，即使客户不增加席位或升级套餐，其使用量增加也会带来更多付费。
##### v5: 加倍投入“仅销售”模式 (Doubling down on “sales-only”)
在观察到销售业务持续增长并优于自助服务业务后，v5 版本旨在鼓励更多潜在客户通过“仅销售”路径开始使用，目标是进一步提高新客户的 ACV。此版本的入门价格提高了3倍，最高价格提高了50%。
主要变化：
- 移除中间层套餐，以简化并更好地区分自助服务和仅销售路径。
- 取消查询限制，所有人均可无限查询，提供更好的产品体验。
- *Rows returned per query* 限制被 *Rows per sheet* 限制取代，以引导需要处理更大数据集的潜在客户与销售联系。
- 引入新的连接器类别以更好地使价格与价值对齐：*Standard* (包含), *Premium* (+$100/月/连接), *Enterprise* (仅在 *Better* 套餐提供，起价$500/月/连接)。

大约在同一时间，推出了 [Equals Experts](https://equals.com/experts/) 服务——一个分析专家团队，可按需提供定制实施、模型构建和报告自动化帮助。所有顶级套餐订阅均包含10小时的 Equals Experts 时间。
##### v6: 迄今最简单的模型 (Our simplest model yet)
v6 版本主要基于用户希望连接的数据源数量定价，取消了套餐层级和使用限制，旨在进一步提高 ACVs 和赢单率。所有用户都能体验 Equals 的全部功能，包括 [data explorer](https://equals.com/explorer/)、[full-featured spreadsheets](https://equals.com/spreadsheets/)、[BI-grade dashboards](https://equals.com/dashboards/) 和 [AI Assist](https://equals.com/ai/)，且每个席位的价格更低。
该模型基于两个核心认知：
1. 连接器的数量比席位数量更能代表价值。
2. 用户对不同连接器的支付意愿存在差异。
这些认知在公司完全关闭自助服务业务，并要求所有潜在客户在使用产品前与团队互动后变得清晰。为特定[用例](https://wrap-text.equals.com/i/145050360/speak-more-clearly-to-what-equals-is-great-for)和连接数据源引导客户，能让他们更快看到价值并取得成功。未来可能会重新开启自助服务。
### 总结
定价策略的调整永无止境，它必须随着产品演进、市场变化和业务目标的提升而不断适应，因此企业需要主动行动并持续优化。
