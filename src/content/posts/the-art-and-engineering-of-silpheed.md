---
title: "The art and engineering of Silpheed"
date: 2026-06-02T08:01:20Z
category: reading
description: "Silpheed 的厉害之处不是在 Mega-CD 上“硬塞电影”，而是把 FMV 重新设计成适合瓦片式显存、16 色调色板、150 KiB/s 光驱和双 CPU 协作的系统工程：艺术选择主动服从硬件约束，编码格式再把这些约束变成压缩机会。"
source: "https://fabiensanglard.net/silpheed/index.html"
---

## TL;DR
Silpheed 的厉害之处不是在 Mega-CD 上“硬塞电影”，而是把 FMV 重新设计成适合瓦片式显存、16 色调色板、150 KiB/s 光驱和双 CPU 协作的系统工程：艺术选择主动服从硬件约束，编码格式再把这些约束变成压缩机会。

## 核心机制
Game Arts 没有把真实影像压缩成小窗口、低质量的 CD-ROM 视频，而是从底层限制反推美术风格：扁平多边形、总共 16 色、少量抖动、偏电影化的黑边和 15fps 为主的帧率。这让画面天然更容易被 Mega-CD 的瓦片系统表示，也避免了当时许多 FMV 游戏常见的压缩脏感。

Mega-CD 与 Genesis 的结构本身很别扭：Genesis 主 CPU、VDP、Z80/YM2612 音频系统仍在工作，Mega-CD 侧另有 12.5MHz m68k、256KB Word RAM、512KB Program RAM、Ricoh PCM、图形 ASIC 和慢速 CD-ROM。Silpheed 利用 Mega-CD 子 CPU 在 Word RAM 中双缓冲渲染背景 B，Genesis 主 CPU负责 HUD 和精灵层，两边通过共享内存与音频混音协同。

视频格式的关键不是传统意义上的连续帧差分压缩。Silpheed 每帧自包含，包含本帧所需的所有 tiles 和 tilemap；真正的压缩来自 tilemap 结构本身。以某一帧为例，896 个 tile 中有 456 个只是 15 种纯色 tile 的重复引用，单靠 tilemap 复用就削掉约 50% 的带宽。

剩下的 tile 里，许多只有两种颜色。Mega-CD ASIC 的 “Font bit” 寄存器原本用于快速生成双色文字，Silpheed 把它当成解压辅助：写入两个 4-bit 颜色索引和一个 16-bit 位图模式，ASIC 就能展开成两行 8 像素的 4-bit tile 数据。对示例帧来说，234 个双色 tile 用这种方式生成，进一步节省带宽和 CPU 的 nibble 写入成本。

tilemap 本身也被压缩。正常 768 个 tile 位置若各存 10-bit 索引约需 960 字节；Silpheed 利用索引常按扫描顺序线性递增的特征，用 768-bit 位图标记“自动递增”还是“读取立即值”，示例中压到 96 字节位图加 556 字节 payload，约少 30%。

## 约束如何塑造美术
文章最有价值的点在于它把“美术品味”解释成工程策略。Silpheed 的画面之所以到今天仍被称赞，不只是艺术家厉害，而是艺术家接受了 16 色、低带宽、瓦片复用、局部低帧率这些限制，并用扁平科幻几何、强对比构图和受控调色把限制伪装成风格。

复杂纹理关卡暴露了这套方法的边界。Stage 1 和 Stage 10 的“fractal”质感很难压缩，几乎不能利用纯色 tile 或双色 ASIC trick，只能大量使用 raw tile，并把帧率降到 7.5fps。这说明 Silpheed 的奇迹不是通用视频编码突破，而是内容、编码和硬件特性高度匹配后的局部最优。

玩法画面还用了调色板循环：激光和爆炸不是存储多色动画，而是保留调色板末端四个颜色并逐帧 shift。代价是互动场景的艺术设计实际只能使用 12 色，而非 cutscene 可用的完整 16 色。

## 值得保留的判断
Silpheed 的工程价值在于它没有把硬件当成缺陷列表，而是把硬件暴露出来的结构变成表达语言：纯色 tile、双色 tile、线性 tilemap、低帧率、窄带宽、调色板循环，全都进入了美术和编码决策。

这也是 Mega-CD 时代 FMV 的一条反例：同样是 150 KiB/s 光驱和弱 CPU，失败作品试图模拟电影，Silpheed 则设计了一种“看起来像电影的实时硬件友好图像”。它不是更强的压缩，而是更聪明地选择了什么值得被压缩。
