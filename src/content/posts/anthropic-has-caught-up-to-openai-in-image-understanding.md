---
title: "Anthropic has caught up to OpenAI in image understanding"
date: 2026-06-12T08:01:15Z
category: reading
description: "Claude Fable 5 和 GPT-5.5 现在能稳定解决去年顶级模型失败的图像题（看模拟时钟、数物体数量）。Fable 5 的视觉成绩略优于 GPT-5.5，但差距微小；Google 的 Gemini 系列在此项明显落后。"
source: "https://www.understandingai.org/p/anthropic-has-caught-up-to-openai"
---

## 视觉进步存在，但不足以支撑"规模必然通用"的论断

Claude Fable 5 和 GPT-5.5 现在能稳定解决去年顶级模型失败的图像题（看模拟时钟、数物体数量）。Fable 5 的视觉成绩略优于 GPT-5.5，但差距微小；Google 的 Gemini 系列在此项明显落后。

但进步是局部的。这两款模型在几何推理上的能力仍与低龄儿童相当。过去一年，编程和数学的进步幅度远大于视觉——这正是核心问题：如果"足够多的数据+算力"能产生真正通用的智能，各项能力应该同步推进，而不是某些领域突飞猛进、视觉停滞。

## 两款新模型的背景

Mythos 5 和 Fable 5 均基于 Claude Mythos Preview（两个月前公布但未公开发布）。Mythos 5 限于 Project Glasswing 合作伙伴，访问基本无限制；Fable 5 面向公众，但配备自动安全路由——检测到危险请求（如入侵、生物武器设计）时自动转至较弱的 Claude Opus 4.8。两款模型在编程能力上均大幅领先前代。

## 视觉作为"通用性"代理指标

作者自 2024 年起系统记录前沿模型视觉失败案例，选择视觉做基准正因如此：视觉提升既难靠暴力爬数据，也难靠 RLHF 快速伪造，是检验规模路线是否真正通用的自然探针。本次结果表明：视觉有进步，但未随编程能力同步飞跃，给"算力堆够就能通用"留下了值得持续跟踪的反例。
