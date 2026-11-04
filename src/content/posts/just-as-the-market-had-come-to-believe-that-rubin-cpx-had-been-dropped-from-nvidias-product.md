---
title: "Just as the market had come to believe that Rubin CPX had been dropped from Nvidia’s product…"
date: 2026-11-04T00:51:45Z
category: reading
description: "Nvidia 据称已重启 Rubin CPX，计划于 2027 年第一季度投产，通过重新设计 GPU 规格和独立机架，为长上下文推理提供性价比更高的 *prefill* 方案。郭明錤的最新产业调查与市场此前认为 CPX 已被移出产品路线图的判断相反；新版更强的 prefill 性"
source: "https://medium.com/@mingchikuo/just-as-the-market-had-come-to-believe-that-rubin-cpx-had-been-dropped-from-nvidias-product-9b32bd864286"
author: "郭明錤 (Ming-Chi Kuo)"
---

Nvidia 据称已重启 Rubin CPX，计划于 2027 年第一季度投产，通过重新设计 GPU 规格和独立机架，为长上下文推理提供性价比更高的 **prefill** 方案。郭明錤的最新产业调查与市场此前认为 CPX 已被移出产品路线图的判断相反；新版更强的 prefill 性能及架构调整，显示 Nvidia 仍高度重视这一环节的专用计算需求。

这一定位源于推理工作负载的构成：当前超过 50% 的 AI 推理工作量来自输入上下文处理及相应 KV cache 的构建。新版 CPX 必须搭配 Vera Rubin NVL72 使用，Nvidia 建议 CPX 与 Rubin GPU 按 1:1 配置。CPX 负责 prefill、建立 KV cache，再通过 Ethernet RDMA 将缓存传给 Rubin，由后者承担 decode，把输入处理和后续生成分配给不同 GPU。

为支撑这项分工，CPX 的计算性能提升至接近 Rubin，单颗 GPU 的最大功率也与 Rubin 一致，达到 2,300 W；显存则从旧设计的 128 GB GDDR7 改为 168 GB HBM4，低于 Rubin 的 288 GB。每个计算托盘配置八颗 CPX，合计约 1.34 TB HBM4，足以覆盖大多数长上下文 prefill 工作负载及其 KV cache 需求。其产品目标是在满足这类任务的算力与显存需求的同时，降低 prefill 成本。

配套机架也从此前与 Rubin 共用的设计，改为独立的 MGX ETL 机架，客户可按需求选择 64、128、192 或 256 颗 CPX。每 64 颗组成一个机架模块，包含八个计算托盘和一个交换托盘，使 prefill 资源能够以模块化方式配置。

互连架构进一步体现了这种专用化取舍：NVLink 仅用于单个托盘内八颗 CPX 的 scale-up，每颗带宽为 1–1.5 TB/s，低于 Rubin 的 3.6 TB/s；同一模块内不同托盘之间的 scale-out 使用 Spectrum-6 Ethernet，经全铜 L1 链路连接；跨模块则由各模块的 Spectrum-6 交换机通过 OSFP 光链路互连。新版 CPX 因而把接近 Rubin 的计算性能、面向长上下文的 HBM4 容量，以及分层互连和独立机架组合起来，试图让占据大量推理工作量的 prefill 获得更灵活、成本更低的专用基础设施。
