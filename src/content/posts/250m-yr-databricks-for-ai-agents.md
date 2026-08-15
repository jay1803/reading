---
title: "$250m/yr databricks for AI agents"
date: 2026-06-12T08:01:14Z
category: reading
description: "Agent 运行产生的 prompt、tool call、trace、eval 和 cost 数据构成了新一代 clickstream。ClickHouse 的 append-only 列存架构天然适配此类大规模追加写入、低延迟查询负载，存储与查询成本比 Datadog 便宜 10-20x。Anthropic、O..."
source: "https://newsletters.feedbinusercontent.com/813/813e59c3667cc5c0439086d0990bda7a459c1820.html"
---

## AI agent 遥测正在复制 Web clickstream 的历史，ClickHouse 正以成本优势和 bundling 策略拿下这个市场

Agent 运行产生的 prompt、tool call、trace、eval 和 cost 数据构成了新一代 clickstream。ClickHouse 的 append-only 列存架构天然适配此类大规模追加写入、低延迟查询负载，存储与查询成本比 Datadog 便宜 10-20x。Anthropic、OpenAI、Sierra、Lovable 均已是其客户。

## 增长轨迹与估值

2026年5月 ARR 达 $250M，较2025年底 $160M 增长 +256% YoY。一月 Series D（Dragoneer）定价 $15B，约 94x 多倍。主要客户年化营收：Anthropic $47B、OpenAI $25B ARR、Sierra $200M ARR、Lovable $500M。对比参照：Datadog TTM 营收 $3.67B，+30% YoY，市值 $83B，约 23x 多倍。

## Bundling 策略

四年内完成6笔收购，沿 AI 观测链纵向延伸：PeerDB（托管 Postgres，2024）、HyperDX（observability 平台，2025）、LibreChat（AI 对话平台，2025）、Langfuse（LLM observability，2026）。策略逻辑与 Databricks（$5.4B ARR，$134B 市值，26x）收购 Neon 和 AgentBricks 围绕 data lakehouse 做 bundling，以及 Snowflake（$5B TTM，$83B，16.5x）收购 Crunchy Data 和 Observe 如出一辙。

## 隐含判断

94x 估值倍数（对比 Datadog 23x）反映市场押注 AI observability 是比传统 DevOps 监控更快增长的赛道。ClickHouse 的真正护城河是 open-source→cloud 的高效转化漏斗，加上在关键 AI 工具链节点通过 M&A 构筑的垂直整合。持续性取决于 AI agent 部署规模能否维持现有增速。
