---
title: "★ Claude’s Criminally Bad Electron Mac App Is an Inside Job"
date: 2026-07-04T08:05:45Z
category: reading
author: "John Gruber"
description: "Claude Mac app 自 2024 年 10 月发布以来一直是 Electron 应用——慢、臃肿、非原生。根源不是 AI 编程工具做不了原生 Mac app，而是做决策的人是 Felix Rieseberg：Electron 的联合创始人、Electron 现任行政工作组三名成员之一，在 Anthrop..."
source: "https://daringfireball.net/2026/07/claudes_criminally_bad_mac_app_is_an_inside_job"
---

## Claude Mac App 用 Electron，是人事决定，不是技术限制

Claude Mac app 自 2024 年 10 月发布以来一直是 Electron 应用——慢、臃肿、非原生。根源不是 AI 编程工具做不了原生 Mac app，而是做决策的人是 Felix Rieseberg：Electron 的联合创始人、Electron 现任行政工作组三名成员之一，在 Anthropic 之前先后主导了 Slack 和 Notion 的 Electron 桌面端。

## Breunig 的解释及其短板

Drew Breunig 2026 年 2 月问"为什么 Claude 还在用 Electron"，答案是：AI coding agents 能搞定前 90%，但最后那 10%——边界情况、真实世界支持——仍然耗时难搞。Gruber 不接受这个论证：Bell Labs 的 Tom Cargill 提出的 90-90 法则早就指出最后 10% 耗掉另外 90% 的时间，这与代码是人写还是 AI 生成无关。Gruber 的朋友 Glenn Fleishman、Lex Friedman、Jason Snell 都用 Claude Code 做出了原生 Mac app，证明工具本身不是障碍。

## 内鬼的自白

Anthropic Claude Code 团队的 Boris Cherny 在 HN 上回应 Breunig 的文章，说"做 app 的工程师以前做过 Electron，所以倾向于不做原生。"这里"一些工程师"（some of the engineers）刻意模糊——指的就是 Felix Rieseberg，Anthropic 的 Claude Cowork 和 Claude Code Desktop 工程负责人。

## Rieseberg 的履历

- 2016–2021：在 Slack 带团队开发跨平台 Electron 桌面框架
- 之后：Notion 桌面团队工程经理（Notion Mac app 是 518 MB 的 Electron 应用）
- 现在：Anthropic，Claude Cowork 和 Claude Code Desktop 工程负责人
- 同时至今仍是 Electron 项目行政工作组三名成员之一，还写过 Electron 的官方书

Gruber 的比喻：这就像发现一家蒸馏厂老板家的人先后掌舵了泰坦尼克号、驾驶了兴登堡飞艇、又做了艾米莉亚·埃尔哈特的空中交通管制。一把锤子，钉了所有的螺丝。
