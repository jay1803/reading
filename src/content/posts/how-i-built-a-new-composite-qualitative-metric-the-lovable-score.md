---
title: "How I built a new composite qualitative metric - The Lovable Score"
date: 2026-03-26T08:01:07Z
category: reading
description: "单一定性指标（NPS/CSAT/PMF）各有盲点；把它们加权合并成一个复合分数，才能真正度量用户是否\"爱上\"产品，而非仅仅\"忍受\"产品——这个区别决定了增长能否持久。"
source: "https://www.elenaverna.com/p/how-i-built-a-new-composite-qualitative"
---

## TL;DR
单一定性指标（NPS/CSAT/PMF）各有盲点；把它们加权合并成一个复合分数，才能真正度量用户是否"爱上"产品，而非仅仅"忍受"产品——这个区别决定了增长能否持久。

## 核心洞见
量化指标衡量的是行为（留存、转化、收入），衡量不到用户情感依附。Notion 的 LUV 分数（Love + Use + Value）给了 Elena 关键启示：用复合分数弥补单一指标的失真。Notion 之所以引入 LUV，是因为 NPS 偏低但满意度极高——两者之间的裂缝，只有组合才能显现。

## 具体机制
Elena 为 Lovable 构建的 Lovable Score 由四个分量组成：
- **NPS（35%）**：推荐意愿，附加问题"过去 30 天是否真的推荐了"
- **Sean Ellis PMF score（25%）**：若无法继续使用会有多失望
- **CSAT（20%）**：整体满意度
- **CES（20%）**：完成任务的易用性

所有分量统一换算为 100 分制后加权合并。权重根据各公司业务重点自定——Lovable 侧重口碑传播，故 NPS 和 PMF 比例最高。实施用 PostHog 的 in-app 问卷，注册满 7 天且仍活跃的用户触发。

当前实测值：NPS 60+、30 日真实推荐率 70%+、PMF（极度失望比例）60%、高满意度（7 分）70%、高易用度（7 分）50%，合成分 80+。

## 隐藏限制
Elena 明确提出 PMF 的门槛应比 Sean Ellis 的原始标准更高：40% "极度失望"已不够，应提到 50-60%——因为 AI 和 SaaS 竞争烈度导致 PMF 在持续衰减（她称之为"PMF treadmill"）。此外，Lovable Score 的目标不是拉高分数，而是**防止它下滑**——规模扩张天然会拉低这类情感指标，主动防守比优化更重要。

**值得质疑**：复合分数的权重设计是主观的，缺乏跨公司可比性；不同产品的 CES 采集点（功能级 vs. 整体体验级）对分数影响很大，文章未涉及。

## 复合分数的意义，是给"用户还在意吗"这个问题一个可以月度追踪的答案——而这个问题，单靠北极星指标永远回答不了。
