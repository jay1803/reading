---
title: "Etched - Building AI Hardware to Make Inference Faster and Cheaper - [Invest Like the Best, EP.480]"
date: 2026-07-01T08:03:04Z
category: reading
description: "Gavin Uberti（CEO）和 Rob Wachen（COO）2023 年从哈佛退学创立。核心命题：所有现有 AI 芯片都在 ChatGPT 之前设计，它们是通用架构对 inference 的改装。Etched 押注 transformer 架构将长期主导，于是放弃通用图编译器，只为 transformer..."
source: "https://colossus.com/episode/the-future-of-ai-hardware/"
---

## Etched 押注的不是"更好的 GPU"，而是一个架构范式转变

Gavin Uberti（CEO）和 Rob Wachen（COO）2023 年从哈佛退学创立。核心命题：所有现有 AI 芯片都在 ChatGPT 之前设计，它们是通用架构对 inference 的改装。Etched 押注 transformer 架构将长期主导，于是放弃通用图编译器，只为 transformer inference 的物理原理做优化。公司已获 $800M 融资，客户需求超 $1B，首款产品（完整机架，含芯片、板卡、冷板、互联、电源）已量产。

## Thermal throttle 才是 GPU 的真正天花板，不是 flops 数量

GPU 真正能用上的 MFU 通常只有 20-50%。原因：Denard scaling——电压降一半，功耗降四分之一；但 GPU 无法大幅压低电压，导致堆 flops → 功耗上升 → 芯片降频 → 有效算力不增反减。

**第一个核心技术赌注：低压 inference。** 比特币矿机运行电压不到 GPU 的 1/4，说明物理上完全可行。Etched 发明了新的供电机制，让芯片运行在不到其他任何 AI 芯片一半的电压下，从根本上解决 thermal 限制后再堆 flops。

## 芯片间延迟 4000ns 是 GPU 集群的隐形内存杀手

Blackwell 点对点延迟约 4000ns，导致 8 卡 TP 并行的 tokens/s/user 提升远低于 8x。

**第二个核心技术赌注：Cluster-Scale Memory。** 完全自研互联栈（第二层以上全定制），延迟压缩超 5x，使整个 scale-up 集群的 SRAM 和 HBM 可以作为单一内存池使用。物理极限约 2-3ns（光速），当前 4000ns 与极限之间还有三个数量级的空间。扩大世界规模时，time per token 线性下降。

## 不做编译器是最反直觉、信息量最高的技术决策

其他 AI 芯片公司默认路径：构建图编译器，兼容任意 PyTorch/CUDA/ONNX。Etched 的判断：未来产生主要流量的模型不超过 100 个，且全是 transformer 架构。

结论：Kernels-first，直接为物理原理写 kernel primitives，不做通用编译器。前期"开箱不可用"，但算力利用率大幅更高，且顺应 AI 写 kernel 的趋势——他们已经让 Codex 仅凭文档从零跑起完整模型。唯一认同这套哲学的早期支持者：高频交易公司（同样恨编译器，全写自己的 kernel）。数十人从 HFT 加入 Etched。

## 生产 = 产品：40 天上线 vs 竞对 10 个月

芯片回来之前就完成了所有事：700 台 FPGA 跑通完整 inference 栈、把无芯片的机架发到客户数据中心装好网络/CPU/存储、用热模拟芯片预先验证冷板方案、整条生产线就绪。

芯片回来后，从拿到硅到跑通 inference：**40 天**。一家著名 AI 芯片公司同样的过程花了 10 个月。"The best ability is availability."

## 人才哲学：Legends × 天真相乘，不是相加

**Legends**：用"项目型招募"——列出各行业有史以来最难的技术问题，逆向追溯谁真正做了 zero-to-one，然后追求 20 次以上。Brian Leuler（建立 NVIDIA 整个 HGX/DGX 团队，覆盖 80%+ NVIDIA 营收）被说服加入。

**天真**（chips on shoulders put chips in data centers）：高中机器人世界纪录级竞争者，两人团队打败 20 人团队，每三个月重新设计一次机器人。这类人逼着 Legends 打破被经验固化的约束。两类人必须共同工作：一人知道"十亿美元的坑"在哪，另一人根本不知道有坑而敢于跳。

## 为什么 Google/Meta/OpenAI 内部芯片永远不会是最好的芯片

从前沿实验室内部芯片团队跳槽到 Etched 的人给出了最清晰的理由："这个产品对我的公司不是 existential 的。Google 不会因为 TPU 失败而倒闭。"

Etched 的存亡完全取决于这块芯片。这让供应商关系、招募强度、决策速度都不在同一量级。NVIDIA 是最好的 AI 芯片公司，因为它只做芯片。这个规律会延续。

## Rob 的动机：六个月才能确诊，模型一秒钟就知道

16 岁，IV 期骨癌，存活率不到 30%。两年化疗加手术，重新学走路。GPT-4V 发布当天，Rob 找出确诊前拍的背部肿块照片，问 ChatGPT：这是什么？模型立刻回答：可能是肿瘤，立刻做 MRI。当年的诊断花了六个月。他准备去给父母看，收到通知：今天的图片额度用完了，请升级专业版。

这个时间点就是他决定 AI 基础设施必须规模化的那一刻。

## 对未来的物理极限和宏观判断

芯片间互联延迟：4000ns → 光速极限 2-3ns，三个数量级的空间。电压还可以继续下降。集群规模从 NVL72 到未来万卡乃至更大。

更激进的判断：2027 年知识工作中的 agent 数量将超过人类劳动力。推理成本将成为国家生产力的主要变量，衡量单位将从 GDP per capita 变为 agents per megawatt。一万亿美元的单一数据中心"只是时间问题"。
