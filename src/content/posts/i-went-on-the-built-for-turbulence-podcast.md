---
title: "I went on the Built for Turbulence podcast"
date: 2026-06-03T08:01:13Z
category: reading
description: "Martin Alderson 是英国工程负责人、Catchmetrics 联合创始人，做过 20 年企业软件交付，并在 martinalderson.com 写 AI、软件工程与商业经济交叉分析。主持人 Pascal Finette 强调他的稀缺性在于：既实际用 agents 和 LLMs 构建产品，又能把技术..."
source: "https://martinalderson.com/posts/built-for-turbulence-podcast/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## 嘉宾背景
Martin Alderson 是英国工程负责人、Catchmetrics 联合创始人，做过 20 年企业软件交付，并在 martinalderson.com 写 AI、软件工程与商业经济交叉分析。主持人 Pascal Finette 强调他的稀缺性在于：既实际用 agents 和 LLMs 构建产品，又能把技术变化翻译成市场结构和组织竞争问题。

## TL;DR
这场对话最重要的判断不是“AI 让软件开发更快”，而是软件公司的护城河、企业 IT 安全边界、员工工具权限、模型供应链和组织规模优势正在同时被改写；如果管理层仍把 AI 当成 Copilot 采购和培训项目，就会在真实执行力差距形成前误判风险。

## SaaS 最大风险不是客户重写 CRM，而是成本曲线被小团队打穿
Martin 认为 SaaS 公司有三类暴露：客户用自建工具替代 SaaS、AI-native 竞争者用更低成本重做产品、模型和 agent harness 直接让用户不再需要某些 SaaS。第一类现在还有限，因为 CRM、ERP 这类系统仍有运维、安全、修 bug 的长期负担；更危险的是 5 到 10 人团队带着大量 agents 做出更便宜、更 API-first、更 agentic-first 的竞品。

Figma 例子说明第三类风险：用户并不一定要买一个完整设计软件，可能用 Claude Design、Canva AI 或代码 agent 直接生成 deck、UI、UX。它未必达到专业设计师水准，但足以覆盖大量“没必要请高端设计”的需求。

## “Figma Trap”：SaaS 正在向潜在竞争者支付使用费
Figma 一边把 AI 功能接进产品，一边因为没有基础模型而向 Anthropic 等模型公司买 token；Anthropic 同时又能推出 Claude Design 这种逼近 Figma 使用场景的产品。Martin 把这视为新的平台依赖问题：过去被 Apple Sherlock 只是被平台复制功能，现在 SaaS 公司还在按用户使用量付钱给可能复制自己的供应商。

这个结构会扩散到几乎所有 AI 化 SaaS：越多 AI 功能意味着越依赖 OpenAI、Anthropic、Google 等上游模型；上游越懂客户 workflow，越有能力把下游产品的一部分吃掉。

## AI 代码风险正在反转：未经 AI 审计的人写代码可能更危险
Martin 倾向认为 vibe coding 的安全和可靠性问题是阶段性问题。例子是 Anthropic 的 auto mode：不再让 agent 完全 YOLO，也不让人类机械地点 accept，而是把权限请求交给另一个模型判断是否安全。对他来说，这已经显著提高生产力，因为人类反复批准长命令时也会疲劳和失察。

他的反直觉判断是：行业叙事会从“AI 写的代码不安全”转向“没有经过 AI 审计的人写代码才鲁莽”。随着模型能做 code review、安全审计、自愈 refactor、测试条件生成，风险中心可能不在 AI 生成本身，而在没有把 AI 审查纳入软件运行前流程。

## 非技术人更会 vibe coding，因为他们离业务语境更近
Martin 观察到产品、市场、财务等非工程角色经常能在周末做出真正贴合自己需求的工具，因为他们最懂业务域、利益相关者和“差一点”的细节。传统开发流程里，需求被写成 spec，经过数周或数月交付后才发现不对；agent 让需求方可以用“不是这个，改成那个”的连续迭代逼近真实想法。

关键不只是速度，而是心理成本下降。人不会因为第五次改回第一版而愧疚，也不会担心浪费开发团队时间；这让原本被组织摩擦压掉的实验重新出现。

## Copilot 式采用会制造危险的低估
Martin 认为“全员发 Copilot license + 半天培训”可能是 existential risk，因为糟糕或平庸的工具体验会让管理层得出“AI 没什么用”的错误结论。与此同时，另一类公司正在用 Claude Code、Codex、Cowork 等工具把 spreadsheet 变成 Python 模型、跑 Monte Carlo 分析、重构业务流程。

企业安全策略也面临重写：过去“客服为什么要运行 Python”会被视为入侵信号；未来每个知识员工都可能通过 agent 间接写代码。大企业若只允许低效工具，员工会用个人 Claude Code 订阅在家做工作，既降低合规性，也说明正式工具链已经落后于真实生产力需求。

## 开放权重和本地模型决定未来租金结构
Martin 猜测 OpenAI、Anthropic 的 API 推理可能有 80-90% gross margin，订阅产品则可能接近盈亏平衡或略有利润；但 API 价格依然高到会推动企业把不需要 frontier model 的任务迁到本地或小模型。Qwen、Google 等本地可跑模型的快速进步，让 2026 年很可能出现更多“云端 master agent + 本地模型执行子任务”的组合。

他对行业长期结构的担心在于 open weights 正逐步变得更封闭：Meta 退后，新模型 license 更重，训练前沿模型的资本开支越来越高。最差情形是 3 到 5 家巨头形成 oligopoly，靠模型依赖抽租，同时创新速度下降；但算法效率提升和训练技术突破仍可能压低进入壁垒。

## 最后留下的问题
CEO 该问的不是“我们训练了多少人、买了多少 Copilot license”，而是：如果只用 5 到 10 个优秀的人加 agents 重建整个业务，组织会长什么样，阻碍我们到达那里的东西是什么？
