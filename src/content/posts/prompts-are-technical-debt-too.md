---
title: "Prompts are technical debt too"
date: 2026-05-21T05:49:55Z
category: reading
description: "精心调教的 agent prompt 不是低成本“配置”，而是一种比代码更容易静默腐烂的技术债：它绑定具体模型版本，升级后可能从增益变成负担，而且退化通常不会报错，只会表现为“模型好像变笨”。"
source: "https://seangoedecke.com/prompts-are-technical-debt-too/"
---

## TL;DR
精心调教的 agent prompt 不是低成本“配置”，而是一种比代码更容易静默腐烂的技术债：它绑定具体模型版本，升级后可能从增益变成负担，而且退化通常不会报错，只会表现为“模型好像变笨”。

## 核心主张拆解
- “所有代码都是技术债”的类比可以直接迁移到 prompt：AGENTS.md、CLAUDE.md、skills、MCP、工具 prompt、agent wrapper loop 都会增加未来维护面。
- Prompt 确实重要。小改动可能显著改变模型表现，Codex、Cursor、OpenCode、Copilot 之间的体感差异，很大概率来自细微提示词差异。
- 关键问题是 prompt 调优强绑定模型版本。给 GPT-5.4 精修出的 prompt，不保证适配 GPT-5.5；每次模型升级都要重新学习“怎么拿住这个模型”。
- Prompt 债比代码债更隐蔽。坏代码通常会报错或拖慢理解；坏 prompt 往往只是让新模型显得“不如传闻中强”，很难归因。
- 固定旧模型也不是现实解法。当前模型进步速度仍快，一个围绕 GPT-4.1 深度定制的 harness，可能输给围绕 Opus 4.7 的极简 harness。

## 具体建议
- 大多数人应选择 Claude Code、Codex、Cursor、Copilot 这类第三方 AI coding tool，并尽量少配置，借用供应商团队随模型更新做 prompt 评测和调优。
- MCP 和 skills 除非必要，否则应避免或默认关闭，因为它们也会扩大 prompt / 行为表面的维护债。
- AGENTS.md 应只写项目相关的具体事实，少写行为 steering，例如“think step by step”“you are a skilled engineer”“答对给 200 美元”这类随模型变化快速过期的咒语。
- 不要让模型往 prompt 文件里塞大量未审阅文本；prompt 应像代码一样由人有意识地写，并在能删除时删除。

## 值得质疑
- 文章默认第三方工具团队的 prompt 评测一定优于个人定制；对非典型工作流、强私有上下文或特定工具链，定制 prompt 仍可能有稳定收益。
- “避免 MCP / skills”对普通用户成立，但对把工具能力显式化的场景可能偏保守；稳定 API 能力和脆弱行为 steering 不应完全混为一谈。
- 论证方向很强，但经验数据较少，尤其缺少跨模型升级后“极简 harness vs 深度定制 harness”的对比证据。

## 最后一层
Prompt 的危险不在于它无效，而在于它一开始有效：越像杠杆，越容易被当成系统能力；等模型底座改变时，它留下的不是清晰 bug，而是一堆难以归因的性能噪音。
