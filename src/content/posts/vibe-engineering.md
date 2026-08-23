---
title: "Vibe engineering"
date: 2025-10-09T16:09:00Z
category: reading
author: "Simon Willison"
description: "AI coding agent 的实际效益与工程师现有水平成正比：测试套件越完善 agent 循环越快、规划越前置 agent 偏差越小、文档越齐全 agent 越少读代码。AI 奖励已有优秀习惯，惩罚缺失优秀习惯——门槛在原地，上限在抬高。"
source: "https://simonwillison.net/2025/Oct/7/vibe-engineering/"
---

## TL;DR
AI coding agent 的实际效益与工程师现有水平成正比：测试套件越完善 agent 循环越快、规划越前置 agent 偏差越小、文档越齐全 agent 越少读代码。AI 奖励已有优秀习惯，惩罚缺失优秀习惯——门槛在原地，上限在抬高。

## 核心主张拆解
Willison 以「vibe engineering」命名区别于 vibe coding（纯提示驱动、接受任何能用的输出）的另一端：有经验的工程师用 AI agent 加速同时完全保留对代码的理解与责任。他列出受 AI 放大的核心工程实践：

- 自动化测试：测试套件完整，agent 可在循环中迭代验证；无测试则 agent 的"已完成"毫无意义
- 提前规划：先迭代 spec 再交给 agent 写代码，比直接开写效果显著更好
- 完善文档：模型可从文档推断实现，无需读遍 codebase
- 版本控制纪律：agent 能自主 git bisect 追溯 bug，前提是 commit history 有意义
- 管理能力：给 agent 清晰指令、足够上下文、可操作反馈，与管理初级工程师的技能高度重叠

并行跑多个 agent 处理不同问题已成为资深工程师的实际工作方式（Willison 本人已在实践）。

## 反驳或薄弱处
文章给出十几条"好习惯"清单，但没有排优先级，也没有说明当这些条件不满足时具体会差多少——偏向论断而非论证。"vibe engineering"这个名字本身也显得随意（Willison 自嘲"可能是愚蠢的名字"），且 "vibes" 在 AI 圈已有疲感，能否黏住仍是问号。

**终：** Willison 没说的是：这对初级工程师意味着什么。若 AI 放大的是资深经验，junior 的成长路径可能比任何时候都更难走——这才是结构性的那个问题。
