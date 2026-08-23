---
title: "“A model that produces code which compiles and passes the tests it was given is not the same as a model that produces correct, secure, maintainable, well-architected software”"
date: 2026-05-02T08:02:52Z
category: reading
author: "Gary Marcus"
description: "这篇短文的核心不是反 AI coding，而是提醒“可运行 / 通过测试”与“正确、安全、可维护、架构良好”之间有系统性缺口；LLM 的 next-token prediction 能显著扩展写代码速度，但它天然不等于软件工程质量保证，尤其会放大缺经验 vibe coder 的误判。"
source: "https://garymarcus.substack.com/p/a-model-that-produces-code-which"
---

## TL;DR
这篇短文的核心不是反 AI coding，而是提醒“可运行 / 通过测试”与“正确、安全、可维护、架构良好”之间有系统性缺口；LLM 的 next-token prediction 能显著扩展写代码速度，但它天然不等于软件工程质量保证，尤其会放大缺经验 vibe coder 的误判。

## 核心主张拆解
**OpenAI 的 80% 代码 claim 只能说明产出占比，不说明质量闭环**
Gary Marcus 借 TNW 对 Greg Brockman “OpenAI 80% code AI-written” claim 的报道强调：如果指标只是生成代码并通过给定测试，它证明的是工具参与度和局部 productivity，不证明模型能承担正确性、安全性、可维护性、架构一致性这些更难的工程责任。

**Brockman 的“现实主义”承认很关键**
Marcus 认为 OpenAI 罕见承认了这层限制：AI coding 确实已经有用，next-word prediction 对代码生成的帮助超出很多人的预期；但 robustness 是另一类问题，不能从“写得出来”自动推出“系统可靠”。

**风险最大的是把测试通过误读成工程完成**
给定测试覆盖的是已知场景，真实软件还包含未测边界、长期演化、权限 / 安全、依赖变化、架构债务和团队可读性。LLM 可能让 novice / vibe coder 更快得到一个“看起来能跑”的结果，同时降低他们对隐藏风险的警觉。

## 值得质疑
- 文章本身很短，更多是观点提示而非完整论证；它没有给出 AI-written code 在缺陷率、安全漏洞、维护成本上的数据。
- “next-word prediction 不足以保证 robust code”方向合理，但仍需要区分不同工程场景：一次性脚本、内部工具、核心基础设施、金融 / 医疗系统的风险阈值完全不同。
- OpenAI “80%”的口径未展开：是行数、commit、diff、生成初稿，还是生产代码占比；不同定义会改变结论强度。

## 最后一层
真正该警惕的不是 AI 写代码，而是组织把 “it compiles” 当成生产力胜利的终点。AI coding 的正确位置是加速草稿和局部实现；工程判断、测试设计、安全审查和架构约束，反而会因为生成速度变快而更重要。
