---
title: "🎙️ How I AI: Quests, token leaderboards, and the elite AI adoption playbook & Notion’s spec-driven development"
date: 2026-05-12T08:01:38Z
category: reading
description: "AI adoption 的关键不是给每个人发工具，而是把“会用 AI”变成一套可见、可激励、可治理的组织操作系统：Sendbird 用任务市场、token 分层和安全模板把非工程团队变成 builder；Notion 则把 spec、CI、云端 agent 和会议自动化重组为新的研发生产线。"
source: "https://www.lennysnewsletter.com/p/how-i-ai-quests-token-leaderboards"
---

## TL;DR
AI adoption 的关键不是给每个人发工具，而是把“会用 AI”变成一套可见、可激励、可治理的组织操作系统：Sendbird 用任务市场、token 分层和安全模板把非工程团队变成 builder；Notion 则把 spec、CI、云端 agent 和会议自动化重组为新的研发生产线。

## 核心洞见
### 组织转型要产品化，而不是培训化
Sendbird 的 “Automators” 把内部自动化需求做成 marketplace：任何人可以发起 quest，标注风险、受益人和节省周数，完成者获得经验值、礼品卡、与高管喝茶或在全员会上展示的机会。重点不是“要求大家用 AI”，而是让 AI 采用本身具备反馈、身份、荣誉和可传播案例。

### 非技术团队真正需要的是安全边界，不只是工具权限
营销团队能在几天内做出带 Stripe、定制设计和 Konami Code 彩蛋的 swag store，原因不是他们突然变成全栈工程师，而是公司预先提供了通过 InfoSec 审核的模板：认证、环境、数据库、安全配置都已封装。非工程团队的瓶颈从“不会写代码”转向“敢不敢上线”，模板把这个风险降到了可管理区间。

### token 用量成为 AI fluency 的组织仪表盘
John Kim 按 token/day 把员工分为 Beginner、Intermediate、Expert、Architect、Catalyst、AI God，AI God 超过 100M tokens/day。这个指标不用于羞辱或绩效惩罚，而是让 manager 看见谁需要 enablement、谁能成为 champion。更激进的是，他关注 token 曲线是否在周末和假期变平滑：如果 AI partner 能 24/7 工作，组织产能就不再完全跟随人的在线时间波动。

### AI-first hiring 抬高的是学习驱动力，不是年限门槛
Sendbird 改写 JD，降低对多年经验的依赖，强调 curiosity、agency、energy。背后的判断是：知识获取成本正在下降，20 分钟就能搭出某个主题的学习中心；稀缺的是愿意自己深入、自己试错、自己把能力转成产出的那类人。

### Notion 的研发重心从“代码是事实”转向“spec 是事实”
Ryan Nystrom 描述的 Notion 工作流里，Markdown spec 放在 repo 中，包含 plain English 功能说明、代码指针和验证步骤。工程师更新 spec，再让 Codex 实现、验证、提交 PR。spec 的版本历史变成 changelog，非技术 stakeholder 也能理解系统意图。这里的关键变化是：AI 更擅长把明确意图编译成代码，所以组织应把意图写得更清楚，而不只是把代码写得更快。

### CI 速度是 AI coding velocity 的硬上限
如果 CI 一小时，agent 每轮迭代就空等一小时；如果 CI 三分钟，同样时间可多跑约 20 倍循环。Notion 正在把 CI 时间压到原来的 25%，因为 agent 不会累、不会睡、可以并行跑 VM，但基础设施慢会直接吞掉这部分优势。人类 DX 投资也自然变成 agent DX 投资：清晰 CLI、文档、验证路径和云端开发环境会同时放大人和 agent。

### 管理者会重新靠近代码
Ryan 管 6 个人但每天写代码，因为 AI 自动生成 standup pre-read：从 Slack、任务、PR、指标、昨天会议 transcript 汇总，团队把 standup 时间用于决策、阻塞和下一步。他还能从 Notion task 或 Slack mention 触发 background agent，20 分钟后拿到带实现、截图、preview URL 的 PR。AI 消掉的是会议准备和信息综合的杂活，反而让 line manager 更有条件回到一线技术判断。

## 隐藏限制
这套打法默认组织已经有较强的安全、模板、CI、内部工具和领导示范能力；缺这些基础时，“让所有人用 AI”很容易变成影子 IT、低质量自动化和 token 消耗竞赛。Sendbird 的 token leaderboard 也需要明确文化语境：如果它滑向绩效监控，原本的激励机制会迅速变成压力系统。

## 值得保留的判断
AI adoption 的成熟形态不是“员工学会几个 prompt”，而是公司把意图表达、权限边界、验证循环、激励系统和内部市场全部重做一遍；谁先把这些基础设施产品化，谁才真正拥有 AI 组织杠杆。
