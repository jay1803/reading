---
title: "MI300X vs H100 vs H200 Benchmark Part 1: Training – CUDA Moat Still Alive"
date: 2025-01-02T11:00:37Z
category: reading
description: "理论上，MI300X在规格和总拥有成本（TCO）方面应该比Nvidia的H100和H200有巨大优势。"
source: "https://semianalysis.com/2024/12/22/mi300x-vs-h100-vs-h200-benchmark-part-1-training/"
---

理论上，MI300X在规格和总拥有成本（TCO）方面应该比Nvidia的H100和H200有巨大优势。
纸面规格并不代表现实环境中预期的性能。如果AMD能够通过这款内存提供低于市场的性能，它将成为市场上非常强大的竞争对手。

我们发现由于 AMD 公开发布的软件堆栈中的缺乏以及 AMD 的测试的缺乏，MI300X 的纸面优势并未实现。

AMD 的软件体验充满了错误，因此使用 AMD 进行开箱即用的培训是不可能的。我们曾希望 AMD 能够在训练工作负载方面成为 NVIDIA 的强大竞争对手，情况并非如此。
在 AMD 试图尽快填补 CUDA 护城河的同时，NVIDIA 工程师也在加班加点地通过新功能、库和性能更新来加深护城河。

我们希望以任何方式做出贡献，尝试改善 AMD 生态系统。尽管由于我们的错误报告和轮胎踢动，AMD 软件现在好多了，但其公共软件堆栈仍然存在不足。
如果 Lisa Su 和 AMD 领导层加倍投资，重点关注软件和测试堆栈，他们就有机会在培训方面与 Nvidia 竞争。
### Key Findings
1. 判断实际性能的唯一方法是运行基准测试。
2. Nvidia 的开箱即用性能和体验令人惊叹，我们在基准测试期间没有遇到任何 Nvidia 特定的错误。
3. AMD 的开箱即用体验非常难以使用，需要相当大的耐心和努力才能达到可用状态。在我们的大多数基准测试中，AMD PyTorch 的公共 AMD 稳定版本仍然存在问题，我们需要解决方法。
4. 如果没有多个 AMD 工程师团队对我们遇到的 AMD 软件错误进行分类和修复的支持，AMD 的结果将远远低于 Nvidia。
5. 我们与 Sustainable Metal Cloud 合作在 256 H100 上运行非官方 MLPerf Training GPT-3 175B，以测试不同 VBoost 设置的效果
6. 对于 AMD 来说，公开稳定发布的软件的真实世界性能与其纸面销售的 TFLOP/s 相差甚远。 Nvidia 的现实世界性能也低于其营销 TFLOP/s，但相差不大。
7. 与 H100/H200 相比，MI300X 的总拥有成本 (TCO) 较低，但在 AMD 软件的公共稳定版本上，MI300X 的每 TCO 训练性能较差。如果使用 AMD 软件的定制开发版本，情况就会发生变化。
8. 训练性能较弱，MI300X的矩阵乘法微基准测试表明，AMD公开发布的软件在单节点训练吞吐量上仍然落后于Nvidia的H100和H200。
9. MI300X 的性能受到 AMD 软件的阻碍。 BF16开发分支上的AMD MI300X软件具有更好的性能，但尚未合并到AMD内部回购的主分支中。
10. AMD 的训练性能也受到阻碍，因为 MI300X 无法提供强大的横向扩展性能。
11. 许多 AMD AI 库都是 NVIDIA AI 库的分支，导致结果不佳和兼容性问题。
12. AMD 客户倾向于仅使用手工制作的内核进行推理，这意味着它们在非常狭窄的明确定义的用例之外的性能很差，并且不存在快速转移工作负载的灵活性。
### Executive Recommendation to AMD
我们提供了 Lisa Su 和 AMD 领导团队的反馈的详细列表，但在此提供摘要：
1. 为 AMD 工程师提供更多计算和工程资源来修复和改进 AMD 生态系统，相对于 Nvidia 为工程师提供的内部 GPU 盒，他们的内部 GPU 盒非常少。
2. AMD 需要将数千个 MI300X、MI325X 连接到 PyTorch CI/CD 进行自动化测试，以确保不存在 AMD 性能回归和功能性 AMD 错误。
3. AMD 执行团队应亲自集中地内部测试（即“dogfood”）正在向公众发布的产品，而不是专注于测试内部版本。
4. AMD 应与 Meta 合作，尽快让生产LLM训练工作负载在 PyTorch ROCm 上运行，PyTorch ROCm 是 AMD 对 CUDA 的回应，通常情况下，Meta 不使用的 PyTorch 代码路径存在大量错误。
5. ....
### General Matrix Multiply (GEMM) Performance
基于 Transformer 的架构（即 ChatGPT、Llama 等）中的大多数 FLOPS 都用于矩阵乘法，也称为 GEMM。因此， GEMM 性能很好地代表了前沿 Transformer（例如 ChatGPT、Llama、Claude、Grok 等）在硬件上训练的效果。

