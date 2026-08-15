---
title: "Rise of the Triforce"
date: 2026-02-24T10:55:40Z
category: reading
description: "Dolphin 2512-395 正式支持 Triforce 街机硬件——Sega、任天堂、Namco 2002 年合作的 GameCube 基础街机平台，而任天堂从未为它开发过任何游戏，只是授权 IP 并提供硬件。这次合并的核心来自 crediar 一人在私人 fork 上维护了十年以上的模拟器工作。"
source: "https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/"
---

## TL;DR
Dolphin 2512-395 正式支持 Triforce 街机硬件——Sega、任天堂、Namco 2002 年合作的 GameCube 基础街机平台，而任天堂从未为它开发过任何游戏，只是授权 IP 并提供硬件。这次合并的核心来自 crediar 一人在私人 fork 上维护了十年以上的模拟器工作。

## 硬件本质：GameCube 穿了件铝壳

每台 Triforce 的核心是一块原版 GameCube 主板，外加两块 Sega 定制板：AM-Baseboard（JVS 输入输出 + 视频信号）和 AM-Mediaboard（游戏存储 + 网络）。游戏不走 DVD，而是从 GD-ROM（Dreamcast 格式，更便宜且已在街机中验证）或 NAND 卡匣加载进 RAM 后运行——GD-ROM 可能整台机器生命周期只需插入一次，靠电池备份维持数据。游戏可访问的 RAM 与普通 GameCube 完全一致：24+16 MiB，DIMM RAM 只是只读盘符。

Sega 当时几近破产：Dreamcast 败给 PS2，32X 和 Saturn 连续失误耗尽资源。与任天堂合作是「五年前不可想象」的事——三方联手正是绝境中的求生策略。

## 九款游戏，每款都是特例

游戏库总计 9 款，涵盖马里奥赛车 GP 1/2（Namco 开发、任天堂 IP）、Virtua Striker 3/4 系列、F-Zero AX、关键的阿瓦隆（需五台 Triforce 联机的街机卡牌游戏，至今因触摸屏缺失无法在 Dolphin 中游玩）、棒球游戏 Gekitou Pro Yakyuu，以及 F-Zero AX Monster Ride。

F-Zero AX 与 GX 家用版共用开发团队，但物理引擎有意调得更难：AX 抓地力更低、漂移更极端——长期玩 AX 再回 GX，玩家会感觉赛车「被粘在地面上」。Monster Ride 把玩家锁进五自由度运动模拟器（Cycraft），机柜会真实甩动座舱配合画面，从未离开过日本；存量极少，至今有开源 Cycraft 模拟器。

存档卡（磁卡/IC 卡）是当时街机圈的创新：进度跟着卡走，可带到任何有同款游戏的机器继续。磁卡限写 50 次，Virtua Striker 4 的 IC 卡还能绑定 Sega ALL.Net 全球排行榜（服务已于 2017 年终止）。

## 模拟的代价

旧 Triforce 分支（2012 年）靠硬编码和绕过检查勉强运行部分游戏，质量不达标，两年后废弃。crediar 独立维护 fork 逾十年，2025 年中接触 Dolphin 团队。审查历时数月：主要障碍是内存安全 bug、潜在死锁，以及每款游戏每个版本都有独立的硬件怪癖——街机模拟不像主机模拟，修一处不能带动其他。

马里奥赛车 GP 1/2 多机联机在发布前最后关头攻克（能承受 80ms Wi-Fi 延迟）；F-Zero AX 联机至今未解；关键的阿瓦隆因触摸屏模拟缺失仍不可玩。NetPlay 和 TAS 工具也尚未支持。

## 留下的那个想法
任天堂是这套系统最大的受益者：出 IP、出硬件平台，却让 Sega 和 Namco 承担所有开发风险——最终九款游戏里没有一款来自任天堂。Triforce 作为街机工业黄昏期的共同求生平台，结果是大多数游戏在日本以外几乎没人见过实机。而 F-Zero AX 是整个库里唯一没有家用移植版的游戏，二十年来只能在它生来所属的街机柜中存在——现在，那个地方是 Dolphin。
