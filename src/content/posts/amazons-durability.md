---
title: "Amazon’s Durability"
date: 2026-05-06T08:02:42Z
category: reading
author: "Ben Thompson"
description: "Amazon 的耐久性来自一种反复复用的资本配置模式：先为自己建设高固定成本基础设施，把原本的边际成本资本化，再把这些“内部 primitives”开放给外部客户，用规模扩大回报、降低单位成本，并在十年尺度上形成护城河。ASCS、AWS、Trainium、Bedrock、Leo 卫星网络都属于同一个母题。"
source: "https://stratechery.com/2026/amazons-durability/"
---

## TL;DR
Amazon 的耐久性来自一种反复复用的资本配置模式：先为自己建设高固定成本基础设施，把原本的边际成本资本化，再把这些“内部 primitives”开放给外部客户，用规模扩大回报、降低单位成本，并在十年尺度上形成护城河。ASCS、AWS、Trainium、Bedrock、Leo 卫星网络都属于同一个母题。

## 核心主张拆解
- Amazon Supply Chain Services 是十年前“Amazon logistics 会走 AWS 路线”的兑现：Amazon 先用自营电商需求支撑仓储、货运、最后一公里配送网络，再把这套网络包装成第三方可购买的供应链服务。
- 这个模式的关键不是短期利润率，而是把长期资本开支变成可复用平台。Amazon.com、AWS、物流、卫星服务都遵循“自己是第一个、最好的客户；外部企业是第二阶段增量规模”的路径。
- 物流开放对 FedEx、UPS 构成压力，因为 Amazon 不只是新增一个配送产品，而是在把十多年积累的全链条供给侧能力外部化。

## AWS 与 AI 的反转
- 2023 年 SemiAnalysis 对 AWS 的批评在训练时代成立：AWS 自研 Nitro/EFA 网络、不采用完整 Nvidia 方案、坚持自研芯片，使它在大规模 GPU 训练集群上弱于 Microsoft、Oracle 和 neoclouds。
- 但 AI 计算市场重心从训练转向推理后，AWS 的弱点部分变成优势。推理更容易被拆成单服务器或较松耦合资源，agentic workload 又高度依赖 CPU、内存、网络调度和异构资源利用率，这些正是 Nitro、Graviton、Trainium 和 AWS 抽象层长期优化的方向。
- Jensen Huang 的“tokens-per-watt”逻辑强调昂贵 Nvidia GPU 在电力约束下更赚钱；Ben 的反驳是，Amazon 这类公司可以向上游投资电力、数据中心和自研 silicon，从长期看电力更商品化，逻辑芯片的自研回报空间更大。
- Trainium 的价值不必来自客户主动选择芯片，而可以通过 Bedrock 这样的 PaaS 抽象隐身实现：客户买的是模型/API/managed agents，底层跑在 Trainium、GPU 或 TPU 上并不重要。这复刻了 Graviton 先支撑 RDS 等托管服务、再逐步外溢到客户实例的路径。

## Anthropic 与云竞争格局
- Amazon 能投资 Anthropic，是因为 AWS 已经变成现金机器；基础设施投资前期慢，后期给战略选择权。
- Anthropic 横跨 AWS、Google 等云，对企业是卖点，也削弱了 Microsoft-OpenAI 独占绑定的价值。Microsoft 后来放松 Azure 对 OpenAI API 的独占，部分原因是独占会限制 OpenAI 自身成长。
- Amazon 在 frontier model 接入上可能比 Microsoft 和 Google 更中性：Microsoft 和 Google 的核心业务更直接受 AI 颠覆，需要把大量算力优先投向自家软件、搜索、广告和模型；Amazon 的核心仍扎根于实物商品、物流和数据中心，更容易把芯片资源卖给外部客户。

## 下一组长期赌注：Leo 与无人配送
- Amazon Leo 表面上像 Starlink 的后来者，但按 Amazon 模式看，它可能先服务内部需求，再开放给外部企业。
- 如果未来配送从人力转向无人机，成本结构会从人工边际成本转为无人机资产折旧；这种系统需要广覆盖、可靠、低依赖的通信网络。Amazon 不愿在 AI 芯片上受制于 Nvidia，也未必愿在无人配送通信上受制于 SpaceX。
- Leo 的潜在意义不是“另一个卫星互联网”，而是 Amazon 把物流、计算、通信三类实体基础设施连接成更完整的长期平台。

## 更大的公司类型判断
- Ben 提出一个有用分类：公司与物理世界绑定越深、分发控制越稳，对“必须拥有最强模型”的焦虑越低，但越有动力投资 AI 基础设施。
- Apple 和 Amazon 可以接受不拥有领先模型，因为它们掌握硬件、零售、物流、设备或实体触点；Microsoft 相信企业分发足够强，所以偏向云与应用整合；Google 和 Meta 作为 attention aggregators，用户竞争只隔一次点击，必须重仓自研模型。
- Amazon 的长期优势在于威胁通常来得足够远：它可以提前多年投入基础设施，在市场形态改变后让既有资产突然变得合适。

## 值得质疑
- 文章强调 Amazon 长期主义的复利，但低估了资本密集项目的执行风险：物流、卫星、自研芯片都可能出现回报周期过长、监管压力、组织惯性或技术路线偏差。
- “推理时代利好 AWS”这个判断成立方向清晰，但强度仍取决于 Trainium 生态、开发工具、模型支持和客户迁移摩擦；底层芯片被 PaaS 抽象隐藏，不代表供应商锁定与性能差距会完全消失。
- Leo 与无人机配送的连接很有想象力，但目前更像战略期权，不是已验证业务闭环；把它直接类比 AWS 还需要更多需求、单位经济和监管证据。

## 最后一层意思
Amazon 最可怕的地方不是某个单点业务强，而是它能把今天看似笨重、慢、资本消耗巨大的基础设施，变成十年后别人必须租用的产业地基。AI 时代如果越来越依赖真实世界的电力、物流、数据中心、通信和资本耐心，Amazon 的旧打法反而会重新变得锋利。
