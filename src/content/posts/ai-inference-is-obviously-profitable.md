---
title: "AI inference is obviously profitable"
date: 2026-06-27T08:04:38Z
category: reading
author: "Sean Goedecke"
description: "\"AI 推理不赚钱、靠烧投资人的钱撑着\"是错的。推理层面的毛利率是 70-80%，问题在于 OpenAI、Anthropic 把推理利润拿去补贴天价训练成本和人才竞争——亏的是公司，不是推理本身。"
source: "https://seangoedecke.com/ai-inference-is-obviously-profitable/"
---

### 推理本身盈利，亏损来自训练军备竞赛

"AI 推理不赚钱、靠烧投资人的钱撑着"是错的。推理层面的毛利率是 70-80%，问题在于 OpenAI、Anthropic 把推理利润拿去补贴天价训练成本和人才竞争——亏的是公司，不是推理本身。

### 成本测算：每百万 token 约 $1

4 块 A100（400W/块）运行未量化 70B 稠密模型，产出约 200 万 tokens/小时。工业电价下，电力成本约 13¢/小时；按每块 $20k、五年折旧算，GPU 摊销约 $1.80/小时。综合约 $1/百万输出 tokens。

GPT-5.4-mini 定价 $4.50/M，Anthropic 前沿模型贵 3-6 倍，70-80% 利润率极度合理。

### 开源模型提供旁证

DeepSeek 公开声称 R1 推理毛利超 80%，且因权重开源、竞争者可自由部署相同模型，无法维持高溢价——市场价格必然逼近真实成本。DeepSeek-V4-Pro 市场均价约 87¢/百万输出 tokens，可以视为当前成本下界的近似。

### 订阅制不赚钱，API 赚钱

按月订阅（近乎无限推理）大概率不盈利——用 API token 调用 Claude Code 的费用约是订阅价的 10 倍。但这只是定价策略问题，不代表推理本身亏损。已有用户转用 DeepSeek API 做 agentic coding，成本比订阅低得多。

### AI 泡沫破裂不会终结推理业务

就算 OpenAI、Anthropic 倒闭，买下其模型权重的任何实体都能继续以盈利方式卖推理服务——不需要训练，只需要跑推理。推理业务的存续不依赖训练融资泡沫。
