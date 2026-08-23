---
title: "What I learned this week - Pretraining parallelisms, Can distillation be stopped, Mythos and the cybersecurity equilibrium, Pipeline RL, On why pretraining runs fails"
date: 2026-04-17T08:02:24Z
category: reading
author: "Dwarkesh Patel"
description: "模型: openai-codex/gpt-5.4"
source: "https://www.dwarkesh.com/p/what-i-learned-april-15"
---

- 模型: openai-codex/gpt-5.4

## TL;DR
这篇杂记真正串起来的一条线是，AI 的前沿竞争正在从“谁模型更聪明”转向“谁更能驾驭系统约束”。预训练并行受通信、batch floor 和数值精度卡死，RL 训练受长链推理的尾部分布拖垮，商业护城河受蒸馏与工具外显侵蚀，网络安全的跃迁也更接近组合式 exploitation 能力增强，而非某种神秘的智能断层。

## 预训练并行的真正约束
- Horace He 那部分最重要的启发，是把并行策略理解成一串“补丁链”，每种并行都在修上一个方案的瓶颈。
- 纯 data parallel 很快撞上 HBM 上限，FSDP 通过分片参数解决存储问题，所以它成为默认起点。
- FSDP 超出直觉的地方，在于通信可以更好地和计算重叠。权重 all-gather 不依赖前一层激活，能在当前层计算时预取下一层。
- 真正决定 FSDP 能撑到多大规模的，是 compute time 与 comms time 的交叉点。GPU 越多，单卡计算时间下降，通信时间却不跟着降，MFU 会突然塌掉。
- 这也解释了两个常被忽视的现实约束：一是 hierarchical collective 只能把拐点往右推，消不掉拐点；二是 sequence 数量决定了 data-parallel 的 batch floor，attention 不易跨序列拆分，所以即便带宽还够，也不能无限扩 GPU。

## 蒸馏拦不住，护城河会向工作流外移
- 作者对 frontier labs 的担心很直接：如果复现“模型汁水”只需要大约 1T token，而成本只有几千万美元级别，模型能力的封闭性很难构成长期护城河。
- 隐藏 chain of thought 也未必能真正防蒸馏，因为推理 token 并不是一种神秘物质。你可以诱导模型直接开始解题，也可以把隐式推理重建成 RLVR 目标。
- 更难隐藏的是 agentic tool use。真正高价值的行为往往发生在本地文件、bash 命令、代码 diff、工具调用里，这些外显轨迹天然更接近监督信号。
- 更狠的一点是，AI 产品公司甚至可能比底层模型公司更适合蒸馏。因为它们拿得到用户多轮迭代后的 gold diff，能直接把用户最终接受的结果设成 RL target，把被拒绝的中间过程当负样本。
- **证据薄弱处**：1T token 和成本估算明显是量级判断，方向有价值，精确幅度不宜当成事实。

## 网络安全的跃迁更接近组合攻击能力
- Mythos 相比旧模型的关键差别，更接近“终于能把 5 个普通漏洞串成一条 exploit chain”，而不是单独多会找一个洞。
- 这意味着安全能力的跃迁可能来自组合搜索和长期规划，而不是单点推理能力突然爆炸。
- 作者对攻防平衡相对没那么悲观，因为软件今天本来就比 20 年前更安全，行业已经长期处在高强度审计下。如果 AI 先被美国公司和防守方掌握，短期也可能是防守收益更大。
- 最强反驳也很扎实：找到漏洞和修掉漏洞不是同一难度。修补要兼容历史行为、边缘依赖和一堆脏现实，这一侧比“发现问题”慢得多。
- 所以真正的分水岭，在于人类组织能不能把修补速度、形式化验证、内存安全迁移这些防守机制一起提上来。

## Pipeline RL 暴露了“长思维模型”的训练经济学
- 强化学习越往后推，模型回答长度的均值会变长，方差也会变大。容易题很短，难题可能要想 100k token。
- 训练系统最怕的不是平均更长，而是尾部更长。因为所有 GPU 都得等最慢那批 rollout，利用率会被 straggler 拖垮。
- 简单地批量多生成一些 rollout，会把系统拖进 offline RL，因为等训练 step 更新完，后面很多轨迹已经是旧策略生成的。
- Pipeline RL 的关键修补是 in-flight weight updates，也就是轨迹还在生成时就把新权重插进去，让下一轮训练用到的更多短轨迹和部分长轨迹来自更新后的策略。
- 这说明长链推理模型的瓶颈已经延伸到训练经济学，问题变成系统能否承受这种长度分布。

## 预训练失败往往死于因果性与偏差管理
- 作者最后一组笔记最有价值，因为它把“训练跑崩”拆成两类：breaking causality 和 adding bias。
- expert choice、token dropping 这类技巧会在训练里引入部署时看不到的信息，让 token 的命运依赖未来 token 或全局分配，从而破坏 causal 结构。
- 数值问题更阴险。FP16 collective 在大规模累加时会把很多小梯度直接吞掉，误差不是噪声，而是系统性 bias；variance 还能平均掉，bias 会层层复利。
- 这也是为什么“kernel 优化是可验证任务，所以很快会被 AI 自动化”这种说法未必靠谱。很多工程问题并不缺目标函数，真正稀缺的是对隐性失真、跨系统漂移和边界条件的整体掌控。

## 收束
最值得记住的是，这篇文章反复指向同一个现实：AI 竞赛的胜负越来越取决于谁能处理那些看上去不性感的约束，像通信拓扑、轨迹新鲜度、因果性、补丁速度和数值偏差。模型智能还在涨，但真正稀缺的东西已经越来越像系统纪律。