这意味着，尽管市场上的 BF16 TFLOP/s 高得多，但 MI300X 比 H100 和 H200 慢 14%。 AMD 结果使用了由 AMD 首席工程师手工制作的自定义 docker 映像，但其性能仍然比 Nvidia 的 GPU 慢。

最近，网上流传着一个基准测试，声称在GEMM上，AMD MI300X的性能接近H100。

该基准测试有两个主要问题：它没有正确执行 L2 缓存清除，并且只是简单地采用最大性能，而不是特定形状迭代过程中的中值/平均 TFLOP/s。
### HBM Memory Bandwidth Performance
众所周知，AMD MI300X 具有比 Nvidia H100 和 H200 更好的内存带宽，提供 5.3 TB/s 的带宽，而 H200 为 4.8 TB/s，H100 为 3.35 TB/s。改进的 HBM 内存带宽在推理中非常有用，有时在训练中也很有用。
### Scale Up NVLink/xGMI  Topology
扩展结构对于 GPU 集群极其重要，因为它为前沿模型训练中使用的张量和专家并行性提供了极快的路径。因此，我们进行了基准测试来衡量放大织物的性能。

H100 和 H200 上的纵向扩展结构称为 NVLink，为每个 GPU 提供 450GByte/s 的带宽，并将 8 个 GPU 连接在一起。在 MI300X 上，纵向扩展结构称为 xGMI，理论上它连接 8 个 GPU，每个 GPU 提供 448GByte/s 的带宽。从表面上看，MI300X的纵向扩展网络在性能上与H100/H200极其相似且接近，仅提供了0.5%的纸面带宽。不幸的是，现实情况却大相径庭。

首先，MI300X 的 xGMI 是一种点对点结构，这意味着它实际上并没有在 GPU 对之间提供 448GByte/s 的带宽。相反，每个 GPU 只能以 64GByte/s 的速度相互通信。

由于 Nvidia 的 NVLink 使用交换拓扑，一个 GPU 可以以 450GByte/s 的速度与另一个 GPU 进行通信。
### All Reduce/All to All/Reduce Scatter/All Gather Collectives Overview
### Multi Node RCCL/NCCL Collectives and Scale Out Network Benchmarks
典型的 GPU 集群几乎总是需要比单层网络更多的层，因为单层网络只能支持 128 个 GPU（对于 Broadcom 以太网或 Nvidia Spectrum X 以太网）和 64 个 GPU（对于 H100/H200 InfiniBand）。在这样的多层网络中，部署通常使用 8 轨优化的胖树，其中 8 个 GPU 中的每一个都连接到一个单独的交换机（这种连接称为“轨道”）。在我们的 AI Neocloud 手册和剖析文章中，我们详细解释了铁路优化网络的工作原理。

这与 Nvidia 的 NCCL 团队形成鲜明对比，该团队可以访问 Nvidia 11,000 个 H100 内部 EOS 集群上的研发资源。此外，Nvidia 还拥有集体沟通主题专家 Sylvain Jeaugey。还有许多其他世界级集体专家在 Nvidia 工作，不幸的是，由于薪酬和资源吸引力较低，AMD 在很大程度上未能吸引集体图书馆人才 - 与 Nvidia 的工程师相反，在 Nvidia 中，这种情况并不少见。由于 RSU 价值的升值，工程师每年赚取超过 100 万美元。

为了帮助缓解这些问题，TensorWave 和 SemiAnaanalysis 目前正在与 AMD RCCL 团队合作，以提高集体性能。 TensorWave 慷慨地赞助了 AMD 一个中型集群，以帮助 RCCL 团队拥有更多资源来完成他们的工作。事实上，Tensorwave 在购买了许多 GPU 后还必须提供 AMD GPU 来让他们修复软件，这太疯狂了。
### AMD’s User Experience is Suboptimal and the MI300X is Not Usable Out of the Box
