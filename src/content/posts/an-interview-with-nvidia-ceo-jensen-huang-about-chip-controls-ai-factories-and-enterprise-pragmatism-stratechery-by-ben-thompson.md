---
title: "An Interview with Nvidia CEO Jensen Huang About Chip Controls, AI Factories, and Enterprise Pragmatism – Stratechery by Ben Thompson"
date: 2025-05-20T10:27:27Z
category: reading
author: "Ben Thompson"
description: "Jensen Huang，Nvidia 联合创始人兼 CEO，主导了 Nvidia 从游戏 GPU 公司转型为全球最重要的 AI 算力基础设施公司。[补充：Huang 在 1993 年联合创立 Nvidia，在 AI 热潮爆发前数年已开始布局 GPU 用于通用计算，其对赌式押注最终奠定了 Nvidia 在 AI..."
source: "https://stratechery.com/2025/an-interview-with-nvidia-ceo-jensen-huang-about-chip-controls-ai-factories-and-enterprise-pragmatism/"
---

## 嘉宾背景

Jensen Huang，Nvidia 联合创始人兼 CEO，主导了 Nvidia 从游戏 GPU 公司转型为全球最重要的 AI 算力基础设施公司。[补充：Huang 在 1993 年联合创立 Nvidia，在 AI 热潮爆发前数年已开始布局 GPU 用于通用计算，其对赌式押注最终奠定了 Nvidia 在 AI 时代的垄断地位。] 采访者 Ben Thompson 为 Stratechery 创始人，此次访谈在 Computex 2025 台北主题演讲结束后进行。

## TL;DR

AI 管控的正确姿势不是"阻止对手"，而是"在对手建立生态前抢先占领"——Huang 认为当前的芯片出口限制恰好把中国市场拱手相让给华为，等同于替竞争对手清场；而 AI 真正的颠覆不在模型层，在于用"AI 工厂"把 $1 trillion 的 IT 预算扩展到 $50 trillion 的全球制造与运营预算。

## 扩散规则做对了 10%，还差 90%

Huang 的立场是：对海湾国家开放是进步，但不允许进入中国市场意味着放弃了全球 50% 的 AI 研究者和开发者生态。他的核心逻辑是：AI 是计算平台，平台价值来自装机量驱动开发者正向飞轮——放弃中国市场，就是主动切断这个飞轮在全球最大研究者池中的运转。H20 禁令让 Nvidia 写下 $5.5B 存货损失，放弃 $15B 销售额和约 $3B 税款，而中国 AI 市场年规模约 $50B——"放弃 $50B 市场，相当于放弃整个波音公司，不只是一架飞机"。

DeepSeek 他直接承认是"深度优秀的工作"，认为限制反而激励了中国团队用更少资源做出更好的算法优化。他不认为这令人惊讶："走进 Anthropic 或 OpenAI 的走廊，里面有大量来自中国的世界级 AI 研究者。"

**证据薄弱处**：Huang 对"开放中国市场对美国长期领导力有利"的论证主要来自平台飞轮类比，未触及安全/军事双用途风险的反驳。

## AI 工厂：Nvidia 正在从 IT 预算搬入制造与运营预算

Huang 在 Computex 用"AI 工厂"重新定位整个行业。核心论点：过去 60 年，Nvidia 卖的是工具（进 IT 预算）；接下来，机器人用于实体制造（进 CapEx），AI 数字工人用于运营（进 OpEx）——全球 CapEx+OpEx 约 $50 trillion，IT 预算只有约 $1 trillion。全球劳动力短缺（美国失业率历史低位）意味着企业有强烈意愿为机器人/AI 代理支付 $100K/年，因为这直接扩大产能而非取代就业，最终净效应是 GDP 增长。

## Dynamo：AI 工厂的操作系统

Dynamo 把推理流程拆成 pre-fill（上下文处理，浮点密集）和 decode（token 生成，带宽密集）两段，并在数据中心内动态调度、解耦分配。Huang 的论点是：任何单一芯片架构要么擅长高 token 率（低总吞吐），要么擅长高总吞吐（低交互性），很难同时做好——Dynamo 的软件层让整个数据中心作为一个 GPU 统一运转，在 Pareto 曲线上填满面积而不是只能贴着一条轴。他称之为"AI 工厂的操作系统"。

这也是 GTC（面向超大规模云厂商）与 Computex（面向企业 IT 和 OEM）两场主题演讲风格如此不同的原因：同一套架构，在 GTC 讲反 ASIC 的 Pareto 逻辑，在 Computex 讲"买全套最好，买任何部分也行"的企业实用主义。

## 全栈销售，但边界松散

Huang 的策略是：Nvidia 的每个层次（计算、NVLink 网络、软件）都设计成可被单独采购，这并非妥协，而是平台策略——提高采用率，锁定生态，让客户从局部进入后自然扩展。NVLink Fusion 允许第三方 ASIC 接入，是主动让利而非被动防守。Huang 说："我有偏好，但我们要确保能服务客户想要的任何形式。"

## 留下的那个想法

Huang 谈芯片政策时使用的是外交语言，谈 GeForce 驱动时却真的兴奋起来——Ben Thompson 在现场注意到这一点。Nvidia 的产品飞轮（GeForce → CUDA → 数据中心 → 机器人）本质上是用"让游戏玩家爽"这件消费品来反哺整个算力生态，这个路径是任何纯 AI 芯片创业公司无法复制的护城河，而 Huang 从不单独解释它，因为他觉得这理所应当。
