---
title: "Dust: Pretraining Transformers Without Backpropagation"
date: 2026-10-16T03:55:36Z
category: reading
description: "Dust 证明 Transformer 语言模型可以完全不做反向传播,仅靠前向扰动完成从零预训练,部分实验中甚至以更多计算换得低于 backprop 的损失,但尚未达到实用的计算效率。"
source: "https://qlabs.sh/research/dust"
author: "E-Reverance"
---

Dust 表明，Transformer 语言模型可以完全不做反向传播、仅靠前向扰动完成从零预训练，并在部分实验中以更多计算换得低于 backprop 的损失；它尚未达到实用的计算效率，但显著推进了零阶方法训练语言模型的能力边界。

这项研究的出发点是：backprop 的高效率伴随着可微分性约束，架构、优化器和硬件也围绕它共同演化。作者借用 **The Bitter Lesson** 与 AlphaGo Zero 的经验提出假设：随着计算资源增加，更通用的搜索方法可能突破这些约束，找到梯度下降难以探索的优化路径,甚至支持包含外部程序或多步循环计算的网络。Dust 当前验证的是这种路线能否胜任 Transformer 预训练；更好的泛化、非可微架构训练和复杂循环计算，都仍属于后续研究目标。

Dust 的关键突破是把搜索移到 **activation space**，并让每个 token 都成为一个"虚拟种群成员"。传统 weight-space Evolution Strategies（ES）为不同成员扰动权重，再分别评估前向结果；EGGROLL 用低秩扰动降低了生成成员的成本，却仍然受到逐成员评估的限制。Dust 在每个线性层的输出上，对每个 token 独立加入 Gaussian noise，同一条序列中的数千个 token 因而能够并行提供扰动反馈。单个 token 上的效果相当于该层权重发生了一次低秩扰动，却无需真正构造那份权重。这里的收益也不能简单归结为激活维度更低：长序列的激活张量可能比权重矩阵更大，真正新增的是沿 token 轴并行获取搜索反馈的能力。

把这些反馈转成学习信号，需要解决每次扰动应获得多少奖励。Dust 以同一 token 在多次扰动下的平均损失作为基线，损失下降越多，该次噪声获得的奖励越高；如果扰动能通过 attention 影响后续 token，就把未来的损失下降按衰减系数 γ 纳入奖励。奖励加权的噪声经过多次采样平均，得到该层输出误差的估计，再与前向计算中已经取得的层输入做外积，形成权重更新。backprop 也使用这个外积结构，但它通过 chain rule 求输出误差，Dust 则通过种群估计。Embedding 使用对应 token 行的累加更新；另有每层两个 residual mixing scalars，仍用普通 weight-space ES 训练。增加采样次数能够抵消无固定方向的估计噪声，但每次更新也因此需要大量前向计算。

有限计算下，主要障碍是不同层、不同 token 的扰动相互干扰：某个 token 的损失变化混入了其他扰动的影响。Dust 因此把不同 block 和不同层类型拆到独立的扰动前向中，并缓存干净前向结果，只重算被扰动 block 及其后续部分。Query、key、value、gate 和 value embedding 的扰动对最终 token loss 的影响太弱，便改用 attention 输出的局部反馈：比较扰动引起的输出变化与已估计输出梯度的方向，据此分配奖励。Language modeling head 则直接在缓存 logits 上扰动，每次只重算部分词表的 cross-entropy，以很小的成本获得更大的采样种群。调参结果显示，key、value、gate 和 value embedding 需要接近不衰减的未来奖励，其他层无需未来 token 的奖励。噪声幅度、奖励衰减和各层采样份额，可以通过短程训练搜索，也可以先用与 backprop 梯度的 cosine similarity 筛选候选，再由训练效果决定；后一种做法意味着，训练过程虽不依赖反向传播，部分超参数筛选仍借助了 backprop。

主要实验在 FineWeb 上训练 GPT-style Transformer，使用含 4096 个 token 的 BPE 词表，每批为 8 条、每条 2048 tokens 的序列，只训练一个 epoch；基础模型有 8 层、宽度 512。Dust、backprop 和同架构的 EGGROLL-Transformer 都分别调参，主要采用固定学习率的 momentum SGD，每个实验单元运行三个随机种子，并报告最佳 validation checkpoint 的 test loss。训练预算从 100k 到 20M tokens，Dust 每次更新的采样数从 64 到 16k。这个种群数不包含成本较小的 head 和 attention 内部采样，单次采样也因缓存而略便宜于完整前向；因此，种群大小既不等同于总计算量，也不能被理解为"一次前向就完成一次更新"。

