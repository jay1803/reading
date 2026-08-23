---
title: "Visual-Focused Algorithms Cheat Sheet"
date: 2025-11-04T10:50:02Z
category: reading
author: "Nick M"
description: "从排序到神经网络、从压缩到密码学，40+ 个算法背后只有三种底层逻辑反复出现：分治（快排、FFT、视频压缩）、贪心局部最优（Prim's、Kruskal's、Huffman）、迭代松弛（Dijkstra's、Bellman-Ford、梯度下降）。理解这三种骨架，等于同时理解了大半个算法世界。"
source: "https://photonlines.substack.com/p/visual-focused-algorithms-cheat-sheet"
---

## TL;DR
从排序到神经网络、从压缩到密码学，40+ 个算法背后只有三种底层逻辑反复出现：分治（快排、FFT、视频压缩）、贪心局部最优（Prim's、Kruskal's、Huffman）、迭代松弛（Dijkstra's、Bellman-Ford、梯度下降）。理解这三种骨架，等于同时理解了大半个算法世界。

## 核心洞见

**覆盖范围**：排序（选择/插入/堆/快排/归并/Timsort）、搜索与图（二分、BFS/DFS、MST、最短路、最大流、Union-Find）、压缩编码（Huffman、LZ、DCT、JPEG、视频）、优化（单纯形法、整数规划、Newton、模拟退火）、机器学习（回归、SVM、决策树/随机森林/Boosted Trees、梯度下降、反向传播、七类神经网络、强化学习）、密码学（SHA、RSA、Diffie-Hellman）。

**非显然细节**：
- Timsort 是 Python/Java 默认排序算法——对真实数据（局部有序）比纯快排更快；本质是插入排序（处理小段 run）与归并排序（合并 run）的混合。
- LZ 压缩单遍动态构建字典，Huffman 需两遍（先统频率再编码）——LZ 的优势在工程实用性而非压缩率。
- JPEG 对亮度（Y）和色度（Cb/Cr）量化步长不同：人眼对亮度更敏感，色度可更激进压缩；DCT 本身不丢信息，量化才是"有损"来源。
- Bellman-Ford 在 V−1 次迭代后的"第 V 次"不冗余——它是负权环探测器。
- Ford-Fulkerson 用残差图（反向边）允许"撤回"已分配的流，是其能找到全局最大流的关键。
- PPO 用惩罚项近似约束取代自然策略梯度的二阶矩阵，换来一阶优化器的可扩展性；代价是偶尔接受坏更新。

## 隐藏限制
字符串搜索算法（KMP、Rabin-Karp 等）被作者以篇幅为由省去；视频压缩仅覆盖 H.264/H.265 框架，未涉及 AV1 等现代编解码器；复杂度分析普遍只给 Big-O，无常数因子或实测数据支撑。

## 同一个算法，不同的空间
梯度下降和 Bellman-Ford 在结构上几乎相同：都是对"当前估计"做迭代松弛直到收敛——前者作用在参数空间，后者作用在图的最短路径上。这种跨领域的同构感，是这份 cheat sheet 值得当参考手册反复翻看的原因。
