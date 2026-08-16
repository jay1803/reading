---
title: "Donkey.bas is 45 Years Old – 131 line of Glory"
date: 2026-08-16T10:59:00Z
category: reading
description: "DONKEY.BAS 是 1981 年 Bill Gates 与 Neil Konzen 为 IBM PC 写的 131 行 GW-BASIC 演示游戏，是个人电脑工业化起点的现场证物——微软联合创始人亲自下场写游戏 demo，说明当时软件生态几乎是空白。"
source: "https://donkeybas.com/"
---

## 摘要

DONKEY.BAS 是 1981 年 Bill Gates 与 Neil Konzen 为 IBM PC DOS 写的图形演示游戏，随 IBM PC 出货，用于展示 CGA 彩色图形与 PC 扬声器音效。完整代码仅 131 行 GW-BASIC，操作极简：只需切换车道躲避迎面而来的驴。

这 131 行的意义不在于游戏本身，而在于它是 1981 年个人电脑工业化起点的现场证物——微软联合创始人亲自下场写游戏 demo，说明当时的软件生态几乎是空白，需要操作系统厂商亲自填内容。代码本身也值得一看：在极度受限的硬件上，它用 DEF SEG/POKE 直接操作内存，用 SCREEN 1,0 切换 CGA 模式，用 PLAY 命令驱动蜂鸣器，是 BASIC 时代典型的"紧贴硬件"写法。

此页面是 2026 年的 JavaScript 重制版，45 周年纪念，可在浏览器中直接游玩，并附有原始 BASIC 源码。
