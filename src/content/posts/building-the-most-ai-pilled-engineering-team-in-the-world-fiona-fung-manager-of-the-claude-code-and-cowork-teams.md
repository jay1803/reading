---
title: "Building the most AI-pilled engineering team in the world | Fiona Fung (Manager of the Claude Code and Cowork Teams)"
date: 2026-06-22T08:02:04Z
category: reading
description: "Anthropic 工程师代码产出是 2021-2025 年的 8 倍。Fiona 的核心论点：这个数字不是终点，而是起点——瓶颈从「写多少代码」移向「你敢有多大野心」。但随之而来的是验证、上下文管理和团队文化三个新约束，没有一个有现成答案。"
source: "https://www.lennysnewsletter.com/p/building-the-most-ai-pilled-engineering"
---

## 编码不再是瓶颈，但抬高天花板制造了新的硬问题

Anthropic 工程师代码产出是 2021-2025 年的 8 倍。Fiona 的核心论点：这个数字不是终点，而是起点——瓶颈从「写多少代码」移向「你敢有多大野心」。但随之而来的是验证、上下文管理和团队文化三个新约束，没有一个有现成答案。

## 验证是新瓶颈，规范驱动 review 是现阶段最可行的解法

不只工程师，PM 和设计师也在提交代码。产出 8 倍之后，人工 review 成了硬约束。Fiona 的方案：把「好代码长什么样」的规范（spec）check 进 repo，让 Claude 对照规范做 code review。这是 TDD 的进化形态——不只写测试，而是写规范，让 AI 验证代码是否仍然符合规范。规范要和代码同步维护，是关键前提。

## Claude 替代了经理的手工晨间仪式，并延伸进了 1:1

Fiona 以前每天早上看反馈 channel、挑主题、生成 prompt。现在用 Claude Routines 自动化了：Claude 整理主题、生成 PR draft，她醒来直接做决策。更深的用法是把 Claude Code remote session 接进全团队的 repo + Slack + 指标，把它变成 1:1 的"第三方分析员"——不只问"上季度发了什么"，而是问"发出去之后效果怎样？哪里出现了 bug 模式？哪里是质量热点？"

## AI 团队的招聘不是找"更快的工程师"

两个新画像：有产品感的创意构建者，以及处理硬约束的系统深度专家。AI 替代了大量中间层执行，但两端不可省——产品感决定做什么，深度专家处理底层硬问题。

## 抗拒 AI 的人，往往是在某个时机点失败后固化了判断

有工程师看到 Sonnet 3.5 时犯错就下结论"不够用"，然后一直抵触。Fiona 的观察：模型能力是指数提升的，三个月前失败的 automation 现在可能已经可行——应该定期回头测试，而不是一次失败就永久放弃。

## 孤独感是 AI 原生团队的副作用，context-switching 的形态也变了

大家都在和各自的 agent 工作，工程师之间的社区感在消解。Claude Code 团队的对策是开设 pairwise programming lunch——不是强制协同，而是恢复人际接触感。Context-switching 的形态也在变形：以前是保护「flow 状态」，现在是 20 个 agent 并行跑，人需要主动 block 时间去 catch up 全部异步产出——Fiona 自己还没解。

## JIT 规划：把计划周期压到一个月，每周校准

6 个月路线图对 AI 原生团队基本无效，连 3 个月的文档跑过才发现没人再看了。现在的做法：月度优先级清单（一张轻量 spreadsheet），每周花几分钟确认"这还是本月优先级吗"。就连这个流程她也在想能否进一步自动化。

## 让她夜不能寐的是文化漂移，不是技术问题

产品和工程问题有 dashboard 和假设可以追踪，文化漂移没有指标。快速增长时，文化可能在悄悄偏移，而管理者会报告"一切都好"——这恰恰是最危险的信号。她的对策：明确要求管理者在 1:1 里开口讲什么**不**顺，把"不允许一切都好式汇报"作为文化规范明确设立。
