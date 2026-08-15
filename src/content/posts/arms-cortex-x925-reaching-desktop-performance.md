---
title: "Arm's Cortex X925: Reaching Desktop Performance"
date: 2026-03-06T08:53:42Z
category: reading
description: "Arm 的 Cortex X925 在 SPEC CPU2017 整数性能上已与 AMD Zen 5 和 Intel Lion Cove 的最高桌面配置持平——这是一个运行在 4 GHz 的 ARM 核心，没有 x86 的频率优势，却凭借更高的 IPC 打平了场面。"
source: "https://chipsandcheese.com/p/arms-cortex-x925-reaching-desktop"
---

## TL;DR
Arm 的 Cortex X925 在 SPEC CPU2017 整数性能上已与 AMD Zen 5 和 Intel Lion Cove 的最高桌面配置持平——这是一个运行在 4 GHz 的 ARM 核心，没有 x86 的频率优势，却凭借更高的 IPC 打平了场面。

## 核心洞见

X925 是一颗 10-wide 乱序核心，ROB 实际可用约 525 条指令窗口（Zen 5 是 448，Lion Cove 是 576），分支预测精度在 SPEC CPU2017 中与 Zen 5 相当甚至略优，前端吞吐 10 IPC。整数成绩打平是真实的，依据充分。

## 具体机制

- **分支预测**：一级 BTB 约 2048 条目、可追踪 16384 条分支，接近 Zen 5 量级；X925 在 505.mcf 和 541.leela（最难预测的两项）中反超 Zen 5。
- **调度器布局**：4 个整数调度器各 28 项，高度对称；3 个 FP 调度器各约 53 项（单个 FP 调度器条目数接近 AMD Bulldozer 整个 FP 调度器）。
- **向量短板**：128-bit 向量宽度，Zen 5 和 Lion Cove 均为 256-bit；这直接拖累了浮点套件，数个科学计算负载（如 554.roms）需要执行超过 Zen 5 两倍的指令数。
- **缓存**：L1D 64KB/4 周期，L2 2MB/12 周期（Nvidia GB10 配置），读带宽 64B/cycle——与老一代 AVX2 x86 CPU 持平，但低于 Zen 5 / Lion Cove 的当代水平。

## 隐藏限制

整数持平的结论成立，浮点则明显落后 Zen 5：aarch64 在几个科学计算负载上编译结果条目数比 x86-64 多一倍以上，IPC 优势完全不够覆盖。此外 X925 的向量加速（SVE 128-bit）、物理地址空间（仅 40-bit）、L3 最大仅 32MB，都指向它是消费端产品而非服务器级核心。

## 边缘判断

Arm 赢了整数，但高性能 CPU 市场的护城河还有很深的一段：游戏负载更吃内存子系统（L3 容量是软肋）、x86 软件生态的惯性极大，而 Arm 自己并不制造芯片——这颗核心能否真正落地桌面，取决于合作伙伴。竞争格局改变，但不是今天。
