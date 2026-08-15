---
title: "Designing a Low Latency 10G Ethernet Core (2023)"
date: 2025-10-09T23:33:59Z
category: reading
description: "Xilinx 内置的同步 gearbox 有两个不必要的设计缺陷，导致市面上大多数商业低延迟以太网核都带着免费的延迟损耗——一个个人 FPGA 项目通过自定义 gearbox 单步节省 8.5ns，最终实现 58.2ns 回环延迟，跻身商业竞争水平。"
source: "https://ttchisholm.github.io/ethernet/2023/05/01/designing-10g-eth-1.html"
---

## TL;DR

Xilinx 内置的同步 gearbox 有两个不必要的设计缺陷，导致市面上大多数商业低延迟以太网核都带着免费的延迟损耗——一个个人 FPGA 项目通过自定义 gearbox 单步节省 8.5ns，最终实现 58.2ns 回环延迟，跻身商业竞争水平。

## 核心洞见

10G 以太网用 64b/66b 编码，线路速率为 10.3125Gbps；GTY 收发器接口宽度（16/32/64 等）均无法整除 66，必须做宽度转换（gearbox）。异步 gearbox 最简单，但跨时钟域本身就要吃掉约 30ns（TX+RX 合计）。同步 gearbox 用单时钟解决问题，但 Xilinx 内置实现有两处额外损耗：(1) 输入输出都带寄存器，无法把 PCS 编码/scrambling 合并到同一周期；(2) 每 64 周期才连续暂停 2 次（而非每 32 周期暂停 1 次），拉高了最大延迟上界。把 gearbox 自行实现并集成进 PCS，就能同时消除这两处，平均节省 8.5ns——是全系列优化中单步收益最大的一项。

## 具体机制

设计跑在 32-bit/322MHz：第一周期传 32+2bit（含 header），第二周期传剩余 32bit，PCS 编码/scrambling 在同一周期内完成。其余低延迟手段包括 PMA buffer bypass（绕过 GTY 内置缓冲区）、Slicing-by-N CRC 算法（并行 CRC，不等全帧到达）、最小化缓冲级数。验证用 cocotb + pyuvm，Sequencer 随机生成包长，BFM 在 loopback 中引入可配比特/周期延迟，pytest 驱动多配置回归，集成进 CI/CD。

商业对标实测延迟（TxSoP 到 RxSoP 回环）：Orthogone 32-bit/322MHz 约 34.1ns、LDA Tech 32-bit/322MHz 约 33.5ns、LDA Tech 16-bit/644MHz 约 21.8ns、Orthogone 16-bit/644MHz 约 20.2ns。该项目 32-bit/322MHz 实测 58.2ns。

**证据薄弱处**：商业核的延迟数字大多引用"MAC/PCS 延迟之和"（Method 1），而非实测回环值，与本文的 Method 2（TxSoP→RxSoP）不可直接比较；更激进的商业产品实测延迟可能比 spec sheet 看起来更高。

## 隐藏限制

从 58.2ns 跨越到 ~20ns 还需要三步叠加：16-bit/644MHz 接口（约节省 19.2ns，但需要 -3 速率等级器件且 gtwizard IP 无法直接配置）、MAC/PCS 更紧密集成（6-12ns，包括预加载 PCS/CRC 和去掉 XGMII 中间层）、TX/RX 时钟同步（用 RX 恢复时钟驱动 TX，消除 CDC；需外部 jitter attenuator 如 Si5395，或用 Xilinx FRACXO，但相位噪声待验证）。这三步都有各自的非平凡工程代价。

## 一句话留下的想法

商业低延迟核 spec sheet 里"18-34ns"的数字，和你真正能测到的回环延迟，是两件事——行业的测量方法还没有统一标准，这让横向比较的意义大打折扣。
