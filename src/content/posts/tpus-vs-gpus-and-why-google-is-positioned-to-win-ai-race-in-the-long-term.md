---
title: "TPUs vs. GPUs and why Google is positioned to win AI race in the long term"
date: 2025-11-30T20:20:18Z
category: reading
description: "Google 的 TPU 项目不是\"我们也做芯片\"的防守姿态，而是一个已经运行了十年、深度嵌入 Google 全部 AI 产品推理路径的基础设施护城河——掌控 ASIC 的云厂商能把毛利率从 20-35% 重新推回 50%+，目前只有 Google 拥有一个真正成熟可用的 ASIC。"
source: "https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference"
---

## TL;DR
Google 的 TPU 项目不是"我们也做芯片"的防守姿态，而是一个已经运行了十年、深度嵌入 Google 全部 AI 产品推理路径的基础设施护城河——掌控 ASIC 的云厂商能把毛利率从 20-35% 重新推回 50%+，目前只有 Google 拥有一个真正成熟可用的 ASIC。

## 核心发现
- **架构根本不同**：GPU 是通用并行处理器，带缓存、分支预测、线程管理等架构"行李"；TPU 核心是 Systolic Array（脉动阵列），数据一次性载入权重后流经计算单元，无需反复写回内存，从而大幅降低 HBM 读写次数，Operations Per Joule 显著优于 GPU。
- **性能数据**：TPUv7（Ironwood）单芯片 4,614 TFLOPS(BF16) vs. TPUv5p 的 459 TFLOPS，提升 10×；内部员工称 TPUv6 比 GPU（Hopper 代）效率高 60-65%，更早代次也有 40-45%；客户对比显示同等工作负载 v5e pod 的价格远低于 8 张 H100。
- **Jensen 的反应**：OpenAI 疑似租用 Google TPU 后，Jensen Huang 亲自致电 Altman 确认——Nvidia 官方账号甚至主动转发 OpenAI 否认的报道。这种反应本身说明威胁已被视为真实。

## 为什么 TPU 还没赢
- **生态锁定**：AI 工程师深度依赖 CUDA/PyTorch，TPU 主要靠 JAX/TensorFlow；迁移成本不是技术问题，是历史惯性问题。
- **多云困境**：AWS/Azure/GCP 三家都有 Nvidia GPU，TPU 仅限 GCP；数据 egress 成本实际上把客户锁在了"数据在哪就在哪跑"的逻辑里，跨云使用 TPU 不现实。
- **厂商锁定恐惧**：押注 TPU 后若 Google 涨价无处可逃，这是客户不敢全押的主要原因——即便 TPU 性价比实际更高。
- 值得注意的是，inference 场景对 CUDA 依赖远低于 training，TPU 在 inference 渗透的机会窗口比 training 大得多。

## 战略意义
AI 浪潮正将云计算从 50-70% 毛利率行业拉低至 20-35%——Nvidia 75% 的毛利吃掉了大量利润。控制 ASIC 的云厂商能绕开这一宿命。
- Google 不仅设计芯片前端 RTL，连合作方 Broadcom 都不再掌握完整设计细节，且 Google 自持完整软件优化栈；相比之下 AWS Trainium、Azure MAIA 差距显著。
- Google 内部 Gemini 推理全链路已切换到 TPU，对外 GCP 仍销售 Nvidia GPU——自己用最好的算力，同时对外维持 GPU 供应以保市占。
- SemiAnalysis 评估：TPUv7 与 Nvidia Blackwell 不相上下。

## 边缘判断
Google 真正的护城河不是 Gemini 模型，是 TPU 软硬件栈。外部生态不成熟恰好对 Google 有利：内部算力优势不被竞争对手复制，外部客户迁移摩擦也在阻止 Anthos 式的流量外流。Google 可能的下一步不是公开出售 TPU，而是通过 neocloud 合作伙伴有选择地放开——既扩大生态，又不让最优算力彻底商品化。
