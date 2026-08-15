---
title: "Correlated randomness in Slay the Spire 2"
date: 2026-06-18T08:02:39Z
category: reading
description: "Slay the Spire 2 的所有随机数生成器第一次输出之差是固定常量——这是 C# =System.Random= 输出对种子呈线性的数学必然，而非开发者的疏忽。Spire 2 的\"修复\"方向正确（为不同 RNG 分配不同初始种子），但底层算法的线性性使这个修复形同虚设。"
source: "https://tck.mn/blog/correlated-randomness-sts2/"
---

## TL;DR
Slay the Spire 2 的所有随机数生成器第一次输出之差是固定常量——这是 C# =System.Random= 输出对种子呈线性的数学必然，而非开发者的疏忽。Spire 2 的"修复"方向正确（为不同 RNG 分配不同初始种子），但底层算法的线性性使这个修复形同虚设。

## 发现
- Neow's Bones 在 Underdocks 约 54% 概率给出 Debt（均匀分布应为 ~10%），大量玩家把这归咎于"手气差"，实为 CRNG 导致的必然偏差。
- Rebound 在单人游戏的 Trash Heap 中字面意义上不可能出现，导致游戏内成就系统（Compendium）无法完成。
- Underdocks 首战掉药水概率 76%，Overgrowth 仅 4%——相差近 20 倍。
- Large Capsule 在 Underdocks 出现概率约 1.65%（Neow 选项），但一旦出现则 63% 概率附带稀有遗物，远强于平均水平。
- Act 2 的 Doll Room、Crystal Sphere，以及几乎所有事件的第一次随机结果，均可从 Neow 选项或首战金币数量反向推算。
- Spire 2 使用浮点 [0,1] 再乘以范围的采样方式（而非 Spire 1 的取余法），导致几乎每一对 RNG 之间都存在可利用的相关性，覆盖范围远超 Spire 1。

## 根因：线性性如何传播
Spire 2 的做法是 =new Rng(seed + hash("name"))=，为每个 RNG 分配不同偏移量的种子。问题出在 =System.Random= 的实现：
1. 构造函数把 =MSEED - abs(seed)= 写入 =SeedArray[55]=，再用减法填充其余 55 个槽位。
2. =InternalSample= 每次输出 =SeedArray[i] - SeedArray[j]=，同样是减法。
3. 减法保持线性：=(x₁·S + y₁) - (x₂·S + y₂) = (x₁-x₂)·S + (y₁-y₂)=。
4. 结论：任意 RNG 的第 n 次输出均可写成 =x·S + y=，两个种子相差 =d= 的 RNG，其第一次输出恰好相差 =x·d=，这个差值是已知常数。

## 破坏了什么假设
Spire 2 的修复思路本身成立：不同种子 → 不同序列。失效点在于 C# 默认 PRNG 的线性性——开发团队大概假设"标准库的随机生成器足够好"，而实际上这个算法明确被文档记录为不适合需要统计独立性的场景。

修复方案极其简单：将 =System.Random= 替换为任意非线性 PRNG（如 PCG32，50 行代码，3 行改动），即可消除所有相关性，并顺带解决 Spire 1 跨平台种子不一致的历史问题。游戏仍在 Early Access，修复窗口大于 Spire 1 当年。
