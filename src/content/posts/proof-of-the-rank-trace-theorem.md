---
title: "Proof of the rank-trace theorem"
date: 2026-10-06T17:43:05Z
category: reading
description: "实对称矩阵的秩迹不等式 (tr A)² ≤ r·tr(A²) 的完整证明：先对角化矩阵，再用 Cauchy-Schwarz 不等式作用于非零特征值向量，并依赖迹在相似变换下的循环不变性质。"
source: "https://www.johndcook.com/blog/2026/09/05/proof-of-the-rank-trace-theorem/"
author: "John"
---

实对称矩阵的 **rank-trace inequality** 把矩阵的秩与迹联系起来：若 A 的秩为 r，则 (tr A)² ≤ r·tr(A²)。其中 tr A 是矩阵对角线元素之和；当 A 非零时，这个不等式给出秩的下界 r ≥ (tr A)² / tr(A²)。证明的核心是将 A 对角化，再把问题化为特征值向量上的 **Cauchy-Schwarz inequality**。

实对称矩阵 A 可以通过相似变换化为对角矩阵 D，对角线上排列着 A 的特征值。相似变换保持秩与迹，且 A² 与 D² 也相似，因此可以在 D 上证明原不等式。把非零特征值组成向量 v＝(λ₁,…,λᵣ)，其维数正好等于矩阵的秩 r；再取同维的全 1 向量 w。Cauchy-Schwarz inequality 给出 (λ₁＋…＋λᵣ)² ≤ (λ₁²＋…＋λᵣ²)·r。特征值之和等于 tr A，特征值平方之和等于 tr(A²)，代入便得到所需结论。

上述证明中，迹在相似变换下保持不变，依赖于 **迹的循环性质**。将矩阵乘积的对角线元素展开求和，可以看到 tr(AB) 与 tr(BA) 都是在求和 AᵢⱼBⱼᵢ，交换求和指标即可证明二者相等。于是，若 D＝P⁻¹AP，就有 tr D＝tr(P⁻¹AP)＝tr(APP⁻¹)＝tr A。这个性质可以推广到多个因子的循环移位，例如 tr(ABC)＝tr(BCA)＝tr(CAB)，但不能推广到任意排列，交换部分因子的顺序可能改变迹。整个证明由此把矩阵层面的秩与迹，归结为非零特征值的数量、总和与平方和之间的约束。
