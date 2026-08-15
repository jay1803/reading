---
title: "Superpowers 为什么能执行长任务且确保交付质量？"
date: 2026-06-06T08:04:03Z
category: reading
description: "Superpowers 通过「先明确需求、再执行」+「Subagent 按任务独立运行」破解了 AI 长任务质量断崖问题——关键不是模型更强，而是 Harness 强迫 AI 严格 Follow Spec，这才是质量保障的核心。"
source: "https://justinyan.me/post/6657"
---

## TL;DR
Superpowers 通过「先明确需求、再执行」+「Subagent 按任务独立运行」破解了 AI 长任务质量断崖问题——关键不是模型更强，而是 Harness 强迫 AI 严格 Follow Spec，这才是质量保障的核心。

## 核心洞见
- 作者自己做 Agent orchestration 时发现：任务超过 20 分钟后质量断崖式下跌，根因是没有严格 Follow Spec，而非模型能力不足。
- Superpowers 的整条 pipeline 前一步输出即后一步输入：brainstorming → writing-plans → executing-plans / subagent-driven-development。
- Subagent 不继承主 Session 的 context，使每个 Subagent 干净独立、不撑爆主 context，也让部分任务可并行执行。

## 具体机制
### Brainstorming 阶段
一次只确认一个问题；提供 Visual Companion 生成粗糙 web demo 做可视化方案确认；贯彻 YAGNI 原则；产物是 Spec 文档——人类完成这步就算完成了最难的一步。

### Writing-plans 阶段
将 Spec 拆成 2–5 分钟原子任务（写失败测试 → 最小实现 → 测试通过 → 提交），贯彻 DRY/YAGNI/TDD/频繁 Commit；明令禁止 AI 偷懒行为（TODO、add appropriate error handling、similar to Task N）；Plan 完成后强制 self-review（Spec 覆盖度/占位符扫描/一致性检查）。

### Executing-plans 阶段
每个 Task 创建独立 Subagent；每个 Subagent 走两阶段 Review：Implementer（执行）+ Code Quality Reviewer（质量复核）；明令禁止执行中途询问"要不要继续"——这是任务能跑 1 小时以上的关键。Red Flags 机制禁止：在 main/master 直接写代码、未修完 issues 就跳下一步、Subagent 自己去读 Plan 文件（Subagent 只接收主 Session 给的必要 context）。

## 隐藏限制
- 不适合小需求：若 AI 自动触发 Superpowers 会把简单问题复杂化，浪费 token 和时间，需人工判断后再调用。
- 依赖特定 CLI 的原生 Subagent 支持（Claude Code、Codex CLI）；不支持 Subagent 的环境退化为单 Session 串行执行，失去并行优势。
- 「便宜模型 + 好 Harness 可替代昂贵模型」——作者因此将自己产品基座从 Gemini 换成 DeepSeek，节省成本；同样逻辑也适用于非软件工程的 Agent 产品设计。
