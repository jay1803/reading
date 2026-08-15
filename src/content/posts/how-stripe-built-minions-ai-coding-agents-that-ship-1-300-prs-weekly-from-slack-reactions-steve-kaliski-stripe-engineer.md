---
title: "How Stripe built “minions”—AI coding agents that ship 1,300 PRs weekly from Slack reactions | Steve Kaliski (Stripe engineer)"
date: 2026-03-26T08:01:39Z
category: reading
description: "Steve Kaliski，Stripe 软件工程师，入职六年半，专注 developer tools 与支付基础设施。他是 Stripe 内部 AI 编程 agent 项目\"minions\"的核心构建者；采访者为 Claravel，产品人，主持\"How I AI\"播客。"
source: "https://www.lennysnewsletter.com/p/how-stripe-built-minionsai-coding"
---

## 嘉宾背景
Steve Kaliski，Stripe 软件工程师，入职六年半，专注 developer tools 与支付基础设施。他是 Stripe 内部 AI 编程 agent 项目"minions"的核心构建者；采访者为 Claravel，产品人，主持"How I AI"播客。

## TL;DR
Stripe 的 minions 每周自主提交 1,300 个 PR——但这个数字背后的真正前提不是 AI 有多强，而是 Stripe 多年来为人类工程师打磨的开发环境有多好：好的 DX 直接决定了 agent 的 one-shot 成功率。

## activation energy 才是瓶颈，不是执行力
Steve 的核心体感：他已不记得上一次"从文本编辑器开始工作"是什么时候。工作的起点是 Slack、Google Doc、Jira ticket——在那里点一个 emoji，minion 就启动了，测试跑完、PR 开好，他再跳进去做最后微调。大公司里"好想法到落地"之间的摩擦力（协作成本、权限边界、沟通层级）在这个模型下趋近于零。

## 好的 developer experience 就是好的 agent experience
Stripe 的 minions 架构：在已登录的云端开发环境（devbox）里创建独立分支，以 Goose（Block 的开源 agent harness，Stripe fork 了一个版本）为执行框架，配上 Stripe 所有内部工具（文档、CI、MCP server、代码搜索）。agent 的 one-shot 成功率高，核心原因是 Stripe 为人类工程师写了大量"如何在这个 codebase 里做 X"的标准路径文档——agent 直接沿这条路走。Steve 引用同事说法：对人类好的 DX，对 agent 同样好；反过来也成立。

## 1,300 个 PR 的代码 review 怎么做得完
Steve 的逻辑：如果写代码本身的时间减少了，工程师可以把精力重新放在 review 上。但更关键的是 CI 基础设施——有完善的测试覆盖、集成测试、蓝绿部署，reviewer 才有信心。他明确说：无论是人写的还是 robot 写的，CI 的置信度要求是一样的。同时他预判：如果写代码成本趋近于零，瓶颈会移动到 review、想法生成、分发，而不是消失。

## 云端并行 >> 本地 worktree
Steve 直接点名：无论 MacBook Pro 多强，跑三四个 git worktree 就开始像飞机起飞，不可持续。云端虚拟环境才能真正解锁多线程 agentic 工程——他可以在地铁上通过手机 Slack 同时启动多个 minion，到办公室时已经跑出结果可以跳进去。他觉得这是目前大型工程团队投资最不足的地方。

## agent 作为经济主体：machine payment protocol
第二个 demo：Claude 被要求规划同事 Jen 的生日派对，并被赋予用 Stripe 的"machine payment protocol"（与 Tempo 共同设计）支付第三方服务的能力。全程 Claude 自主：用 BrowserBase（花几分分钱）打开 Jen 的个人网站获取兴趣，用 Parallel AI 搜纽约场地，用 PostalForm 生成 PDF 邀请函并实际寄出，最后向 Stripe Climate 捐 $1.65 抵消碳排放——总花费约 $5-6。Steve 的核心主张：未来会有一批"主要客户是 agent"的 API-first 业务，不需要 dashboard，不需要 landing page，只需要一个超有用的单一 API。

## 留下的那个想法
Steve 说，他在同时养育两个孩子（4 个月和 2.5 岁）和构建 AI agent，然后意识到自己给 agent 写的 soul.md 文件跟养孩子在做同一件事——"我不知道是哪个在影响哪个，但它们同时在发生。"采访者补了一句："我在真的给我的 agent 写灵魂文件。"
