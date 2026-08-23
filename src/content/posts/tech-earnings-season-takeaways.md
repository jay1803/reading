---
title: "Tech Earnings Season Takeaways"
date: 2026-05-12T08:01:38Z
category: reading
author: "Tanay Jaipuria"
description: "这轮 tech earnings 最不显然的信号是：AI 已经从“产品叙事”进入“资本开支、组件供给、CPU/内存结构、广告变现、工程组织、SaaS 定价与商业分发”的全栈重定价阶段。短期赢家不是单点模型应用，而是能同时拿到算力、内存、用户上下文、分发入口和业务闭环的平台。"
source: "https://www.tanayj.com/p/tech-earnings-season-takeaways"
---

## TL;DR
这轮 tech earnings 最不显然的信号是：AI 已经从“产品叙事”进入“资本开支、组件供给、CPU/内存结构、广告变现、工程组织、SaaS 定价与商业分发”的全栈重定价阶段。短期赢家不是单点模型应用，而是能同时拿到算力、内存、用户上下文、分发入口和业务闭环的平台。

## 关键发现
四大 hyperscaler 的 AI capex 已经进入超常规区间：Amazon 约 200B 美元，Microsoft 约 190B，Google 约 180–190B，Meta 约 125–145B，合计超过 700B。更重要的是，Google 已经明确说 2027 capex 会显著高于 2026，Pichai 也承认 Google Cloud 收入本可以更高，但短期被 compute supply 限制。

供给瓶颈正在从“GPU 是否够”扩散到 memory、wafer、substrate。Apple、Meta、Amazon、Intel 都点名 memory/HBM/高带宽 DRAM 成本和供给压力；Meta 的 capex 上调主要来自 memory pricing，Intel 则警告关键组件涨价可能反过来压制需求。

一个被低估的二阶效应是：memory 短缺反而加速企业上云。因为供应商优先满足最大客户，hyperscaler 相比企业自建 on-prem 更容易拿到组件；Amazon 说一些原本拖延的云迁移谈判正在因为供给差距而加速。

## AI 基础设施的叙事变化
AI infra 不再只是 GPU 故事。Amazon、Intel、AMD 都强调 agentic workload 会重新拉高 CPU 重要性：训练约 1 CPU 对 7–8 GPU，推理约 1 对 3–4，而 agentic workload 可能接近 1 CPU 对 1 GPU。AMD 因此把 server CPU TAM 预期上修到 2030 年超过 120B 美元，年复合增长率超过 35%。

这意味着 agentic AI 的真实成本结构可能比“买更多 GPU”更复杂：实时推理、多步编排、代码生成、工具调用和控制平面会把 CPU、memory、networking、storage 都重新拉进瓶颈集合。硬件投资机会也因此从 GPU 单因子扩展到完整 AI data center bill of materials。

## 核心业务的 AI 回报
AI 对广告与推荐系统的回报已经非常具体。Meta 季度广告收入约 56B 美元、同比增长 32%；Google Search ads 约 60B、同比增长 19%，且 search queries 达历史新高，反驳了“AI 会迅速吃掉搜索”的早期叙事。

Google 还提到目前只有约 20% 查询被 monetized，AI mode 和更好的广告推荐可能提高变现覆盖率。Meta 的 ranking 改进让 Instagram Reels 时长提升 10%、Facebook 全球视频时长提升 8%；Lattice/GEM 模型改进让 landing page view ads 转化率提高超过 6%。这类增量直接作用在巨额收入基座上，所以比许多“AI feature launch”更有财务含金量。

## 工程组织的 AI 化
AI coding 已经变成企业最普遍、最容易对外披露的 AI adoption 指标。DoorDash 称超过一半、接近三分之二代码由 AI 编写；HubSpot 说 100% 工程师使用 AI 工具，单工程师更新代码行数增加 73%；Spotify 说每员工 compute 消耗上升，但产出指标接近翻倍。

披露数字本身不完美，因为“AI 生成代码占比”不能直接等于工程质量、产品速度或利润率。但它有两个现实意义：第一，coding agents 是 AI 在企业内最先规模化落地的 killer use case；第二，上市公司正在把它当成向华尔街证明 AI adoption 深度的代理指标。

## SaaS 的防守逻辑
SaaS 面临的核心问题不是立刻的“seat collapse”，而是 agentic workflow 会不会把 seat-based UI 软件压缩成 headless tools、MCP servers 和上下文数据库。Atlassian 说暂时没看到 seat compression，反而看到扩张和交叉销售，Rovo AI credits 月环比增长 20%+；HubSpot 的表述更准确：headless，不是 humanless。

SaaS 厂商的共同防线是“context”。Atlassian 说人类会管理 agent teams，而 context 是避免混乱的锚；HubSpot 说 AI 没有上下文只能产出 output，有上下文才产生 outcome；Datadog 则把策略拆成 “AI for Datadog” 和 “Datadog for AI”，包括 MCP server、AI security agent，并把安全调查从数小时压到约 30 秒。

## Agentic commerce 的现实边界
横向购物 agent 的阻力不主要是技术，而是数据、信任、激励与用户行为。Amazon 认为第三方 horizontal agents 价格和商品信息不准、缺少个性化和购物历史，所以用户更可能从特定零售商自己的 agent 开始；Pinterest 也认为 agentic commerce 的瓶颈在用户行为和生态激励，而非纯技术能力。

但 AI 已经在 commerce 的 top/mid funnel 起作用。Shopify 披露 AI-driven traffic 同比增长 8 倍，来自 AI-powered searches 的订单增长近 13 倍，新买家订单率接近其他渠道 2 倍。更合理的判断是：AI 先改变发现与搜索，再逐步进入交易闭环；“全自动购物代理”不会一夜替代现有零售入口。

**值得质疑**
这些披露来自 earnings call，本身有管理层叙事管理和资本市场定位成分。尤其是 AI-generated code 占比、agentic product traction、AI traffic/order 增长，都需要继续看是否转化为利润率、留存、ARPU、net expansion 和真实 productivity，而不是只停留在 adoption metric。

另一个风险是 capex 与需求之间的时间错配。hyperscaler 同时大幅扩张 2026–2027 投资，短期 demand 确实强，但如果推理价格继续下降、模型效率提升、企业 AI ROI 兑现慢于预期，某些资产可能经历利用率和折旧压力。

## 最后一层
这篇文章真正指向的不是“AI 热度还在”，而是 AI 正在把科技行业重新分层：控制稀缺供给、拥有用户上下文、能把模型改进转成现金流的平台会更强；只有界面、叙事或单点 agent demo 的公司会越来越难证明自己在价值链里的位置。
