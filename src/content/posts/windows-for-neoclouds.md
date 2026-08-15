---
title: "windows for neoclouds"
date: 2026-05-08T08:01:45Z
category: reading
description: "AI agent 时代的存储瓶颈不只来自训练数据变大，而是来自工具调用、生成代码/视频、长期 agent memory 三类“必须长期保存且快速读取”的数据指数叠加；VAST Data 的核心叙事是用 disaggregated shared everything 把共享 flash 存储做成 neocloud..."
source: "https://newsletters.feedbinusercontent.com/162/1629001cd801153109779bdd73e36d299a60ad1a.html"
---

## TL;DR
AI agent 时代的存储瓶颈不只来自训练数据变大，而是来自工具调用、生成代码/视频、长期 agent memory 三类“必须长期保存且快速读取”的数据指数叠加；VAST Data 的核心叙事是用 disaggregated shared everything 把共享 flash 存储做成 neocloud / AI 数据中心的基础操作系统。

## 核心主张拆解
- GPU 集群的真实负载正在从单机/单任务 I/O 变成数十万 GPU 对同一数据池的并发读写：训练数据、checkpoint、embedding、模型输出、agent memory 都需要共享访问。
- VAST 把自己放在 Weka/DDN 的 HPC 高速存储、Pure/Dell/NetApp 的传统企业存储之外：它卖的不是单点性能或可靠性，而是“价格、性能、规模、韧性、易用性”同时突破的共享架构。
- AI agents 放大了存储需求的形态：AI coder 生成代码，AI filmmaker 生成视频，agent 调工具产生过程数据，再叠加长期记忆，导致数据从 CRUD/BI/big data 的结构化系统转向 PDF、音频、视频、多模态文件系统。
- Sacra 给出的需求侧客户图谱很清楚：xAI 这类 AI lab、CoreWeave/Lambda/Crusoe 这类 neocloud、Microsoft/Google 这类 hyperscaler，以及后续需要安全、合规、权限控制的企业 agent 应用。

## 更大意义
- “windows for neoclouds”的重点是抽象层：如果 VAST 能把 GPU、DPU、TPU、高速网络、大 SSD 统一包装成开发者可用的 API 和数据层，它的位置会从存储供应商上移到 AI infrastructure software layer。
- Jensen Huang 的 AI 五层蛋糕里，VAST 想占的是硬件之上的软件基础设施层：向下遮蔽异构硬件复杂度，向上服务模型公司、应用开发者和企业内部 agent。
- 若这个方向成立，neocloud 的竞争不会只看 GPU 供给和融资成本，还会看谁能用更低成本 flash、更高数据缩减率、更简单的共享数据层提高 GPU 利用率。

## 证据薄弱处
- 可见内容主要是 Sacra newsletter、Sacra AI 摘要和一小段 Renen Hallak 访谈；完整访谈被会员墙锁住，因此不能把 CEO 叙事当成已验证事实。
- “flash 价格上涨 8x”“三重数据指数”是强判断，但正文没有展开数据来源、时间区间或基准口径。
- 文章把 AI 存储需求增长与 VAST 份额增长绑定得很紧；真正需要验证的是客户部署规模、单位经济性、与 Weka/DDN/Pure/NetApp 的具体 benchmark，以及这些 workload 是否真的要求 VAST 式共享 flash 架构。

## 收束
如果 agentic workload 真的让 memory、生成物、checkpoint 都变成长期热数据，AI 云的核心约束会从“有没有 GPU”推进到“能不能让海量 GPU 持续、低延迟、低成本地共享同一片数据”。
