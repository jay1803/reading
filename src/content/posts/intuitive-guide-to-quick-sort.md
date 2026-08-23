---
title: "Intuitive Guide to Quick Sort"
date: 2025-11-04T10:47:18Z
category: reading
author: "Nick M"
description: "Quick Sort 在实践中跑赢 Merge Sort，核心原因是 cache-locality：L1 缓存比 RAM 快 100 倍，Quick Sort 顺序访问内存的特性让数据长期驻留缓存——尽管它的比较次数比 Merge Sort 多约 25%。"
source: "https://photonlines.substack.com/p/intuitive-and-visual-guide-to-quick"
---

## TL;DR
Quick Sort 在实践中跑赢 Merge Sort，核心原因是 cache-locality：L1 缓存比 RAM 快 100 倍，Quick Sort 顺序访问内存的特性让数据长期驻留缓存——尽管它的比较次数比 Merge Sort 多约 25%。

## 核心洞见
In-place Quick Sort 的关键创新是用双指针在原数组内就地交换，彻底避免 Merge Sort 式的额外内存分配。每一轮 partition 结束后，pivot 必然落在最终排序位置，左侧全 ≤ pivot，右侧全 ≥ pivot；递归只处理剩余子数组，无需额外合并步骤。

## 具体机制
1. 选 pivot（通常选首元或末元）
2. 左指针从 pivot 右侧向右扫，找第一个 > pivot 的元素；右指针从末端向左扫，找第一个 < pivot 的元素
3. 两指针未交叉时：交换两者所指元素，各自推进一步；循环
4. 指针交叉后：将右指针位置的元素与 pivot 交换——pivot 落位
5. 对 pivot 左、右两个子数组递归执行

## 隐藏限制
- 已排序数组 + 固定选首元作 pivot：每轮 partition 极度不平衡，退化为 O(n²)；随机化 pivot 是标准解
- 不稳定排序：相等元素的原始顺序无法保证（Merge Sort 天然稳定）
- 比 Merge Sort 多约 25% 比较次数，并行化能力也更弱

选 pivot 的策略直接决定算法性能上界——将 pivot 随机化是把 O(n²) 最坏情况概率化为可忽略的唯一手段，这个细节在大多数教科书里只有一句话。
