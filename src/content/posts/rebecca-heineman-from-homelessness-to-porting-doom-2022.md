---
title: "Rebecca Heineman – from homelessness to porting Doom (2022)"
date: 2025-11-20T13:54:34Z
category: reading
author: "Adam Gordon Bell"
description: "Rebecca \"Burger Becky\" Heineman，跨平台移植专家，视频游戏行业先驱。1980 年赢得北美首届 Atari 2600 Space Invaders 全国锦标赛，由此入行。曾参与创立 Interplay，主导了 Wolfenstein、Doom 等经典游戏的主机移植工作，覆盖 Apple..."
source: "https://corecursive.com/doomed-to-fail-with-burger-becky/"
---

## 嘉宾背景

Rebecca "Burger Becky" Heineman，跨平台移植专家，视频游戏行业先驱。1980 年赢得北美首届 Atari 2600 Space Invaders 全国锦标赛，由此入行。曾参与创立 Interplay，主导了 Wolfenstein、Doom 等经典游戏的主机移植工作，覆盖 Apple II、Commodore、Super Nintendo、Game Boy、3DO 等几乎所有当时主流平台。主持人 Adam Gordon Bell，CoRecursive 播客创始人。

## TL;DR

一个从未写过代码、靠自学逆向 Atari 2600 硬件起家的无家可归少年，用 10 周时间把 Doom 移植到 3DO——一台比原版硬件慢 5 倍的主机——交出了 bug-free 的版本；而委托方对"90% 完成"的定义，是"游戏在 PC CD 上能跑，3DO 也有 CD 播放器"。

## 自学路径：从流浪少女到移植专家

Becky 15 岁时离家出走，住在超市垃圾桶旁，靠 JC Penny 的临时工作维生。进入行业的契机是赢得 Atari 锦标赛后被聘为街机修理工，从修理电路板中学会 TTL 逻辑；而真正的编程能力来自一个硬件巧合：Apple II 和 Atari 2600 共用 6502 处理器，她用 Apple II 的 monitor 反汇编了自己盗版的 Atari 游戏卡带，逐寄存器摸索出整个 2600 的显示架构。没有课程，没有教材，靠迭代试错，她自主掌握了一套当时连正规开发者都需要授权才能获取的技术。

## "90% 完成"是一句谎言

Art Data 的 CEO 以 25 万美元买断 Doom 在 3DO 的授权，对外宣称游戏开发 90% 完工，但实际上：原开发者从未存在，Art Data 拿着的只是一张 PC 零售版 Doom 的 CD——他的逻辑是"游戏在 CD 上能跑，3DO 有 CD 驱动器，所以算 90% 完成"。Becky 被迫从零开始，在 10 周内完成一个理应需要 6-9 个月的移植，合同价格也从 1 万美元重新谈到 4 万美元，且坚持先收到 2 万美元才动工。

## 3DO 的算力硬伤与权衡取舍

3DO 搭载 12 MHz ARM 处理器；而基于 Jaguar 版本的 Doom 在同一台机器上最初只跑出 3 帧/秒（Wolfenstein 移植版跑 30 帧）。Becky 向 John Carmack 打电话汇报，Carmack 的建议是缩小渲染窗口，减少需要绘制的像素量。最终通过缩窗口 + 软件优化，帧率提升到约 10 帧——勉强可玩，但地板和天花板依然要用软件渲染，因为没有足够时间为硬件 blitter 重写代码。

## CEO 与移植工作的结构性冲突

CEO 持续要求加入新武器和新地图，理由是"只要把武器的 JPEG 放进游戏目录里不就能用了吗"——他字面上认为新武器资产可以自动生效。Becky 应对方式是把他导入音乐制作（让他用教会乐队为 Doom 的 MIDI 曲目做翻唱录音），给他营造"在为游戏做贡献"的感知，从而让自己专注开发。最终成品是 bug-free 的、有高质量 CD 原声带的 Doom 3DO 移植，Art Data 随后压货 5 万份，实际销出约 3-4 千份，公司随即倒闭。

## 留下的那个想法

Becky 说，真正理解计算机，从 Apple II 或 Commodore 64 学起比从 Python/JavaScript 入门有效得多——因为 1977 年的 8 位机和现代 CPU 的底层结构没有根本区别：寄存器、栈、内存 IO、固件，一样不少。现代语言的抽象层让人误以为理解了编程，但看一眼编译器输出的汇编"是一部小说"，那才是真相。
