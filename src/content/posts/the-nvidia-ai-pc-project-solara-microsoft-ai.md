---
title: "The Nvidia AI PC, Project Solara, Microsoft AI"
date: 2026-06-04T08:02:07Z
category: reading
description: "AI PC 的时机问题：Nvidia 的 RTX Spark 针对 2023 年的 AI，而 2026 年真正的 AI 运行在云端；微软反而因为没有手机而具备了主导\"代理时代\"设备生态的独特优势。"
source: "https://stratechery.com/2026/the-nvidia-ai-pc-project-solara-microsoft-ai/"
---

## TL;DR
AI PC 的时机问题：Nvidia 的 RTX Spark 针对 2023 年的 AI，而 2026 年真正的 AI 运行在云端；微软反而因为没有手机而具备了主导"代理时代"设备生态的独特优势。

## 核心主张拆解

### RTX Spark：为错误的时代设计的芯片
RTX Spark 拥有 20 个 ARM CPU 核心、Blackwell GPU（6144 CUDA 核心）、128GB LPDDR5X 内存，主打本地推理。Ben Thompson 认为它三年前会很有意义，但 AI 已从 chatbot 进入推理与 agentic 阶段——推理模型需要更大 KV cache 和更强 decode 速度，agentic 任务需要强 CPU 调用云端推理。RTX Spark 把过多 die 面积押在 GPU 上，而该 GPU 在推理性能上本就不及云端，还牺牲了 CPU。结论：适合 2023 年的 chatbot，不值 2026 年的价格或 Windows on ARM 的软件妥协。

### Project Solara：把云端变成"中枢"
微软内部秘密开发 Solara——一个基于 Android（非 Windows）的设备平台，让 AI 代理取代 app。核心范式转变：手机不再是中枢，云端才是，设备变成"辐射"（spokes）。可穿戴设备过去失败是因为交互摩擦；Solara 的逻辑是"人短暂触发，代理在云端后台完成工作"。目前专注企业市场（context 和 compute 已在云端），有 Qualcomm 和 MediaTek 作为芯片合作伙伴。

### MAI 模型：企业"专属模型"策略
微软发布 7 个从头训练的模型（MAI 系列）。旗舰 MAI-Thinking-1 在盲评中与 Claude Sonnet 4.6 持平，在编码基准上与 Claude Opus 4.6 持平。核心卖点：企业通过强化学习环境（RLE）定制模型，结果只属于自己，不与前沿实验室共享数据。麦肯锡案例：MAI 调优模型胜过 GPT 5.5，成本效率提升 10 倍。

## 反驳或薄弱处
- Project Solara 现阶段是 vaporware，只有原型设备和意向合作；
- 企业放弃前沿模型换"自有模型"是否划算，尚待验证；
- MAI 的维护成本和迭代速度能否跟上 OpenAI/Anthropic，仍是未知数。

## 更大意义
微软没有手机，这曾是弱点；在代理时代，如果"代理在云端、设备只是触点"的范式成立，Azure + Project Solara 恰好绕开了历史最大劣势。Ben 的"thin is in"论点在这里得到了硬件层面的注脚。
