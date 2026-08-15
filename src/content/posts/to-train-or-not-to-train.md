---
title: "To Train or Not to Train"
date: 2026-04-28T08:02:08Z
category: reading
description: "应用层公司不该把“训练模型”当成技术身份，而应把它当成规模化后的经济性与差异化工具：真正可持续的投资不是抢着替代前沿模型，而是把自有用户轨迹、评测环境和工作流数据沉淀成可反复 post-train 的资产。"
source: "https://www.tanayj.com/p/to-train-or-not-to-train"
---

## TL;DR
应用层公司不该把“训练模型”当成技术身份，而应把它当成规模化后的经济性与差异化工具：真正可持续的投资不是抢着替代前沿模型，而是把自有用户轨迹、评测环境和工作流数据沉淀成可反复 post-train 的资产。

## 核心主张拆解
### 1. “训练自己的模型”其实是一条成本曲线，不是二元选择
文章把训练拆成从 prompt/RAG/harness、微调小模型、在开源基座上 SFT/RL、继续预训练，到从零预训练的连续谱。对应用公司来说，现实重心几乎都在 post-training，而不是从零预训练；Cursor、Intercom、Cognition 等案例都更接近“在强开源基座上做面向任务的强化/微调”。

### 2. 训练成立的第一理由是单位经济性
当调用规模足够大，前沿 API 的延迟和成本会直接吞掉毛利。文章举 Intercom Fin Apex 1.0：成本约为前沿模型的五分之一、响应快约 0.6 秒、解决率更高；在每周约 200 万次对话的规模下，这不是优化细节，而是商业模型的一部分。Cursor 被指出可能受制于外部 API 成本与 Claude Code 的捆绑式 compute 补贴，这说明模型依赖会变成毛利与竞争风险。

### 3. 第二理由是 proprietary traces，而不是“会训练”本身
应用层真正的优势是最接近用户真实任务：Cursor 有补全接受/拒绝数据，Intercom 有海量客服对话，OpenEvidence 有医生查询与引用数据。公开 benchmark 很难覆盖这些垂直场景；自有 traces 可以变成更贴近产品真实工作的 eval 和 post-training 数据。Cursor 的 Cursor-bench 就是把内部真实轨迹转成更有代表性的评测。

### 4. 最低风险的路径是训练系统里的“小而无聊”的模型
文章最强的实操建议是：不要一上来训练核心 reasoning model，而是在 pipeline 中训练 query rewriting、routing、intent classification、retrieval ranking、tool selection、bug detection、context selection 等小模型。Decagon、Sierra、Cognition 都是在“多个专用模型 + 必要时调用前沿模型”的系统里做增量优化。这样即使前沿模型继续升级，小模型的低延迟、低成本、专用数据优势仍可能保留。

### 5. 最大风险是前沿基座迭代会抹平旧训练收益
作者认为 2022-2024 年很多微调收益在 GPT-4、Claude 3.5 等新基座发布后消失；现在模型迭代更快，因为实验室也用模型来写代码、训练和调试下一代模型。若应用公司把大量资源押在“主 reasoning 模型替代前沿模型”上，下一次基座升级可能迅速让这笔投资贬值。

### 6. 基础设施降低了门槛，但没有降低“何时该做”的门槛
Tinker、Prime Intellect Lab、Applied Compute、Mercor/Surge AI/Fleet 等 RL 环境与 post-training 服务，让 10-20 人团队也能开始训练。但作者保留一个强规则：no GPUs before PMF。没有 PMF、没有足够 traces、没有清晰 underserved pipeline 环节时，训练模型只是在提前支付复杂度。

## 值得质疑
- 文章把“post-training 基础设施成熟”视为降低门槛，但没有充分展开长期维护成本：数据清洗、eval 漂移、线上回归、模型监控、事故责任，可能比一次训练更贵。
- Intercom、Cursor 等案例都属于高频 AI-native 使用场景；对低频、弱反馈、数据稀疏的应用公司，proprietary traces 的价值可能远低于文章暗示。
- “训练小模型做 pipeline 中无聊环节”是稳健建议，但它也可能被前沿模型的更低价格、更快 inference、原生工具调用能力继续压缩空间。

## 最后一层
这篇文章真正的结论不是“应用公司要不要训练模型”，而是“应用公司是否已经拥有足够独特的真实任务分布”。如果没有，训练只是昂贵的技术表演；如果有，模型训练只是把产品现场积累的分布优势转化成成本、速度和质量优势的一种工程手段。