在 100k tokens 预算下，Dust 用几百次采样就能取得低于 backprop 的损失；在 1M tokens 下，需要约一千次采样。训练扩展到 10M 和 20M tokens 后，Dust 在已测种群范围内仍落后于 backprop，但差距随采样增加而缩小。10M tokens 的改善曲线已趋平，拟合极限略高于 backprop；20M tokens 的曲线到 16k 次采样仍在下降，幂律外推的极限为 4.431，95% 区间为 3.89—4.58，低于 backprop 的 4.633。这个结果属于仍在下降曲线上的外推，不能当成已实际训练达到的性能。与 EGGROLL-Transformer 相比，优势更明确：EGGROLL 使用 16k 的种群，仍未达到 Dust 仅用 64 次采样的效果；在 1M、10M 和 20M tokens 下，损失还高出 0.4—0.6。作者据曲线外推，估计 EGGROLL 要追平 Dust 的最低种群结果，需要多出数千至约一万倍的种群；文中所称 10³—10⁴ 倍效率优势也依赖这类外推，并非全部经过对应规模的直接实测。

换用 Adam 后，Dust 的有效性仍然成立。研究在 1M tokens 上重新为三种方法调参，Dust 与 backprop 的损失都改善，EGGROLL 的结果却与其 SGD 结果在每个种群下相差不到 0.01。Dust 随种群增加继续逼近 backprop，其拟合极限为 5.248，95% 区间为 5.17—5.30，低于 backprop 的 5.361；这同样是外推极限。Dust 和 backprop 此处各运行五个种子，EGGROLL 运行三个；由于给 token embedding 分配了额外采样，Dust 的总采样数约为图中标示种群的 1.4 倍。这说明扰动估计能够与现代优化器配合，尚不能证明已有专门适配 Dust 的最优优化方法。

模型变大也没有出现零阶方法通常被预期的效率崩溃。在固定 10M tokens 下，研究比较了 2M、7M、38M 和 243M 参数四种模型。从种群 256 起，模型由 2M 增大到 7M、再到 38M 时，损失持续下降，243M 模型只略逊于 38M；即使在最小种群下，243M 模型也与小约 120 倍的 2M 模型表现接近，在其他种群下则更好。小模型较早饱和，大模型能够继续利用更大的种群：超过 1k 次采样后，38M 与 243M 模型获得的改善约比两个小模型多 30%。不过，模型越大，在相同种群下与自身 backprop 基线的差距仍略有增加；"种群效率更高"也不代表大模型的绝对计算成本更低。结果支持的解释是，过参数化带来的表达能力和搜索空间几何收益，能够在一定范围内抵消维度增加造成的估计方差。

梯度方向的测量进一步说明了这种方法为何能学习。研究在由 backprop 训练至 10M、100M 和 1B tokens 的 checkpoint 上，比较 Dust 估计与真实 backprop 梯度的 cosine similarity，采样规模从 64 扩大到 128k。所有层类型的方向一致性都随种群增加而改善，并能由一个两参数饱和模型较好拟合，各层类型拟合误差 RMSE 均低于 0.06；在大种群下，多数层的对齐程度也没有随 checkpoint 的训练 token 数增加而明显恶化。相同前向计算预算下，EGGROLL 到 128k 种群时，除 head 外各层类型的 cosine similarity 仍低于 0.05。这里的 1B tokens 指梯度测量所用 checkpoint 的训练规模，不能据此声称 Dust 已完成 1B-token 预训练；这些测量支持更大训练规模下仍有可用学习信号，却尚未证明追平 backprop 所需的种群会停止增长。

Dust 延续了早期 node perturbation 的思路，区别在于把逐 token 奖励、虚拟种群和 attention 局部反馈组合起来，直接检验从零学习语言表征的能力。MeZO、亿级参数 ES 微调以及 Neural Thickets 等工作主要搜索预训练模型附近的有效解，Dust 面对的是尚未形成这些表征的初始化网络。它已经展示：不依赖端到端 chain rule，也能获得接近 backprop、且可能通向不同优化轨迹的更新方向；但这些轨迹偶尔取得更低损失，究竟是否来自对高阶曲率或更平坦区域的探索，机制仍未确定。实际替代 backprop 还需要数量级的计算效率改善，非可微架构和多步循环网络上的优势也尚待实验。Dust 最重要的进展，是把"更多搜索能否替代精确反向求导"推进为一个可测量、可扩展、同时具有明确成本边界的预训练问题。
