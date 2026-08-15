---
title: "Clickhouse is winning the Observability Wars"
date: 2026-07-02T08:03:15Z
category: reading
description: "作者在十年可观测性工作中用过所有主流平台，结论是：1TB/天时选什么都差不多，5TB/天以上选择就已经决定了三年后的命运。Elasticsearch 会炸 shard，LGTM 要 180+ pods，Datadog 要专职团队管账单；ClickHouse 在 50TB/天的架构图和 1TB/天几乎一样——只是多..."
source: "https://matduggan.com/clickhouse-is-winning-the-observability-wars/"
---

## 规模才是唯一变量，ClickHouse 是唯一不随规模"变形"的后端

作者在十年可观测性工作中用过所有主流平台，结论是：1TB/天时选什么都差不多，5TB/天以上选择就已经决定了三年后的命运。Elasticsearch 会炸 shard，LGTM 要 180+ pods，Datadog 要专职团队管账单；ClickHouse 在 50TB/天的架构图和 1TB/天几乎一样——只是多了几个 shard。

## 为什么列式存储在日志场景碾压行式数据库

ClickHouse 列式存储的效果是：一个 40 字段的日志表，查询只涉及 3 列时，磁盘 I/O 只读那 3 列。行式数据库（Elasticsearch/Postgres）必须读全行。对"几十个字段但每次查询只碰三四个"的可观测性数据，这意味着 800GB vs 40GB 的扫描量差距。

压缩比同理：同一列内的值大量重复（service_name、hostname、相同错误串），ZSTD 可达 10–14x；Elasticsearch 约 2–3x。存储成本的差距不是百分比级别，是整数倍。

日志的数据形态恰好对 ClickHouse 有利：append-only、时间有序、读取模式几乎总是"窄时间范围全字段扫"或"宽时间范围聚合加几个过滤条件"——刚好是列式数据库最擅长的两类查询。

## 各规模层级的成本与运营现实

1TB/天：所有方案粗略可用。Datadog $45–75K/月；ClickHouse $1.5–2.5K/月。差距存在，但还不会让人疼。

5TB/天：Elasticsearch 的 Kafka 变成强制依赖（无 Kafka 则 bulk-reject 风暴会打垮集群），分片数学开始复杂，Elastic 商业许可几乎必买，约 $40–55K/月（不含许可）。LGTM 进入 65+ pods 的微服务模式，哈希环故障是真实运营风险，约 $22–32K/月。Datadog $180–350K/月，还需要一个专职削减账单的管道团队。ClickHouse $7–11K/月，只是加了几个 shard。

50TB/天：Elasticsearch 要同时跑三个集群（日志/指标/APM），约 $95–140K/月加商业许可；LGTM 约 180+ pods，需要 3–5 人专职平台团队；Datadog 可能超 $1M/月，大多数公司在这个量级已是"Datadog APM + 自建 ClickHouse 日志"混合方案。ClickHouse 约 $18–28K/月，架构图和 1TB/天版本的差别只有 shard 数量。

## 真正的代价

ClickHouse 不是没有代价：schema 必须在最早期设计好，ORDER BY 键选错会在两年后开始刺痛；没有原生 PromQL，metrics 需要 Grafana 插件或 chproxy 适配；加 shard 后的数据 rebalance 是手动的（大多数团队预分配或用 clickhouse-copier 迁移规避）；Materialized views 在 5TB/天量级从"推荐"变为"强制"。

权衡的本质：把复杂度前置于架构设计阶段，而不是让它在规模扩张中以运营负担和账单暴增的形式分期偿还。
