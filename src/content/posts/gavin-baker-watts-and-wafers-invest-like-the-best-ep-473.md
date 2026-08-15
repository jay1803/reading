---
title: "Gavin Baker - Watts and Wafers - [Invest Like the Best, EP.473]"
date: 2026-05-21T05:49:55Z
category: reading
description: "Gavin Baker 是 Atreides Management 的 founding partner 与 CIO，长期研究科技、半导体、AI 基础设施和资本市场周期。这是他第六次参加 Patrick O'Shaughnessy 的 Invest Like the Best，对话主线是 AI 下一阶段的两个物理..."
source: "https://colossus.com/episode/watts-and-wafers/"
---

## 嘉宾背景
Gavin Baker 是 Atreides Management 的 founding partner 与 CIO，长期研究科技、半导体、AI 基础设施和资本市场周期。这是他第六次参加 Patrick O'Shaughnessy 的 Invest Like the Best，对话主线是 AI 下一阶段的两个物理约束：watts 和 wafers。

## TL;DR
这场对话最不显然的线索是：AI 的核心变量不是“需求会不会爆发”，而是供给约束能否以足够慢、足够纪律化的方式释放。电力短缺可能被资本主义、燃机产能和轨道计算逐步缓解；真正能决定有没有泡沫的，是 TSMC 是否继续控制 wafer 供给，以及前沿模型 token 是否继续保持稀缺和高溢价。

## AI 需求已经像指数，但市场仍在用周期框架误读它
Baker 认为 2026 年 3-4 月的回撤不是基本面破裂，而是一次可以“积累未来 alpha”的错杀：Anthropic 单月新增约 110 亿美元 ARR，相当于 Palantir、Snowflake、Databricks 多年建设出的业务规模之和，这在商业史上没有先例。DeepSeek 事件也类似，表面上是“模型成本下降”，实际很快体现为推理模型更吃 compute、亚洲 GPU 租赁价格上涨、DRAM 走强。对他来说，AI 基本面更强、科技相对估值却接近十年低位，是市场效率失灵的窗口。

OpenAI 与 Anthropic 在他眼里不是同一种资产：Anthropic 的 token 成本和资本效率显著更好，可能烧掉的钱比 OpenAI 少 80% 左右；如果算“unconstrained run-rate revenue”，即在 compute 充足情况下的收入，它的真实销售倍数可能远低于表面估值。Baker 也赞成不把融资估值推到极限，原因是资本密集型竞赛需要长期投资者信任，类似 Elon 对 SpaceX 投资人的“圣约”式纪律。

## Watts 会缓解，但监管和轨道计算会改变地面数据中心的价值曲线
电力短缺在 Baker 看来会被资本主义解决，时间点大概从 2027-2028 年开始改善；真正变得更硬的约束可能是 zoning、审批和政治反弹。轨道计算不是“太空里的五角大楼数据中心”，而是把 Blackwell rack 级别的 compute 作为卫星，用大面积太阳能板、散热器和 Starlink 已在使用的激光链路，把多个 rack 组成虚拟数据中心。

他不认为轨道计算会立刻毁掉地面数据中心，因为训练仍会长期留在地面，人类会消耗所有能拿到的 compute。但如果监管让地面数据中心越来越难建，SpaceX 式可复用发射、太阳同步轨道供电和真空激光互联会让“太空 inference”成为强替代。对电力、冷却和传统数据中心供应链来说，风险是地面产能大扩张刚落地时，市场开始相信 orbital compute 不是科幻。

## Wafers 是泡沫阀门，TSMC 的产能纪律可能比需求更重要
Baker 把 TSMC 看成这轮 AI 周期最关键的泡沫调节器。历史上每个 foundational technology 都倾向于出现泡沫，因为市场正确识别了大技术，但供给最终超过需求；2000 年的严重性来自债务融资和大量闲置光纤。今天的不同是 GPU 几乎 100% 利用，buildout 仍主要由经营现金流支持，但如果 wafer 供给完全放开，Nvidia 理论上可以卖出 2-3 万亿美元 GPU，需求也可能被推入过度建设。

所以他最想盯的是 TSMC 的产能决策：扩得太慢会逼 Intel 或 Samsung 成为真正第二来源，扩得太快会制造泡沫；最理想状态是既保持先进制程领先，又释放足够产能防止客户转向。Elon 的 Terafab 是另一个变量：如果它结合 Intel 的制程知识、半导体设备商 A-team、Elon 对硬件工程人才的吸引力，以及对台日韩工程师的极端招聘设计，就可能成为美国本土制造的一条不同路径。

