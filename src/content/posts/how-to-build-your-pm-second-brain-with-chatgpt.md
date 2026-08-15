---
title: "How to build your PM second brain with ChatGPT"
date: 2026-02-14T20:35:18Z
category: reading
description: "ChatGPT Projects 真正的价值不是用来对话，而是作为持久化的上下文存储器——把原本需要 PM 大脑同时承载的几百个碎片（Slack 讨论、用户调研、产品决策、内部文档）卸载给 AI，让人只负责判断，不再负责记忆。"
source: "https://www.lennysnewsletter.com/p/how-to-build-your-pm-second-brain"
---

## TL;DR
ChatGPT Projects 真正的价值不是用来对话，而是作为持久化的上下文存储器——把原本需要 PM 大脑同时承载的几百个碎片（Slack 讨论、用户调研、产品决策、内部文档）卸载给 AI，让人只负责判断，不再负责记忆。

## 核心洞见
PM 工作的认知瓶颈不是思考力不足，而是 context 太碎——产品方向、过去决策、用户反馈散落在 Slack/Notion/Docs，大脑拼合它们本身就消耗了大量带宽，根本没法专注在真正的产品判断上。作者在 monday.com 接手第一个 AI Agent 项目时，靠把所有碎片文档"倾倒"进 ChatGPT Project，终于在信息混沌中找到了方向感。

## 具体机制
1. 创建 Project，用 instructions 设定"人格"——让 AI 知道如何挑战你、哪里应该推回、用什么风格思考；用 ChatGPT 自身写这段 instructions 最高效（描述你要什么，让它输出配置文本）。
2. 输入原则：万物皆文本。Slack 频道 export、支持文档页 Command+P 存 PDF、竞品调研 CSV、deck 截图——只要能导出为 PDF，就能喂进去。
3. Project 是活的：每产出新文档（PRD、strategy doc、sign-up form）就喂回 Project，知识库随工作自动成长，后续每条 thread 自动继承最新上下文。

## 隐藏限制
**值得质疑**：作者完全未涉及把内部敏感文档上传至 ChatGPT 云端的数据安全与合规问题；随文件量增大，Projects 的实际召回精度也可能下降——文章呈现的是理想状态而非压测结果。整套方法论的前提是 AI 记住了你喂进去的东西，但这个假设并不总成立。

## 零摩擦入口是真正的创新
这套方法的价值不在机制多精巧，而在它把信息管理的门槛降到几乎为零——"倾倒"替代"整理"，让上下文管理从一件需要意志力的事变成一个自然副产品。
