---
title: "Visualizing the Gilbreath expectation sequence"
date: 2026-08-30T07:32:40Z
category: reading
description: "Gilbreath 猜想的难点转化为研究一个随机差分过程产生的期望序列，最新数值实验显示其非单调衰减可能受二进制数位结构和 Sierpinski gasket 控制。"
source: "https://terrytao.wordpress.com/2026/07/14/visualizing-the-gilbreath-expectation-sequence/"
---

Gilbreath 猜想的难点可以转化为研究一个由随机差分过程产生的期望序列，而最新数值实验显示，这个序列的非单调衰减可能受二进制数位结构和 Sierpinski gasket 控制。所谓 **Gilbreath expectation sequence**，来自一个倒金字塔形的 Gilbreath array：顶层放置相互独立、均值为 1 的指数随机变量，以下每个元素都等于其正上方两个元素之差的绝对值；左侧对角线上各随机变量的期望构成序列 \(a_n\)。由于这个过程具有平稳性，第 \(n\) 行任意位置的期望都等于 \(a_n\)。

这个随机模型与素数间隔相连：若顶层改用最初一批归一化素数间隔，那么这些间隔被猜测渐近服从几何分布；在 prime tuples conjecture 等标准猜想下，Gilbreath array 前若干行的元素应按相应尺度衰减。因此，Gilbreath 猜想是否成立，与 \(a_n\) 随 \(n\) 衰减得多快密切相关；随机指数模型提供了一个可计算的代理问题，用来分离素数分布本身的复杂性与绝对差分运算产生的动力学。

原则上，每个 \(a_n\) 都能通过复杂的多元积分写成显式有理数，但直接计算很快变得困难。Tao、Chase 和 Hunter 的论文只求出了有限范围内的精确值，其余部分依靠大量 Gilbreath arrays 的 Monte Carlo 模拟；数值结果依大数定律与已知精确值高度吻合。Michael Ross 随后把精确计算推进到更大的 \(n\)，仍保持同样良好的拟合。尽管这些计算提供了可靠的有限尺度图景，序列的渐近行为依然不清楚：\(a_n\) 明显不单调，目前甚至无法证明它有界，原论文只能得到一个下界型不等式，限制它不可能衰减得过快。

Ross 的新数值结果进一步提出了一条经验公式，其中 \(n\) 的二进制展开所含 1 的个数 \(s_2(n)\) 决定了相当一部分波动。这个看似突兀的二进制统计量与 Lucas's theorem、Kummer's theorem 以及 Sierpinski gasket 有直接联系：如果 Gilbreath array 顶层除一个孤立的"尖峰"外全部为零，反复取相邻绝对差就会生成 Sierpinski 三角形图案；从第零行开始计数时，第 \(n\) 行非零的 1 恰有 \(2^{s_2(n)}\) 个。这个数量与经验预测具有相同的数位依赖形状，虽然具体常数并不一致，说明序列的起伏很可能继承了模 2 二项式系数的分形结构。

一般随机初值下，数值动画显示许多局部 Sierpinski gasket 会短暂形成，随后逐渐衰减，彼此相遇时还会发生"碰撞"并破坏原有结构。这为 \(a_n\) 的非单调性提供了具体机制，却还没有导出可信的渐近概率模型：整个过程既不像熟悉的独立随机场，也不像已有的随机形状增长模型。Tao 因而把问题指向概率论和统计物理，希望找到能够同时描述分形生成、衰减与碰撞的尺度极限；Gilbreath expectation sequence 的核心谜团，正是确定二进制分形骨架如何在连续随机振幅的相互作用下塑造长期衰减。

这项研究也展示了 coding agent 对数学探索方式的实际改变：论文中由 Python 生成的静态图，可以在约一小时内改造成包含精确值、Monte Carlo 数据、Ross 经验预测和阵列演化过程的交互式 applet；代理还把反复积累的可视化经验维护在一份 skill Markdown 文件中。这里的可视化并非仅用于展示结果，它让有限尺度上的 Sierpinski 碎片、碰撞和衰减直接可见，从而把一个难以解析处理的期望序列转化为可观察的随机分形动力系统。
