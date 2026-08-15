---
title: "Bloom filters are good for search that does not scale"
date: 2025-11-08T10:15:01Z
category: reading
description: "Bloom filter 全文搜索存在一个可量化的断点：文档数超过约 7,200 篇时，倒排索引的空间效率就已超过 Bloom filter 索引——不是某个模糊的\"规模足够大\"，是 7,200 篇。"
source: "https://notpeerreviewed.com/blog/bloom-filters/"
---

## TL;DR
Bloom filter 全文搜索存在一个可量化的断点：文档数超过约 7,200 篇时，倒排索引的空间效率就已超过 Bloom filter 索引——不是某个模糊的"规模足够大"，是 7,200 篇。

## 发现
作者确实构造出了可工作的大规模 Bloom filter 搜索方案：对整个词典建树，每个叶节点存储含对应词的文档过滤器指针；查询复杂度降为 O(log n)，技术上成立。

## 为什么重要
Bloom filter 对小型静态网站有吸引力，是因为每篇文档的 filter 只需约 1.25 KB，而同等覆盖的倒排索引初始成本约 9 MB。但倒排索引只存一次词典，此后每增加一篇文档仅增加指针；Bloom filter 则让每篇文档独立编码全部词汇，空间随文档数线性增长。两条线在约 7,200 篇时交叉。

## 破坏了什么常识
"Bloom filter 省空间"是真的，但仅在 filter 数量远少于词典大小时成立。根本原因：filter 之间没有信息共享，各自重复编码相同词汇；而倒排索引天生共享词典。这一逻辑可以迁移：任何"单体高效、集合失效"的结构（比如人均 blocklist）都会遭遇同样的边界。

## 值得留下的想法
作者把"Bloom filter 之间没有 synergy"上升为一条通用设计原则——这比搜索结论本身更有用，是判断任何去中心化数据结构适用边界的简洁工具。
