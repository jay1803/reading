---
title: "The status of the Hodge conjecture"
date: 2026-10-24T13:29:34Z
category: reading
description: "Hodge conjecture 的核心障碍是无法把满足 Hodge 条件的有理拓扑类普遍转化为代数几何对象；Markman 对 abelian fourfolds 的突破解决了重要特例，但尚未给出通向一般情形的方法。"
source: "https://terrytao.wordpress.com/2026/09/12/the-status-of-the-hodge-conjecture/"
author: "Terence Tao"
---

Hodge conjecture 的核心障碍，是数学家仍不知道如何把满足 Hodge 条件的有理拓扑类普遍转化为代数几何对象；Markman 对 abelian fourfolds 的突破解决了重要特例，却尚未提供通向一般情形的方法。Claire Voisin 在 Terence Tao 博客的这篇客座文章中，区分了已有路线的适用边界，以及不同类型的反例可能对整个理论造成的影响。

Hodge class 同时受到拓扑与复几何的约束：它首先是偶数次的有理 Betti cohomology class，扩张到复系数后，又能由具有特定类型的闭微分形式表示。对次数为 2p 的类，这要求形式具有 (p,p) 型，即局部表达中分别含有 p 个全纯与反全纯微分。复余维为 p 的代数子簇所给出的上同调类满足这个条件；Hodge conjecture 断言，在光滑复射影簇上，这一必要条件也足够——每个 Hodge class 都是代数子簇之类的有理系数线性组合。

这里的**射影性**至关重要。若把范围扩大到紧复流形，就会出现存在非零二次 Hodge class、却没有任何余维一闭解析子集的例子，因此必须考虑全纯向量丛及其奇异推广 coherent sheaves 的 Chern classes。但 Voisin 已在 2002 年证明，某些紧 Kähler manifolds 具有非零 Hodge classes，其上所有 coherent sheaves 的 Chern classes 却全部为零。这为解析方法划定了边界：任何成功证明都必须实质性地利用原空间的代数性。

Cornalba–Griffiths 在 1975 年提出过一条利用代数性的路线：从射影簇 X 中去掉一个超平面截面，得到仿射 Zariski 开集 U；X 上的偶数次有理上同调类限制到 U 后，可以通过 U 上全纯向量丛的 Chern classes 来表示。下一步是利用 Hodge 条件，使这些向量丛能够延拓为 X 上的 coherent sheaves，进而获得代数对象。关键缺口始终存在：Hodge 条件究竟如何保证这种代数化，至今没有解决。

另一条路线试图按余维归纳。Deligne 的 Hodge structures 理论给出一个深刻归约：要证明 Hodge conjecture，只需证明每个正次数 Hodge class 都能在某个稠密 Zariski 开集上限制为零。换言之，这个类必须支撑在某个代数超曲面上，该超曲面可以具有严重奇异性；这一性质称为具有至少一阶 **coniveau**。但把类支撑到超曲面上本身就是极强的要求，多数上同调类，包括全纯形式给出的类，都不具备这一性质。归约明确了目标，却没有提供识别这种支撑的普遍方法。更根本的困难在于，代数几何能够很好地处理复系数上同调与 Hodge 条件，却缺乏对有理 Betti cohomology 的同等理解，两者的交会因此依然难以掌握。

即使完全理解某些 Hodge classes 的构造，也远不意味着能证明它们代数化。Voisin 举出的例子包括由上同调空间的最高外幂，经多重线性代数构造得到的一维 Hodge 类空间，其生成元的代数性仍未解决。Künneth standard conjecture 与 Lefschetz standard conjecture 也对应特定 Hodge classes 的代数性问题：这些类可以在任意光滑复射影簇的自乘 X×X 上构造出来。它们在 **motives** 理论中承担基础作用，因此这些具体特例本身就具有超出单个猜想的意义。

Markman 的近期进展发生在 Weil abelian varieties 上。Abelian variety 是可以嵌入复射影空间的复环面；Weil 型要求它具有满足虚二次关系的额外自同态，在复维数为 2n 的切空间上，该自同态的两个共轭特征值各出现 n 次。这样的结构通过形式运算产生一个二维的、次数为 2n 的 Hodge 类空间，称为 Weil classes。Markman 证明了所有 abelian fourfolds 上的 Hodge classes 都是代数的；这一问题经典地归约为 Weil classes 的代数性，而他的证明绕道研究某些六维 Weil abelian varieties 家族上的 Weil classes，再取得四维情形的结论。

把单个代数簇放入家族后，Hodge conjecture 又出现了变形层面的检验。在光滑射影家族中，各纤维的拓扑保持不变，复结构却可以变化，因此一个沿路径平行移动的有理上同调类，未必始终满足 Hodge 条件。它继续满足条件的参数位置构成 **Hodge locus**。Cattani–Deligne–Kaplan 在 1995 年证明，这些轨迹具有闭代数子集的结构，符合 Hodge conjecture 所预言的行为。但当家族定义在数域上时，猜想还要求相应轨迹具有数域上的定义；现有定理没有给出这层算术信息，更精确的缺口涉及 Hodge classes 是否都是 absolute Hodge。

这个缺口提供了一种潜在反驳方式：找到一个 Hodge class，其 Hodge locus 无法定义在数域上。前述通过显式线性代数构造的类无法提供这种反例。若这样的反例存在，Voisin 认为它对 motives 理论的破坏仍相对有限，并可能促成修正版猜想，即只要求 absolute Hodge classes 都是代数的。相比之下，**variational Hodge conjecture** 若失败，后果严重得多：一个在起始纤维上已由代数循环表示、且变形过程中始终保持 Hodge 性质的类，是否在其他纤维上也保持代数性？否定答案将直接推翻 Lefschetz standard conjecture，动摇 motives 理论的重要基础。

变形理论能在特定条件下回答这个问题。Bloch 为代数子簇提出的 semiregularity，以及 Buchweitz–Flenner 为向量丛和 sheaves 建立的对应条件，能在相关类保持 Hodge 性质时保证几何对象随之变形；对向量丛，需要所有 Chern classes 都保持 Hodge。Markman 正是成功利用了 Buchweitz–Flenner semiregular sheaves，处理六维 Weil abelian varieties 上的 Weil classes。然而，Voisin 判断这类条件过于受限，难以覆盖一般情形。首先，整数系数版本的 variational Hodge conjecture 已知不成立，说明某些代数循环无法在原有同调类中替换成 semiregular 对象，至少需要考虑取倍数。

更深一层的障碍来自代数循环携带的额外信息。一个循环除普通 Hodge class 外，还有更精细的 Deligne–Beilinson class；当普通上同调类为零时，后者就是 Abel–Jacobi invariant。已知存在这样的家族：起始循环的 Hodge class 能沿家族继续保持 Hodge 性质，但它的 Deligne class 无法延拓为另一纤维上任何代数循环的 Deligne class。因此，粗粒度上同调层面的可变形性，并不足以保证给定循环及其精细不变量一起变形。Hodge conjecture 的一般解法必须跨越的，正是可被形式运算识别的 Hodge 条件，与真正能够存在、支撑并随家族延续的代数循环之间的距离。
