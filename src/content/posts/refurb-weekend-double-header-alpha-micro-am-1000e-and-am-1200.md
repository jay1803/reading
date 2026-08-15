---
title: "Refurb weekend double header: Alpha Micro AM-1000E and AM-1200"
date: 2026-03-23T08:01:21Z
category: reading
description: "Alpha Micro 是已知唯一以 little-endian 运行 Motorola 68K 的系统——做法是硬件翻转地址线——动机不是性能优化，而是让数万台机器上已编译的 AlphaBASIC P-code 无需重新发行即可迁移到新 CPU。"
source: "https://oldvcr.blogspot.com/2026/03/refurb-weekend-double-header-alpha.html"
---

## TL;DR
Alpha Micro 是已知唯一以 little-endian 运行 Motorola 68K 的系统——做法是硬件翻转地址线——动机不是性能优化，而是让数万台机器上已编译的 AlphaBASIC P-code 无需重新发行即可迁移到新 CPU。

## 关键时刻
两台待修机：AM-1000E（1982，已被加装 Interlink Dimension-030 加速卡+8MB 内存，超出原厂所有内存配置选项）和 AM-1200XP（1987，70MB 硬盘），原装硬盘均死亡。AM-1000 的 Maxtor 经冷冻法取回约 1/3 扇区，磁盘数据显示所有者为 Key Curriculum Project（Berkeley，《The Geometer's Sketchpad》的出版商），系统运行记录跨越 1989—1994 年。两台机器均通过 BlueSCSI 挂载他人提供的 AMOS 镜像引导，AM-1200 最终成功运行 AMOS 2.3A（发布于 2000 年 5 月，距 AM-1200 发布已近 14 年）。

## 背后逻辑
AMOS 是实内存操作系统（无 MMU，程序可直接踩踏其他进程内存），安全设计近乎虚设——超级用户账号 [1,2] 默认无密码，安全边界完全依赖前端应用而非操作系统本身。作者少年时在救世军驻地发现菜单 Cancel 键的竞态条件，用一次意外的 dot prompt 逐步拿下操作员权限，系统管理员事后以"告诉我怎么做到的"换取了他的合法登录账号。硬件层面：Dimension-030 加速卡的指令缓存疑似故障，强制开启 CACR 后跑分无任何变化；10MHz 68010 的 AM-1200 升级板性能提升完全对应时钟频率，无超出预期的微架构收益。

## 边缘判断
Alpha Micro 的完整存活路径是：68K 实体机 → ISA/PCI co-processor 卡 → x86/Windows 上的纯软件 68K 仿真器，最后一块真正的 AM 硬件（SSD 安全狗）缩进 USB dongle。这不是失败，而是垂直市场遗留系统的理性终局：客户忠诚但不够多，产品够好但不够大，每一次多元化赌注（UNIMOS、Motorola 88000、AlphaConnect）都压错方向，最终只有"让老客户永远跑老软件"这一条路走得通。