## 前沿 token 的溢价还在扩大，应用层暂时被挤压
最关键的模型层问题是：经济回报是否继续集中在 frontier tokens。Baker 原本也惊讶于 Gemini 3.1 Pro 从惊艳变成不可忍受的速度，但这反而让他更相信前沿能力的溢价。Google 失去低成本 token 领先后，前沿 Pareto frontier 变成 Anthropic、OpenAI、xAI/Grok 和仍勉强在边界上的 Gemini 竞争。

价格结构也变了：AI 正从 all-you-can-eat 转向 usage-based pricing。普通每月 250-300 美元套餐给用户的是被 rate limit、少输出 token 的版本；真正理解 frontier AI，需要 Claude Code/Codex 级 harness、企业计划和按量付费。这对 OpenAI/Anthropic 的 ARR 极其利好，但也制造了新的不平等：最强 AI 只向付得起钱的人开放。

## 芯片创业要“不同且难”，prefill/decode 拆分会延长 GPU 寿命
Baker 不看好“更好的 GPU”创业，因为 Nvidia、Google、Amazon、AMD 都会看到最早的 TSMC 制程路线，也能快速跟进任何容易复制的 trade-off。新芯片公司的机会必须是不同且难，例如 Cerebras 的 wafer-scale computing；prefill 与 decode 拆分让创业公司能分别针对 memory capacity 和 memory bandwidth 做更极端的架构选择。

这个拆分还会改变 GPU 金融：旧 Hopper、Ampere 可以继续负责 prefill，前面接 Cerebras 或 Groq LPU 这类系统做 decode，GPU 使用寿命可能从市场担心的 1-4 年延到 10-15 年。若融资方相信 compute 资产寿命更长，GPU 私募信贷成本可能下降，从而进一步降低 AI buildout 的资本成本。

## 应用公司必须进入 token path，或者在足够窄的领域先长出数据护城河
Baker 对 AI 应用层偏谨慎：即使算上 Cursor 和 Cognition，AI 已经在应用层净摧毁了数万亿美元价值。应用公司要么在 token path 里，要么在足够垂直、模型公司懒得做但仍能产生 venture outcome 的 niche 里，并且在 frontier labs 进入前形成数据护城河。否则，通用模型一旦覆盖该场景，应用公司会被压扁。

他认为 Cursor、Cognition、Anthropic 早期押注 coding 是正确的，因为 coding 可能是通往 ASI 和“有用 AI”的最短路径。更广泛地看，今天价值增长最快的公司，往往是“每个员工可有效使用 GPU 数量”最高的公司；这意味着组织能力的核心正在从人均软件工具，转向人均可调度 compute。

## 大厂分化和市场定价失真，是这轮交易最复杂的部分
Google 失去 TPU 成本优势，但仍有最大 compute installed base、YouTube 数据、搜索和 GCP；Meta 的绝对位置不如 Google，但 Zuckerberg 把公司转成 AI-first 的速度值得重估；Amazon 依靠 Trainium、Nova 和未来 18 个月零售机器人效率提升保持强位；Microsoft 则选择把 compute 用于自己产品和模型，而不是最大化卖给 OpenAI/Anthropic，短期损失可能很大，但这是为“frontier API 不再开放”的世界下注。

市场内部的 AI 相关资产相关性也在瓦解：2024-2025 年 AI basket 可以整体交易，2026 年 1 月后，scale-up networking、scale-out、DRAM、NAND、HDD、semi-cap equipment 开始分化。Baker 认为 DRAM 中个位数倍数与 semi-cap 四十倍估值不可能同时正确；低质量短缺供应商在牛市里涨最多，但高质量、被错误放进 basket 的公司可能才是更可持续的机会。

## 最后的边缘风险：AI 会提高社会和地缘政治 beta
Baker 极度乐观 AI 的长期福利，例如 AI 已帮助一个罕见病患儿家庭找到可能有效的现有药物并启动公司研发治疗方案。但他也认为 AI 是 event horizon：个人安全、深伪诈骗、政治暴力、AI 领袖被攻击、战场 AI 改变战争节奏，都在提高世界的方差。

他尤其强调 Ukraine 的优势不只是无人机，而是可能拥有美国和以色列之外最好的 battlefield AI；如果美国 AI 优势扩大，会利好美国，但也会让对手感到不稳定。理想结局是新的 Pax Americana，坏结局是更高 beta 的全球冲突。真正的任务不是压制 AI，而是用谦逊处理 Luddite 式担忧，避免最强能力只服务资本和强者。

收束：这集真正值得留下的是一个投资框架：AI 不是单一技术浪潮，而是一组物理瓶颈、资本纪律、组织吸收能力和地缘政治反馈共同组成的动态系统；能看懂需求的人很多，能持续看懂约束释放节奏的人更少。
