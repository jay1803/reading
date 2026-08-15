---
title: "How to Improve at Sensemaking AI?"
date: 2026-05-04T08:02:01Z
category: reading
description: "AI 时代的高质量 sensemaking，关键能力是先把一个自己尚未相信、但影响巨大的替代 frame 搭起来；在软件工程里，“代码生成已经很便宜”这个锚点足以重排 SDLC、测试、规范、架构与团队分工，也解释了为什么“软件暗工厂”阵营和传统务实工程师会彼此听不懂。"
source: "https://commoncog.com/how-to-improve-at-sensemaking-ai/"
---

## TL;DR
AI 时代的高质量 sensemaking，关键能力是先把一个自己尚未相信、但影响巨大的替代 frame 搭起来；在软件工程里，“代码生成已经很便宜”这个锚点足以重排 SDLC、测试、规范、架构与团队分工，也解释了为什么“软件暗工厂”阵营和传统务实工程师会彼此听不懂。

## 核心主张拆解
- 最大风险是 frame fixation：当 AI 变化速度超过旧经验的解释力，人会把不合框架的数据判为噪音、炒作或愚蠢，从而错过职业与商业层面的结构性转向。
- Data-Frame 理论给出的动作是并行 elaboration：保留原有判断，同时刻意补全一个替代 frame，用新锚点、案例碎片和反常信号去测试它是否能解释更多现象。
- 软件工程是文章的样本域：AI 编程反应分裂成三类——拒绝 AI 的 never-AI、坚持传统工程纪律的务实采用者、相信 agent 可生成/审查/交付代码的“software dark factory”实验者。
- 务实采用者的核心 frame 是“代码仍需人类逐行负责，工程基本功没有变”；暗工厂 frame 的核心锚点是“代码生成便宜后，人类可转向 harness、spec、architecture constraints、oracles、tests、linters 与外层需求冲突处理”。
- 这个锚点会连带改写很多旧启发式：可维护性、API 设计、服务边界、测试覆盖、文档粒度、形式化方法、代码可读性与人类介入位置，都可能重新定价。

## 关键证据与案例
- Anthropic 内部报告显示，工程师倾向把可验证、低风险、无聊或 papercut 类型任务交给 Claude；受访者估计 27% 的 Claude-assisted 工作原本不会被做，使用数据中 8.6% 属于 papercut fixes。
- 行业二阶效应已经出现：AI slop PR 让 code review 成为瓶颈；curl 一边拒绝垃圾安全报告，一边接受高质量 AI-augmented findings；Zig 制定严格反 LLM 政策。
- 高可信开发者的 field reports 显示 agentic coding 能扩大修复、重构和功能实现的可行边界；Cloudflare 用约 1000 美元 token 和一周时间复刻 Next.js，冲击了 Vercel 的平台绑定优势。
- Sam Shillace、OpenAI harness engineering、Adam Jacob、Justin Cormack、Marc Brooker 等人的共同点，是他们都在探索“构建生产软件的机器”，并且许多人经历过 cloud / DevOps / serverless 这类旧锚点失效的技术迁移。
- “cattle not pets”是历史校准案例：云让服务器从昂贵、长寿、独特配置的 pets，变成可替换、可编排、可故障注入的 cattle；当时看似疯狂的 Chaos Monkey，后来变成分布式系统韧性实践的一部分。

## 具体方法
- 技法一：补全替代 frame。不要急着相信暗工厂，只要认真问“如果代码很便宜，SDLC 哪些成本结构会改变？”然后寻找能支撑或破坏这个 frame 的新锚点。
- 技法二：读 takes 是为了识别 frame。Gabriella Gonzalez 反对 spec-first coding，代表高可信的务实工程师 frame；Hrishi Olickel 和 Marc Brooker 对 spec-driven development 的实践，则暴露出另一个 frame：spec 能给 agent 长时间自治所需的地图。
- 技法三：收集过往技术迁移碎片。目标是准备 10–20 个校准案例，尤其关注两类：新技术如何创造公司竞争优势，以及社会/行业扩散实际花了多久、卡在什么地方。
- 历史片段能防止线性幻想：汽车出现后马没有立刻消失，二战用马数量仍极高，铁路公司在 Ford 成立二十年后仍雇用大量马；技术扩散通常比口号复杂得多。

## 证据薄弱处
- 暗工厂的证据仍主要来自 field reports、社交媒体、内部实验和早期实践，真实 tradeoff、规模上限、质量事故率、组织迁移成本都还没有被充分量化。
- 软件工程样本未必能直接外推到其他行业；“代码便宜”这一锚点在文字、设计、投研、运营、法律等领域需要替换成各自真正变便宜的生产要素。
- 文章默认“高影响且低成本可调查”的 frame 值得探索，但现实中注意力有限；筛选哪些替代 frame 值得并行 elaboration，本身仍需要判断力。

## 最后一层
真正有用的怀疑，应当同时追问：我在质疑事实，还是在保护一个已经失效的旧锚点？
