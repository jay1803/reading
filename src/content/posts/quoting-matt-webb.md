---
title: "Quoting Matt Webb"
date: 2026-03-29T17:23:59Z
category: reading
description: "Agent 把编程变成了一个\"无限算力暴力求解\"的问题——而这反而让架构变得比以往任何时候都重要。"
source: "https://simonwillison.net/2026/Mar/28/matt-webb/#atom-everything"
---

## TL;DR
Agent 把编程变成了一个"无限算力暴力求解"的问题——而这反而让架构变得比以往任何时候都重要。

## 核心主张拆解
Matt Webb 的观察：agent 会在 while 循环里无限迭代直到解决问题，代价是烧掉海量 token。真正的挑战不是"能不能解"，而是能不能解得**可维护、可组合、可进化**——这是纯粹的算力无法保证的。

解法落在库和接口设计上：底层必须有封装良好、接口设计让"正确做法即简单做法"的库，让 agent（和人）在叠加功能时整体质量是往上走的，而不是往下腐烂的。

作者自述：现在"vibing"（他用这个词替代 coding 和 vibe coding），看代码的时间越来越少，思考架构的时间越来越多。

## 收束行
当写代码的认知摩擦被 agent 接管，剩下来真正由人负责的判断，只有一件事：这个系统，往后加东西是会变好还是变烂？
