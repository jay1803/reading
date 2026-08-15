---
title: "AMD 2.0 – New Sense of Urgency | MI450X Chance to Beat Nvidia | Nvidia's New Moat"
date: 2025-05-06T16:03:04Z
category: reading
description: "AMD 的 ROCm 差距本质上是一个永久性追赶陷阱：RCCL 是 NCCL 的 copy-paste fork，NCCL 每次大重构（2.27/2.28 已启动）就迫使 AMD 消耗数千工程小时同步代码，而 NVIDIA 同期在推进下一代特性——AMD 永远落后\"一次重构\"的距离，靠加人根本解不了这个结构性问题。"
source: "https://semianalysis.com/2025/04/23/amd-2-0-new-sense-of-urgency-mi450x-chance-to-beat-nvidia-nvidias-new-moat/"
---

## TL;DR
AMD 的 ROCm 差距本质上是一个永久性追赶陷阱：RCCL 是 NCCL 的 copy-paste fork，NCCL 每次大重构（2.27/2.28 已启动）就迫使 AMD 消耗数千工程小时同步代码，而 NVIDIA 同期在推进下一代特性——AMD 永远落后"一次重构"的距离，靠加人根本解不了这个结构性问题。

## 核心主张拆解
### 文化转型是真实的，但基础依然薄弱
Lisa Su 在 SemiAnalysis 12 月文章发布次日主动约谈，AMD 从此进入"战时模式"。可量化的进展：MI300X 加入 PyTorch CI/CD（此前为零）、benchmark 可复现程度已超 NVIDIA、MLPerf Inference 5.0 附带完整复现指南。但 devrel 团队实质上仍只有 Anush Elangovan 一人，NVIDIA GTC 有 500+ 开发者专场，AMD "Advancing AI" 只是几个产品主旨演讲。

### ROCm 的四个结构性缺口
1. **Python 层缺失**：NVIDIA 的整个 CUDA 栈每一层都有 Python 接口（nvmath-python、cuda.binding、CuTe Python、cuTile、Warp，共五种 Python DSL），一个此前需要 C++ extension + pybind 30 分钟才能完成的 cuBLASLt 自定义 epilogue 调用，现在只需 3 行 Python。ROCm 除 AITER 和 Triton 外几乎空白，无线程级 Python DSL，连规划都未启动。
2. **RCCL 结构性落后**：LL128 协议刚刚支持（Blackwell 发布即三协议齐备），rail-optimized tree 已落后 NCCL 多年；PyTorch SymmetricMemory API 在 NVIDIA 已上线 8 个月，AMD 预计 Q2 2025 才会有初步支持；User Buffer Registration（训练端到端提升 5–20%）AMD 无时间表。
3. **基础设施拖后腿**：SLURM+容器（NVIDIA 一行 `srun --container-name`，AMD 需多层间接调用）、Docker UX、GPU 指标导出器（缺 matrix core activity、CU occupancy）均落后且无具体 roadmap。
4. **推理生态缺位**：disaggregated prefill、Smart Routing、NVMe KV Cache Tiering 全无支持；NVIDIA 已开源 Dynamo 框架将上述能力民主化。

### 资源差距被短视的财务决策放大
AMD 全公司约有 3,000–4,000 张 MI300 实际可用（NVIDIA 仅 EOS 集群就有 15,600 张 H100，另有数十个 64–1,024 规模集群）；更关键的是 AMD 用不足一年的短期突发合同，而非 NVIDIA 式的多年持久部署——每个 GPU 小时都有隐性 P&L 压力，工程师无法做高风险探索性项目。AMD 账上有 50 亿现金，这是选择问题，不是能力问题。

### 薪酬基准错配是人才流失的结构原因
AMD 把 AI 软件工程师的薪酬拿去与 Juniper、Cisco、ARM 对标，而这些公司不以 AI 软件见长。与 NVIDIA PyTorch Lead、NCCL 工程师做同岗对比，NVIDIA 薪酬显著更高。顶级工程师的备选项是 Google TPU 团队或 OpenAI Chip 团队，两者薪酬更好且有更高的成功概率（自身即是最大客户），AMD 的"弱者逆袭"叙事无法靠讲故事弥补薪酬差距。

### 硬件窗口：MI355X 错位竞争，MI450X 是唯一赌注
MI355X 世界大小仍为 8 GPU，无法参与 GB200 NVL72（72 GPU 世界大小）的前沿推理竞争；AMD 自己的定位是对标风冷 HGX B200 NVL8/B300 NVL16。MI450X（IF64/IF128）预计 2026 H2 量产机架级方案，若执行到位可与 VR200 NVL144 正面竞争——这是 AMD 第一次在时间上有机会与 NVIDIA 旗舰方案同台。

## 反驳或薄弱处
- MI450X 竞争力结论完全来自 SemiAnalysis 内部估算，MI355X 架构参数、MI450X 规格与定价 TCO 均在付费墙后，公开版本无法独立验证。
- SemiAnalysis 同时向 AMD/NVIDIA 提供咨询并持有分析模型订阅业务，文章既是报告也是施压工具，利益立场需留意。

## CUDA 护城河是飞轮，不是城墙
400 万 CUDA 外部开发者构成自我强化飞轮：新算法（FlashAttention、Mamba）默认先出 CUDA，ROCm 移植滞后数个季度；bug 发现速度远快于 ROCm，因为 CUDA 生产流量巨大。这个差距无法靠 AMD 内部加人解决——AMD 复现不了外部社区密度，而外部社区密度本身就是 CUDA 领先的结果，是个先有鸡还是先有蛋的问题，打破它需要的时间以年计，不以季度计。
