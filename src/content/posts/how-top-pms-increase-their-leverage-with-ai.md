---
title: "How top PMs increase their leverage with AI"
date: 2026-07-01T08:03:03Z
category: reading
description: "\"协调与对齐\"型 PM 正在被淘汰。Colin Matthews 用\"三架梯子\"描述当前顶尖 PM 如何用 AI 真正扩大影响力，而不只是用 AI 写文案。"
source: "https://www.lennysnewsletter.com/p/how-top-pms-increase-their-leverage"
---

## PM 的 AI 杠杆分三个维度，每个维度三个台阶，向上一阶即数量级效率差

"协调与对齐"型 PM 正在被淘汰。Colin Matthews 用"三架梯子"描述当前顶尖 PM 如何用 AI 真正扩大影响力，而不只是用 AI 写文案。

### 个人杠杆：从"帮你写"到"替你做"

- 第一阶：AI 帮你生成文字，你复制粘贴到别处。大部分人停在这里。
- 第二阶：AI 直接生成制品——幻灯片、财务模型、小原型。
- 第三阶：AI 替你完成整条待办。前提是通过 MCP 把 LLM 连接到 PostHog、Notion、Amplitude 等工具，让它端到端拉取和推送数据、跑完分析。示例：一句提示让 Claude 通过 PostHog 对比"分享照片用户"与"不分享用户"30 天留存，输出带源头链接的 HTML 报告。

关键操作：做完任何新任务后，立刻让 LLM 把这套流程保存为 skill，下次一键复用。

### 产品杠杆：从"独立原型"到"直接开 PR"

- 第一阶：用 Lovable/Replit/Magic Patterns 做 web 原型。速度快，但代码和真实产品脱节，验证后仍需从头翻译成真实代码。
- 第二阶：用 Claude Code/Codex 在真实代码库上做原型。关键前提：请工程师用一句提示从主仓库提取"纯前端 + 本地 mock 数据"子仓库，不依赖任何环境变量或后端服务，PM 在此安全沙箱里原型，产出代码直接兼容真实组件与设计规范。
- 第三阶：让 Agent 直接开 PR 交给工程师 review 并合并。适用范围：文案改动、小 UI/UX 调整、使用现有后端接口的视图变更。知道"这件事该写文档、做原型、还是开 PR"本身就是 PM 的核心判断力。

### 系统杠杆

原文此处截断，无可用内容。
