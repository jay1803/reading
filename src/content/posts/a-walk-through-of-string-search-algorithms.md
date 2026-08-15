---
title: "A Walk-Through of String Search Algorithms"
date: 2025-11-04T10:50:02Z
category: reading
description: "Boyer-Moore 之所以快到 grep 每字节只用 3 条 x86 指令，是因为它从末尾往前匹配，失配时直接跳过大段文本——处理的字节越少，比处理得越快更值钱。"
source: "https://photonlines.substack.com/p/a-walk-through-of-string-search-algorithms"
---

## TL;DR
Boyer-Moore 之所以快到 grep 每字节只用 3 条 x86 指令，是因为它**从末尾往前匹配**，失配时直接跳过大段文本——处理的字节越少，比处理得越快更值钱。

## 五种算法的分野
- **Boyer-Moore**：bad character + good suffix 两张跳表，失配时可跳 n 位；单模式场景最快，模式串极短时优势消失。
- **Rabin-Karp**：rolling hash 让窗口滑动只需一次加减而非全量重算；不适合单模式搜索，但可把多个模式哈希进同一张桶，一次扫描全部命中。
- **KMP**：前缀表（partial match table）记录每个位置的最长 border，失配时直接跳，线性时间。
- **Aho-Corasick**：把所有模式构建成 trie + failure links，一次遍历找所有模式——本质是 KMP 的多模式扩展。
- **Z 算法**：构建 Z-array（每个位置与前缀的最长公共子串长度），线性时间；文章称其比 KMP"更高效"，但实际时间复杂度相同，差异仅在常数与实现复杂度。

## **值得质疑**
文中用 ASCII 值加总作为 Rabin-Karp 的哈希示例——生产中完全不可用，碰撞率极高（任何 ASCII 和相同的字符排列都会误判）；正式实现需用多项式滚动哈希。

## 留下的那个想法
所有高效算法共享同一个结构：预处理阶段把"失配时跳多远"编码进表格，搜索时直接查表。跳过的字节永远不需要被看见。
