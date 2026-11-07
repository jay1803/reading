---
title: "Pricing Inflation Swaps in the Japanese Bond Market"
date: 2026-11-07T07:28:06Z
category: reading
description: "日本的 inflation swaps 利率与盈亏平衡通胀率（breakeven inflation，BEI）几乎重合，却与债券定价模型预测的显著价差相冲突，因此，两者的一致不能证明它们准确反映了市场的通胀预期。Jens H. E. Christensen、Mizla Shres"
source: "https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/10/pricing-inflation-swaps-in-japanese-bond-market/"
author: "Jens H. E. Christensen, Mizla Shrestha, Mark M. Spiegel"
---

日本的 inflation swaps 利率与盈亏平衡通胀率（breakeven inflation，BEI）几乎重合，却与债券定价模型预测的显著价差相冲突，因此，两者的一致不能证明它们准确反映了市场的通胀预期。Jens H. E. Christensen、Mizla Shrestha 和 Mark M. Spiegel 的研究发现，日本通胀挂钩国债中包含规模可观、随时间变化的流动性溢价和通缩保护价值，这些因素无法相互抵消，却没有在实际 swap-BEI 价差中显现。这构成了日本债券与通胀互换市场尚未得到充分解释的定价谜题。

这一问题的起点是相同现金流应有相同价格的金融市场原则。Fleckenstein、Longstaff 和 Lustig 在 2014 年发现，利用美国 Treasury Inflation-Protected Securities（TIPS）与 inflation swaps 构造的投资组合，即使现金流与名义国债完全匹配，价格仍会显著不同。名义国债比 TIPS 更容易交易，由此形成的流动性优势可以解释这种差异：投资者要求较不流动的 TIPS 提供更高收益率，而 BEI 是名义国债收益率减去通胀挂钩国债收益率，因此被压低。自 2018 年起的十年期数据也显示，美国 inflation swap 利率持续高于 BEI；美国十年累计通缩的可能性很低，TIPS 的通缩保护价值有限，流动性溢价主导了价差。

日本原本应当更容易出现这类偏离。日本通胀挂钩国债 JGBi 仅占政府债务约 1%，与庞大的名义 Japanese government bonds（JGBs）市场相比，流动性差异足以影响收益率。同时，日本长期通胀水平远低于美国，通缩保护更有价值：2013 年起发行的 JGBi 在存续期累计通胀为负时，仍保证偿还全部本金。这项保障提高债券价格、降低实际收益率，从而推高 BEI；通常为正的流动性溢价则提高实际收益率、压低 BEI。标准 inflation swaps 不提供本金通缩保护；按照本文的定价框架，互换合约初始价值为零，之后通过净额结算或订立反向合约平仓，无须像债券一样在二级市场转售，因此也不包含上述债券流动性溢价。这两类债券特有因素理应使 swap 利率与 BEI 分离。

然而，Bloomberg 自 2018 年起提供的日本数据表明，十年期 inflation swap 利率与 BEI 几乎完全一致，其他期限也存在同样现象。要用债券特有因素解释这种重合，就必须证明流动性溢价与通缩保护的影响在不同期限、不同时间持续抵消。研究因此采用 Christensen 和 Spiegel 的收益率曲线模型，加入债券特有的流动性风险因子，利用不同债券的横截面价格及其时间变化识别两种效应。样本包括 2005 年 1 月至 2025 年底发行的全部 30 只日本通胀挂钩国债，以及 1995 年至 2025 年底、覆盖六个月至十年的六种期限名义零息债收益率，并纳入每两年一次的调查通胀预测，以约束预期通胀估计。

模型结果排除了两种效应持续抵消的解释。JGBi 的流动性溢价规模显著，并在样本期内由负转正；对于 2013 年以后发行、附带本金保障的债券，通缩保护折算成收益率的价值曾长期达到约一个百分点，在疫情前后波动较大。随着日本通胀自 2022 年起持续走强，通缩保护价值降至接近零。两种因素对实际收益率的净影响在约 2022 年之前大幅为负，之后转为正值，因此模型预测 swap-BEI 价差应在此前为负、此后为正。实际价差却始终接近零。进一步剔除这两类债券特有因素后，模型推算的十年期 inflation swap 利率除 2022—2023 年外，也与市场报价明显不同。

一个可能的传导渠道是，inflation swap 交易商需要在 JGBi 市场对冲头寸，因此将对冲工具中包含的流动性风险和通缩保护价值带入了互换报价。但这仍只是候选解释：模型估计，两类因素对收益率的合并影响均值为 0.24 个百分点、标准差为 0.85 个百分点，幅度之大，使单靠交易商对冲需求解释全部异常显得不足。研究并未确定究竟还有哪些因素支配日本 inflation swap 的价格，而是揭示了实际报价与模型之间无法由现有机制充分解释的缺口。

由此，直接用日本 BEI 推断预期通胀仍需要调整其中嵌入的溢价，观察到 inflation swap 给出相近数字也不能免除这一步。两个市场价格高度一致，可能反映它们共同受到同一组定价因素影响；价格之间的相互印证，不能替代对价格组成的识别。
