---
title: "Claude Opus 4.8 is here. Is it as good as they say?"
date: 2026-05-29T08:01:15Z
category: reading
description: "Claire Voe 是《How I AI》的主持人，自称是产品负责人和 AI 重度使用者。这期是她拿到 Anthropic Opus 4.8 早期访问后的快速评测，主要测试场景是 Claude Code 里的编码任务，以及 Claude Cowork 里的业务战略分析。"
source: "https://www.lennysnewsletter.com/p/claude-opus-48-is-here-is-it-as-good"
---

## 嘉宾背景
Claire Voe 是《How I AI》的主持人，自称是产品负责人和 AI 重度使用者。这期是她拿到 Anthropic Opus 4.8 早期访问后的快速评测，主要测试场景是 Claude Code 里的编码任务，以及 Claude Cowork 里的业务战略分析。

## TL;DR
Opus 4.8 的问题不是“不聪明”，而是“过快形成局部确信”：它在绿地原型、一次性功能和工具调用上很顺手，但进入真实代码库、边界 bug、数据驱动战略时，容易把假设当事实，缺少向外扩展验证的耐心。Claire 的结论是：这是一款体验更好、语气更干净、速度更快的模型，但未必比 Opus 4.7 更适合需要事实锚定和长链路判断的高风险工作。

## Opus 4.8 的卖点是长期代理能力，但实测优势更像“快速可用”
Anthropic 对 Opus 4.8 的定位是面向 agent 的 step-change model：更诚实、更少 design slop、更长任务跨度、更适合企业环境，并宣称在 Sui Bench Pro 上达到 69.2%，比 Opus 4.7 高近 5 个点，比 GPT-5.5 高近 10 个点，比 Gemini 3.1 高 15 个点。价格并不低：每百万输入 token 5 美元、每百万输出 token 25 美元，effort 默认 high，fast mode 会明显更快。

Claire 的实际体验承认它“好用”：响应快、文字不烦、没有明显 slop tells，能按架构要求执行，也能在 Claude Code 中较长时间自主编码。但她没有感受到宣传里最关键的“更诚实”和“长程自治”优势；更突出的感受是模型效率高、局部执行强，但验证链条偏短。

## 绿地编码能一口气做出来，最后 10% 反复掉链子
她让 Opus 4.8 在 Claude Code 里为 ChatPRD 做一个完整 prototyping capability：给出架构约束、平台选择和功能要求后，模型规划并自主编码约 20 分钟，推到 preview branch 后功能确实跑起来了。这个阶段是它最亮眼的地方：能吃下 spec、产出 feature、遵守既定架构。

问题出现在后续打磨。随着她把功能从“能跑”推进到“更完整、更边界正确”，Opus 4.8 开始持续引入 bug；在 bug hunting 时，它甚至会基于假设编造原因。Claire 特别强调，她已经很久没在模型里看到这么直接的 hallucination，而这次在 high effort 下仍反复出现。她的判断是：模型并非推理预算不足，而是 grounding 不够稳定。

## 真实代码库暴露了它的“边界感”缺陷
在已有代码库中，Opus 4.8 对“自己该在什么抽象层工作”把握不好。她让模型处理几个需要 rebase 和检查的分支，因为底层 PR 改动较大，代码状态需要修复。结果模型经历多轮 rebase/fix cycle，仍不断把 edge-case bugs 带入代码。

这和绿地任务形成对照：在新 surface area 上，它可以快速建立结构并产出东西；但在已有系统里，它需要理解历史状态、隐含约束、分支上下文和局部改动边界，这时它更容易过窄地抓住某个代码点，然后把局部解释当成全局事实。

## 它不够“野心大”，不像最强 agentic coding 模型会主动突破任务上限
Claire 还测试了一个更开放的任务：让 Claude Code 想出适合 9 岁孩子、能体现 agentic coding 边界的酷东西。模型给出的方向很强：构建一个游戏，然后自己看屏幕、试玩、调难度，直到适合孩子。这个 prompt 本身很像前沿 coding agent 应该做的事。

实际产出却偏保守。它确实做出了可玩的东西，后来也能改成 3D，普通标准看很厉害；但 Claire 认为它没有达到“10x agentic coding”的惊艳感。她连续要求“more / do better”，模型仍没有主动扩大创意边界。这里的缺陷不是不会写代码，而是缺少前沿模型那种主动提高目标上限的野心。

## 战略分析里，4.7 比 4.8 更能贴住真实数据
最负面的对比来自 Claude Cowork 的 business strategy 测试。她给 Opus 4.7 和 4.8 同样的业务上下文，让它们分析过去三个月时间分配与 10x business priorities 的偏差，再生成战略提示和 roadmap。

Opus 4.7 的输出更 numbers-anchored：结构清楚，能把数据放进上下文。Opus 4.8 虽然拿到同样数据，却更难发现关键数据，容易过度放大小样本，把局部点当真相。后续 roadmap 任务里，4.8 的结果更手挥；当她追问是否搜索 GitHub、是否验证线上事实时，模型承认没有。这个模式与编码测试一致：它会很自信，但自信不总是来自事实验证。

## 适用边界：做原型可以，做事实密集型决策要加验证 harness
Claire 最终建议把 Opus 4.8 用在 greenfield prototypes、one-shot features、快速工具调用和轻量设计任务上。它体验好、速度快、语气干净，设计输出也改善了过去 Claude Design 里令她讨厌的斜体强调词问题。

但她会谨慎用于三类任务：已有代码库里的复杂分支和边界 bug、需要数字约束的战略工作、需要长程自主验证的任务。她认为可能可以通过 prompting 或 harness 改善，例如强制模型搜索 GitHub、验证 bug、列出证据来源、在高置信结论前做数据检查；但默认状态下，她会继续在战略任务上优先用 Opus 4.7。

## 收束行
Opus 4.8 更像一台“快而顺手的局部执行器”，不是一台已经证明自己能长期守住事实边界的 autonomous worker。
