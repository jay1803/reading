---
title: "3T+ token/day coinbase of the inference economy"
date: 2026-06-03T08:01:13Z
category: reading
description: "OpenRouter 正在从“方便开发者切模型的 API 聚合器”变成 AI 推理经济里的信任中介：当 agent 工作流把推理量放大到聊天机器人的约 7 倍，路由层不再只是价格、延迟、模型选择问题，而是密钥、供应链、安全责任和企业托管能力的集中入口。"
source: "https://newsletters.feedbinusercontent.com/6c6/6c6e756f14de1aaef08e47a553d9446d6c175a47.html"
---

## TL;DR
OpenRouter 正在从“方便开发者切模型的 API 聚合器”变成 AI 推理经济里的信任中介：当 agent 工作流把推理量放大到聊天机器人的约 7 倍，路由层不再只是价格、延迟、模型选择问题，而是密钥、供应链、安全责任和企业托管能力的集中入口。

## 发现
Sacra 估算 OpenRouter 在 2026 年 3 月达到 5000 万美元年化收入，高于 2025 年底的 1900 万美元，YoY 增长 1840%。它的规模指标同样跳得很快：2026 年 2 月还在每日处理 1T tokens，5 月已经超过每日 3T tokens，并覆盖约 800 万开发者。

这轮增长的核心驱动力不是单纯“更多人调 API”，而是 chatbot 到 AI agent 的迁移。agent 需要更多轮推理、更多工具调用、更多上下文路由，单个用户/任务背后的 token 消耗密度显著提高，模型网关因此吃到推理量膨胀的杠杆。

OpenRouter 刚宣布由 CapitalG 领投的 1.13 亿美元 B 轮，估值 13 亿美元。按 Sacra 给出的 5000 万美元 forward revenue，大约是 26x forward revenue multiple。这个估值隐含的判断是：LLM gateway 不是一次性开发者工具，而可能成为长期推理流量入口。

## 竞争格局
模型路由层已经被多类玩家同时夹击。开源/自托管侧有 LiteLLM、Helicone，应用平台侧有 Vercel AI Gateway，通用 API 中间件侧有 Merge Gateway。竞争焦点从“能不能连多个模型”升级为“谁能成为企业可信的托管推理控制面”。

LiteLLM 2026 年 3 月的供应链攻击把安全问题推到前台。文章称该事件影响到 Mercor 等客户，并涉及私有源码、客户数据和下游 secret API keys 外泄。这个事件强化了托管网关的叙事：企业可能愿意把路由、安全、审计、密钥管理交给更可信的集中供应商，而不是自己拼装开源中间层。

## 为什么重要
“Coinbase of inference economy”这个类比的重点不是交易所，而是安全信任品牌。在加密资产里，Coinbase 赢过很多更灵活、更便宜的替代品，因为零售和机构用户把“不被黑、合规、可托管”看得比费率更重。OpenRouter 若能成立类似位置，它卖的就不是 API convenience，而是推理时代的 custody、routing 和 governance。

这也解释了为什么模型层之外还有高价值入口。基础模型公司掌握模型能力，云厂商掌握算力和企业账户，但开发者/企业实际调用时仍需要跨模型选择、供应商冗余、成本控制、故障切换和密钥隔离。网关层如果成为默认调用路径，就能在模型 commoditization 和推理量增长之间抽取中间层价值。

## 值得质疑
这篇可用正文主要是 newsletter 摘要，不是完整 Sacra 付费报告；关键数字来自 Sacra 估算，未展开收入口径、take rate、GMV 与净收入关系、客户集中度、留存或毛利。26x forward revenue 是否合理，取决于 OpenRouter 能否把开发者流量转成企业级安全与治理预算，而不是只停留在高增长但低粘性的 API 中转。

## 最后一层判断
OpenRouter 最值得跟踪的不是 token/day 本身，而是它能否把“多模型调用入口”升级成企业推理安全层；如果能，模型路由会像支付、身份、云安全一样，从边缘工具变成基础设施预算。
