---
title: "The Mathocalypse"
date: 2026-11-08T22:52:57Z
category: reading
description: "AI 一旦能批量攻克数学共同体数十年未解的难题，人类数学家的核心挑战就会转向理解证明、重建知识联系，以及维系共同探索的意义。"
source: "https://scottaaronson.blog/?p=10169"
author: "6bitquant"
---

AI 一旦能批量攻克数学共同体数十年未解的难题，人类数学家的核心挑战就会转向理解证明、重建知识联系，以及维系共同探索的意义。Scott Aaronson 在《The Mathocalypse》中描述了这样一场冲击：OpenAI 一次公布 372 项重大数学成果，发布得到 Timothy Gowers、Edward Witten 等人组成的顾问团队建议，其中包括他妻子、复杂性理论学者 Dana Moshkovitz 长期致力于证明的 Unique Games Conjecture（UGC）。贯穿全文的张力是：一个问题可以已经获得形式验证，人类却仍然没有真正理解它为何成立。

UGC 的重要性在于，它意味着大量优化问题即使只要求近似解，只要近似效果略优于 semidefinite programming relaxation 所能达到的水平，仍然是 NP-hard。文中所述证明附有 Lean certificate，但包括这项成果在内的绝大多数新证明，当时尚无人读懂。Dana 的初步阅读揭示了*形式正确性与人类可理解性之间的鸿沟*：关键论断散落在全文各处，引用经常无关或令人困惑，一些构造如何绕过已有不可能性结果也交代不清。她需要借助 Astra，把分散的内容拼成 noise gadget 的 completeness 和 soundness 陈述，才能开始判断论证。

更深的陌生感来自证明采用的数学结构。UGC 证明构造了一种带有 noise test 的全新递归编码，既非熟悉的 long code，也非 short code；同批论文还绕过 UGC，直接给出 Max Cut 和所有 constraint satisfaction problems 的最优近似困难性证明。Dana 仍然希望找到使用更自然的 half space code 的证明。对她而言，职业目标被机器抢先完成，同时也证实了她始终坚持、却曾受到许多同行怀疑的判断：UGC 确实成立。她设想，未来拥有创造性方向感的人，可以让 AI 帮忙检验和实现想法，同时从这些陌生构造中学习新的数学。

Aaronson 强调，这种处境已经覆盖数学、理论计算机科学与数学物理中所有追求明确问题答案的研究者。文中列举的成果包括 L=BPL，即随机化与确定性对数空间计算能力相同，解决了一个重要的去随机化猜想；Fourier Transform 与整数乘法的时间复杂度突破自 1960 年代以来的 O(n log n) 屏障，降至大约 O(n log^0.9999999999999 n)，尽管指数改善极小，仍改变了长期存在的渐近边界；矩阵乘法则通过完全不同于既有路线的方法达到 O(n^(9/4))，超越文中对照的 O(n^2.373) 一类结果。

量子复杂性方面，Unitary Synthesis Problem 得到的肯定答案甚至违背多数研究者的预期：对每个 n-qubit unitary transformation U，都存在一个 classical oracle A，使量子计算机访问 A 后能在多项式时间内实现 U。这可能影响从黑洞 Hawking radiation 中解码信息等问题，但论文并未提供高效构造 A 的方法，因此不能直接推出这些任务已经可以高效完成。其他成果包括证明 Parity 不属于 QAC⁰，以及为 total Boolean functions 建立随机化与量子 query complexity 之间接近四次方的分离。后一个问题是 Aaronson 自 1998 年起关注的方向，最优分离指数的已知范围曾为 2 到 6，后来缩小到 3 到 4，新结果终于逼近上限。

其余突破同样足以单独成为一个领域的年度大事：sensitivity 与 block sensitivity 之间出现超二次分离；具有全局谱隙的二维 Hamiltonian 满足 area law；permanent 的 determinantal complexity 下界从二次提高到 Ω(n³)；一般图的 perfect matchings 数量可以用随机多项式时间算法近似计算，maximum matching 可以用随机近线性时间算法求得；有理数上多项式方程可解性的不可计算性也得到证明，将 1970 年代已经解决的整数情形推进到长期悬而未决的有理数情形。成果还涉及 Riemann hypothesis、Hodge Conjecture 和 Birch–Swinnerton-Dyer Conjecture 的部分进展，但 P≠NP、P=BPP 与 NEXP⊄P/poly 仍未解决，说明这波突破远未抹平所有难度层级。

成果如何进入公共知识，随之成为制度问题。按照文中叙述，OpenAI 公布成果前一天，Virginia Williams 与 Josh Alman 已发布由 Anthropic 模型提供关键想法的论文，把 3SUM 的时间复杂度降至 O(n^1.9992)，把 All-Pairs Shortest Paths 降至 O(n^2.9995)，推翻相应的长期复杂度猜想。Anthropic 选择付酬邀请人类研究者先消化证明，再以可理解的形式发布；OpenAI 则直接公开未经充分整理的 AI 证明。后一种方式迅速开放成果，却让研究者陷入竞争激烈、可能缺乏认可且难有乐趣的解释工作；前一种方式改善了传播质量，却让私人公司有权决定哪些数学家成为 AI 成果的代表与中介。

让冲击进一步放大的，是文中所述的低计算门槛。这些结果据称来自 OpenAI 最新内部通用模型，平均每题只使用约三小时 GPT-Pro 级别计算，无须依赖上万个 agent 和数百万美元算力的专门工程。模型接受了约 8,000 道长期开放问题的测试，单次尝试就解决了约 5%。这个成功率意味着，即使模型仍然会在绝大多数问题上失败，它也足以在短时间内取得许多研究共同体多年未能实现的进展；而同一模型还可能在安全委员会许可后，于数月内向付费 ChatGPT 用户开放。

数学共同体已经开始通过集体阅读、解释和重建证明来适应这一变化。Aaronson 提到 Simons Institute、UT Austin 等地的研究者正迅速投入这项工作，但理解现有成果只能处理眼前任务，更长远的问题是如何保留探索的动力。Quanta 的 Jordana Cepelewitz 将这种处境比作突然被传送到迷雾中的山顶：人获得了终点，却失去登山过程中形成的工具、路线知识、意外发现与合作经历。Aaronson 相信，人类仍能借助 AI 清除迷雾、重建路径，而且共同体依然存在；真正困难的是，在机器可以直接抵达山顶的世界里，继续让人愿意关心寻找路径这件事。

由此，他把数学冲击延伸到对 AI 能力与风险的判断：如果每次突破都被重新归类为“AI slop”“竞赛小题”，甚至用来贬低整个数学传统，那么人类创造力不可触及的信念就失去了接受经验检验的条件。他赞同 Scott Alexander 在致 Steven Pinker 的公开信中提出的要求：面对 AI 风险，应当按证据更新判断，贯彻 Pinker 自己倡导的经验主义。数学研究的价值因而越来越取决于一个共同体能否把机器给出的答案转化为可理解、可传授、可继续探索的知识，同时承认，能够如此迅速改写知识边界的系统，也已经改变了人类必须认真对待的风险。
