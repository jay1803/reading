---
title: "Towards Continual Learning"
date: 2026-06-06T08:04:42Z
category: reading
description: "让 AI 系统真正\"在职学习\"有两条路：改权重 vs 改 Token 空间。当下最可行的是 Token 空间——用记忆、Skill 文件和 Meta-Harness 让冻结权重的模型从外部持续变聪明，直到从外部感知不到它没有真正改过权重。"
source: "https://www.tanayj.com/p/towards-continual-learning"
---

## TL;DR

让 AI 系统真正"在职学习"有两条路：改权重 vs 改 Token 空间。当下最可行的是 Token 空间——用记忆、Skill 文件和 Meta-Harness 让冻结权重的模型从外部持续变聪明，直到从外部感知不到它没有真正改过权重。

## 核心主张拆解

人类之所以有用，核心不在于原始智力高，而在于能积累上下文、复盘失败、在反复执行中形成细小改进。现有模型训练后权重冻结，无论执行多少次同一任务都不会变好（除非有 Skill 文件和记忆机制）。

解决连续学习有两条根本路径：

**权重空间（In-Weights）**
- 方案：定期后训练/RL on production traces、测试时训练（TTT）、元学习
- 障碍一：灾难性遗忘——微调新任务会导致旧能力悄然退化，稳定性与可塑性难以兼顾
- 障碍二：治理——一旦知识训入权重就无法"撤销"特定人不该看到的信息；公司级可行，个人粒度的独立权重集在工程上极具挑战
- Cursor 案例是当前最接近生产的实现：每 5 小时将生产流量用作奖励信号更新一次模型，但仍是全用户共享同一权重

**Token 空间（In-Context / Harness）**
- 上下文层：运行时记忆、Skill 文件动态改写、隔夜日志回顾（"dreaming"）；可按公司/团队/个人粒度 scope
- Harness 层：Meta-Harness 循环——编码 Agent 读取历史跑分记录，持续提出新工具/提示/脚手架代码，优化模型外部包裹而不动权重
- 优点：更便宜、治理粒度细、回滚成本低
- 缺点：效果依赖正确检索存储在记忆/Skill 文件里的信息，检索失败则学习失效

## 公司图谱

| 方向 | 代表公司 | 核心做法 |
|---|---|---|
| 权重层新架构 | Learning Machine、Chronologies、TTT-E2E | 推理时持续更新权重、不遗忘的连续学习 |
| 生产数据微调 | Applied Compute（Specific Intelligence）、Trajectory | 用生产 traces 做 RL/后训练 |
| Token 空间 | LangSmith Engine（Meta-Harness as a Product）、NeoSigma、Letta/Mem0/Pinecone | 提 PR 修 harness、持久记忆跨会话 |

Satya Nadella 的判断：公司 tacit knowledge 最终会以 LoRA 层形式沉淀进权重，成为企业的新型知识产权。

## 值得质疑

文章对 Token 空间的治理优势着墨颇多，但对其核心缺陷——检索失败、上下文窗口限制、记忆压缩失真——几乎没有量化讨论。"从外部感知不到差别"的预测缺乏具体时间窗口和评估指标。

## 收束

短期内 Token 空间主导是最可能的路：冻结权重 + 越来越聪明的外部包装，按公司和个人 scope。让公司 know-how 真正沉淀进权重（LoRA 层），可能需要一次更大的突破——各大前沿实验室正在押注这个方向。
