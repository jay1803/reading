---
title: "Google's Statistics: Heads They Win, Tails You Lose."
date: 2026-09-22T12:26:46Z
category: reading
description: "Google 把偏弱的广告增效证据包装成\"good chance\"\"directional insights\"，把乐观解读的风险转嫁给广告主：平台只需证明广告可能有效，预算负责人却要独自判断证据是否足以支持下一笔投入。"
source: "https://www.kaushik.net/avinash/googles-statistics-significance-replication-risk/"
author: "Avinash Kaushik"
---

Google 把统计上偏弱的广告增效证据包装成"moderate chance""good chance"和"directional insights"，实质上把乐观解读带来的风险留给广告主承担：平台只需证明广告可能有效，掌管预算的人却必须判断这份证据是否足以支持下一笔数百万美元的投入。

Google 对 Brand Lift、Search Lift 和 Conversion Lift 的官方解释是：Certainty 达到 90% 以上属于"very good chance"，70%—90% 是"good chance"，50%—70% 是"moderate chance"，低于 50% 才归为"no lift"；同时又称 50% 以上的研究都可能提供有价值的 **directional insights**。这种分层几乎总能导向有利于继续投放的说法：结果强，可以宣称广告有效；结果弱，也可以说方向值得关注，再花钱测试。问题在于，"directional"无法回答任何具体预算决策：该不该继续投、减少投入、修改创意、改变媒介策略、把钱转给 Meta，还是重新设计实验。

假设一家企业在 YouTube 投入 500 万美元，以品牌 Consideration 为 KPI，Brand Lift Study 报告提升 3 个百分点、Certainty 为 70%。Google 会把它称为广告造成结果的"good chance"，但负责品牌媒体的 Senior Director 必须向 CMO 或 CFO 说明，这是否足以支撑再投 500 万美元。双方承担的后果并不对称：Google 销售广告，保留任何"可能有效"的信号符合其商业利益；企业承担预算损失，需要回答首轮投放是否真的有效，以及同样的投入是否值得重复。Google 虽提醒客户依据自身业务需求和风险承受力解读结果，但"moderate""good"和"directional"这些听起来像决策依据的词，仍然掩盖了证据强度与资金风险之间的距离。

为把抽象的 Certainty 转换成管理者真正关心的问题，可以采用受生物统计学家 Steven Goodman 启发的简化 Bayesian replication model：假定第二轮投放的平台、受众、季节、促销、创意和样本量均与第一轮相同，把"真实效果究竟是多少"的不确定性与"再次测量会产生多少误差"的不确定性合并，估计复现实验可能出现的结果。这里需要观察三个量：重复投放后出现任何正向提升的概率，哪怕只有 0.01 个百分点；重复结果达到至少 90% Certainty 的概率；以及 **Replication Risk**，即重复结果无法达到这一证据门槛的概率。对预算负责人来说，最后一个量直接回答了"再花 500 万美元后，仍无法有把握地向 CFO 说投放有效"的可能性。

首轮只有 70% Certainty 的 +3 点提升，在这一模型下意味着：同等条件下再次投放，出现任何正向提升的概率仅为 65%，达到至少 90% Certainty 的概率只有 30%，因而 Replication Risk 高达 70%。Google 所谓的"good chance"，转换成重复决策的语言，就是再花 500 万美元后只有三成概率获得足以支持"有效、可以继续投入"的强证据。Google 展示的 Certainty 会按 5 个百分点向下取整，因此页面上的 70% 实际可能代表 70% 至不足 75%，精确的复现概率会随之浮动几个百分点；这一技术细节不会改变整体风险判断。

作者把 90% Certainty 设为重大商业决策的最低门槛，并不声称它具有神奇的统计意义，只是明确规定自己在向 CMO 或 CFO 宣告"这次有效，可以再投"之前愿意接受的最低证据强度。即便首轮达到 90%，同条件重复时达到高 Certainty 的概率也只有 50%，出现任何正向提升的概率为 82%；若决策涉及 1,000 万美元，这组赔率仍可能令人不安。把首轮门槛提高到 95%，Replication Risk 才会降至 40%，重复出现正向提升的概率升至 88%，企业承担的赔率才更有利。

低于 90% Certainty 的结果并非毫无用途，但用途取决于决策后果。若几乎没有资金风险，它可以帮助形成新假设、改进实验设计、尝试不同创意或追加小额测量；若数百万美元将据此配置，就应直接检查复现概率，而不能把"directional"当作行动理由。弱证据还可能造成双重损失：效果未必能够复现，同时首轮观测到的 +3 点提升可能夸大真实效果，这分别对应 Type S（方向）与 Type M（幅度）错误所揭示的风险。

这套判断同样适用于 Meta、TikTok，以及费用随媒体预算增长的 Agency 所提供的"高信心"测算。广告平台可以合理地从提示性证据中发现销售价值，企业却必须自行规定何种证据足以承受下一笔预算；**一旦把"有用的信息"误当成"充分的证据"，企业就等于把自己的风险容忍度交给了从继续投放中获利的一方。**
