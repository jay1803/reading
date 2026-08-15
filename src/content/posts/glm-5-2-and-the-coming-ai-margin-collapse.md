---
title: "GLM 5.2 and the coming AI margin collapse"
date: 2026-07-08T08:04:03Z
category: reading
description: "前沿 AI 实验室的商业模式是\"大额训练开销 + 超高推理毛利\"：作者估算 Anthropic/OpenAI 按 $25/MTok 收费时，纯算力成本上的毛利率约为 90%。DeepSeek 事件让市场误认为威胁在训练端（固定成本），真正的压力来自推理端（规模可变的边际成本）。"
source: "https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/"
---

## 推理利润率，而非训练成本，才是即将崩塌的护城河

前沿 AI 实验室的商业模式是"大额训练开销 + 超高推理毛利"：作者估算 Anthropic/OpenAI 按 $25/MTok 收费时，纯算力成本上的毛利率约为 90%。DeepSeek 事件让市场误认为威胁在训练端（固定成本），真正的压力来自推理端（规模可变的边际成本）。

## GLM 5.2：第一个达到前沿级别的开源模型

作者将 GLM 5.2（Z.ai）视为首个真正与 Opus / GPT-5.5 抗衡的开放权重模型，实际使用中几乎无法区分。现有弱点：大量 thinking 导致速度慢；无视觉支持；Z.ai 和 Fireworks 的网络搜索能力差，目前需 ddgr 之类的 CLI workaround。

## 迁移成本低到几乎为零

Z.ai 和 Fireworks 同时提供 OpenAI 和 Anthropic 兼容端点，切换只需更改 base URL 和 API key，Claude Code 和 Codex 均适用。作者认为追踪前沿实验室频繁变更的政策条款，比切换提供商的成本还高。

## 成本：$4.40/MTok，约为 Opus 的 20%

即使考虑 thinking 导致的 token 增量，大多数工作流可节省 50% 以上。Wafer 的测试显示在 AMD 硬件上运行 GLM 5.2 比 Nvidia Blackwell 的推理成本低 2.75 倍，后续成本仍有下行空间。

## 企业端风险与上限

Z.ai 的中国背景及宽松数据条款对企业几乎不可接受，但开放权重意味着可使用第三方提供商或完全自建——连内部敏感数据都可纳入 Opus 质量的 agentic 工作流。第二篇文章将分析推理利润率坍塌后谁赢谁输。
