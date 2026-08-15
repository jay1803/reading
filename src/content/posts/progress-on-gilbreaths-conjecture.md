---
title: "Progress on Gilbreath’s conjecture"
date: 2026-07-12T08:02:55Z
category: reading
description: "Gilbreath 猜想：从素数出发，对连续项反复取差的绝对值，每行首项始终是 1。命题简单到可以对任何知道素数的人解释，但几十年来无人能证明。Erdős 预测证明它需要两百年——Cook 认为这个关于猜想的元猜想比猜想本身更有意思。"
source: "https://www.johndcook.com/blog/2026/07/11/progress-on-gilbreaths-conjecture/"
---

## Tao 的工作解释了 Gilbreath 猜想为什么"应该"成立，但承认连第一步严格证明都远超当前技术

Gilbreath 猜想：从素数出发，对连续项反复取差的绝对值，每行首项始终是 1。命题简单到可以对任何知道素数的人解释，但几十年来无人能证明。Erdős 预测证明它需要两百年——Cook 认为这个关于猜想的元猜想比猜想本身更有意思。

## Tao 等人做了什么

Tao、Chase、Hunter 三人的新论文走了两条路：

1. *概率模型*：把素数换成满足 Cramér 分布的随机数组，证明这类随机模型几乎必然满足 Gilbreath 性质。关键条件是初始数据"不集中于任何等差数列"——素数满足这个条件，因此可作为猜想成立的启发式依据。

2. *确定性逆定理*：用纯初等方法证明，Gilbreath 数组要违反猜想，只有两种路径：出现极长零串，或出现极长同值块。两者在概率上均极不可能出现。

## 但这离证明还差多远

Tao 在论文中明确写道："even the first step … is far out of reach"。Cramér 猜想是推导链的第一环，而 Cramér 猜想本身也未解。随机模型与真实素数之间的鸿沟就是整个未解问题所在。论文的意义是建立了一个精确的启发式框架，而非走向证明的实质一步。
