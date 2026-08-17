---
title: "Fable's judgement"
date: 2026-08-17T15:43:06Z
category: reading
description: "与其给 AI 规定行为规则，不如把判断权直接交给顶层模型——自主决策比逐条指令更高效，并可将实现类任务下发给低功耗子模型以节省 token。"
source: "https://simonwillison.net/2026/Jul/3/judgement/#atom-everything"
---

## 别规定行为，把判断权交给模型

Fable（即顶层模型）在被允许自主决策时比被逐条指令驱动时效果更好。Cat Wu 与 Thariq Shihipar（Claude Code 团队）在 AIE Fireside Chat 上给出的核心建议：与其告诉 Fable「只对较大功能写测试」，不如直接说「由你判断什么时候写测试」。AI 对任务上下文的理解比静态规则更准，过度指定反而削弱了它的优势。

## 模型路由：让顶层模型决定派哪个子模型干活

Jesse Vincent 的延伸技巧：告诉 Fable「对所有编程任务，自行判断用哪个低功耗模型并作为子代理运行」。Simon 随即用这条 prompt 实验，Claude Code 自动将其写成了内存文件，结构如下：

- 实现类工作（写代码、机械编辑）→ 派 Sonnet 或 Haiku 子代理
- 判断类工作（设计、审查、综合、数据分析）→ 留在主模型（Fable）

## 实践结果

Fable token 用量明显下降，同期完成的工作量没有减少。背后逻辑：实现工作很少需要顶层模型的全部能力，而顶层模型本身最擅长的恰好是「决定哪些事情不需要自己亲自做」。
