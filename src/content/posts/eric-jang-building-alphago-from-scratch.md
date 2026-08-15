---
title: "Eric Jang – Building AlphaGo from scratch"
date: 2026-05-16T08:02:54Z
category: reading
description: "模型：openai-codex/gpt-5.5"
source: "https://www.dwarkesh.com/p/eric-jang"
---

模型：openai-codex/gpt-5.5

## 嘉宾背景
Eric Jang：前 1X Technologies AI VP，之前是 Google DeepMind Robotics 高级研究科学家；休假期间重建并改造 AlphaGo/Go bot 项目 AutoGo。对话由 Dwarkesh Patel 主持，主题是：从零实现 AlphaGo、MCTS/self-play/RL 的机制，以及这些机制对 LLM、自动化研究和 AI 发展速度的启发。

## TL;DR
这场对话真正讲的不是“AlphaGo 怎么下围棋”，而是一个更一般的智能工程范式：把原本长程、稀疏、难归因的胜负反馈，转化成每一步都有更好标签的监督学习问题。AlphaGo 的核心优雅在于 MCTS 给 policy/value 网络持续产出高信息量的软标签；相比之下，今天很多 LLM RL 仍像“通过吸管吸监督信号”，必须从整条轨迹的成败里反推哪些 token 有贡献。未来 AI 研究自动化的关键，也许不是单纯让 agent 多跑实验，而是设计出能产生这种局部可验证、可迭代改进信号的环境。

## AlphaGo 的关键不是暴力搜索，而是把搜索压缩进网络直觉
Go 的完整博弈树极深、极宽，朴素搜索不可行。AlphaGo 用两个网络同时压缩问题：policy network 缩小“宽度”，先给出哪些动作值得搜；value network 缩短“深度”，用一个局面胜率估计替代把未来完整下完。

Jang 认为真正震撼的是：一个并不巨大的神经网络，能把近似不可穷举的搜索/模拟过程，摊销进一次前向传播。这也是他把 AlphaGo 和 AlphaFold、AlphaTensor 连接起来的原因：很多 worst-case 很硬的问题，在真实分布上可能有可学习的宏观结构。非直觉处在于，神经网络未必“解决”了 NP-hard 式最坏情况，却可能在我们关心的现实分布上压缩出足够有用的近似。

## MCTS 的美感在于：它给每一步生成更好的软标签
AlphaGo 的 self-play 不是简单奖励赢家、惩罚输家。每一步先用当前 policy/value 做 MCTS，得到一个比原始 policy 更尖锐、更可靠的访问次数分布 π；随后训练 policy 去模仿这个 MCTS 分布，训练 value 去预测最终胜负。

这使 RL 过程退化成非常稳定的监督学习：policy 目标是 KL/交叉熵式地拟合“搜索后的更好分布”，value 目标是分类胜负。更重要的是，它训练的是软分布，而不是单个 argmax 动作；软标签包含更多“暗知识”，比 one-hot 动作信息量更高。

但 MCTS 不是无条件更好。若 value function 很差、搜索次数太低，或 replay buffer 让模型忘掉终局评估，MCTS 也可能把 policy 带偏。所以 AlphaGo Lee 会用真实 playout grounding；实践中也可保留一部分不提前认输、直接下到终局的数据，防止 value 在末期局面失真。

## LLM RL 的核心瓶颈是信用分配，而不只是奖励稀疏
对话中最有价值的类比是：MCTS 能在每个局面局部地产生“你下一步本该怎么走”的改进目标；而很多 LLM RL 只能看整段输出最后是否通过测试，再把奖励分摊给 10 万级 token 空间里的整条轨迹。

Dwarkesh 用 bits-per-sample 解释这个低效：低 pass rate 时，监督学习拿到正确标签可以获得大量信息；RL 只能不断采样错误答案，绝大多数样本只告诉你“这也不对”。Jang 补充，若 policy 几乎不会采到正确动作，就根本没有成功信号。

这解释了为什么 AlphaGo 式局部搜索很诱人，也解释了它为什么不能直接搬到 LLM：语言动作空间太宽，同一个 child 几乎不会被重复采样，PUCT 那套基于访问次数的离散树启发式不再自然成立。未来 forward search 可能会回归，但需要不同于围棋的动作抽象和价值估计方法。

## Off-policy 数据有用，但只在“可回到好轨迹”的邻域里有用
Jang 用 DAgger 类比解释 replay buffer：理想数据不只是最优轨迹本身，还包括最优轨迹附近一圈“偏了但还能纠正回来”的状态。这样的 off-policy 数据能教模型在被扰动后回到好轨迹。

危险在于，如果 buffer 里全是当前 policy 永远不会到达的状态，MCTS 给这些状态重新标注再训练，只是在浪费容量，甚至会拉坏策略。这也解释了为什么他尝试过离线 MCTS relabeling：拿历史局面，用当前网络重新搜索更好动作，像 robotics 里的 Bellman updater/“daydreaming”；它能提升 GPU 利用和稳定性，但必须控制状态分布，不能离当前策略太远。

## 重建 AlphaGo 显示：硬件和初始化会吞掉很多旧技巧，但研究品味仍然稀缺
Jang 用约 $10K 预算重建强 Go bot，并不说明 DeepMind 当年低效；第一次做成某件事的成本，本来就远高于复现和追赶。现在可以借助 KataGo、LLM coding、现代 GPU、best-response training 和更好的工程经验来 warm-start。

他的实践判断是：很多 KataGo/AlphaGo 时代的复杂分布式设施、辅助目标、架构技巧，今天在强初始化和更快 GPU 下重要性下降；但有些 compute multiplier 仍有效，比如先在 9x9 小棋盘学终局 value，再迁移到 19x19。

更重要的提醒是：不要在系统还没跑通、数据还坏、bug 还没清掉时研究 scaling laws。Scaling law 是“工作系统的科学”，不是修烂系统的捷径。

## 自动化 AI 研究现在强在执行，弱在换问题
Jang 用 Claude/Opus 做了大量 AutoResearch 式循环：模型擅长跑实验、改代码、做超参搜索、画图、写报告，甚至能开放式地调整 data loader、augmentation、训练细节，像一个高执行力研究助理。

短板在“研究品味”：当前模型不太会判断一条实验路线是否该放弃，也不擅长从第一性原理跳到另一个更有希望的问题。人类研究者仍需要提出关键诊断问题、识别 bug vs. idea wrong、决定何时横向切换方向。

Jang 认为 Go 这类环境可能适合训练 automated scientist：外层有可验证目标（如 win rate、可复现实验曲线），内层又包含真实研究工程问题（训练稳定性、分布偏移、scaling 预测、实验设计）。但它能否迁移到 AI research、药物发现、机器人等更开放领域，仍取决于外部验证信号是否足够好，以及局部改进是否能真正 stack。

## 收束
AlphaGo 留下的最大启发不是“LLM 应该也长出一棵树”，而是：当一个系统能把昂贵搜索变成高密度监督信号，再把监督信号摊销进模型直觉时，学习曲线会突然变得平滑、稳定、可扩展。未来 AI 自我改进若真的加速，很可能也会先找到类似的信号转换器。
