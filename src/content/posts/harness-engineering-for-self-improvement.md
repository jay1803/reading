---
title: "Harness Engineering for Self-Improvement"
date: 2026-07-08T08:04:03Z
category: reading
description: "近期递归自我改进（RSI）的实际路径是 harness 进化，而不是模型直接重写自身权重。"
source: "https://lilianweng.github.io/posts/2026-07-04-harness/"
---

## 摘要

**近期递归自我改进（RSI）的实际路径是 harness 进化，而不是模型直接重写自身权重。**

Weng 的核心判断：模型周边的"部署系统"层（harness）与模型裸智能同等重要。Claude Code、Codex 这类产品的成功，正是 harness 而非底层权重带来的。近期 RSI 不会从模型改自己的权重开始，而会从 harness 自动优化开始，mature harness 再去驱动 auto-research loop，反过来产出更好的模型。

### 优化对象的递进

Harness 优化的演进轨迹是：instruction prompts → structured context → workflow → harness code → optimizer code。越靠后，模型能操控的设计空间越大，需要的基础能力也越强。

- **Context Engineering**：ACE 把上下文从"越来越长的 prompt"改造成结构化的 itemized playbook，Reflector/Curator 从 rollout 中蒸馏并增量更新条目，避免全量重写带来的漂移。MCE 更进一步，把"如何管理上下文"本身当作可进化的 skill，分离机制（meta-level skill evolution）与内容（base-level context optimization），做双层优化。Meta-Harness 再上一层：优化的对象变成"决定存什么、取什么、怎么呈现给模型"的代码本身。

- **Workflow 搜索**：手工设计（AI Scientist、ScientistOne）已证明可以跑完从提 idea 到写 paper 的完整 loop；但 workflow 设计本身也可以成为搜索目标——ADAS 用 meta-agent 生成代码形式的 workflow，AFlow 用 MCTS 在 workflow 图上做 tree search，实验显示两者均优于手工设计。

- **Harness 自我改进**：Self-Harness（Zhang et al. 2026）用"weakness mining → bounded proposal → regression validation"三段式循环改自己：从执行 trace 中聚类失败模式，向当前 harness 提有限范围的修改，只有在 held-in 修复且 held-out 无回退时才 accept。STOP（Zelikman 2023）更早揭示了递归改进的基础能力门槛：GPT-4 下改进者自我递归提升，GPT-3.5 和 Mixtral 下反而退化——recursion 不创造能力，只放大已有能力。

- **进化搜索**：AlphaEvolve 在代码库中用 `EVOLVE-BLOCK` 标记可进化区域，meta-prompt 与 solution 一起协同进化。DGM（Darwin Gödel Machine）让 agent 直接修改自己的 harness 代码库，从简单初始 config 出发，在 SWE-bench Verified 上 20% → 50%，Polyglot 14.2% → 30.7%——以固定底层模型（Claude 3.5 Sonnet）实现的。

### 开放边界与悬而未决的问题

Weng 自己列的挑战比通常 survey 更锋利：

1. **评估器太弱**：现有 self-improvement loop 只在有快速精确 verifier 的任务上有效（竞程、GPU kernel）。研究品位、novelty、长期价值没有快速 verifier，这是当前 auto-research 的真实天花板。

2. **上下文/记忆生命周期**：Weng 预测 context engineering 最终会被内化进核心模型智能（类比 prompt tricks 消失进 instruction tuning），但"指定目标、约束、上下文、评估"的需求不会消失。

3. **多样性坍缩与 reward hacking**：进化/RL loop 天然趋向已知高奖励模式，evaluator 和权限控制应放在进化 loop 之外，有 held-out test 和人工审查节点。

4. **Coding agent 的短视问题**：当前 agent 能完成当前任务，但无法保护由数百工程师共同维护的 repo 的长期健康——可维护性、所有权边界、迁移成本都不在 sandbox RLVR 的优化目标内。

5. **人类应该上移而不是退出**：人应提供正确抽象层的监督，而不是被移除出 loop。

一个值得警惕的结果：Self-Harness 一类工作若允许程序修改 OS，会打破抽象边界；权限控制和安全层必须放在优化 loop 之外。
