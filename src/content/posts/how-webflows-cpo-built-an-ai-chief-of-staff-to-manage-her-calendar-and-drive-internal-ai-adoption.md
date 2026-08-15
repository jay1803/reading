---
title: "How Webflow's CPO built an AI chief of staff to manage her calendar and drive internal AI adoption"
date: 2026-02-14T21:10:58Z
category: reading
description: "Rachel Wolan，Webflow CPO。16岁开始写代码，做高管后六七年未亲自编码；vibe coding 工具出现后重新下场，至今已构建数十个个人应用，每天在 Claude Code 里工作。主持人 Claire Vo 本身也是前 CPO，同样有编码背景，两人在\"AI 原生高管\"议题上有实质观点交换。"
source: "https://www.youtube.com/watch?v=BTcG59ZR9sg"
---

## 嘉宾背景
Rachel Wolan，Webflow CPO。16岁开始写代码，做高管后六七年未亲自编码；vibe coding 工具出现后重新下场，至今已构建数十个个人应用，每天在 Claude Code 里工作。主持人 Claire Vo 本身也是前 CPO，同样有编码背景，两人在"AI 原生高管"议题上有实质观点交换。

## TL;DR
高管用 AI 为自己构建个人软件，最大收益不是省时间，而是真正理解产品架构——这才能让他们有底气推动组织级 AI 采用，而不只是靠 PPT 在台上讲理念。

## "幕僚长"不是比喻，而是一个真实在跑的本地应用

Rachel 的 AI Chief of Staff 运行在 localhost，每天早晨使用。核心功能：

- **日历分析**：读取过去一周 Google Calendar（只读权限），回答"怎么让上周更好？"并生成"残酷真相"——她收到的输出是："你在以高级 PM 而非 CPO 的方式运作。你在审 PRD、审脚本、录营销视频。Fatal flaw。"
- **邮件分诊**：归档不重要邮件，标记需关注的，草拟回复；Gmail 权限严格限定为读取/归档/草拟/标签，不能发送。
- **晚宴准备**：截图宾客名单 → 自动 OCR + 网络/LinkedIn 搜索 → 结合她的个人 Markdown 档案（沟通风格文档、Webflow 产品更新记录）生成 conversation starters。

技术实现刻意简单：Google Cloud API token、本地运行、多个独立 Claude 终端（避免上下文污染）、数据全部以 Markdown 文件存储。

## Markdown 文件是个人 AI 基础设施的真正杠杆

她把所有个人资料——沟通风格、Webflow 产品发布记录（每月生成更新）、PRD、晚宴研究——都存为 Markdown 文件放在 repo 里，前端用 Markdown renderer 渲染。

这个选择的实际价值：同一套文件既可被 Claude Code 这类 agent 直接调用，也可在 Web UI 查看；不需要数据库；格式对 LLM 友好。她的结论："软件现在和文档一样容易生成了"——可以用完即弃，也可以持续演进，完全按自己需求定制。

## 构建的最大回报是理解架构，而不是省时间

Rachel 明确说，这套系统的最大收获不是效率提升，而是：

1. 真正贴近代码库（能看懂 Webflow monorepo）
2. 能和工程师进行深度技术对话
3. 理解 AI 产品的底层实现逻辑
4. 重燃了创造的乐趣——"这是我职业生涯中做这份工作最有意思的阶段"

这对"AI 原生高管"的定义有实质影响：高管的核心价值不是推广工具，而是自己成为 builder。

## Builder Day 是推动组织 AI 采用的可复制结构

Webflow 做了两次 Builder Day（全员停工一天，各自构建 AI 原型）：

- 第一次（仅设计团队）：约 50% 成员之后持续使用 Cursor——此前几乎没人用
- 第二次（设计、产品、数据科学、用研、分析、工程全员）：一天内产出 80+ 原型

关键设计要素：分角色预热作业 + 工具开通（Cursor/Figma Make/Webflow）+ 工程师 on call 支持 + CEO 级评审团 + 奖项与荣誉。

配套的硬性要求："没有原型，不能和我开会。"

团队调研反馈：大多数人感到 fun / empowering / eye-opening——Rachel 用"bluepilled"形容：那一刻人们突然意识到什么是可能的。

## 留下的那个想法

她用数字倍数来校准 AI 的输出语气：不满意就清空上下文重来；想要微调就说"10x"，想要彻底重写就说"100x"。把提示词当旋钮而不是命令——这个细节揭示她与 AI 的工作关系更接近"调音"而非"发指令"，也暗示对 AI 输出的控制精度远比大多数人想象的要高。
