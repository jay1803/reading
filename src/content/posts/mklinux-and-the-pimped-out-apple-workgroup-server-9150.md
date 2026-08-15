---
title: "MkLinux and the pimped-out Apple Workgroup Server 9150"
date: 2026-08-03T08:04:54Z
category: reading
description: "Apple 服务器史的主线不是技术演进，而是内部派系决定了 Linux 何时被支持、何时被抛弃，以及哪台机器成了孤儿。WGS 9150 出厂时带的是 NetWare，A/UX 4.0 始终没出现；MkLinux 在接近保密状态下诞生，在 Jobs 回归后被解散。最终证明：MkLinux 的 Mach 微内核代码逐..."
source: "https://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html"
---

## MkLinux 是公司内斗的产物，其微内核代码直接传承至今天的 macOS

Apple 服务器史的主线不是技术演进，而是内部派系决定了 Linux 何时被支持、何时被抛弃，以及哪台机器成了孤儿。WGS 9150 出厂时带的是 NetWare，A/UX 4.0 始终没出现；MkLinux 在接近保密状态下诞生，在 Jobs 回归后被解散。最终证明：MkLinux 的 Mach 微内核代码逐字出现在了 macOS 的 XNU 里。

## WGS 9150 的异类身份

Workgroup Server 线中其他型号都是 Quadra 或 Power Mac 改名重贴标签，唯独 9150 没有对应的台式 Mac——它是那条线上唯一一台"专门设计的服务器"外壳，从 Quadra 950/AWS 95 的机箱改来，把软驱挪到底部（Mac 史上绝无仅有）以腾出顶部给 DAT 和 CD-ROM。1994 年 4 月发布，同一场发布会 Spindler 演示的是 NetWare 跑在 8150 上；A/UX 4.0 和 PowerOpen 从未兑现，9150 只拿到了 System 7.5 和 AppleShare。

硬件上，9150 搭载 80MHz PowerPC 601（焊死在主板，陶瓷 QFP 封装），8MB 焊死 RAM + 8 条 72-pin SIMM 槽最多 256MB，5 个 NuBus 槽，内置 MESH SCSI-2 控制器独立于外置 SCSI（CURIO），板载 Ariel 视频芯片（DA-15 接口）。1995 年 4 月出了 120MHz 601+ 升级版（Gestalt ID 57），配 Peltier 主动散热，是第一代 NuBus Power Mac 里最快的。

## MkLinux 的政治起源

Nassi 接管 Apple 操作系统组后认为 Copland 的 NuKernel "根本不可能飞"。他在 Encore 公司时就接触过 CMU 的 Mach 微内核，想用"Linux 作为 Mach 上的一个任务"来证明这条路走得通。但 Mac 硬件部门负责人 Howard Lee 担心 Mach 的高可移植性会让 IBM 觉得 Apple 不忠于 PowerPC——Star Trek（把 System 7 移植到 Intel）的取消正是前车之鉴。

于是团队几乎在保密状态下运作：外包给法国格勒诺布尔的 OSF 研究院，在 HP 9000 PA-RISC 和 x86 上交叉编译，用 gcc 2.7.1，通过串口 gdb 跨平台调试。1996 年 WWDC 发布 DR1，随 CD 附上全部源代码，这是 Apple 第一次正式支持开源项目。Nassi 在 Jobs 回归前三个月的 1996 年 11 月离职——他明确反对 Amelio 收购 BeOS，认为 Mach 才是正道；Jobs 带来 NeXTSTEP，OSF 和 LTG 已经替他把微内核移植好了，MkLinux 失去了继续存在的公司价值。

DR1 仅支持 NuBus Power Mac（6100/7100/8100），因为 LTG 只在这些机器上开发。这三款机型到 DR1 发布时全部已经停产。DR2.1（1997 年 3 月）是首个同时支持 NuBus 和 PCI Power Mac 的版本，被定为"参考版"。社区在 1998 年接管后发布了 DR3，支持范围扩至几乎所有四位数型号 Power Mac（含 Workgroup Servers）及早期 beige G3，最终 R2/pre-R2 在 2002 年 8 月关停。

MkLinux 与 macOS 的代码传承有直接证据：MkLinux 启动日志里有一行 "COLOR" 输出，对应的 C 函数在 XNU（Jaguar，10.2）里逐字复现，直到 10.3 才被删除。Apple 的 2000 年内核文档明确写道，"系统软件其他部分，如 Mach，基于此前用于 Apple MkLinux 项目、Mac OS X Server 和 NeXT 收购技术的技术。"

## 实装限制：三条硬约束

在 WGS 9150 上安装 MkLinux R2（最终版 R2RC5）后，作者碰到三条无法绕过的限制：

**RAM 上限**：9150 可装满 264MB（8+256），但 Mach 的 VM hash table 有硬上限。超过约 191MB，Mach 内核进入死循环，机器挂死。安装镜像能接受 -m200 但安装后的系统内核不能；最终稳定值是 -m136，写在 lilo.conf 的 `mach_options=` 行。这意味着插满的 264MB RAM 在 MkLinux 下只能用 136MB。

**CPU 升级**：Sonnet Fortissimo G3/400 装进 PDS 槽后，Mac OS 8.6 正常跑 400MHz（通过双倍泵总线实现，Metronome 工具确认），但 Mach 内核检测到 G3 激活就立刻挂死，原因是 601 和后续 PowerPC CPU 有重要架构差异，加上总线骗局让 Mach 无所适从。解法：把 Sonnet 扩展的 Type 从 scri 改回 INIT，使其在 MkLinux Booter 之后加载。这样 MkLinux 启动时 G3 未激活，仍跑 601；进 Mac OS 后 Sonnet INIT 才激活 G3。L2 cache stick（256K）可以留在主板。

**显卡**：NuBus 显卡（Radius PrecisionColor Pro 24XK）在 Linux task 很早就触发 machine check，kernel panic；A/V PDS 卡被 Mach 正确检测，但 pager 和 Linux task 根本不启动；HPV PDS 卡（7100 版，1MB VRAM）虽然 Mach 不认识（标为 "unknown (using VDS port)"），却是唯一能让系统正常启动的选择，以 8-bit 1024×768 运行。安装方式：通过 Sonnet 的 ribbon cable 适配套件，把 HPV 卡用 NuBus 槽的固定孔位机械固定（电气上仍走 PDS），需要把卡的固定片向后折弯，因为 9150/8100 的 PDS 连接器方向朝下，与 7100 相反。

## Spindlerplastic 问题

Q900 系谱（Q950、AWS 95、WGS 9150）的机箱用的 ABS 塑料增塑剂已经挥发殆尽，无法修复，只有重新熔化才能添加新增塑剂。这意味着所有卡扣、固定片和铰链迟早全部碎裂。作者用尼龙螺丝固定主板，最终以活页夹解决主板偏移导致 interrupt/reset 开关被意外触发的问题。这是任何 Q900 系谱机器的保存者都会遇到的结构性问题。
