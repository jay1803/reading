---
title: "The AI Steering Layer"
date: 2026-06-25T08:02:23Z
category: reading
description: "大模型输出能力几乎无限，但团队需要的是品牌一致、设计对齐、代码规范化的输出。LukeW 提出的解法是在工具层和代码库之间插入一个持久化的\"steering layer\"——本质是系统化的 context 注入，而不是依赖每个人自己写好 prompt。"
source: "https://www.lukew.com/ff/entry.asp?2155"
---

## AI 一致性的工程答案：steering layer 而非一次性 prompt

大模型输出能力几乎无限，但团队需要的是品牌一致、设计对齐、代码规范化的输出。LukeW 提出的解法是在工具层和代码库之间插入一个持久化的"steering layer"——本质是系统化的 context 注入，而不是依赖每个人自己写好 prompt。

## 机制与形态

Steering layer 的核心是：将品牌规范、设计 token、开发指令、参考图片等编码为结构化 context，让所有 AI 调用都以此为基础生成输出。最简单的形态是一批文本/图片文件；复杂的情况下是动态 retrieval system（根据不同问题拉取对应 context）。

LukeW 给出三个实例：
- *LukeW Character Maker*：guidelines + 参考图 + prompt rewriting → 任何人都能生成符合品牌风格的图片资产
- *Sol 官网*：design token + agents.md + agent skills → 整个团队用 AI agent 更新网站时自动"snap to"设计和开发规范，无需开发经验
- *Ask LukeW*：不仅有指令，还有多套经过数年迭代的 retrieval system，动态为每个问题拉取最相关 context

## 住在代码库里，还是独立 UI

Steering layer 最自然的位置是代码库本身——利用 version control、review 流程、团队协作基础设施。但非开发人员（设计师、PM、文案）需要贡献或维护时，需要一个独立 UI。如何让更多人能编辑 steering layer 而不破坏一致性，是下一步的工程方向。
