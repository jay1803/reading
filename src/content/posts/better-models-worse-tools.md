---
title: "Better Models: Worse Tools"
date: 2026-07-06T08:01:44Z
category: reading
author: "Simon Willison"
description: "新版 Claude（Opus 4.8、Sonnet 5）在使用 Armin 的 Pi 编程助手时，会在 ~edit~ 工具的 ~edits[]~ 数组里加入自创字段，导致 Pi 因 schema 不匹配拒绝调用并触发重试。旧版模型没有这个问题。编辑内容本身通常正确，问题仅出在幻构的多余 key 上。"
source: "https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything"
---

## 越新的 Claude 模型，越可能在第三方工具调用中幻构字段

新版 Claude（Opus 4.8、Sonnet 5）在使用 Armin 的 Pi 编程助手时，会在 ~edit~ 工具的 ~edits[]~ 数组里加入自创字段，导致 Pi 因 schema 不匹配拒绝调用并触发重试。旧版模型没有这个问题。编辑内容本身通常正确，问题仅出在幻构的多余 key 上。

Armin 的推测：这是 RL 训练的副作用。新模型被专项训练去使用 Claude Code 内置的 edit 工具（search-and-replace 格式），这种能力"专化"让它在其他编程工具的类似 schema 上反而表现更差——"更强"的模型在特定工具格式上产生了负迁移。

OpenAI Codex 走了另一条路，采用专有的 ~apply_patch~ 机制，同样需要专项适配。这带来一个工程问题：第三方编程工具套件（如 Pi）可能需要维护多套 edit 工具实现，按用户选择的底层模型动态切换，才能保证工具调用的可靠性。
