---
title: "Spec-driven development: The AI engineering workflow at Notion | Ryan Nystrom"
date: 2026-05-12T08:01:38Z
category: reading
description: "Ryan Nystrom 是 Notion 工程师，2024 年 12 月随 Campsite 被 Notion 收购后加入，参与 Notion AI 与 2026 年 2 月发布的 Custom Agents；他同时管理 6-7 人团队并继续写代码。访谈聚焦三件事：Notion AI 如何重塑团队管理、Noti..."
source: "https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering"
---

## 嘉宾背景
Ryan Nystrom 是 Notion 工程师，2024 年 12 月随 Campsite 被 Notion 收购后加入，参与 Notion AI 与 2026 年 2 月发布的 Custom Agents；他同时管理 6-7 人团队并继续写代码。访谈聚焦三件事：Notion AI 如何重塑团队管理、Notion 内部如何把 Codex 接入后台 VM 交付 PR，以及为什么 spec-driven development 正在变成工程组织的新工作流。

## TL;DR
这场访谈最关键的不是“AI 帮工程师写更多代码”，而是工程组织的瓶颈从“人写实现”迁移到“人定义上下文、验证闭环和交付管线”：会议、代码评审、CI、规格文档、后台 VM 全部变成 agent 可执行的工程基础设施。

## 高质量 standup 来自自动上下文，不来自更勤奋的管理者
Ryan 的 Afterburner 项目每天由 Notion AI Custom Agent 自动生成会议 pre-read：读取过去 24 小时 Slack、Notion 任务、PR、Honeycomb CI 指标、昨天会议 transcript，再汇总成决策、进展、bug、风险、开放问题。

这个流程把 standup 从“每个人轮流报流水账”改成“直接讨论需要判断的事情”。它的价值不只是节省约 20 分钟准备时间，而是把安静工程师、零散小胜利、CI 秒级优化等信息自动拉到桌面上，降低由表达风格差异造成的信息偏差。

非直觉点：更频繁的会议本身不是问题；低带宽、低信息密度的会议才是问题。AI 让高频同步重新可行，因为准备成本被压到接近零。

## 管理者重新写代码，是 AI 时代的硬技能回归
Ryan 明确主张 line manager 应该继续写代码，Claire 进一步把范围扩到 Director、VP、CTO、CPO：现在不是只优化 stakeholder management 的阶段，而是重新掌握代码、自动化、模型能力、工具链的阶段。

他的理由很实际：AI 降低了经理重新接触代码的摩擦，会议准备、状态同步、报告整理等管理 toil 被 agent 吃掉后，经理可以把时间还给真实创造。Ryan 描述这是“更放松、更有趣、产出更多”的 win-win-win，而不是传统效率三角里的取舍。

这里隐含的组织判断是：未来优秀技术管理者不是脱离实现的协调者，而是能用 agent 放大团队、理解验证路径、亲自修补系统摩擦的人。

## Boxy 把代码任务从本地 IDE 推到后台 VM
Notion 内部的 Boxy / Software Factory 允许在 Notion task 评论里 @mention Codex，触发后台 VM 安装 Codex 或 Claude Code 执行任务。Ryan 展示的例子是朋友请求“tab block 能否 copy link to tab”：他写了几句话、贴一张截图、列出一个 URL 刷新时切换 tab 的边界条件，Codex 约 20 分钟后返回 PR、preview URL、测试说明和 UI 验证截图。

这个案例的重点不是 demo 很炫，而是工作入口改变了：工程师不需要在本机开环境、复制 prompt、手动跑流程；任务从协作系统直接进入隔离执行环境，并回流为可审查的 PR。

非直觉点：代码评审的情绪成本也下降了。Ryan 可以直接对 Codex 说“我不懂这段，解释给我听”“我觉得不对，修类型错误”，而不必像面对同事那样管理语气、面子和心理负担。

## Spec-driven development 把规格文档从会议材料变成执行入口
Ryan 展示 Notion AI agent harness 重写时的做法：不先写代码，而是先在 repo 里维护 `agent specs` Markdown 文档。他用 Whisper 口述功能想法，让 Codex 学习现有 spec library 后整理成正式 spec；spec 包含行为、代码指针、验证方式，再让 Codex 按 spec 实现。

他认为这可能是软件工程未来形态：spec 成为 feature 的 plain-English source of truth，也成为 changelog。后续修改不是直接改代码，而是更新 spec，让 agent 根据新的规格同步实现。

关键限制也在这里：spec 不能只是产品说明，必须包含足够技术细节和验证路径。Ryan 强调工程师角色会转向系统思考、架构设计和 verification loop 设计；如果 agent 无法验证正确性，第一优先级不是继续写功能，而是先构建让 agent 自测的工具。

## CI 速度变成 agent 产能上限
Ryan 把 CI 速度视为 AI 工程组织的核心基础设施：人类时代，快 CI 意味着更快反馈、更小 PR、更敢迭代；agent 时代，这个效果被放大，因为后台 agent 不会疲劳，但会被一小时 CI 卡住。

如果 CI 三分钟返回，agent swarm 可以持续推进、修复、验证；如果 CI 一小时返回，VM 和 agent 都在空转。Claire 用 Stripe 每周 1,300 个 agent PR 的例子补强这个判断：慢 CI 会直接把 AI coding 的理论产能变成队列拥堵。

结论很硬：想吃到 AI engineering 红利，不能只买 coding agent，还要投资 DevEx、CI、preview 环境、验证 CLI、后台 VM 和权限边界。

## Prompting 的核心是反驳与证据，而不是礼貌请求
Ryan 常在 prompt 里写“我完全不知道自己在做什么，像给 5 岁小孩解释”，尤其面对 CI 这种自己不是专家的领域。他也会故意反推模型：“你错了， defend your argument”，要求它给出有证据的反方理由，而不是顺着用户说“看起来没问题”。

这暴露出一个实际技巧：模型越能长期执行，越需要被要求解释依据、抵抗 sycophancy、在被挑战时保留正确判断。Ryan 偏爱 Codex 的原因也在这里：它不花哨，但适合长任务、后台多开、长时间 grinding 和代码审查。

收束来看，AI 没有让工程管理消失；它把管理和工程都推向更明确的规格、更快的反馈、更可验证的执行系统。
