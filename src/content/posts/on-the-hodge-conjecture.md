---
title: "On the Hodge conjecture"
date: 2026-10-23T20:24:14Z
category: reading
description: "Burt Totaro 在 Terence Tao 博客撰文探讨 Hodge conjecture 现状：为何悬而未决的猜想比速解更能推动数学发展，以及 Eyal Markman 2025 年证明四五维 abelian varieties 情形的意义。"
source: "https://terrytao.wordpress.com/2026/09/11/on-the-hodge-conjecture/"
author: "Terence Tao"
---

Hodge conjecture 的价值，在于它持续催生了连接拓扑、代数几何与分析的新思想；AI 即使能迅速证明新的特例，也不能仅凭解题速度衡量对数学的贡献。Burt Totaro 提出的反事实是：如果某个超人预言机在 William Hodge 于 1950 年提出猜想的第二天就宣布答案为真，并让数学界把问题视为解决，围绕它发展起来的大量知识可能根本不会出现。理解今天 AI 公司投入巨量资源攻克这类难题的意义，需要同时考察证明了什么，以及寻找证明的过程创造了什么。

Hodge conjecture 所凝结的核心谜团，是实几何的灵活性与复几何的刚性如何联系起来。研究对象是由代数方程定义的 **smooth complex projective variety**，目标是理解其中可能存在的复代数子空间。Wei-Liang Chow 在 1949 年的定理保证，在这一背景下，复解析子流形也是代数的。但实子流形远比复子流形自由，不能指望每个实子流形都能连续变形成复子流形。粗略地说，猜想试图用某些积分是否为零，识别哪些拓扑信息能够由复代数几何实现；精确表述则是：有理上同调中的每个 **Hodge class** 都应当是某个 **algebraic cycle** 的类。这里的代数闭链允许对子簇作有理系数组合，不能简单等同于把单个实子流形变形成复子流形。

支持猜想的基础证据来自 Solomon Lefschetz 约在 1924 年开展的工作：**Lefschetz (1,1)-theorem** 解决了余维为 1 的情形，相关结果也给出维数为 1 的代数闭链情形。不过，Lefschetz 和 Hodge 的一些重要证明按今天的标准存在缺口，完整论证依赖后来许多数学家完成的艰深分析工作，尤其是 Kunihiko Kodaira 在 1950 年前后的贡献。即便有这些基础成果，一般情形下最早尚未解决的案例——复四维簇上的余维 2 代数闭链——至今仍显得遥不可及。

直接解决的范围有限，却没有阻止猜想带来广泛的理论进展。它提供了一条研究纲领：代数闭链的结构应当受到 **Hodge theory**，也就是代数函数积分所携带的信息的控制。这一期待推动了 Phillip Griffiths 从 1960 年代开始发展的 **Variations of Hodge structure**，以及 Pierre Deligne 的 **absolute Hodge cycles**。其生产力也体现在推翻既有预期上：Griffiths 运用 Hodge theory，否定了 Grothendieck 关于代数等价与同调等价相同的猜想。近几十年，Claire Voisin 继续通过 Hodge theory 的新用法揭示代数闭链的结构，说明一个悬而未决的猜想仍能支撑大量可证明的知识。

Eyal Markman 在 2025 年证明四维和五维 abelian varieties 满足 Hodge conjecture，是这条研究路线的重大进展。Abelian varieties 是具有复代数结构的环面，相对于一般代数簇属于非常特殊的一类，却在数论等领域占据重要地位。这项成果背后有一条长期积累的链条：André Weil 在 1977 年识别出 **Weil type** 的 abelian varieties，其中存在大多数其他 abelian varieties 上不会出现的额外 Hodge classes；Ben Moonen 与 Yuri Zarhin 在 1995 年证明，在四维等低维情形，解决 Weil type 这一特殊类别就足以推出所有 abelian varieties 的结论。

将这些特殊 Hodge classes 实现为代数闭链，还需要把单个实例上的结论推广到连续变化的一族簇。Spencer Bloch 在 1972 年引入、Ragnar-Olaf Buchweitz 与 Hubert Flenner 在 2003 年推广的 **semi-regularity**，提供了在满足条件时完成这种推广的机制。长期以来，这个条件被认为过于苛刻，难以用于猜想的困难案例。Markman 的突破是构造出足够多的 semi-regular sheaves，并结合近几十年发展起来的 derived equivalences 与 hyperkähler manifolds 理论，完成四维和五维的证明。最终论证还需要把 Buchweitz–Flenner 的定理扩展到 **twisted sheaves**；Jonathan Pridham 于 2024 年提供了这一环节。

Totaro 相信，投入足够努力可以继续推进这些方法，但 AI 公司争取快速宣布突破的商业压力，可能改变数学家的研究节奏与评价标准。AI 生成的证明究竟能带来多少洞见，仍需具体检验；Markman 的成果则展示了一项突破如何依赖跨越数十年、由多人不断修正和连接的理论。数学思想的力量来自人们持续的讨论、检验与相互启发，因此评价 AI 对 Hodge conjecture 的贡献，还要看它能否把新的结论转化为数学共同体可以理解、延伸并用于其他问题的方法。
