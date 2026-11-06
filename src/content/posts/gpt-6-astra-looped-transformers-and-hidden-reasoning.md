---
title: "GPT-6 Astra, Looped Transformers, and Hidden Reasoning"
date: 2026-11-06T19:14:42Z
category: reading
description: "GPT-6 Astra 的突出进步集中在 computer use，而围绕它的 Looped Transformer 架构传闻，需要与“模型正在隐藏推理过程”的担忧分开判断：循环复用网络权重能够增加内部计算、提高部分任务的表现，但现有证据没有证明它会让 chain of thou…"
source: "https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and"
author: "Sebastian Raschka, PhD"
---

GPT-6 Astra 的突出进步集中在 computer use，而围绕它的 Looped Transformer 架构传闻，需要与“模型正在隐藏推理过程”的担忧分开判断：循环复用网络权重能够增加内部计算、提高部分任务的表现，但现有证据没有证明它会让 chain of thought 更不忠实，也没有证明它是推理可监控性下降的原因。

Sebastian Raschka 使用 Astra 后认为，它在写作、数学、编程等方面全面超越 GPT-5.6，优势尤其体现在 3D rendering、动画和图形界面操作。文章引用的 ARC-AGI-3 成绩达到 99.9%，相比 GPT-5.6 Sol 的 7.8% 提升巨大；但在更接近实际工作的 Artificial Analysis Coding Agent Index 和综合 Intelligence Index 中，Astra 虽处于前沿，领先幅度并没有同样悬殊。理解这些结果需要区分模型与 **agent harness**：独立评测在部分任务中使用统一 harness，有利于公平比较，却可能无法充分发挥针对自家工具环境训练的模型。要确定这一影响，需要让 Astra 在相同任务、不同 harness 中接受对照测试。模型能力变化也意味着旧的 AGENTS.md、SKILL.md 值得重新审查：能节省重复探索的工作流仍有价值，过时的细密指令则可能限制新模型找到更好的解决办法。

图形任务的意义超出了演示效果。Astra 能通过鼠标在浏览器版 MS Paint 中重画人物照片，也能操作 Blender 等软件；这类能力让模型可以直接使用尚未提供 API 或 CLI 的工具。专用接口通常更高效，GUI 操作则带来跨软件的通用性，因此 Raschka 预计，模型训练与 harness 开发都会进一步向 computer use 倾斜，把代理能力扩展到技术用户之外。文章援引 OpenAI 购入数万台 Mac mini 和 Mac Studio 用于强化学习的报道，其用途是提供真实 macOS 环境：harness 把截图送给模型，模型预测点击、按键、滚动等动作，执行后再接收新截图，最后由任务成功与否及验证器提供训练反馈。模型运行和权重更新仍主要依赖 GPU，Mac 承担交互环境的角色。这延续了 RLVR 的训练思路，也让能够审计、限制电脑访问权限的开源 harness 更加重要。

Astra 是否采用 **recurrent depth**，目前仍缺乏官方确认。The Information 的报道提出了这一说法，OpenAI Chief Scientist Jakub Pachocki 则表示，包括 Astra 在内的当前前沿模型，其计算图深度与 GPT-4 相差不超过两倍；这句话同样可以由增加普通 Transformer blocks 来解释，无法单独证实循环架构。Raschka 认为采用循环机制很有可能，但把 Astra 的成功主要归于这一架构调整，超出了已有证据；训练数据和训练方法的改进更可能承担主要贡献。

Looped Transformer 的基本机制，是让中间表示多次经过同一组 Transformer blocks，在增加有效计算深度时共享权重。2026 年 7 月发布的 Nanbeige4.2-3B 提供了具体例子：输入先经过一组包含 22 个 blocks 的网络，再把输出送回这组网络运行一遍，形成 44 次 block applications，却只保存 22 个不同 blocks 的权重。与包含 44 个独立 blocks 的普通模型相比，它减少了 Transformer 主体的参数存储；embedding 和输出层需要另算，在该模型中，两者约占总计 3B 参数的四分之一，因此不能把主体参数减半直接理解成整个模型减半。

**权重共享节省存储，并不会消除重复计算。** 两轮前向传播仍需执行全部 44 次 block applications，训练时反向传播也要穿过两轮，其计算成本接近具有 44 个独立 blocks 的模型，只是优化器要更新的独立参数更少。KV cache 同样不能因权重共享自然减半：同一个 block 在两轮接收的 hidden states 不同，生成的 keys 和 values 也不同，所以两轮需要分别缓存。Nanbeige 团队尝试过跨轮共享 KV cache，缓存确实缩小了一半，但性能下降，最终发布版本仍使用独立缓存。他们还发现，从头训练循环架构优于把已有预训练模型改造成循环模型；增加到更多轮虽能带来小幅收益，却拖慢训练、降低优化稳定性，因此选择固定两轮。

循环次数也可以按 token 动态分配。2018 年的 Universal Transformer 已经探索反复应用同一个 block，并通过每个位置上的 learned halting probability 决定何时停止：逐轮累加停止概率，达到阈值后结束，同时设置最大轮数。ByteDance 的 Ouro-Thinking 2.6B 则把包含 48 个 blocks 的网络重复应用四轮，形成 192 次 block applications，并引入 learned exit gate。但这里存在实现层面的区别：公开的 Hugging Face 代码会先计算所有配置轮次，再选择输出，所以拥有动态出口并不等于实际省掉了后续计算。

