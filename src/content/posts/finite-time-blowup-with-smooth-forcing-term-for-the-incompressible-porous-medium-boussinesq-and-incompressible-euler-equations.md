---
title: "Finite time blowup with smooth forcing term for the incompressible porous medium, Boussinesq, and incompressible Euler equations"
date: 2026-10-15T07:14:20Z
category: reading
description: "Alpöge 与 Buckmaster 证明三类流体方程在光滑外力下可有限时间形成奇点，为 Navier–Stokes 全局正则性问题提供新构造路径。"
source: "https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/"
author: "Terence Tao"
---

Alpöge 与 Buckmaster 已在光滑初始数据和光滑外力下，证明三类流体方程能够在有限时间内形成奇点，为攻克三维不可压缩 Navier–Stokes 方程的全局正则性问题提供了新的构造路径；Navier–Stokes 本身以及无外力情形仍未由这项工作解决。三个已取得结果的模型分别是不可压缩多孔介质（IPM）方程、二维 Boussinesq 方程和三维不可压缩 Euler 方程。其中，IPM 的相应结果此前已由 Córdoba 与 Martínez-Zoroa 取得，Alpöge 与 Buckmaster 改进其方法，将适用范围扩展到后两类方程。Tao 判断，这一路线很有希望进一步推广到 Navier–Stokes，但这仍是对后续研究的预期。

构造的核心是让**解的奇异性不断增强，同时让外力保持光滑**。从一个低频、带外力的解出发，每一步都加入一个频率更高的微小修正，使它在接近预定爆破时刻时才显著增长；为使修正后的解仍满足方程，也要同步调整外力。关键在于，解的修正可以产生较大影响，所需的外力修正却足够小。如果每轮修正的频率迅速提高，并对外力修正施加足够强的控制，就有望在无限迭代的极限中得到有限时间爆破的解，而外力依然光滑。

实现这种不对称增长，需要利用背景流动中的**不稳定性**。设原来的解为 u，加入的高频修正为 v，外力的对应修正为 g；要让 g 很小，v 就必须近似满足原方程在 u 附近的差分方程。在可以忽略非线性效应的阶段，这归结为求解线性化方程，并选择适当的背景解，让最初呈指数级微小的扰动在临近爆破时迅速放大。困难在于把增长的时机和幅度控制到恰当范围：到达爆破时刻时，扰动必须强到足以破坏光滑性，又不能提前大到使非线性效应摧毁整个估计。

在 Boussinesq 方程中，这一机制有一个可明确求解的局部模型：接近爆破时刻、靠近空间原点时，背景解在空间上呈线性变化，高频修正则呈平面波形态。这个特殊假设形式能够精确满足相应方程，无须额外加入非线性修正，从而把核心增长机制化为一组显式的常微分调制方程，并展示出所需的不稳定性。不过，把局部模型变成完整的严格构造，还必须处理空间截断等大量技术问题。相较于 Córdoba–Martínez-Zoroa 的原始方案，新构造中的常微分方程似乎具有更强的不稳定性，高频修正也表现出更好的空间局域性，这些改进使方法能够适用于更多流体方程。

这项研究大量使用 AI 辅助，相关工作也已在 Lean 中完成形式化。作者仍在整理和简化证明，初步预印本因外部事件而提前公开，完整论述尚未全部打磨完毕，Boussinesq 论文的引言已可作为理解主要机制的入口。Tao 强调，这类进展的首要价值在于揭示新的数学机制、增进理解，解决某个具体难题是衡量这一目标的代理指标。

另一条独立路线来自 Ganeshram、Duruisseaux 与 Anandkumar，目标是没有外力、没有边界的 Euler 方程。他们使用 physics-informed neural network（PINN）寻找近似自相似的爆破解，并得到了数值上稳定的候选形态。要把它升级为严格的有限时间爆破证明，仍须证明该形态具有足够强的稳定性，能够在候选解残差所要求的误差容限内，将近似解扰动为真实解。两条路线分别推进了逐级高频构造和近似自相似构造，但光滑外力下的严格爆破结果、无外力下的数值候选解，以及 Navier–Stokes 的最终突破，仍是必须区分的三个成果层级。
