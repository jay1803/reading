---
title: "Clouded Judgement 8.22.25 - Workflows Are the New Databases"
date: 2025-10-10T00:35:18Z
category: reading
author: "Jamin Ball"
description: "AI Agent 的核心瓶颈不是模型能力，而是执行持久性。Workflow engine（持久化工作流引擎）正在成为 AI 时代的新型数据库——对 AI 应用不是可选组件，而是生存性基础设施。"
source: "https://cloudedjudgement.substack.com/p/clouded-judgement-82225-workflows"
---

## TL;DR
AI Agent 的核心瓶颈不是模型能力，而是执行持久性。Workflow engine（持久化工作流引擎）正在成为 AI 时代的新型数据库——对 AI 应用不是可选组件，而是生存性基础设施。

## 核心主张拆解
AI Agent 本质上无状态、概率性：输出需要被串联、重试、编排、与外部系统对接。以销售外呼 Agent 为例——拉 CRM 数据、信息增强、生成邮件、限流、等待回复、升级至人工——整个流程需要持久性、并发控制与可观测性，无法用单次 API 调用解决。

当下大多数团队在用队列 + cron + 状态机 + 胶水代码拼凑，小规模可用，规模一上去就会断裂。历史平行性是文章核心论证：数据库存储状态，workflow engine 存储执行进度；数据库保障数据持久性，workflow engine 保障执行持久性；数据库标准化数据访问，workflow engine 将标准化编排逻辑。Inngest、Temporal、Trigger.dev 是当前领域的早期玩家。

作者进一步指出："vibe coding"应用（Replit、Loveable、Bolt 等）能从后端集成 durable workflow infrastructure 中受益最多——这是将原型推向生产级别的关键缺口。

## 值得质疑
作者发文后追加说明，澄清本意不是"workflow engine 替代数据库"——原类比推得过远，反映论证本身存在过度类比风险。核心论点高度依赖历史路径类比（Auth0、Stripe、Twilio），没有任何上述早期玩家的实际牵引力或市场规模数据佐证。

## 这个类别注定出现，但谁赢是另一个问题
Workflow engine 先行者（Airflow、Netflix Conductor）此前并未形成大类别。数据库时代产出多个赢家（PostgreSQL、MySQL、Oracle），且部分商品化。AI 浪潮是否足以改变历史格局，还需观察——更值得关注的问题是：谁来定义这个类别的标准，而不只是谁先进入市场。
