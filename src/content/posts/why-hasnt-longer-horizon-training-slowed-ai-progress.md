---
title: "Why hasn't longer-horizon training slowed AI progress?"
date: 2026-05-08T08:01:45Z
category: reading
description: "AI 进展没有明显被“长任务 RL 更贵”拖慢，核心原因可能不是单一 scaling law 失效，而是三个变量同时遮蔽了真实速度：训练 FLOP 的有效利用率仍在快速上升，人类对接近或超过自身水平的智能增长很难校准，模型能力又常由记忆、工具熟练度、坚持性、人格倾向等非纯智力因素放大。"
source: "https://seangoedecke.com/why-hasnt-longer-horizon-training-slowed-ai-progress/"
---

## TL;DR
AI 进展没有明显被“长任务 RL 更贵”拖慢，核心原因可能不是单一 scaling law 失效，而是三个变量同时遮蔽了真实速度：训练 FLOP 的有效利用率仍在快速上升，人类对接近或超过自身水平的智能增长很难校准，模型能力又常由记忆、工具熟练度、坚持性、人格倾向等非纯智力因素放大。

## 核心主张拆解
Sean Goedecke 反对把 AI 进展简单建模成“任务 horizon 变长 → 每次 reward 更贵 → 训练必然减速”。这个推理在抽象层面成立，但实际 AI 研发受大量非平滑因素支配：训练 bug、工程效率、prompt / harness 技巧、工具使用能力、上下文利用、模型愿不愿意持续执行步骤，都会让能力曲线出现跳变。

第一层解释是“真实有效 FLOP”可能还在暴涨。AI lab 未必能以数量级速度增加 GPU，但可以通过修掉低级训练错误、减少浪费、改进训练代码，把同样硬件变成更多有效训练量。作者用 GPT-4 训练中 FP16 累加小值导致数值错误的例子说明：复杂训练系统的效率瓶颈往往不是缺少天才想法，而是存在足够多愚蠢 bug；修掉这些 bug 可能买到数量级效率提升。

第二层解释是人类对智能增长的感知尺度不可靠。GPT-3 到 GPT-4 显得巨大，是因为模型从明显低于多数人类，跳到某些场景接近人类；一旦 frontier model 进入“是否比我聪明”很难判断的区间，人类只能靠长期结果、事后是否同意它、复杂任务表现等间接线索判断。于是“进展没慢”可能部分是观测误差，“原始智能真的变慢”也可能发生，只是我们缺少稳定测量仪器。

第三层解释是 capability 不等于 intelligence。2025 年前后模型突然更 agentic，未必全是智力提升，也可能是工作记忆更强、对 LLM harness 更熟、能更好 attend context window、或人格更适合 Claude Code / Codex 这类工具环境。这些能力可以通过系统提示、训练配方、工具协议和产品层技巧获得，不必完全依赖更长 horizon 的 RL 暴力训练。

## 反驳或薄弱处
作者最强的洞见是把“长任务训练成本”从单变量理论拉回复杂工程现实：AI 进展不是连续函数，更像一组 lightning strikes。一个训练 bug 能浪费百倍算力，一个 clever trick 能让模型实用性跃迁，一个局部 spiky capability 能制造“整体智能提升”的错觉。

薄弱处在于文章主要是解释框架，缺少可量化分解：有效 FLOP 提升到底多大、工程 bug 修复贡献多少、agentic jump 中多少来自模型本体、多少来自 harness 和 prompt，文章没有数据。它更像对过度简化 slowing thesis 的拆解，不是替代性的预测模型。

Apple “Illusion of Thinking” 的 Tower of Hanoi 例子也很关键：模型失败可能不是不会推理，而是不愿意执行几百步。若同一模型能写代码求解、能完成较小子问题，那么测试测到的是 persistence / task framing，而不只是 reasoning。这提醒我们：很多 benchmark 把“能力缺失”误读成“智力缺失”。

## 最后一层判断
“RL 任务变长所以 AI 会自然减速”听起来干净，但现实研发不干净：浪费的 FLOP、被修复的低级错误、工具环境、模型性格、上下文机制、产品化 harness 都会改变能力外观。真正难判断的是，AI 进展可能已经在某个底层维度放缓，同时在工程和产品层继续以跳变方式释放能力。
