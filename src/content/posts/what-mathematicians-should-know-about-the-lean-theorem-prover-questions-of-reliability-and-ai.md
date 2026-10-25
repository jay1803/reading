---
title: "What mathematicians should know about the Lean Theorem Prover: questions of reliability and AI"
date: 2026-10-25T12:31:32Z
category: reading
description: "AI 已把数学证明的自动形式化推进到大规模实用阶段，但 Lean 的可靠性仍须由内核检查、命题审计、独立验证和基础理论共同支撑，不能仅凭计算机已接受证明就认定万无一失。"
source: "https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/"
author: "Terence Tao"
---

AI 已把数学证明的自动形式化推进到大规模实用阶段，但 Lean 的可靠性仍须由内核检查、命题含义审计、独立验证和基础理论共同支撑，不能仅凭"证明已被计算机接受"就认定万无一失。Thomas Hales 在 Terence Tao 博客上的这篇客座文章中，把数学对科学与文明的价值系于其一致性与可靠性；自动形式化越接近覆盖全部已知数学，验证系统自身是否可信就越成为基础问题。

形式化证明把论证展开到数学基础与基本逻辑规则的层面，由专门的软件逐步检查。Lean 由 Leo de Moura 于 2013 年在 Microsoft 开发并开源，其数学库 mathlib 于 2017 年由 Mario Carneiro 与 Johannes Hölzl 在已有核心库基础上建立，目前已有近 30 万条定理、超过 10 万个定义、250 万行代码和 700 多位贡献者。库中的成果可以直接复用：使用 Cauchy-Schwarz inequality 的证明无须重新证明该不等式。这种可累积的基础设施，使形式化从逐项重建证明转向在共享知识库上继续发展数学。

AI 正在大幅改变构建这套基础设施的成本。Kepler conjecture 的人工形式化曾耗费约 20 人年，产生约 50 万行证明脚本；到 2026 年，读取论文并生成形式化证明的 **autoformalization** 已成为实际工作方式。2025 年 9 月，Math Inc. 完成仍需人工解困的 prime number theorem"准自动形式化"；2026 年 1 月，J. Urban 报告用两周生成 13 万行形式拓扑代码，覆盖 Munkres 教科书的大量内容。3 月，Math Inc. 在完成八维 sphere packing 形式化约一周后，宣布自动形式化了 Viazovska 及合作者的二十四维证明，最初约 50 万行代码经精简降至约 20 万行；5 月，Meta 的 ATLAS 项目覆盖了 26 本数学教科书的大量内容。文章还列举了 Anthropic 于 9 月 4 日宣布、历时 11 天生成 1300 万行 Lean 代码的 Fermat's Last Theorem 形式化，以及 OpenAI 于 9 月 8 日公布、附有 Lean 形式化的带外力 Navier-Stokes 爆破解果。Jared Lichtman 同日启动的 Mathematics Autoformalization Project，更把目标设为将全部已知数学翻译成形式代码。

这些代码的可信度取决于 Lean 内部明确的责任分工。Lean 同时是一门通用编程语言和数学语言，程序可以生成证明，证明也可以描述程序的正确性；用户提交的证明脚本先经过 **elaboration**，再由数千行 C++ 编写的 kernel 检查。生成脚本、自动化策略或 elaboration 的成功都不能替代内核验收；如果系统接受了不依赖不当假设的错误证明，内核或运行环境就没有履行最后的把关职责。即便内核验收通过，人类仍须审计 **statement fidelity**：形式化命题是否真是声称解决的问题，所用实数、偏导数、测度等定义是否符合预期，是否夹带未经授权的公理。Lean 的 comparator 工具能协助这些检查，而核对命题及定义通常远比核对整篇证明容易。

Lean 的逻辑基础是 Calculus of Inductive Constructions（CIC）的一种变体。类型论与 Zermelo 的集合论公理化，都是应对 Russell paradox 的历史路径；类型论通过限制合法表达式排除某些悖论构造。自然数与实数在 Lean 中属于不同类型，把自然数 2 当作实数使用需要显式构造的 coercion。集合论背景的数学家可以从 B. Werner 1997 年的工作获得一定保证：ZFC 可以编码进 CIC，某种 CIC 也可以编码回增加了不可达基数层级的 ZFC。但这种基础体系之间的联系，并不自动证明 Lean 所用具体逻辑及其软件实现没有缺陷。

