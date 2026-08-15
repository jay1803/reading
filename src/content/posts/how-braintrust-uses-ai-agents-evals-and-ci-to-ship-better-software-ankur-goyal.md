---
title: "How Braintrust uses AI agents, evals, and CI to ship better software | Ankur Goyal"
date: 2026-06-16T08:02:20Z
category: reading
description: "Ankur Goyal，Braintrust 创始人兼 CEO。Braintrust 是 AI evals 和可观测性平台，客户包括 Notion、Stripe、Vercel、Zapier 等团队。主持人 Claire Voeu 是产品负责人，节目为「How I AI」。本期定位面向 senior/staff e..."
source: "https://www.lennysnewsletter.com/p/how-braintrust-uses-ai-agents-evals"
---

## 嘉宾背景
Ankur Goyal，Braintrust 创始人兼 CEO。Braintrust 是 AI evals 和可观测性平台，客户包括 Notion、Stripe、Vercel、Zapier 等团队。主持人 Claire Voeu 是产品负责人，节目为「How I AI」。本期定位面向 senior/staff engineer、VP of Engineering 和 CTO。

## TL;DR
这场对话最不显然的一条线：rigorous benchmarking 本来是工程领域长期被"合理化"省略的步骤——以前总有借口说没时间跑完所有测试。Ankur 的核心主张是，AI agent 已彻底消除了这个借口，严格性不再是奢侈，而是默认应有。这个逻辑同构地延伸到 evals、CI，形成了一套统一的工程哲学：**没有任何借口不追求严格性**。

## Agent 终结了"没时间做严格基准测试"的借口

Ankur 的团队在做查询优化时，让 Codex 连续运行数天，穷举所有开源列存储格式与执行引擎的组合矩阵——这在人力成本下几乎不可能批准。他举了 Bloom filter 的例子：传统上工程师会跑几个关键 benchmark，然后用理论论证代替剩余测试（"bullshit the rest"）——现在没有借口了。以前团队需要向业务解释为什么要花一年时间封闭做基准测试，现在可以说"让 agent 在后台持续跑，我们照常交付其他东西"，CEO 会很容易同意。

Claire 补充了一个非直觉推断：人类对枯燥但关键的问题注意力会衰减（decaying attention），practical quality 实际上比理论 quality 低得多；agent 的优势不仅在于速度，而在于**持续、无衰减地运行**。

## Agent Line——可以委托的事情比你想的多得多

"Agent line"的判断标准：如果把当前会议/决策/交互的信息等价地给一个 agent，它能解决同样的问题吗？凡满足这个条件的，都在 agent line 以下，应该委托出去。Ankur 不接 12 点后的会议，每天下午进入完整的 maker schedule，同时运行 4-6 个 foreground agent（每个独立 tmux session，对应不同任务分支）。

非直觉推断：agent line 在持续上移，而最优秀的工程师正在通过写 skill、搭集成来主动推高公司内的 agent line，这是高杠杆的工程领导力行为。Codex 是他目前唯一见到会定期反驳自己的模型，这对攻克硬问题至关重要。

## Eval 是现代版 PRD，核心是定义"what good looks like"

传统编程关注 how；机器学习（包括 LLM）将任务从 how 转向 what——regression 里你不定义斜率，你给数据；transformer 里你定义 next token prediction 的 what，让 GPU 找 how。Eval 就是这个逻辑在 AI 产品开发中的体现：你编码"成功是什么样的"，让模型去找 how。Ankur 认为 eval 是现代 PRD——传统 PRD 用 prose 写 user story，eval 将 user story 量化成可打分格式。

他现场 demo：上传一批文档 QA 问题 → 写基础 prompt → 让 GPT-5.4 自动生成 scoring function（包括：代码片段简洁、只用一种语言、避免 em dash 等准则）→ 对整个数据集批量评分。Agent 在这个 playground 环境中的危险性远低于在本机 bash 环境，这本身也是一个重要设计理念：在受控安全空间里允许 agent 充分自主。

## 用 David 的品味构建可扩展的 eval，而不是替代他

Braintrust 的设计师 David 是公司 tastemaker，但无法手动审阅所有 AI 生成内容。Ankur 的做法：先大量跑 evals 做量化提升 → 觉得足够好时才去找 David 做 vibe check → David 往往推翻结论 → 把 David 的反馈转化为新的 scoring criteria → 再次量化。这样每次见 David 都不会重复同一个错误，且 David 的审美覆盖范围持续扩大。

很多人担心"把自己的专业变成系统等于建造自己的替代品"。Ankur 的反驳：这让你的品味影响力扩大了，质量上限更高了——"we're able to get more things to that bar"。

## 投资 CI 是 AI 时代加速工程速度最高杠杆的举措

Ankur 的框架：每个工程师现在都在构建平台，agent 在平台之上完成人工曾手动完成的工作。对 AI 产品团队，首要任务不是 prompt engineering，不是选 agent 框架，不是重写数据库，而是建立一条将真实数据转化为 eval 的 pipeline。CI 就是这个逻辑在软件工程领域的同构体现。当感到受制时，不要继续堆功能，而要"暂停，改善 CI，赚取加速的资格"。他们甚至用 eval 分析 Claude Code 内部使用情况，定位工程师卡住的点和 agent 需要升级权限的节点。

工程产品的制作范式已从"constructing"转向"carving"——太容易造出功能过多的东西，需要大量时间删减。90% 的用户投诉最终以移除导致混乱的功能结束，而不是增加复杂度。

## 收束
Ankur 周六手写了整个 eval 脚本，不用 Copilot，不用 autocomplete——因为 AI 生成的 3000 行垃圾代码让他意识到：对 eval 这个**衡量 AI 质量的最后防线**，你必须首先完全理解问题才能委托给 agent。这是整场"没有借口不追求严格性"哲学里最内嵌的悖论：在你把严格性外包给 agent 之前，你需要对那个严格性本身保持手工级别的理解。
