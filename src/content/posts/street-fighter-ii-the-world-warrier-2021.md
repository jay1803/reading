---
title: "Street Fighter II, the World Warrier (2021)"
date: 2026-02-14T20:39:06Z
category: reading
description: "《街头霸王II》标题拼错 \"Warrier\" 时 GFX ROM 已烧制完毕，无法改任何像素；主美 Akiman 在截止前三天用 sprite 拼接 + 调色板重映射，把 Guile 小腿 sprite 里唯一可见的那一个像素当成画笔，把 'l' 的顶部截断造出 'i' 上方的点。"
source: "https://fabiensanglard.net/sf2_warrier/"
---

## TL;DR
《街头霸王II》标题拼错 "Warrier" 时 GFX ROM 已烧制完毕，无法改任何像素；主美 Akiman 在截止前三天用 sprite 拼接 + 调色板重映射，把 Guile 小腿 sprite 里唯一可见的那一个像素当成画笔，把 'l' 的顶部截断造出 'i' 上方的点。

## 关键时刻与背后逻辑
CPS-1 硬件严格分离 GFX ROM（tile 图形数据）和指令 ROM（68000 CPU 逻辑）。GFX 已定型不可改，但 CPU 仍控制"调用哪个 tile、叠在哪里、用哪套调色板"。Akiman 先把末尾 "ier" 三个 tile 换成从 "World" 借来的 "or" tile——问题从拼错字母变成了多出一个 'l'，标题读作 "Warrlor"。

突破点是 Guile 小腿 sprite（tile 0x96）：256 个像素中只有左下角 1 个可见，其余全透明。搭配 logo 蓝色调色板重映射，那 1 个像素成了深蓝色笔触。三次叠加精确坐标遮断 'l' 顶部，'i' 上的点凭空出现。代价：每次绘制浪费 255 个透明像素只控制 1 个有效像素。

## 边缘判断
为修这次 typo 专门生成的正确 "IOR" tile 集，在所有后续改版里从未被使用——副标题已改成 "Champion Edition"，然后 "Hyper-fighting"。
