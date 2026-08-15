---
title: "Prompting 1.1 - Lovable Documentation"
date: 2025-10-11T22:38:33Z
category: reading
description: "幻觉（hallucination）不是 AI 的错，是你的错：每一处未被填满的上下文，都是模型自行发明内容的授权书。"
source: "https://docs.lovable.dev/prompting/prompting-one"
---

## TL;DR
幻觉（hallucination）不是 AI 的错，是你的错：每一处未被填满的上下文，都是模型自行发明内容的授权书。

## 核心洞见
文章把 prompting 能力分为四层：结构化模板（CLEAR 框架，强制拆出 Context / Task / Guidelines / Constraints）→ 对话式（流畅但不失完整）→ 元提示（让 AI 改善你的提示词本身）→ 反向元提示（让 AI 总结已发生的流程，积累可复用提示词库）。四层是工具箱，不是进度条——任务越复杂，往上取用。

CLEAR 五项：**C**oncise（去冗余，直达需求）/ **L**ogical（步骤化拆解复杂任务）/ **E**xplicit（说清楚不想要什么）/ **A**daptive（初始输出不满意时主动迭代）/ **R**eflective（复盘哪些提示词有效）。

## 具体机制
- **Few-shot vs Zero-shot**：Zero-shot 靠模型通识；Few-shot 在提示词里附 2-3 组输入输出样例，让模型"续写"而非"理解"——对格式要求强的场景（如特定代码注释风格）效果显著，代价是消耗更多 token。
- **幻觉防控四路**：① 把 PRD / 数据模型 / tech stack 存入 Knowledge Base，减少模型猜测；② 引用真实文档片段做 grounding；③ Chain-of-thought（要求先解释思路再给答案）；④ 明令"若不确定，请说不确定"而非编造。
- **Diff & Select 原则**：精确命名目标文件或组件，同时声明"不要动其他部分"——这是控制 AI 修改范围的唯一可靠手段；越精确越省 token、越少引入回归 bug。
- **Chat vs Default 分工**：Chat mode 用于规划和 debug，不直接改代码；Default mode 用于落地执行。混用会导致调试对话中无意触发代码改动。

## 隐藏限制
"文件锁"在 Lovable 里不真实存在——用提示词声明"不要改这个文件"只是 workaround，对话越长上下文越容易被遗忘。文章本身也承认：极简修改（改一行 CSS、换一个 label）直接手动操作比烧一条 prompt 更快，过度依赖 AI 处理琐碎任务反而拖慢开发节奏。

## 元提示暴露的比它解决的更有价值
Meta Prompting 最有意思的地方不是改善了提示词，而是揭露了你的隐性假设——那些你"以为 AI 懂"但从未写明的部分，让 AI 重新提问时就全部浮出水面。
