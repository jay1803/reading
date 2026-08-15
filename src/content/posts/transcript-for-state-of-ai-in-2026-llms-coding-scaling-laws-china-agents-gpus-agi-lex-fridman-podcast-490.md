---
title: "Transcript for State of AI in 2026: LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI | Lex Fridman Podcast #490"
date: 2026-02-14T20:39:06Z
category: reading
description: "Sebastian Raschka：ML 研究员，著有《Build a Large Language Model from Scratch》与《Build a Reasoning Model from Scratch》，专注 LLM 教育与开源实验，通过\"从头复现已有模型\"方式做研究。"
source: "https://lexfridman.com/ai-sota-2026-transcript/?utm_source=rss&utm_medium=rss&utm_campaign=ai-sota-2026-transcript"
---

## 嘉宾背景
- Sebastian Raschka：ML 研究员，著有《Build a Large Language Model from Scratch》与《Build a Reasoning Model from Scratch》，专注 LLM 教育与开源实验，通过"从头复现已有模型"方式做研究。
- Nathan Lambert：Allen Institute for AI（AI2）post-training 负责人，RLHF 教材作者，RLVR 术语共同发明者，发起 ATOM Project（美国真正开放模型倡议）。[补充：AI2 近期获 NSF 1 亿美元拨款用于开源模型研发。]

## TL;DR
2026 年 AI 进步的核心不在架构革新（transformer 本质未变），而在"如何分配这笔算力"——scaling 已从预训练单腿走路，分裂为预训练、RLVR、推理时扩展三条并行赛道，各有不同的成本曲线与天花板；谁选对了比例，谁就赢得这一轮。

## 没有公司独占技术，竞争的是算力预算与组织文化
Sebastian：2026 年不会有公司拥有其他公司没有的技术——研究员频繁跳槽，思路极速流动；真正的护城河是算力规模与执行文化。Anthropic 以"押注代码 + 低混乱度"建立优势；中国方面，继 DeepSeek 之后，Z.ai（GLM）、MiniMax、Kimi K2 已迎头赶上，DeepSeek 的王冠松动。Nathan 补充：中国公司开源的核心驱动是争夺美国企业市场——美国公司因安全顾虑不愿付费给中国 API，开源权重是绕过这一障碍的唯一路径，且这种策略正在奏效。

## 架构本质未变，收益来自训练流程与系统优化
从 GPT-2 到今天，架构差异仅是 MoE、Multi-Head Latent Attention、Group Query Attention 等旋钮微调——Sebastian 可以从 GPT-2 代码出发，逐步加入这些组件得到任意现代模型。真正带来能力跃升的是：（1）训练流程从"预训练"扩展为预训练→中期训练→后训练三段；（2）FP8/FP4 精度压缩让实验速度大幅提升；（3）数据配比优化——OLMo 3 用比前代更少的 token 训出更好的模型，靠的是筛选而非堆量。预训练数据集规模已达数十万亿 token，Qwen 文档记录到 50 万亿，闭源实验室传言达 100 万亿。

## RLVR 是 2025 最大的后训练突破，scaling 曲线无天花板
Nathan（RLVR 术语共同发明者）：RLVR 的关键在于将 RLHF 里"学出来的偏好奖励模型"替换为数学/代码题的可验证答案——信号直接，优化可以无限延伸，已有 log(compute)→线性 performance 的实证曲线；RLHF 则相反，超过一定量偏好信号就饱和。Sebastian 演示：对 Qwen3 base 仅做 50 步 RLVR，准确率 15%→50%——并非学到新数学，而是解锁了预训练里已储存的推理能力。AI2 的 11 月版本 RL 跑了 5 天，12 月版本多跑了 3.5 周，性能明显提升。Grok 4 被报道预训练与后训练消耗了相当的算力。两人分歧点：Qwen 的基准数据污染问题使很多 RLVR 实验无法被干净复现。

## Scaling 三腿同时有效，但"花在哪"是当下最重要的工程决策
三条 scaling 路径长期均有效：预训练是固定成本，一次投入永久保留；推理时扩展是按查询付费；RL 后训练介于两者之间。小模型 + 更多推理时 compute，往往比直接训练更大基础模型更划算——Claude 4.5 Sonnet 先于 Opus 发布，正是因为较小的模型可以更快完成实验迭代。GPT-5 的路由设计（多数查询走小模型）是这一逻辑的产品化体现。Sebastian：下一阶段关注点将是 RLVR 2.0——不只奖励最终答案正确，还奖励中间推理步骤的质量（Google 的 process reward models 方向）。

## 工具调用是打破幻觉的最现实路径
gpt-oss-120b 是第一个真正以工具调用为一等公民设计的开放权重模型。Sebastian：让模型知道何时"去查"而不是"去记"，是降低幻觉最务实的方向——不是让它记住 1998 年世界杯冠军，而是让它调 Google 工具搜 FIFA 网站。当前障碍是信任：没有用户愿意给一个可访问文件系统的模型开放工具权限；容器化是解决之道，但成本和摩擦尚未消除。

## AGI 定义之争掩盖了一个更务实的问题
Nathan 认为 AI 的"jagged"特性（某些前端代码超人，分布式 ML 代码却很差）使"超级程序员"这一 AGI 里程碑本身概念模糊；实践中，人与模型的分工是人用超强 AI 填补其薄弱环节，而不是 AI 整体接管。Sebastian 强调"独立性"才是真正的分水岭——"帮人建网站"与"AI 自主决定去建网站"是本质不同的两件事。两人均认为 AI2027 报告叙事框架有价值，但过度线性化了一个本质上凌乱的研究过程。

## Adam Project — 开源模型的地缘政治维度
Nathan 的核心论点：开源模型是 AI 研究生态的入口和人才培养渠道；中国公司通过开源权重在全球积累技术影响力；2025 年 7 月出现了四五个 DeepSeek 级别的中国开源模型，而美国方向几乎为零。建议是美国需要投入约 1 亿美元训练一批领先一代的真正开放模型，作为研究基础设施——而非单一机构垄断，必须多方协作形成可复现的生态。White House AI Action Plan 已将"鼓励开源/开放权重 AI"写入专章。

## 留下的那个想法
整场对话最让人停下来的是 Nathan 随口提到的一件事：Cursor 在博客里透露，其 Composer 模型每 90 分钟基于真实用户反馈更新一次权重——这是目前已知最接近"实时持续学习"的商业部署，而它几乎没有引发任何讨论。
