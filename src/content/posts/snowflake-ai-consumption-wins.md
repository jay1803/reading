---
title: "❄️ Snowflake: AI Consumption Wins"
date: 2026-05-30T08:04:01Z
category: reading
author: "Kevin Palmer"
description: "AI 对企业软件的分化不在“谁讲了更多 agent 故事”，而在谁能把 agent 工作量直接转成收入。Salesforce 已经证明 Agentforce 有真实使用量，但还没证明这种使用会弥补核心 SaaS 增长放缓；Snowflake 的消费模型则把 AI 查询、治理和计算需求直接计入产品收入，所以同一个..."
source: "https://www.appeconomyinsights.com/p/snowflake-ai-consumption-wins"
---

## TL;DR
AI 对企业软件的分化不在“谁讲了更多 agent 故事”，而在谁能把 agent 工作量直接转成收入。Salesforce 已经证明 Agentforce 有真实使用量，但还没证明这种使用会弥补核心 SaaS 增长放缓；Snowflake 的消费模型则把 AI 查询、治理和计算需求直接计入产品收入，所以同一个 AI 叙事在两个公司身上给出完全不同的估值反应。

## 核心主张拆解
市场正在重新定价软件商业模式：按席位收费的应用软件需要证明 AI 不会压缩人类 seat expansion；按用量收费的数据/计算平台反而可能随着 agent 工作量上升而扩大收入池。文章用 Salesforce 和 Snowflake 同日财报做对照，核心判断是：AI adoption 本身不是护城河，AI consumption 能否进入清晰收入线才是。

Salesforce 的问题不是 Agentforce 虚，而是整体基座太大、组合太杂、定价太不清。Agentforce ARR 达到 12 亿美元、同比增长 205%，季度新增 ARR 从前两季的 1 亿、2.6 亿升至约 4 亿；但剔除 Informatica 后 organic revenue 只有约 9% 增长，current RPO 常汇增速 13%，低于市场想看到的 15%+ 再加速信号。Marketing、Commerce、Tableau 继续拖累，AI 新产品还没有足够大到改写整体收入曲线。

Salesforce 的披露也变得更“干净”但更难验证。旧的六云拆分被压缩成 Applications 和 Infrastructure & Data 两桶；前者常汇增长 7%，后者常汇增长 23%。这让 Agentforce 嵌入所有应用的叙事更顺，但也削弱了投资者追踪 Marketing Cloud、Tableau、Informatica 贡献与拖累的颗粒度。

Headless 360 是 Salesforce 最关键也最危险的新方向：它允许 Claude Code 等外部 AI agent 访问 Salesforce 应用里的数据，相当于给 agent 提供合规入口。Anthropic reportedly 已是 Salesforce 最大客户之一，Q1 使用量因 Headless 360 增长五倍。但管理层没有说明怎么收费，只说会与客户和伙伴寻找公平 monetization。真正的风险是 value abstraction：Salesforce 从工作界面退化成 agent 背后的数据层。

Snowflake 的财报直接打破了“agent 会绕开数据层”的熊市叙事。产品收入 13.3 亿美元，同比增长 34%，较上季 30% 加速，并比管理层预期高 7 个百分点；全年产品收入指引从 56.6 亿美元上调到 58.4 亿美元，隐含增速从 27% 提到 31%。客户层面，过去 12 个月收入超过 100 万美元的客户本季新增 46 个，接近去年同期 26 个的两倍，NRR 126%，说明增长来自既有客户扩用而非只靠新 logo。

Snowflake 更强的点在于 AI 产品开始访问非 Snowflake 数据。Cortex Code 活跃账户超过 7,100，Snowflake Intelligence 账户环比翻倍；CEO Sridhar Ramaswamy 表示客户正在用这些工具访问 Microsoft、Salesforce、SAP 应用内的数据。这把 Snowflake 从“自己的数据仓库”推向“跨企业系统的受治理 agent 数据层”。

## 关键数据
- Salesforce：营收 111 亿美元，同比增长 13%，剔除 Informatica 后 organic revenue 约 9%；non-GAAP EPS 3.88 美元，同比增长 50%；current RPO 336 亿美元，同比增长 14%，低于 340 亿美元以上共识。
- Salesforce：Agentforce ARR 12 亿美元，同比增长 205%；28.6 万亿 tokens processed，环比增长 152%；3.8 billion Agentic Work Units，环比增长 111%；Data 360 ingest 52 万亿 records。
- Salesforce：宣布 250 亿美元 accelerated share repurchase，用债务加速回购；股本稀释后股数同比下降 10%，但因利息费用上升，下调 operating/free cash flow growth 指引至 4%-5%。
- Snowflake：总营收 13.9 亿美元，同比增长 33%；产品收入 13.3 亿美元，同比增长 34%；non-GAAP operating margin 12%，同比提升 3 个百分点；non-GAAP EPS 0.39 美元。
- Snowflake：全年产品收入指引 58.4 亿美元，同比增长 31%；Q2 产品收入指引 14.15-14.2 亿美元，同比增长约 30%，高于 13.8 亿美元共识。
- Snowflake：RPO 92.1 亿美元，同比增长 38%，但低于 94.3 亿美元共识；文章认为这不是主线，因为消费型业务更看实际用量而非 committed backlog。

## 为什么 Snowflake 更像赢家
Snowflake 的收入函数更贴近 AI 工作量：agent 查询更多数据、执行更多分析、触发更多治理与计算，都会增加 consumption。Salesforce 的收入函数仍要穿过 seat、renewal、bundle、legacy cloud、partner access pricing 等多层结构，AI 使用量和收入之间的传导链更长。

AWS 五年 60 亿美元承诺是 Snowflake 本季的成本与毛利率信号。它换来更深的 Graviton 和 AWS 自研 AI 加速器使用权，目标是在 AI workload 增长时降低 compute cost。管理层仍指引 75% product gross margin，说明 Snowflake 想证明 AI consumption 不必牺牲软件级经济性。

Natoma 收购补上 agent 行动层。Natoma 是企业级 Model Context Protocol 实现；MCP 让 agent 不只读取数据，还能在企业权限、身份和安全框架内采取动作。文章的判断是：能行动的 agent 会比只回答问题的 agent 消耗更多计算，Snowflake 因此把治理边界从数据读取扩展到 agent workflow。

## 薄弱处与待验证点
Snowflake 的 38% 盘后涨幅包含情绪修复。文章承认此前 sentiment 已经很低，单季 beat 和上调指引不等于长期胜局。RPO miss 也值得跟踪，只是短期被 consumption acceleration 掩盖。

Salesforce 不是没有资产。Agentforce ARR、Headless 360 demand、Anthropic 使用增长都说明客户需求存在；关键缺口是 monetization formula 和 cRPO 再加速。如果 Headless 360 能形成清晰 usage pricing，Salesforce 仍可能把“被 agent 抽象掉”的风险转成“向 agent 收过路费”的机会。

## 最后一层判断
这篇文章最有价值的不是看多 Snowflake、看空 Salesforce，而是给 AI 软件股一个更硬的筛选器：不要只看 AI usage 指标有多大，要看 usage 是否绕过人工 seat、进入可计量、可提价、可扩毛利的收入机制。AI 会奖励能把机器工作量货币化的公司，惩罚只能把机器工作量包装成新 dashboard 的公司。
