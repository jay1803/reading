---
title: "Streamline Workflow with CEOS: Claude Meets EOS"
date: 2026-03-03T23:53:57Z
category: reading
description: "Brad Feld 在 90 分钟内用 Claude Code 把完整的 EOS 框架打包成可 fork 的开源 skill 包（CEOS）。核心主张是：AI skills 就是 prompt engineering 文档，一套公司操作系统可以只靠 Markdown + git history 运行，不需要 Sa..."
source: "https://feld.com/archives/2026/02/streamline-workflow-with-ceos-claude-meets-eos/"
---

## TL;DR
Brad Feld 在 90 分钟内用 Claude Code 把完整的 EOS 框架打包成可 fork 的开源 skill 包（CEOS）。核心主张是：AI skills 就是 prompt engineering 文档，一套公司操作系统可以只靠 Markdown + git history 运行，不需要 SaaS 订阅、不需要数据库。

## 核心洞见
三条基础设计原则驱动整个项目：
- **Everything is a file**：所有 Rock、Scorecard、L10 会议记录都是带 YAML frontmatter 的 Markdown 文件，可读、可 diff、可被任何工具解析；git history 即审计链。
- **Skills, not software**：CEOS 不是应用，是一组 Claude Code skill——每个 skill 教 Claude 如何主持一个特定的 EOS 工作流（设定 Rocks、跑 L10 会议、IDS 问题解决）。
- **Fork and own**：上游 repo 只有 skill 和模板，公司数据住在自己的 fork，拉 upstream 获取 skill 更新但数据不受影响。

## 具体机制
Claude Code 自主决定了这些关键设计细节，而 Feld 只提供了方向：
- **YAML frontmatter 的边界**：只给有生命周期状态的对象加 frontmatter（Rock: `on_track/off_track/complete`；Issue: `ids_stage`）；纯参考文档（V/TO、Accountability Chart）用 plain markdown——区分标准不是复杂度，而是"文件是否有随时间变化的状态"。
- **Skill description 陷阱**：description 字段应该写"什么时候用"，而不是"做什么"——一旦写了 what，Claude 读完描述就跳过正文细节，导致执行走捷径。
- **Skills 松耦合**：各 skill 互相引用但不自动调用（L10 skill 提到 ceos-ids 能创建 issue 文件，但让用户决定何时切换）。
- **.ceos marker 文件**：借鉴 .git 的零字节标记文件，让每个 skill 不管工作目录在哪里都能可靠找到 repo root，不需要环境变量或硬编码路径。

## 隐藏限制
CEOS 的完整度依赖用户主动跑 skill——EOS 的价值在于节律执行，而 skill 本质是被动响应式的，不会自动提醒你该开 L10 了。把流程知识封装进 AI 和把执行节律内化进团队是两件事。

## 收束
大多数开源项目的文档止步于两层：用户向（能做什么）和贡献者向（怎么加）。让生态真正可扩展的是第三层——机器向的数据契约（YAML frontmatter 作为可解析的 parsing contract）——但这层通常被遗漏。