Mixture-of-Recursions 进一步用 learned router 为不同 token 分配循环深度，路由依据包含上下文信息的 hidden representation，同一个词在不同语境下可以获得不同计算量。论文比较了两种方案：expert-choice routing 在每轮挑选继续处理的 token，退出者不再进入后续轮次；token-choice routing 则在开始时一次性决定各 token 经过几轮。实验显示，这种设计的收益依赖规模与训练预算：最小的 135M 参数模型上，普通 Transformer 更好；较大模型中，动态循环能够追平或超过普通模型，尤其在较低训练预算下，而最高预算下多条曲线已相当接近。此外，相同训练计算量并不代表相同训练 token 数，跳过部分计算也能让模型在同一预算内读到更多数据。因此，循环结构的优势必须结合模型规模、计算分配与数据量判断。它与 RNN 的共同点是复用权重，关键区别则是 RNN 沿序列时间步传递状态，Looped Transformer 在网络深度上重复处理表示，token 之间仍依赖 attention 交换信息。

这套机制与 chain of thought 的关系，需要区分两种增加计算的方式。文本推理模型在最终答案之前生成中间 token，利用这些 token 记录尝试、检查和回退，相当于把推理轨迹作为 scratchpad；循环架构则增加生成每个 token 之前的内部计算。内部计算增强后，模型可能需要更少的外部推理 token，但 Astra 的评测并不显示它在所有 effort levels 上都比 Sol 输出更少，只显示它达到相同准确率时通常更省 token。更少的试错、更少的回退，也能产生这种结果。文章以 GPT-5.6 Luna 与 Sol 作比较：相近表现下，Luna 使用的 token 比 Sol 多约 80%，这本身不足以说明 Sol 的推理更不透明。

真正需要保留的警觉，是 **推理轨迹的可监控性与忠实性并不由长度直接决定**。OpenAI 从 o1 起就向用户隐藏大部分原始推理轨迹，因此这里新增的担忧主要涉及开发者能否通过轨迹监控模型。文本 chain of thought 本来就不保证完整、忠实地反映内部计算；要指控循环架构进一步恶化这一问题，需要证明它更容易生成误导性的推理说明。Astra 的 system card 确实报告，相比 Sol，推理轨迹的 monitorability 有所退步，主要伴随更短、信息更少的轨迹，但没有把这一退步归因于循环结构。Pachocki 也承认 chain-of-thought monitoring 很脆弱，趋势正在恶化，同时强调相关原因并不依赖架构变化。已有结果支持认真研究监控退步，尚不支持把循环、短轨迹和不忠实推理直接串成因果链。

其他研究进一步展示了内部计算可以怎样扩展。2025 年的 Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach，用 800B tokens 训练了一个 3.5B 参数模型，在两个初始 blocks 与两个最终 blocks 之间循环应用四个共享 blocks。每轮都会重新注入初始网络的输出：将其与上一轮 hidden state 拼接，再经 learned linear projection 送入循环部分。训练时随机采样循环次数，使模型能够适应推理阶段选定的计算预算；还可以比较相邻两轮 next-token 分布的 KL-divergence，在变化低于阈值时提前停止。额外循环的价值因任务而异，HellaSwag 在约八轮后趋于饱和，GSM8K 和 HumanEval 则继续受益。这里所谓 latent reasoning 仍能与文本 chain of thought 共存，内部循环并未取消生成文字推理的能力。

内部计算增加，也需要与知识存储容量分开。2025 年 6 月的 Beyond Parameters: Exploring Virtual Logic Depth for Scaling Laws，分别测试记忆与推理：参数量固定时，增加循环对可记忆的信息量影响很小，增加独立参数才明显扩大容量；但重复应用 blocks 可以在不增加参数的情况下改善多步数学推理。这说明共享权重提供的额外计算能够改善已有信息的加工，却不会相应增加模型存储信息的空间。

2026 年 9 月的 SMELT 则尝试控制更严格的成本条件，同时匹配每 token 计算量、非 embedding 参数总量和 KV cache 需求。研究者让 MoE 模型中间一半的 blocks 执行两次，通过缩小 hidden dimension 抵消额外计算，再增加 experts 补回参数容量，并调整 attention heads 以保持缓存规模接近。实验扩展到 54B 非 embedding 参数；拟合出的 scaling curves 估计，在研究覆盖的计算范围内，达到相同 validation loss 所需的训练计算量可减少约 6.8%—18%。这一结果支持循环结构具有计算效率优势，同时也把结论限定在具体架构、评测指标与实验范围内。

2026 年 8 月的 Full-bandwidth Transformer 则研究跨 token 的 latent feedback：通过 learned gate，把前一个 token 的最终 hidden state 与新采样 token 的 embedding 合并，作为下一次前向传播的输入。在 1B base model 的 MATH500 实验中，这种设计能在保持或提高准确率的同时缩短推理轨迹，但 instruction tuning 后，缩短效果消失。研究也没有证明较短轨迹更不忠实，且缺少“通过增加普通 blocks 扩大模型，是否也会出现同样变化”的对照。综合这些结果，循环计算的价值在于重新分配参数、内部计算与外部推理 token；它是否削弱可解释性，最终要由针对忠实性和监控能力的实验回答，不能仅凭轨迹变短作出判断。
