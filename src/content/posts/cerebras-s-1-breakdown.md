---
title: "Cerebras S-1 Breakdown"
date: 2024-10-22T15:40:18Z
category: reading
author: "Tanay Jaipuria"
description: "chip maker Cerebras recently filed their S-1."
source: "https://www.tanayj.com/p/cerebras-s-1-breakdown"
---

chip maker Cerebras recently filed their S-1.
### Cerebras Overview
Cerebras is a chip maker and one of the many upstarts vying to compete with NVIDIA for AI workloads across both inference and training.

Cerebras builds both hardware and software solutions that aim to make AI faster/easier/cheaper to use, centered around their core offering the Wafer-Scale Engine, which is essentially an extremely large chip, 57 times larger than commercially available GPUs

Cerebras, like most other chip makers today, operates a fabless model and uses TSMC to manufacture their processors.
### The Cerebras Product Suite
- Cerebras Wafer Scale Engine (WSE)是他们的核心产品，是一个巨大的芯片，本质上是 GPU 的替代品，其尺寸大了 3E50 倍。
- Cerebras System (CS)是一种人工智能计算机系统，可以容纳芯片并为其供电/冷却，并且可以集成到现有的数据中心中。
- Cerebras AI 超级计算机提供了一种简化的方式来连接多达 2,048 个 Cerebras 系统，以满足需要该计算级别的用例
- Cerebras 软件平台 (CSoft)这是他们的专有软件平台，与 PyTorch 等框架集成。 CSoft 的图形编译器自动将模型操作映射到 WSE，不需要使用特定于硬件的语言进行低级编程。
- Cerebras 推理堆栈/云是端到端推理服务堆栈，允许模型作为服务在 Cerebras 硬件上运行，并由开发人员通过端点使用。

Cerebras 声称他们的推理和训练速度快了 10 倍
但最终成本/延迟权衡对于大多数开发人员来说可能没有意义。

### Financials
- Revenue: Fast ramp of revenue — $25M in 2022, $78M in 2023, $136M in H1 of 2024
- Revenue breakdown: Roughly 3/4 of the revenue comes from hardware while the remaining comes from services and cloud
- Gross Margins: Aggregate gross margins are in the 40-45% range, with the hardware having lower gross margins than the services/cloud segment. I’m surprised by the hardware gross margins being in the 36-37% range, quite a bit lower than NVIDIA/AMD.
- Other Expenses: R&D is the main expense, over 50% of revenue in H1 of 2024. G&A and Sales and Marketing spend is relatively low, under 15% of revenue in aggregate.
- Margins: Net margins are -48% in H1 of 2024, significantly better than previous years which were below -100%.

有一个巨大的问题：客户集中度。 G42 是 Cerebras 过去 18 个月收入的 80% 以上。我以前从未见过一家公司以如此高的客户集中度上市。
 Cerebras 2023 年从其他客户那里赚取了 1300 万美元，2024 年上半年收入为 1800 万美元。因此，尽管收入增长仍然令人印象深刻，但非 G42收入基础相当小。
### The G42 Relationship
G42 is an Abu Dhabi-based AI and cloud computing holding company owned by Mubadala Capital, which is a customer, investor and partner of Cerebras. Microsoft invested $1.5B in G42 earlier this year.

G42’s relationship with Cerebras is:
- Customer: G42 is Cerebras’ largest customer accounting for 83% of Cerebras’ 2023 revenue and 87% of Cerebras’ H1’24 revenue, representing $65M spent in 2023 and $118M in H1 of 2024. In addition, they signed an agreement to purchase $1.43B worth of hardware/services from Cerebras, which will be pre-paid by February of 2025
- Investor: G42 purchased a 1% stake in Cerebras during its Series F funding round in 2021 for $40M, and has an agreement to purchase another $335M worth of shares before mid 2025. In addition, based on their order sizes as a customer, they have the option to potentially purchase additional shares at a 17.5% discount to the price at the time.
- Partner: G42 is also a partner, offering cloud computing services from Cerebras on their Condor Galaxy Cloud. Cerebras also offers these services on their own cloud.
### Closing Thoughts
Cerebras 进行 IPO 肯定存在一些重大风险，主要与其收入集中度以及与 G42 的关系有关。
然而，鉴于 G42 的持续购买承诺， Cerebras 可能会在未来几年报告强劲的收入增长。

最后，作为一个有趣的事实，S-1 提到关键词的次数：
- AI: 490 times
- G42: 301 times
- GPU: 128 times
- TSMC: 18 times
- NVIDIA: 12 times

## Summary (2026-03-04)
- 模型: openai-codex/gpt-5.3-codex
- 结论: Cerebras 的 S-1 不是“技术不行”，而是“商业结构风险很高”。短期收入增速可能继续很强，但投资可持续性高度取决于 G42 这一个超级客户的兑现与延续。
- 为什么这么判断:
  - 产品层面有真实差异化：WSE + 系统 + 软件栈 + 云服务形成了从芯片到服务的完整链路，不只是单点卖硬件。
  - 财务层面有增长但质量不均衡：2022-2024H1 收入爬坡明显，净利率也在改善，但硬件毛利率（约 36-37%）明显低于市场对 AI 芯片龙头的常见预期。
  - 核心矛盾是客户集中度：2023 年 83%、2024H1 87% 收入来自 G42，这会把“增长故事”转化成“单一对手方风险”。
  - G42 同时是客户/股东/合作方：这种强绑定能放大订单确定性，也会放大治理、议价权和外部地缘/合规扰动的传导。
- 该案例的投资阅读框架（可复用）:
  - 先分离“技术护城河”与“收入质量”，不要被高增速直接等同高质量。
  - 再看订单条款的可执行性：预付款、交付节奏、附带股权折扣条款，哪些是真现金，哪些是或有承诺。
  - 最后做压力测试：若核心客户采购放缓或重议价，毛利率与现金流会如何变化。
- 对你当前研究重点的启发:
  - 这类公司适合做“高波动叙事资产”跟踪，而不是只看单季增速。
  - 若后续要继续跟，建议优先补三块信息：
    - 非 G42 客户扩张速度（验证去集中度）
    - 服务/云收入占比变化（验证商业模式质量提升）
    - 与 NVIDIA/AMD 在单位算力成本与交付周期的可比口径（验证竞争力是否可持续）
