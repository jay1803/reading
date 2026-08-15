---
title: "Sonnet 5 review: I ran 64 generations to find out if it's worth it"
date: 2026-07-02T08:03:15Z
category: reading
description: "Claire 跑了 64 次盲测（PRD 写作、原型生成、Agentic 代码任务、Agent 语音）后，把人类品味分（70%）和 LLM 评委分（30%）合并。两者的排名几乎完全相反：LLM 评委认为 Gemini 3 Pro 和 Sonnet 5 最好，Claire 个人却把 Sonnet 4.6 排第一，S..."
source: "https://www.lennysnewsletter.com/p/sonnet-5-review-i-ran-64-generations"
---

## 核心论点：LLM 评委与人类品味系统性分叉

Claire 跑了 64 次盲测（PRD 写作、原型生成、Agentic 代码任务、Agent 语音）后，把人类品味分（70%）和 LLM 评委分（30%）合并。两者的排名几乎完全相反：LLM 评委认为 Gemini 3 Pro 和 Sonnet 5 最好，Claire 个人却把 Sonnet 4.6 排第一，Sonnet 5 和 Opus 4.8 垫底。

这不是偶然误差——是结构性差异：LLM 评委不区分「能跑但难看」和「有创意但粗糙」，倾向给所有输出 7/10，而 Claire 有明确的审美锚点（最大过敏源是「Claude Slop」，即 Claude 模式化写作的痕迹）。

## How AI Bench 的构建思路

Claire 让 Claude Code 翻看她的历史 session，从中提炼出「适合播客受众的 benchmark」：冻结输入、盲评、有评分标准，测 PRD 写作、原型一键生成、Agentic 多步任务和 Agent 声音测试。benchmark 最终输出一个本地 HTML 评分页，她用 1-5 的肠感分实时打分，JSON 导出后与 LLM 评委分合并。

构建整套流程用了 45 分钟，边录播客边跑 eval，结果在录制途中才揭晓——彻底盲测。

## 「任务已饱和」比排名本身更有价值的发现

Agentic 代码库搜索任务几乎所有模型都表现良好，Opus 4.8、GPT-5.5、Sonnet 5 和 Gemini 3 Pro 差距极小。Claire 的结论是：这类任务已无法区分模型——下轮需要换更难的 Agentic benchmark。AI 自己总结的「退役这个任务」和她的独立判断完全一致，这是对她直觉的一次机器验证。

## Sonnet 5 为何在个人榜垫底

Sonnet 5 的原型生成有大量「跑坏了」的情况——功能失效率偏高。加上 Sonnet 5 的 PRD 写作仍带有 Claude Slop 味道，Claire 对此有极强的识别过敏，直接拉低了肠感评分。

讽刺的是，这期节目本来就是做 Sonnet 5 评测的，最终却发现——在个人榜上——Sonnet 4.6 这个「旧模型」仍然领先。

## 逐任务的实际建议（Claire 加权版）

- PRD 写作：GPT-5.5，内容扎实且结构清晰。
- 原型生成：Sonnet 4.6（简单产品）/ Opus 4.8（复杂 UI 和密集交互）。
- 日常与 Agent 闲聊 / 语音助手：Sonnet 4.6，人格最顺，Claire 为此专门付 API 费。
- Agentic 代码任务：Opus 4.8 或 Sonnet 5 均可，当前任务难度不足以区分。
