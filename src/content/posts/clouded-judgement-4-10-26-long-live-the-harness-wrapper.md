---
title: "Clouded Judgement 4.10.26 - Long Live the Harness (Wrapper?) !"
date: 2026-04-11T08:03:39Z
category: reading
author: "Jamin Ball"
description: "Meta-Harness 这类结果说明，AI 应用里最容易被低估的资产是 harness。它决定模型看见什么、记住什么、何时检索、怎样恢复，同一底模只改这一层就能拉出 6x 的 benchmark 差距，垂直应用因此有机会先靠编排赢，再靠数据走向自有模型。"
source: "https://cloudedjudgement.substack.com/p/clouded-judgement-41026-long-live"
---

## TL;DR
Meta-Harness 这类结果说明，AI 应用里最容易被低估的资产是 harness。它决定模型看见什么、记住什么、何时检索、怎样恢复，同一底模只改这一层就能拉出 6x 的 benchmark 差距，垂直应用因此有机会先靠编排赢，再靠数据走向自有模型。

## 核心洞见
Stanford 用 agent 自动搜索更优 harness，在文本分类上比人工方案高 7.7 分、token 少 4x，在竞赛性 coding benchmark 拿到第一，给数学任务找到的 harness 还能迁移到 5 个未参与搜索的模型。竞争焦点会从底模能力扩展到上下文编排、检索策略、状态管理和错误恢复。
文中隐含的一条应用公司演化路径很清楚：先做出 killer harness，随后把使用过程变成高质量数据，再把数据变成后训练能力，最后才有可能走向预训练。

## 具体机制
论文里最硬的一组数据来自“压缩惩罚”：把历史执行反馈压成摘要，比保留原始 trace 差 15 个中位点。原始 prompts、tool calls、model outputs、state updates 一起保留时，优化器更容易找到有效 harness，省 token 和保性能之间存在直接冲突。
Anthropic 本周推出 Claude Managed Agents，按每个 agent runtime 小时 0.08 美元另加 token 收费，把沙箱执行、上下文管理、容错、权限和长会话一起产品化。平台层开始把“模型 + harness 基础设施”打包出售，切换成本会从模型本身外溢到整套运行环境。

## 隐藏限制
论文证明了编排层的重要性，没有证明通用基准上的 6x 能按同样幅度外推到每个垂直场景。真正难的部分是把行业知识写进检索、状态机、权限边界和错误处理。
Managed Agents 适合买基础设施，差异化 intelligence 仍然更适合留在应用层。越垂直的产品，越需要自己控制关键编排。
同一期 newsletter 给出的 SaaS 估值也说明市场奖励的是经营结果：全行业 EV/NTM 收入中位数 3.0x，Top 5 中位数 16.2x，高增长组 9.9x，中增长组 4.8x，低增长组 2.3x。harness 只有在它真的带来增长、留存或利润率改善时，才会从工程优势变成估值优势。

**值得质疑**
Stanford 论文、Anthropic 发布和应用公司路线图可以拼成一条很顺的产业叙事，但文中的市场倍数数据并不能直接证明 harness 会成为新的估值核心，它只能说明一旦 harness 改善了经营指标，资本市场愿意为结果付钱。

## 留下来的想法
模型会持续替换，harness 更像能沉淀下来的经营资产。谁先把领域工作流写成可迁移、可优化、可计价的 harness，谁就更可能在应用层拿到真实壁垒。
