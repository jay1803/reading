---
title: "Ahoy, DECmate II! the little PDP-8 that could"
date: 2026-06-01T08:01:18Z
category: reading
description: "DECmate II 最值得看的地方，是它把一个已经老去的 12 位 PDP-8 血统压进 1980 年代办公室桌面机外壳后，仍然保留了足够真实的系统质感：它商业上靠 WPS-8 这种办公软件活下来，技术上靠 HD-6120、slushware、OS/278 和一堆不完全兼容的折衷维持 PDP-8 的延续。"
source: "https://oldvcr.blogspot.com/2026/05/ahoy-decmate-ii-little-pdp-8-that-could.html"
---

## TL;DR
DECmate II 最值得看的地方，是它把一个已经老去的 12 位 PDP-8 血统压进 1980 年代办公室桌面机外壳后，仍然保留了足够真实的系统质感：它商业上靠 WPS-8 这种办公软件活下来，技术上靠 HD-6120、slushware、OS/278 和一堆不完全兼容的折衷维持 PDP-8 的延续。

## 关键时刻
PDP-8 从 1965 年的冰箱大小小型机起步，靠低价、简单指令集和易接口能力成为早期小型机代表；到 1970 年 PDP-8/E 已能做到低于 5000 美元，但 4kW 地址限制、128 字页寻址、递归困难和大量特殊位置让它在 1970 年代中期显得过时。

DEC 一开始没有主动把 PDP-8 微处理器化，反而是 Intersil 在 1975 年做出 CMOS IM6100，DEC 随后把它用于 1977 年 DECstation VT78；后续 Harris 为 DEC 做出增强但更不兼容的 HD-6120，成为 DECmate 系列的核心。

IBM PC 5150 的成功迫使 DEC 在 1982 年推出三条桌面线：DEC Professional、Rainbow 100 和 DECmate II。DECmate II 价格为 3740 美元，带 VR201 显示器、LK201 键盘和 RX50 双软驱，比 Pro 和 Rainbow 更快形成可卖产品，因为它沿用了已有 DECmate/WPS 软件生态。

## 具体机制
DECmate II 的基础机型是 PC278-A，核心是 8MHz HD-6120，拥有 32kW 主内存和 32kW control panel 内存；它通过 6121 I/O 控制器、FD1793A 软驱控制器、8751 微控制器和 VPAC 视频芯片，把 PDP-8 式计算、终端显示、键盘、串口和 RX50 存储组合成一个桌面系统。

RX50 是文章里最具 DEC 风格的机械折衷：两个 5.25 英寸盘位共用马达和步进机构，盘片单面写入，下层盘要倒插；控制器可以 8 位访问，也能用 12 位模式服务 DECmate，但 12 位模式相当于用 16 位存储浪费 4 位，容量减半。

DECmate II 的“固件”并不全在 ROM。开机 ROM 先把自身拷入 CP RAM，再从软盘特定磁道加载 slushware；slushware 提供键盘、显示、终端转义、字符集、串口、setup 和扇区访问，成为介于固件和操作系统之间的可替换层。

## 复活过程
原机能进系统，但 System Overview 和 System Test 盘都有坏扇区；Greaseweazle 读盘显示测试盘只读到 749/800 个扇区，Overview 虽有 793/800 个扇区可读，却在早期磁道损坏，足以解释程序崩溃。

作者用 Internet Archive 和 ibiblio 找到可用镜像后，把 RX50 替换为两台 Gotek/FlashFloppy 组成的固态软驱夹层，配置为 `interface = shugart`、`host = dec`、`pin02 = low`、`pin34 = rdy`，DECmate II 最终能完整通过双驱测试并稳定启动。

为了获得干净截图，作者还给 VR201 显示器加了 composite video 输出；这暴露出 DECmate II 的显示本质上是高质量单色视频信号，虽然会切掉少量边缘列和底部扫描线，但比拍 CRT 屏幕可靠得多。

## 软件现场
WPS-8 是 DECmate 存在的商业理由：它从 DEC Datasystem 310W/VT78 发展而来，成为 PDP-8 上的独立文字处理系统，并可扩展到多终端和远程文档管理；DECspell 等功能还需要 Z80 APU 协处理器。

DECmate II 也能通过 APU 跑 CP/M 2.2，通过更罕见的 XPU 跑 CP/M 和 MS-DOS 2.11，但磁盘格式和 I/O 非标准让兼容性始终有限。它更自然的计算环境仍是 OS/278，一个从 OS/8/OS/78 演化来的单任务命令行系统。

OS/278 保留了 PDP-8 世界的味道，也放大了兼容性断裂：KMON、Command Decoder、USR 和 CCL 仍在，但旧 OS/8 软件会被设备处理器接口变化、6120 指令差异、6121 标志行为和 DECmate 特有 I/O 限制卡住。

## 更大意义
DECmate II 是 DEC 小系统组里少数相对成功的机器，因为它没有像 Rainbow 和 Professional 那样承诺完整 IBM PC 或 PDP-11 兼容性，也没有等待不存在的软件生态；它只是把既有 WPS-8 用户和办公室工作流包装进更便宜、更标准化的桌面外形。

DECmate III、III+、Rainbow 190 和 VAXmate 都没能改变 DEC 在个人电脑市场的被动局面；真正稳定的需求来自不愿迁移的 WPS-8 用户，所以 DECmate III 一直卖到 1990 年才停产。

收束来看，DECmate II 几乎不是经典意义上的 PDP-8，却比纯模拟器更能说明一条架构怎样在商业压力、办公软件、外设怪癖和兼容性妥协中继续存在。
