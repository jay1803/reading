---
title: "Snowflake’s Forecast Transformation with Brad Floering"
date: 2024-12-04T11:13:24Z
category: reading
description: "Snowflake 是有史以来增长最快的软件企业之一。自 2012 年 7 月成立以来，截至 2023 年 1 月 31 日，该公司已在 7,800 名客户中增长到超过 $2B 的收入"
source: "https://wrap-text.equals.com/p/snowflakes-forecast-transformation"
---

### Snowflake’s Forecast Transformation
Snowflake 是有史以来增长最快的软件企业之一。自 2012 年 7 月成立以来，截至 2023 年 1 月 31 日，该公司已在 7,800 名客户中增长到超过 $2B 的收入
### Challenges Facing the Early Finance Team
当 Brad 于 2017 年 9 月加入 Snowflake 时，他的任务是建立 FP&A 团队并负责损益预测。这家拥有约 300 名员工的公司刚刚筹集了 D 轮融资，年收入尚未达到 $100M，但很明显，即便如此，Snowflake 也正在做一些特别的事情，需要开始为未来几年作为上市公司运营奠定基础。
#### Issue #1: Usage-based Pricing - Exponential vs. Linear Growth
根据基于使用量的定价预测和确认收入与传统的基于席位的模型有着本质上的不同。在基于席位的模型中，客户承诺在规定的时间内为固定数量的许可证付费。由于购买的座位数量和持续时间在预订时都已知，因此收入可以在全年以等额分期付款确认。当 Brad 加入时，该团队正在利用这种基于席位的识别方法。

要准确预测 Revenue，您必须了解客户在合同期内的消费行为。Brad 发现，基于使用量的计划的客户遵循的消费曲线更具几何性，与基于席位的模型相比，团队在短期内预测过高，而在合同期的后半段预测过低。后一点尤其正确，因为客户在看到 Snowflake 的产品可以做什么后，往往会超出他们最初的使用承诺，将尽可能多的工作负载迁移到平台。
#### Issue #2: The Cold Start
但当您拥有多年的客户使用模式历史数据时，收入预测就会变得更加容易。但是，当全新客户注册时会发生什么？由于没有历史数据可依赖，预测感觉就像是黑暗中的一针。这就引出了 Brad 的第二个问题，在内部被称为“冷启动”：您如何预测以前从未使用过您的产品的客户消费行为，从而推动收入增长？
#### Issue #3: Revenue Contribution: New vs. Existing
### The Search for a Solution
#### Early Approach
Brad 首先构建了一个同期群模型，该模型将根据年龄预测所有客户在相同的非线性或“曲线”时间表上的使用情况（有关如何构建同期群模型的示例，请参阅我们在 [Figma 的自助预测](https://wraptext.equals.app/exploring-figmas-self-serve-forecast-model/?ref=wraptext.equals.com)中的故事）。 这有帮助，但事实证明，单个曲线太不精确了。为了进一步细化客户群，他按一些属性（包括员工人数、初始合同规模、行业和销售细分市场）创建了分组。
### Data Science & Finance - a Masterclass in Collaboration
最终，Brad 意识到团队中不存在解决问题所需的技能。 他寻找在统计建模方面具有更深厚知识以及在 Python、SQL 和 R 中处理大型数据集的经验的人，并于 2018 年 4 月聘请了 Andrew Seitz 担任财务部门的第一位专门数据科学员工。
#### Mapping out the Journey
Andrew 和 Brad 首先草拟了一个框架，该框架可以预测客户整个生命周期的使用情况 。
#### A Three-Model Approach
该框架将通过三个统计模型的组合来预测每个客户的使用情况：冷启动、混合和消耗模型。使用哪个模型的决定取决于客户在生成预测时的年龄。
#### The Forecast Output and Cadence
#### Cracking the Cold Start Problem
他在 Python 中设置了一个工作版本，并在接下来的一个季度中测试了新客户的数百个技术和公司统计属性的组合如何与旧版 Snowflake 客户的冷启动使用模式相关联。
在测试这些属性时，该团队面临着许多初创公司常见的一些挑战。通常，企业统计数据不容易标准化。

Andrew 找到了一种方法来解决这些问题，方法是关注更固定的变量，例如地理位置和销售客户的销售细分。
#### Shipping the First Iteration
有了有效的 Cold Start 模型后，Andrew 开始研究 Hybrid 和 Consumption 模型。
### The IPO Goal Becomes Clear
#### A Change in Leadership
在团队推出新的预测方法后不久，Snowflake 的领导团队发生了转变，Frank Slootman（首席执行官）和 Mike Scarpelli（首席财务官）分别于 2019 年 4 月和 8 月加入。他们的重点很明确：让 Snowflake 处于可以上市的位置。

虽然整个公司都需要做好准备，但对 IPO 的重大依赖性是将收入预测准确性提高到 +0-2% 以内，并且永远不会低于。 Scarpelli 自己的博客文章《将公司扩展到 IPO 及以后》中重申了这种确定性要求，他在那里说：“如果你没有可预测性，也没有预测能力， 只有一个答案：你还没有准备好公开。
#### A New Level of Urgency
### Sprinting to the Finish Line
#### Refining the Hybrid & Consumption Model
Brad 在 2019 年 6 月聘请了他们的第二位数据科学家 Matt Franking。 Matt 的任务是让这三个模型在所需的 IPO 范围内始终如一地提供预测准确性。

到 2019 年 12 月，这些努力的结合使 Snowflake 的收入预测准确性达到了中等个位数。
#### Process Improvements to Close the Gap
帮助财务团队将其客户级别的使用量预测转换为 GAAP 收入。随着 Snowflake 的规模扩大，向越来越多的客户销售产品，他们的合同也越来越复杂。Matt 与会计部门合作，系统地协调了折扣和产品与服务收入确认等因素如何影响财务部门将使用情况预测转化为 GAAP 收入。
### The IPO and Beyond
#### A Call to Action for Operators
首先，财务和运营团队需要提高技术含量以保持相关性。 可用数据的爆炸式增长以及根据这些信息采取行动的需求只会随着时间的推移而增加。 组建一支具有 SQL 和数据建模专业知识的团队将是未来决策桌上占有一席之地的必要条件。

其次，预测工作最具影响力的成果之一是帮助团队打破了追溯报告数字的习惯。大多数财务和运营团队声称，他们只能等待季度结束才能运行报告和分析，但到那时采取行动的窗口已经关闭。团队需要找到方法来利用实时洞察，并在为时已晚之前为主动决策提供信息。

最后，除了团队的技术能力之外，拥有正确的技术堆栈对于实现这一切至关重要。如果不利用 Snowflake 自身产品的功能，Brad 的团队就不可能取得成功。您的数据策略和团队的技术敏锐度可以成为各地公司的竞争优势。收入预测只是 Snowflake 财务团队如何使用自己产品的一个示例。
