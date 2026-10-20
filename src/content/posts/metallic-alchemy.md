---
title: "Metallic alchemy"
date: 2026-10-20T03:52:08Z
category: reading
description: "metallic ratio 之间能否通过有理数运算精确互相构造，取决于它们是否属于同一个二次域，而非名称是否相邻。"
source: "https://www.johndcook.com/blog/2026/08/04/metallic-alchemy/"
---

不同 metallic ratios 能否通过有理数四则运算精确互相构造，取决于它们是否属于同一个二次域：名称上的"金、银、铜、铅"，对应着根号所决定的代数边界。

Metallic ratio M(n) 的连分数表示中每一项都是 n，也可以定义为满足 x＝n＋1/x 的较大根，因此 M(n)＝(n＋√(n²＋4))/2。Golden ratio、silver ratio 和 bronze ratio 分别是 M(1)、M(2)、M(3)，涉及的根式分别为 √5、√2 和 √13。即使同时使用 silver ratio 和 bronze ratio，也无法通过有限次有理数四则运算得到 golden ratio；这些运算可以给出任意接近的近似值，却无法精确产生所需的 √5。

这种障碍并不随"金属"的名称排列。n＞3 的 metallic ratios 没有通行名称，John D. Cook 将 M(4) 暂称为 lead ratio，就能实现一次"铅变金"：M(1)＝(M(4)－1)/2。原因是 M(4)＝2＋√5，与 golden ratio 共享同一个根式，减去 1 再除以 2 就完成了精确转换。

推广来看，M(n) 与 M(m) 能够互相构造，当且仅当 ℚ(√(n²＋4)) 与 ℚ(√(m²＋4)) 是同一个域；等价条件是 **(n²＋4)/(m²＋4) 为某个有理数的平方**。这个判据把逐个尝试的"炼金术"变成了统一的代数问题：两个根式相差一个有理数倍，就不会引入新的无理数成分。

Bronze ratio 也有这样的对应物。将 M(36) 称为 copper ratio、M(393) 称为 tin ratio，由于 (3²＋4)/(36²＋4)＝(1/10)²，且 (3²＋4)/(393²＋4)＝(1/109)²，两者各自都能精确构造出 M(3)，无需把 copper 与 tin 混合使用。原文第二个等式的分母写成了 292²＋4，与等式及前文定义不符，应为 393²＋4。这套数学"炼金术"的关键，在于识别外表不同的数是否共享同一种二次无理结构。
