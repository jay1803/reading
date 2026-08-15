---
title: "Neural Networks: Zero to Hero"
date: 2026-02-14T20:36:35Z
category: reading
description: "Karpathy 的核心主张是：语言模型是学整个深度学习领域最好的起点——不只是 NLP——因为它在一个可理解的任务上迫使你走完所有核心概念：autograd、BatchNorm、优化器、Transformer。别的方向学完再迁移，比从 CV 绕进来快得多。"
source: "https://karpathy.ai/zero-to-hero.html"
---

## TL;DR
Karpathy 的核心主张是：语言模型是学整个深度学习领域最好的起点——不只是 NLP——因为它在一个可理解的任务上迫使你走完所有核心概念：autograd、BatchNorm、优化器、Transformer。别的方向学完再迁移，比从 CV 绕进来快得多。

## 核心洞见
课程全程在代码里推导概念，从不给你黑盒 API。每一集都从头实现一个组件——bigram、MLP、BatchNorm、手动反向传播、WaveNet 风格卷积、GPT、BPE tokenizer——强制保持"为什么这样实现"的追问。这不是"先理论后实践"，而是用实现本身作为理解路径。

## 具体机制
七个视频，累计约 12 小时，严格递进：
1. **Bigram + makemore**（1h57m）：torch.Tensor 基础 + 语言建模框架（训练 / 采样 / 损失函数）
2. **MLP**（1h15m）：超参调整、train/dev/test split、过拟合欠拟合
3. **Activations & Gradients + BatchNorm**（1h55m）：前向/反向传播的统计健康度诊断；BatchNorm 为什么让深网可训练
4. **手动反向传播**（1h55m）：完全不用 autograd，从 cross entropy 到 embedding table 手推梯度；理解梯度如何流过计算图
5. **WaveNet 风格深层卷积**（56m）：树状层级结构；torch.nn 内部机制；典型深度学习开发流程
6. **从头构建 GPT**（2h13m）：严格遵循"Attention is All You Need"，对接 GPT-2/3；causal self-attention 的完整实现
7. **GPT Tokenizer + BPE**（ongoing）：encode/decode 实现；tokenization 为何导致 LLM 大量奇怪行为

## 隐藏限制
内容仅覆盖语言方向，CV / RL 无对应路径。Causal dilated convolutions 在第五集明确标注"尚未涉及"。第七集状态为"ongoing"，课程可能仍在更新中。

## 收束
Tokenizer 一集最具破坏性的一句：LLM 的许多怪异行为（算术错误、奇怪的幻觉模式）根源在 tokenization，而 Karpathy 说"理想情况下有人能把这个阶段整个删掉"。整门课在教你一砖一瓦地盖大楼，最后一集悄悄说也许地基设计错了。