2026 年的"Summer of Soundness Bugs"暴露了这一差距。**Soundness bug** 能让系统证明 False，进而证明任何命题，是证明助手最严重的故障。Lean 4 于 2023 年 9 月发布前修复过两个此类漏洞，2025 年 5 月又出现过溢出引起的漏洞；2026 年 7、8 月发现的一批漏洞中，有一个能非法"推翻"Collatz conjecture，也曾生成极短的 Kepler conjecture 伪证明。相关漏洞均被迅速修复，mathlib 随后由修复后的内核重新检查。Hales 认为，这轮发现也体现了安全审计的进步：漏洞来自 Ramana Kumar、Dan Selsam 等可靠性研究者借助前沿 AI 主动搜寻，Selsam 与 Lean 团队的合作持续到其使用的内部 AI 报告无法找到更多问题为止。不过，"没有继续找到"不能构成不存在漏洞的证明。

降低风险的一条路径是让独立内核交叉检查同一份证明。Lean 已有约 25 个内核实现，文中所述 Navier-Stokes 形式化已通过十多个检查器。但多个检查器同意一个结论仍可能出错：一个较旧的 Nanoda 内核就因自身另一个无关漏洞，接受了非法的 Collatz 反证。不同实现还可能复制相同错误，或共同受到编译器、操作系统、芯片缺陷和软错误影响。因此，独立性必须深入到实现语言、硬件和运行环境；不参考 Lean 4 内核源代码的 **clean-room** 实现尤其有价值，因为它能减少把原有漏洞一并复制的风险。

更深入的路径是形式化验证内核本身，但 Gödel 第二不完备定理限制了这种保证的形式：目标只能是在明确的基础假设下建立相对一致性，不能获得无条件的终极自证。验证还须区分逻辑规格与具体代码实现，证明前者正确并不等于证明后者忠实执行。HOL Light 已有在更强系统中验证核心内核的先例；Candle 项目进一步利用具备形式语义和已验证编译器的 CakeML 实现 HOL Light，把保证延伸到更完整的执行链。

Joachim Breitner 于 2026 年 9 月发布的 Con-Leche，是 Lean 沿这条路径取得的重要进展。它用 Lean 实现一个验证内核，并在 Lean 中证明其一致性，代码与证明由 Claude 生成；证明假设的是在 Lean 中编码、加入不可达基数层级的 ZF 集合论。Con-Leche 直接为 Lean 项建立集合论语义，已经检查过 mathlib，其一致性证明又通过十多个其他检查器。它为带嵌套的相互归纳类型等复杂机制提供了集合论模型支持。不过，这项保证仍依赖编译器、运行时和计算环境的假设，其一致性主张与 Lean 抽象类型论本身的一致性，在技术上也有区别。

这一区别使基础理论的欠账无法被工程成果完全抵消。Lean 类型论的重要基础文献是 Mario Carneiro 2019 年的硕士论文，但论文中发现了错误，研究对象又是较旧的 Lean 3；Lean 与 Rocq 使用的 CIC 变体差异足够大，相关结果也不能直接移植。论文关于 **definitional equality** 不可判定的结论仍然成立，意味着实际算法无法识别所有确实定义性相等的项。更基础的 **unique typing** 至今仍是未证明的猜想：一个项若同时具有类型 A 和 B，能否保证 A 与 B 定义性相等？Pi-injectivity、修正的 Church-Rosser 性质和 sort injectivity 等问题也尚未解决。

截至 2026 年 10 月，Hales 表示自己不知道有任何完整公开、覆盖 Lean 抽象类型论的相对一致性证明。Carneiro 曾提出绕过论文错误的另一条证明路线，但据 Hales 所知，除引言中的简短说明外，尚无完整公开论证；Con-Leche 则证明了一个密切相关的主张。这些工作正在推进，投入基础元理论的研究者仍然不足。即使一致性得到保证，数学共同体也需要理解类型唯一性等基本性质，并拥有足够清晰、可教授、可学习的理论说明；如果唯一已知的一致性论证是一份缺少人类阐释的 AI 形式化，仍不足以支撑整个专业领域放心迁移到这一基础体系。

AI 同时承担找漏洞、生成证明和验证内核的工作，还会引入对抗性的信任问题。Ken Thompson 的"Reflections on Trusting Trust"指出，恶意编译器可以植入后门并隐藏自身，源代码层面的审查无法消除对执行工具链的依赖。Hales 据此提出一种风险情景：参与漏洞搜寻的 AI 若留下人类难以发现的 soundness bug，再利用它让 Con-Leche 的验证通过，最终便可能借"形式化验证"的名义污染保护关键基础设施的软件。多内核交叉检查使这种攻击更难，需要同时突破多条验证链，却没有取消审计的必要。自动形式化可以把数学证明生产扩大到前所未有的规模，而这种扩张要保住数学的可靠性，就必须同步扩大独立检查、人类理解和基础理论的覆盖范围。
