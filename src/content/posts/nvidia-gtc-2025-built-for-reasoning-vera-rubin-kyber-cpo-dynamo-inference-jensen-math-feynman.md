---
title: "NVIDIA GTC 2025 – Built For Reasoning, Vera Rubin, Kyber, CPO, Dynamo Inference, Jensen Math, Feynman"
date: 2025-03-20T20:09:06Z
category: reading
description: "Nvidia 在 GTC 2025 大会上重点介绍了推理能力的重要性，并发布了一系列硬件和软件产品来支持推理能力的发展。Nvidia 认为推理成本的降低将推动 AI 更广泛的应用，并带来需求的增长。Nvidia 还推出了新的 GPU 和系统路线图，包括 Blackwell Ultra、Rubin 和 Rubin..."
source: "https://semianalysis.com/2025/03/19/nvidia-gtc-2025-built-for-reasoning-vera-rubin-kyber-cpo-dynamo-inference-jensen-math-feynman/"
---

## TL;DR
Nvidia 在 GTC 2025 大会上重点介绍了推理能力的重要性，并发布了一系列硬件和软件产品来支持推理能力的发展。Nvidia 认为推理成本的降低将推动 AI 更广泛的应用，并带来需求的增长。Nvidia 还推出了新的 GPU 和系统路线图，包括 Blackwell Ultra、Rubin 和 Rubin Ultra，以及新的 Kyber 机架架构。此外，Nvidia 还发布了 Dynamo 推理引擎，以提高推理效率。
### 主题
#### Reasoning Token Explosion
随着预训练、后训练和推理时间扩展这三种扩展规律的共同作用，AI 模型的发展速度正在加快。
推理成本的降低将推动 AI 在各个领域的广泛应用。
Nvidia 预测，推理模型将消耗大量 token，并且计算需求将大幅增加。

#### Jensen Math Changes Every Year
Jensen Huang 每年都会提出新的计算规则。
今年出现了第三条规则：GPU 数量将按照封装内的 GPU 裸片数量计算，而不是封装数量。
例如，Vera Rubin 架构的机架将被命名为 NVL144，尽管它只有 72 个 GPU 封装。

#### GPU and System Roadmap
Nvidia 发布了新的 GPU 和系统路线图。
- Blackwell Ultra B300：
  - 性能比 B200 提升 50% 以上。
  - 内存容量升级到 288GB，但带宽保持不变。
  - 采用 CoWoS-L 封装技术。
  - 引入 CX-8 NIC，网络速度翻倍。
- Rubin：
  - 采用 TSMC 3nm 工艺。
  - 具有两个计算裸片和两个 I/O 裸片。
  - FP4 算力达到 50 PFLOPs。
  - 采用 Vera CPU。
  - HBM 容量保持 288GB，但升级到 HBM4。
  - NVLink 升级到第 6 代，速度翻倍。
- Rubin Ultra：
  - 具有四个计算裸片和两个 I/O 裸片。
  - FP4 算力达到 100 PFLOPs。
  - HBM 容量达到 1024GB。
  - 采用 Kyber 机架架构。

#### Kyber Rack Architecture
Kyber 机架架构是 Nvidia 推出的新机架架构。
- 将计算托盘旋转 90 度以提高密度。
- 每个机架包含 4 个容器，每个容器包含两层 18 个计算盒。
- NVL576 具有 144 个 GPU（576 个裸片）。
- 使用 PCB 板背板代替铜缆背板。
- 可能会推出 NVL1,152（288 个 GPU 封装）的变体。
- 引入新的 NVSwitch 第 7 代。

#### Blackwell Ultra’s Improved Exponential Hardware Unit
Blackwell Ultra 改进了多功能单元（MUFU），用于计算 softmax。
MUFU 性能比标准 Blackwell 提高 2.5 倍。
这将减少对完美重叠的需求，提高注意力内核的性能。

#### Inference Stack and Dynamo
Nvidia 发布了 Dynamo 推理引擎，以提高推理效率。
Dynamo 具有以下新功能：
- Smart Router：智能路由 token 到预填充和解码 GPU。
- GPU Planner：自动扩展预填充和解码节点。
- Improved NCCL Collective for Inference：降低小消息大小的延迟。
- NIXL – NVIDIA Inference Transfer Engine：抽象数据传输的复杂性。
- NVMe KV-Cache Offload Manager：将 KV-Cache 存储在 NVMe 中，提高预填充效率。
Dynamo 可以显著提高推理速度，即使在现有的 H100 节点上也是如此。

#### AI Total Cost of Ownership – Cost Decline
Nvidia 强调 Blackwell 和 Rubin 将大幅降低 AI 计算成本。
Blackwell 的性能比 Hopper 提升高达 68 倍，成本降低 87%。
Rubin 的性能比 Hopper 提升高达 900 倍，成本降低 99.97%。

#### CPO Insertion
Nvidia 宣布了其首个协同封装光学（CPO）解决方案。
CPO 可以显著降低功耗。
Nvidia 推出了基于 CPO 的 Quantum X-800 3400 和 Spectrum-X 交换机。
CPO 有潜力大幅提高 GPU 的扩展网络基数和聚合带宽。

### 总结
Nvidia 通过发布新的硬件和软件产品，以及强调推理能力的重要性，巩固了其在 AI 领域的领导地位，并致力于降低 AI 计算成本。
