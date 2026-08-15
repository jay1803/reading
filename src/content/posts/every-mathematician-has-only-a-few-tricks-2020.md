---
title: "Every mathematician has only a few tricks (2020)"
date: 2025-11-30T20:20:35Z
category: reading
description: "Gian-Carlo Rota 早年说过：就连 Hilbert 也只用了寥寥几个 trick——这句话远比字面意思深：一个足够普适的 trick 能从量子力学一路覆盖到粒子物理的分类学，表面上是\"方法论的节俭\"，实质是对数学结构同构性的高度压缩。"
source: "https://mathoverflow.net/questions/363119/every-mathematician-has-only-a-few-tricks"
---

## TL;DR

Gian-Carlo Rota 早年说过：就连 Hilbert 也只用了寥寥几个 trick——这句话远比字面意思深：一个足够普适的 trick 能从量子力学一路覆盖到粒子物理的分类学，表面上是"方法论的节俭"，实质是对数学结构同构性的高度压缩。

## 核心洞见

MathOverflow 的这条 thread 以 Rota 的观察为起点，邀请数学家说出自己反复使用的 trick。票数较高的物理侧回答给出了一把万能钥匙：

**"两个对易矩阵可以同时对角化"**

一旦系统具有某种对称性，它的生成元就与 Hamiltonian 对易，只需先对角化对称算符，就能大幅简化本征值问题。这个 trick 的覆盖半径极大：
- **平移对称** → 傅里叶变换（波方程、热方程、自由电子）
- **离散平移** → Bloch-Floquet 定理 → 能带结构 → 导体/绝缘体分类
- **旋转对称** → SO(3) 表示 → 氢原子轨道 → 周期表的列结构（2,6,10,14…）
- **SU(3) 对称** → 粒子物理中的强子动物园变得有序（介子九重态、重子十重态）

另一个 trick 来自后验条件化：**德州神枪手谬误的数学逆用**——先随机射击再画靶，看似荒谬，但"后验地条件化一个随机事件"在数学中是合法操作，被用于 scatter-shot boson sampling：无法精准生成单光子时，直接后选择那些恰好产生光子的晶体，从而绕开控制精度的门槛。

## 值得质疑

缓存版本仅保留了两条回答，原 thread 有大量来自代数、拓扑、分析等方向的 tricks，此处总结覆盖范围有限，不代表 thread 全貌。

## 剩下的想法

"只有几个 trick"听起来像是局限，实则是能力密度的标志——越少的工具覆盖越多样的问题，说明你抓到了底层的结构等价性。Rota 的观察其实是在表扬。
