---
title: "Gilbreath’s conjecture: a Cramér random model and a deterministic analysis"
date: 2026-07-12T08:02:55Z
category: reading
description: "Gilbreath 猜想（1958，实际由 Proth 于 1878 年率先提出）：从素数序列出发，反复对相邻项取绝对差，每一行的首项始终为 1。Odlyzko 已数值验证至前 10^13 行。陶哲轩与合作者 Zachary Chase、Zach Hunter 在新预印本中从两个方向推进：（1）对 Cramér..."
source: "https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/"
---

## Gilbreath 猜想被 Cramér 模型确认，逆定理完整刻画失败模式

Gilbreath 猜想（1958，实际由 Proth 于 1878 年率先提出）：从素数序列出发，反复对相邻项取绝对差，每一行的首项始终为 1。Odlyzko 已数值验证至前 10^13 行。陶哲轩与合作者 Zachary Chase、Zach Hunter 在新预印本中从两个方向推进：（1）对 Cramér 随机模型几乎确定地证明该猜想；（2）建立一个确定性逆定理，完整列举猜想失败的所有可能模式。

### 概率方向：Cramér 模型范围内的几乎确定结论

Chase 此前对 B 较小的均匀分布 {0,...,B-1} 证明了类似结论；新文章将 B 推到 O(log N) 量级，与 Cramér 模型吻合。关键观察：绝对差运算 x → |x-y| 保持"c-separated 集合"的间隔性，即任何 c-分离分布的预像仍是 c-分离的。这意味着：只要初始分布不集中于等差公差为 c 的集合（例如全偶数、全奇数），大型"倒三角形"结构出现的概率就以指数速率衰减。对不超过 O(log N) 大小的初始数据应用 union bound + Borel-Cantelli 引理，得到几乎确定的首项为 1 结论。

文章还分析了连续指数随机模型（模拟前 N 个规范化素数间隙）：第 k 行均值恒为 1，但衰减速率 α_k 尚不清楚；数值显示 α_k ≈ k^(-c)，与猜想相容，但未证明。

### 确定性方向：失败模式的逆定理

若初始数据满足 Cramér 界（|d_i| ≤ log^C N），但最终首项不为 1，则必然出现以下两种结构之一：
1. 某一行出现长度 > c·log N 的连续零串；
2. 经过若干次迭代后，出现长度极长（> log^C N）的连续块，且块内所有值等于某个偶数 v。

奇数 v 的情形可用奇偶分析排除（素数除 2 外全为奇数，导致每行首项奇、其余项偶的固定奇偶结构）；偶数 v 的情形需独立性假设才能用概率手段排除。该逆定理将 Gilbreath 猜想化归为两个更具体（但仍极难）的断言——目前证明仍遥不可及，但问题结构已被完全理清。
