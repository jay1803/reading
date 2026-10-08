---
title: "OpenAI spent millions to solve this famous math problem — mathematicians are furious"
date: 2026-10-08T13:41:19Z
category: reading
description: "OpenAI 用数百万美元算力抢先攻克 Navier-Stokes 难题，抢在学术合作者之前公布成果，引发关于学术优先权与数学共同体开放规范被侵蚀的争议。"
source: "https://www.understandingai.org/p/openai-spent-millions-to-solve-this"
author: "Kai Williams"
---

OpenAI 以数百万美元算力抢先攻克 Navier-Stokes 难题所引发的争议，核心在于这种争夺科研优先权的方式会侵蚀数学界赖以运转的开放与合作规范。文中称，OpenAI 于 2026 年 9 月 8 日宣布，10,000 个 AI agents 协同完成了这一 Millennium Problem 的解答，构成继 1997 年 Deep Blue 击败 Garry Kasparov、2012 年 AlexNet 赢得 ImageNet 竞赛之后的又一个 AI 里程碑。但围绕成果归属与研究伦理的冲突，使这次突破没有获得同样的欢呼。

冲突源于 OpenAI 与两位数学家之间一场资源极不对称的竞赛。NYU 数学家 Tristan Buckmaster 与合作者 Levent Alpöge 已经完成三个与 Navier-Stokes 密切相关的问题，并在 OpenAI 公布成果的前一晚发布了合计约 245 页的三篇论文草稿。Buckmaster 原本想强调，一位数学家与 LLM 能在一个月内完成如此规模的研究，本身就具有重大意义；但此前与 OpenAI 的接触让他转而公开批评这家公司。9 月 3 日，因外界传言 Anthropic 已解决两个 Millennium Problems，他主动联系 OpenAI 的一位数学家，解释传闻很可能指向自己的项目：Alpöge 虽然受雇于 Anthropic，却是在业余时间参与，项目没有得到 Anthropic 的官方支持。

据 Buckmaster 的说法，三天后，他与这位数学家及负责 OpenAI 千禧年难题项目的 Sébastien Bubeck 交谈，得知 OpenAI 在听到有关 Anthropic 的传闻后启动研究，采用了与他们相同的大方向，而这个方向此前"几乎没有人"在做。OpenAI 凭借大规模计算，抢先取得完整的 Navier-Stokes 结果。Buckmaster 还称，Bubeck 提议合并双方工作，让他撰写公布完整结果的论文，条件是承认解答来自 OpenAI 模型，同时不将身为 Anthropic 员工的 Alpöge 列为共同作者。这一提议促使 Buckmaster 将争议公开，随后舆论围绕他的愤怒是否合理、Bubeck 的回应能否为 OpenAI 辩护展开讨论。

更深层的问题是，**数学成果的声望依赖于一个持续交流的专家共同体**。对另一家资源充足的 AI 公司采取竞速策略，与听说学术研究者已有进展后投入数百万美元抢先完成研究，适用的是不同的规范。数学界通常认为，利用同行透露的有希望的初步结果突击抢发，有损合作关系。如果这种行为成为常态，研究者就会被迫将工作保密到可以发表为止，提前分享思路、讨论困难与寻求合作的空间随之缩小。OpenAI 希望借著名难题获得声望，其竞争方式却可能损害赋予这项成果声望的共同体。

这一数学突破涉及流体方程是否会在特定条件下产生失效。Navier-Stokes equations 描述水流、空气等流体中各点速度如何变化；由于多数情形没有可直接预测未来全部状态的显式公式，科学家通常通过很小的时间步长反复计算速度场变化，推进流体模拟。理论问题在于，这些方程是否可能从合理的条件出发，演化出物理上荒谬的结果。文中介绍，OpenAI 找到了一个受特意选取的光滑外力作用的三维流体情形：旋涡向内螺旋收缩，同时像 spaghetti 一样不断拉长，中心区域越来越小、流速越来越快，总能量仍然有限，但局部速度最终无限增长，形成 **singularity**。真实流体不会出现这种无限速度；Buckmaster 与 Alpöge 则在三个相关、较简单的流体模型中找到了类似的异常结果。

数学上的重要性并不意味着流体工程会因此发生剧变。Terence Tao 在 9 月 3 日的 Mastodon 讨论中指出，计算流体力学已经是成熟领域，广泛用于大气科学，其实际能力与局限也已有充分认识。无论证明 Navier-Stokes 解始终保持规则，还是找到会发生 blowup 的病态实例，都具有理论上的智识价值，却不会根本改变天气预报或气候变化的建模方式。由此，这场竞争的意义主要落在数学认识与 AI 研究能力上，而评价这样的突破，也必须把获取成果的方式对未来知识生产条件的影响计算在内。
