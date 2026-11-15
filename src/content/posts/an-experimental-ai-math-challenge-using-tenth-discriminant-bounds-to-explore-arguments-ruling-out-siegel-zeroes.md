---
title: "An experimental AI-math challenge: using tenth discriminant bounds to explore arguments ruling out Siegel zeroes"
date: 2026-11-15T07:23:38Z
category: reading
description: "Terence Tao 提议用一个可量化的数学挑战检验 AI 辅助研究的价值：从不同的 Landau–Siegel zero 排除论证中，推导假想“第十个判别式”的有效上界，借此比较证明方法、寻找改进，并增进人对数学的理解。这项挑战承接他的“Math 2.0”主张：AI 的用途是"
source: "https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/"
author: "Terence Tao"
---

Terence Tao 提议用一个可量化的数学挑战检验 AI 辅助研究的价值：从不同的 Landau–Siegel zero 排除论证中，推导假想“第十个判别式”的**有效上界**，借此比较证明方法、寻找改进，并增进人对数学的理解。这项挑战承接他的“Math 2.0”主张：AI 的用途是增强人类理解数学的能力，而非替代理解；把抽象证明中的常数逐一明确化，正是一类人做起来繁琐、却适合交给 AI 协助的工作。

“第十个判别式”来自 Gauss 的类数一问题：哪些虚二次域的整数环具有唯一分解性质？Gauss 已知九个符合条件的判别式，并猜测名单完整。Heegner 在 1952 年引入模曲线上的 Heegner point，证明了这一猜测，这些数后来被称为 Heegner numbers。更早的 Heilbronn 与 Linfoot 在 1934 年利用如今称为 **Deuring–Heilbronn 排斥现象**的机制，证明若第十个判别式存在，它会排斥其他候选，因此已知九个之外至多还有一个。但这项结果没有给出第十个判别式的大小上界，无法把问题化为有限范围内的计算核查，这就是数论中“无效性”的具体障碍。

这一障碍与 Landau–Siegel zero 紧密相连。类数公式把 Heegner number 与相应二次特征的 L 函数联系起来；进一步推导可以得到一个非常接近 1 的实零点。假想判别式足够大时，这种零点会与 Siegel 定理冲突，但该定理的标准证明同样依赖排斥现象，也无法明确给出“足够大”的门槛。1976 年，Goldfeld 借助适当的高秩椭圆曲线，给出了足以约束第十个判别式的有效结果。随后，Oesterlé 结合 Gross 与 Zagier 的高秩椭圆曲线得到具体上界，又利用 Brumer 与 Kramer 的另一条椭圆曲线进一步改进；后者的高秩由 Mestre、Oesterlé 与 Serre 证明。

Tao 希望把同样的“有效化”工作应用于文章所讨论的新近论证，包括建立 quasi-Riemann hypothesis 的路径，以及直接排除 Landau–Siegel zero 的不同方法。挑战的约束是：**不能借用 Heegner 已经解决类数一问题的方法**，必须从所选论证本身提取假想第十个判别式的上界，并尽力优化常数。若上界足够低，剩余候选就能通过直接计算排除，从而形成类数一问题的一条新证明；这种证明还有机会被高质量地形式化为 Lean 代码，达到纳入 Mathlib 的标准。

即使无法得到全局最好的上界，逐一明确不同证明能达到什么程度，也能揭示各套论证的相对优势、损耗来源与优化空间。压低上界的过程还可能催生新论证，或从过去排除 Landau–Siegel zero 的失败尝试中找出可与新方法结合的有效想法。成果也可能延伸到更高类数的问题：文中提到，Watkins 在 2004 年的工作已解决类数不超过 100 的情形。由于类数一问题早已解决，Landau–Siegel zero 问题在本文的讨论前提下也已有解，Tao 认为这类公开协作较少面临干扰他人正在推进的研究项目的风险。

因此，挑战衡量的成果不限于最小常数。某种方法只能给出极大的上界，依然提供了值得报告的科学信息，即使结果弱于 Goldfeld 或 Oesterlé 的既有界限也有价值。参与者还可以选择另一种优化目标：减少为压榨常数而投入的大规模计算，换取更清晰、便于人类逐步核查的论证。这里需要同时考察数值强度、计算成本与可验证性，而不能仅凭最终上界的大小评价方法。

Tao 要求参与者披露 AI 的使用情况，在评论区提交结果，大量输出则通过 GitHub 仓库等链接提供。他不强制要求 Lean 形式验证，但纯 AI 生成的解答必须经过尽职核查，例如交由独立 AI 工具检查；贡献者应优先保证质量，避免抢先宣称结果，并在改进他人成果时明确署名归功。这个 AI 时代的 Polymath 式实验，最终要检验的是：能否把 AI 的推导能力组织成可检查、可比较、可累积的数学知识，让一个早已解决的问题继续充当理解证明方法的试验场。
