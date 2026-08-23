---
title: "What's going on with Gemini?"
date: 2026-05-30T08:04:01Z
category: reading
author: "Martin Alderson"
description: "Gemini 的问题不是 Google 没有研究、算力或钱，而是它可能根本没在和 OpenAI/Anthropic 争同一条外部 API 赛道：Gemini 3.5 Flash 对外看像一个价格尴尬、编码能力中游的模型，对内却像为 Google 自己的大规模产品 token 消耗和 TPU 推理效率定制的基础设施..."
source: "https://martinalderson.com/posts/whats-going-on-with-gemini/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## TL;DR
Gemini 的问题不是 Google 没有研究、算力或钱，而是它可能根本没在和 OpenAI/Anthropic 争同一条外部 API 赛道：Gemini 3.5 Flash 对外看像一个价格尴尬、编码能力中游的模型，对内却像为 Google 自己的大规模产品 token 消耗和 TPU 推理效率定制的基础设施。真正的短板在开发者侧，Google 的 coding agent 产品线分裂，缺少 Claude Code / Codex 那种能吸引开发者、沉淀 telemetry、反哺模型训练的统一入口。

## 核心主张拆解
作者把 Gemini 的困惑拆成两层：模型本体并非没有竞争力，但外部定位很别扭；平台结构很强，但开发者入口很弱。按他的判断，Anthropic 和 OpenAI 仍在 frontier intelligence 领先区间，Gemini 3.1 Pro 的公开 benchmark 可能强于中国模型，但他在软件工程任务中反而更信任 GLM 5.1 和 Qwen 3.7。

Gemini 3.5 Flash 的矛盾在于“速度强、价格贵、能力不上不下”。它在 coding benchmark 上只是中游，却有约 206 output tokens/s，接近作者所称 Anthropic/OpenAI 旗舰模型的 4 倍；这对用户直接等待的产品体验很有价值。但 $9/MTok、比前代 Flash 贵 3 倍，让它在外部市场难找位置：追求最强能力会加钱买 Opus/GPT，追求低价可用则有中国模型或 OpenRouter 上的托管选择。

换成 Google 内部视角，3.5 Flash 反而合理。Google 自己在 AI Mode、Gmail 等产品里会消耗海量 token，速度直接影响用户体验，而内部真实 serving cost 很可能远低于对外定价。作者借 Hacker News 上关于模型规模和 TPU 8i 单卡运行的估算，推断 Google 的优势在于模型团队和 TPU 硬件团队能高度协同：知道下一代硬件形态，就能反向规划模型尺寸、训练目标和推理经济性。

最严重的问题不是模型，而是 coding agent 策略混乱。Anthropic 有 Claude Code，OpenAI 有 Codex，Google 却同时有 Antigravity、Jules、Gemini Code Assist、Gemini CLI、AI Studio 以及 Android Studio 等专用工具。Gemini CLI 被并入 Antigravity，但作者很少看到开发者实际采用 Google 系 SWE tooling；这意味着 Google 可能错过 AI 收入增长最快的场景，也缺少来自真实开发工作流的高质量 telemetry 与训练数据。

## 值得质疑
这篇文章的硬证据偏少。开发者采用率主要来自作者体感，Gemini 与中国模型的工程能力比较也是个人经验；“单 TPU 8i 可运行”的判断来自 HN 估算，不是 Google 披露；Claude Code / Codex telemetry 对模型改进的价值很合理，但文中没有量化证据。结论可作为战略判断，不宜当作市场份额或技术性能定论。

## 最后一层判断
Google 的风险不是底层能力不足，而是把底层优势翻译成外部开发者愿意长期使用的产品形态。如果它能把 coding agent 入口收束清楚，TPU、自研模型、产品分发和内部 token 需求会变成很硬的结构性优势；如果继续工具分裂，Gemini 会像一个强大的内部基础设施，而不是开发者心中的默认 AI 工具链。
