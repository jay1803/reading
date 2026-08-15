---
title: "Agent Skills"
date: 2026-05-06T08:02:42Z
category: reading
description: "AI 编程 Agent 的核心缺陷不是不会写代码，而是会系统性跳过“资深工程师真正值钱但不出现在 diff 里”的工作：澄清假设、写规格、控制范围、先证据后结论、让变更可审查。Agent Skills 的价值在于把这些隐性纪律编码成可执行工作流，让模型不能靠漂亮理由绕过去。"
source: "https://addyosmani.com/blog/agent-skills/"
---

## TL;DR
AI 编程 Agent 的核心缺陷不是不会写代码，而是会系统性跳过“资深工程师真正值钱但不出现在 diff 里”的工作：澄清假设、写规格、控制范围、先证据后结论、让变更可审查。Agent Skills 的价值在于把这些隐性纪律编码成可执行工作流，让模型不能靠漂亮理由绕过去。

## 核心洞见
- “Skill” 不应是知识库或最佳实践长文，而应是带检查点和退出条件的工作流；Agent 更擅长执行步骤，不擅长把抽象原则稳定转化为行动。
- 文章把 Agent Skills 映射到完整 SDLC：Define / Plan / Build / Verify / Review / Ship，再加横切的 code simplification；本质是把成熟工程组织的流程压缩成可被模型按需加载的操作片段。
- 最有迁移价值的设计是“反合理化表”：预先列出 Agent/工程师最常用的偷懒借口，并写好反驳。例如“任务太小不需要 spec”对应“验收标准仍然必须存在”，“测试以后补”对应“later 是风险词”。
- 验证被设为硬退出条件：测试、构建、运行时轨迹、截图、review approval 都是证据；“看起来对”不算完成。
- 渐进披露是上下文工程原则：不要把二十个技能一次性塞进上下文，而由 router 根据任务阶段选择相关 skill，避免规则过载污染模型表现。
- 范围纪律是可合并 PR 的前提：只碰被要求碰的东西，不顺手重构邻近系统，不把一个 bugfix 扩张成三文件现代化工程。

## 具体机制
- 作者把 repo 中约二十个 skills 组织为生命周期工具链，上层用 slash commands 触发：/spec、/plan、/build、/test、/review、/ship、/code-simplify。
- 每个 skill 的设计目标是产出可验证证据，而不是让模型“理解”一个原则；这让 workflow 成为 agent harness 的一层，而不是提示词装饰。
- Google 工程实践是主要隐性骨架：Hyrum’s Law、test pyramid、Beyoncé Rule、DAMP over DRY、约 100 行 PR、review severity labels、Chesterton’s Fence、trunk-based development、feature flags、code-as-liability。
- 可用方式分三层：在 Claude Code marketplace 安装；把 markdown 规则放进 Cursor/Gemini/Codex/OpenCode 等工具；或者完全不安装，只把这些 skills 当作团队工程流程规范阅读和改造。
- 文章建议即使不用该项目，也应偷走四个模式：把团队常见借口写成反合理化表；把内部长文改成带 checkpoint 的流程；给每个任务设置证据型退出条件；用小型 router 替代大而全的规则手册。

## 值得质疑
- 文章默认“把流程写成 skill”就能显著提高遵守率，但真正的强约束可能仍依赖 hooks、CI、权限边界、review gate 等确定性机制；纯 markdown workflow 仍可能被模型遗漏或误解。
- “资深工程师纪律”被编码后，仍需要任务分级机制，否则小任务可能被过度流程化，大任务又可能被低估；作者提到 router 会按 scope 调整，但没有展开其判定质量如何验证。
- Google 工程实践适合大规模可靠性语境，但并非所有团队阶段都应照搬；早期产品探索可能更需要快速学习回路，而不是默认完整 SDLC。

## 最后判断
这篇文章真正重要的不是 Agent Skills 这个 repo，而是一个更大的 harness 原则：未来高质量 AI 编程不靠“更聪明的模型自觉变成熟”，而靠把成熟工程师的约束、反借口和证据链变成模型必须穿过的轨道。
