---
title: "Jurassic Park computers in excruciating detail"
date: 2026-08-20T12:20:31Z
category: reading
description: "电影剧组借用了约 170 万美元的真实硬件（2026 年等值约 400 万美元），片场每台设备型号均可查证——唯一悖论是 Dennis Nedry 桌上的 Motorola Envoy，那款 PDA 比电影拍摄晚了近两年才发布。"
source: "https://fabiensanglard.net/jurrasic_park_computers/index.html"
---

## 制作团队借来了 170 万美元的真实设备——然后用上了一台不可能存在的 PDA

电影摄于 1992 年 8–11 月，剧组配备了 Apple 提供的 $350K 硬件与 SGI 提供的 $875K 工作站（加上其他 $500K 设备，折合 2026 年约 400 万美元）。这些计算机不是道具，是真机，画面里的型号全部可查证。

唯一的时间线悖论：Dennis Nedry 桌上的 Motorola Envoy PDA 在 1994 年中期才完成研发、1995 年 2 月才正式上市——比拍摄时间晚了将近两年，却神秘地出现在 1993 年的银幕上。

## 控制室硬件清单

- **Ray Arnold 工作站**：SGI R4000 Indigo。画面里几乎只剩轮廓，但机器是真的——控制室旁另建了一个房间，放着 SGI 和 Mac，由 Michael Backes 团队通过无线电配合镜头实时传输动画到片场屏幕。
- **Dennis Nedry 主力机**：SGI IRIS Crimson——体型太大放不上桌，置于地板。配 MIPS R4000/R4400 100–150 MHz、最多 7 种高性能 3D 图形子系统选项、最大 256 MB 内存。平时跑 3D 国际象棋。
- **Mac Quadra 700**：Dennis 两台、Ray 一台。68040 @ 25 MHz，4–68 MB RAM，1991 年发布，Apple 最大力度的产品植入之一。
- **超级计算机背景**：约 4–5 台 Thinking Machines CM-5（每台 $46K，1991 年发布，1993 年仍是全球最快）。Sparc CPU + 4 个向量单元 + 32 MiB RAM/节点，面板红灯随机生成，无任何含义。
- **存储设备**：PLI Mini Arrays。Dennis 堆了 5 台、Ray 堆了 2 台。Hammond 应买的是 1 GiB 版（$3,598/台），7 GiB 总容量在 2026 年等值约 $33,223；而今 7 GiB 硬盘售价 $0.49。
- **Alan Grant 拖车**：Apple PowerBook 100，Motorola 68000 @ 16 MHz，640×400 LCD，System 7.0.1。

## 关键软件与场景细节

- **"It's a Unix system!"**：使用 SGI 实验性 3D 文件浏览器 `fsn`。Lex 打开 `/usr`，进入 `Visitor.Center`（IRIX 支持文件名含空格）。SGI 事后在官网打广告："你在侏罗纪公园看到了它！"
- **Dennis 的视频通话**：QuickTime Video Player 播放 1 分钟预录片段，鼠标光标明显停在播放按钮上。1993 年没有网络摄像头。
- **White Rabbit（`whte_rbt.obj`）**：让 Samuel Jackson 崩溃的锁机程序。这个文件名只出现在原著小说里，电影台词从未提到。
- **`gr_osview`**（IRIX 系统监控）：显示用户时间、系统时间、中断和图形开销——可能是拍摄时真实运行的，因为它会响应键盘操作。
- **Nedryland 源码**：屏幕上可见真实的 Classic Mac OS API 调用，由 Michael Backes 团队制作，并非随机字符。
- **Dennis 书架最上层**：Anthony Meadow 著《System 7 Revealed》——细节考究到了图书陈列层级。
