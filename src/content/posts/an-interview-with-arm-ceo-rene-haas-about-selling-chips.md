---
title: "An Interview with Arm CEO Rene Haas About Selling Chips"
date: 2026-03-27T08:02:35Z
category: reading
author: "Ben Thompson"
description: "Rene Haas，Arm CEO，任职约四年半，此前履历覆盖 NEC 半导体、德州仪器、Nvidia，是半导体行业老将。本次受访主题是 Arm 首次独立举办品牌发布会（Arm Everywhere），宣布从纯 IP 授权公司转型为同时出售自研芯片的公司——Arm AGI CPU，首个客户为 Meta。采访者 B..."
source: "https://stratechery.com/2026/an-interview-with-arm-ceo-rene-haas-about-selling-chips/"
---

## 嘉宾背景
Rene Haas，Arm CEO，任职约四年半，此前履历覆盖 NEC 半导体、德州仪器、Nvidia，是半导体行业老将。本次受访主题是 Arm 首次独立举办品牌发布会（Arm Everywhere），宣布从纯 IP 授权公司转型为同时出售自研芯片的公司——Arm AGI CPU，首个客户为 Meta。采访者 Ben Thompson 为 Stratechery 创始人，此前于 2024 年 1 月首次专访 Haas。

## TL;DR
Arm 卖芯片的决定并非战略深谋，而是 Meta 在 2025 年中主动要求的结果——而 Arm 能快速答应，是因为 CSS（计算子系统）已覆盖芯片 95% 的 IP，卖完整芯片只是"补上最后 5%"。真正的战略押注在后面：agentic AI 使 CPU 的需求从"配角"变成结构性刚需，Arm 认为每个 agent 任务本质上是 CPU 调度任务，数据中心核心数将从 128 走向 512+。

## CSS 让 IP→芯片的门槛低得出乎意料
CSS（Compute Subsystem）是 Arm 在卖芯片之前已经在卖的东西：把所有 IP 块预配置、预验证组合成完整系统，客户可省去 1 到 1.5 年的测试验证时间。它覆盖芯片约 95% 的 IP，缺的只是 PCIe 控制器、内存控制器等 I/O 部分。Cobalt（微软）是第一个真实落地的 CSS 实现。从 CSS 到完整芯片，Arm 跨的门槛比外界感知的小得多——内部技术上早就准备好了。

## Meta 主动要求，决策在 2025 年中完成
最初 Meta 在评估是否授权 CSS，讨论演变成"你们能不能直接帮我们做整颗芯片"。Arm 在同意前谈妥了一个条件：芯片可以卖给其他客户，Meta 同意了。整个决策周期极短，从讨论到发布不足一年。Haas 明确说：如果 Meta 没来问，他不确定 Arm 会主动进入这个市场。

## Agentic AI 把 CPU 从配角变成结构性刚需
所有 GPU 生成的 token，其调度、分发、编排都是纯 CPU 任务。随着数据中心从百兆瓦走向吉瓦，CPU 核心数需求同步爆炸。Graviton 5 已是 192 核，Arm AGI CPU 是 136 核，Haas 认为 256、512 核将成现实。他的判断是每个 core 未来可能各跑一个 agent 或 hypervisor 任务——核心数比单核性能更关键。

## 内存是真正的瓶颈，不是 TSMC 产能
Haas 出乎意料地说：TSMC 3nm 产能并非主要约束（通过后端 ASIC 合作伙伴可以获得 upside）。真正卡脖子的是内存——HBM 大量占用内存厂商产能，加上 CPU 需求飙升，DRAM 极度紧张。他明确表示：如果内存更多，对外公布的财务预测数字还会更激进。

## ARM vs x86：遗留软件是唯一防线
亚马逊 Graviton 带动云原生迁移，新部署超 50% 已是 ARM；Google Axion、微软 Cobalt、Nvidia Grace/Vera head node 也都是 ARM。Haas 说：在白纸设计、软件已移植的前提下，他想不到任何理由从 x86 出发。x86 唯一还在的护城河是本地部署的遗留软件（COBOL 之类）。

## 与 Vera 不竞争：气冷通用 vs 液冷专用
Nvidia Vera 是为 Rubin GPU 供料设计的，走液冷大型机架，接口是 NVLink Fusion。Arm AGI CPU 的首个实现是更小的气冷机架，OCP 标准，面向通用数据中心空间。Haas 的判断是两者并不直接竞争——液冷 GPU 旁边的气冷 CPU 机架本来就是不同用途。

## 留下的那个想法
Arm 在数据中心的最大机遇，部分来自 Nvidia 替它做的一个决定：Nvidia 选 ARM 做 Grace、Blackwell、Vera 的 head node CPU，实质上把 AI 数据中心的软件栈标准化到了 ARM 上。Arm 是这场押注的受益者，但这不是 Arm 自己赢来的——是 Nvidia 赢来的，Arm 搭了便车，然后在便车上盖了座楼。
