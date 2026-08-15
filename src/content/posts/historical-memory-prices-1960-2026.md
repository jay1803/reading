---
title: "Historical memory prices 1960-2026"
date: 2026-06-30T08:04:46Z
category: reading
description: "Stanford DAM 项目对 John C. McCallum 1957–2024 年 DRAM 价格数据集的延续与扩展，新增 NAND 和 HBM 两条线，并接入 Keepa（Amazon 零售价历史）实现月度自动刷新。三类存储的数据来源和可靠性完全不同，不能同等对待。"
source: "https://dam.stanford.edu/memory-prices.html"
---

## McCallum 传承：三轨分离，数据质量差异显著

Stanford DAM 项目对 John C. McCallum 1957–2024 年 DRAM 价格数据集的延续与扩展，新增 NAND 和 HBM 两条线，并接入 Keepa（Amazon 零售价历史）实现月度自动刷新。三类存储的数据来源和可靠性完全不同，不能同等对待。

## DRAM：最完整，但"最低价"追踪的是退市产品

历史骨干是 McCallum 数据集，2024 年中切换为 Keepa Amazon 最低零售价。关键限制：$/GB 是名义美元最便宜挂牌价，不做通胀调整，不是合同价或均价。最低零售价往往是即将退市代际的清仓，而非主流一代的真实定价水位——这是按代际分拆的图表比整体曲线更有用的原因。DDR3/4/5 三代在同一时期可能价格差距巨大，整体最低价只反映退市品。

## NAND：2016 年前仅 4 个锚点，精度存疑

2016 年起有完整月度 NVMe SSD 最低零售价（排除 SATA 和企业盘，剔除单月挂价低于典型价 60% 的异常）；2010–2016 年只有 4 个近似锚点，无等效历史数据集可参考。这段数据的密度与 DRAM 历史不在同一量级。

## HBM：完全没有公开市场，所有数字都是模型估算

HBM 只向 Nvidia、AMD、Google（TPU）、Amazon（Trainium）等加速器厂商以保密合同出售，无现货市场。数据来源是 TrendForce / SemiAnalysis 行业分析师估算，加上 Epoch AI 基于生产量加权的 BOM 成本模型。HBM4 价格是预测值（预计 2026 Q3 上市）。指标双轨：$/GB 和 $/TBps（单栈带宽归一化成本），后者对 AI 加速器横向比较更有意义。所有"HBM 价格"引用在方法论上都是估算，而非交易价格。
