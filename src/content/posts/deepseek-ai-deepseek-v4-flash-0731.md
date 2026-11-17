---
title: "deepseek-ai/DeepSeek-V4-Flash-0731"
date: 2026-11-17T11:01:44Z
category: reading
description: "DeepSeek-V4-Flash-0731 以低廉的 API 价格和超过更大模型的评测表现，成为 Simon Willison 眼中当时最具智能性价比的模型候选。这个于 2026 年 7 月 31 日发布的 DeepSeek V4 系列新版本宣称显著增强了 agentic ca…"
source: "https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/"
---

DeepSeek-V4-Flash-0731 以低廉的 API 价格和超过更大模型的评测表现，成为 Simon Willison 眼中当时最具智能性价比的模型候选。这个于 2026 年 7 月 31 日发布的 DeepSeek V4 系列新版本宣称显著增强了 agentic capabilities，拥有 304B 参数，Hugging Face 上的模型文件达 167GB；Artificial Analysis 将它排在拥有 428B 参数的 MiniMax M3 之前。其每百万输入 token 0.14 美元、每百万输出 token 0.27 美元的定价，结合 Intelligence Index 表现，使它在智能水平与完成评测任务所需成本的对比中格外突出。

不过，实际输出质量也取决于推理强度设置。Willison 通过 OpenRouter 进行 pelican 绘图测试时，默认推理级别下的结果令他失望；将 **reasoning_effort** 调高至 **high** 后，同一测试得到了明显更好的结果。这次体验提示，默认配置下的一次输出不足以展示该模型的能力，推理预算是评估其实际表现时需要保留的关键条件。
