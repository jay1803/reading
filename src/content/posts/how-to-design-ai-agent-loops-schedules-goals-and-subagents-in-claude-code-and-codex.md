---
title: "How to design AI agent loops: schedules, goals, and subagents in Claude Code and Codex"
date: 2026-06-18T08:02:39Z
category: reading
description: "Loop 的本质是让 agent 自己给自己发 prompt，而不是靠人类手指。这没有任何神秘之处——在 AI 之前，heartbeat/cron/hook 早就是标准自动化形式，AI 只是把这些触发方式接上了 LLM。"
source: "https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules"
---

## Loop 不是新范式，就是自动化的 prompt

Loop 的本质是让 agent 自己给自己发 prompt，而不是靠人类手指。这没有任何神秘之处——在 AI 之前，heartbeat/cron/hook 早就是标准自动化形式，AI 只是把这些触发方式接上了 LLM。

现有四种 loop 类型：
- **Heartbeat**：固定间隔（每 5 分钟、每小时）
- **Cron**：在指定时间执行（每天早上 9 点、每周五）
- **Hook**：事件触发（收到邮件、PR 被创建、session 启动）
- **Goal**：给定一个结果，agent 持续执行直到验证成功或卡住——这是 Claude Code 和 Codex 最新内置的一等公民

## Goal loop 是最难写的，也是最容易烧钱的

Goal loop 要求精确定义「验证通过」是什么。成功标准模糊，agent 就会无限循环烧 token，直到自己觉得差不多了才停。
Claire 建议：写 goal prompt 比普通对话 prompt 严苛得多，OpenAI 有专门的 goal 写作指南，甚至可以让 Codex 帮你写自己的 goal。

## 一个有效 loop 需要五件事

Addy Osmani 的 loop engineering 文章中总结得好：
1. **Work trees**：隔离 agent 的工作空间，避免多 agent 互相污染
2. **Skills**：重复性任务的标准做法
3. **Plugins/Connectors**：agent 能访问的工具（GitHub、Slack、Google Calendar 等）
4. **Subagents**：把具体工作分发出去，尤其是验证环节
5. **State tracking**：简单到一个 Markdown to-do 就够，但必须有

## 设计 loop 的正确心智模型：你在招聘员工

「每周五帮我审计日历，看哪里浪费了，发 Slack 告诉我。」——这就是给 EA 设计了一个 cron loop。
「每小时检查新 GitHub issue，有的话立刻写代码提 PR。」——这是给工程师设计了一个 heartbeat loop。
「PR 必须一直改到所有 check 绿了才能结束。」——这是 goal loop。

loop 设计就是在定义 job description，只是执行者换成了 agent。

## 真实 demo 里的两个值得注意的细节

**Claude Code demo（每日老旧 PR 审查）**：agent 被设计为发现需要人工盯的 PR 时，自动 spin off 独立 subagent 去跟进每个 PR 直到 check 绿。主 agent 不需要等——loop 本身在拆解工作。

**Codex demo（每周 skills 识别）**：loop 先找到缺失的 skill，然后为每个 skill 各自启动一个 subagent，并给每个 subagent 一个 goal loop 来验证 skill 在 base branch 上是否真的有效。这是三层嵌套：scheduled loop → subagent → goal loop。

## 两个警告

1. **Loop 很贵**：宽泛的 goal 会让 agent 无休止地烧 token。上线前先监控成本。
2. **Goal prompt 是独立技能**：不同于普通对话 prompt，goal 写作需要极度精准的评估标准，否则产出与消耗完全不成比例。
