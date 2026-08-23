---
title: "Make your prompt tracking more accurate this week"
date: 2026-06-09T08:00:56Z
category: reading
author: "Kevin Indig"
description: "单次运行的 prompt 追踪等同于问卦：同一 prompt 运行 3 次后，仅有 2.2% 的引用保持稳定；LLM 内部采样方差本身就在 10–34% 之间。但\"概率性 ≠ 不可测量\"——天气预报和信用评分同样概率性，照样被系统性追踪。关键字追踪也有个人化和位置差异，行业靠标准化采样解决了。Prompt tra..."
source: "https://www.growth-memo.com/p/how-to-make-prompt-tracking-much"
---

## Prompt tracking 的变异性不是放弃的理由，是方法论未成熟的信号

单次运行的 prompt 追踪等同于问卦：同一 prompt 运行 3 次后，仅有 2.2% 的引用保持稳定；LLM 内部采样方差本身就在 10–34% 之间。但"概率性 ≠ 不可测量"——天气预报和信用评分同样概率性，照样被系统性追踪。关键字追踪也有个人化和位置差异，行业靠标准化采样解决了。Prompt tracking 需要同样的升级。

## 现有追踪方法的六个具体破绽

1. **单次运行**：每个 prompt 本质上是 n=1；引用率必须用置信区间表达，不能用点估计。
2. **推理等级混淆**：高推理 vs 低推理有 18 个百分点的引用率差距，高推理触发 4.6 倍以上的 fan-out 查询——聚合成一个分数无意义。
3. **月度节奏**：Google AI Mode 每周替换 56% 的引用来源，ChatGPT 替换 74%。月度追踪等于每季度看一次银行账单。
4. **跨平台聚合**：将 ChatGPT + Perplexity + Gemini 混成一个"AI 能见度分"，等同于把 Google 排名和 Bing 排名平均。
5. **无 persona**：通用提示返回的答案无人真正看到；买家角色决定了 prompt 措辞，也决定了哪些内容被引用。
6. **只看 Turn 1**：单轮测量看不到品牌是否在第 2、3 轮（比较、定价、风险讨论）中存活。

## 可执行的追踪架构

参考配置（B2B SaaS CRM 类目）：
- 40 个 seed prompts，按品牌/类目/问题加权（12/12/16）
- 各平台分开追踪（ChatGPT、Perplexity、Gemini、Google AIOs）
- 每 prompt 每平台每周运行 5 次，计算提及率 ± CI、引用率 ± CI、排名位置、情感、关联属性
- 16 个高意图 prompt 扩展为 5 阶段购买旅程：Problem → Exploration → Comparison → Validation → Selection

旅程层的核心价值：在高推理模式下，Problem 阶段被引用的品牌在 4 条旅程路径中全程延续到 Selection；低推理模式下为零。持久性（persistence）是单次追踪永远看不到的指标。
