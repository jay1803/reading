---
title: "I'm (mostly) picking models on speed now, not intelligence"
date: 2026-08-03T08:04:54Z
category: reading
author: "Martin Alderson"
description: "Opus 4.6 级别的模型对作者日常任务（写代码、研究整合、数据分析）已经足够。Fable 发布后作者很快切回 Opus，不是因为 Fable 不聪明，而是因为太慢。当足够多的模型都跨过智能门槛，速度就成了差异化的主轴。"
source: "https://martinalderson.com/posts/speed-vs-intelligence/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## 模型智能已过"够用"门槛，竞争轴切换到速度

Opus 4.6 级别的模型对作者日常任务（写代码、研究整合、数据分析）已经足够。Fable 发布后作者很快切回 Opus，不是因为 Fable 不聪明，而是因为太慢。当足够多的模型都跨过智能门槛，速度就成了差异化的主轴。

## 速度的感知阈值：100 tok/s ≈ 100ms

作者把 100 tok/s 类比为 UI 响应的 100ms 黄金标准——快到人类刚好跟得上阅读节奏。50 tok/s 以下明显感觉慢；超过 200 tok/s 反而让人不安。GLM5.2 在 OpenRouter 上不同 provider 的吞吐差距从 <30 到 129 tok/s，说明开放权重模型在服务速度上已形成显著竞争。

## Amdahl's Law 设了速度上限

即使模型推理速度从 50 提升到 250 tok/s（5x），一个 agent 轮次实际只能提速约 2x——剩余的 25 秒是 tool call、本地硬件和人类决策时间，这些不随模型变快。GPU 因 AI 热潮导致硬件成本飙升，进一步压缩了本地端提速空间。速度军备竞赛在 agent 场景下边际收益会递减。

## 价格战与 2027 展望

OpenAI Luna 成本降 80%，GLM5.2 在 OpenRouter 已跌至 $0.42/$1.32/MTok（Opus 的 5%）。Nvidia Vera Rubin 和 AMD MI400 预计 2027 年大规模部署，HBM4 内存带宽单独就能带来 2x+ 的输出速度提升，500 tok/s+ 将成为常态。作者不确定的变量：2-3T 参数超大模型是否会对日常任务形成真正的智能跃升，让当前"够用"的甜蜜点看起来原始。
