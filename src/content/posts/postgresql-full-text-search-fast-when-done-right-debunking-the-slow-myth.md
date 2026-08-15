---
title: "PostgreSQL Full-Text Search: Fast When Done Right (Debunking the Slow Myth)"
date: 2025-04-15T18:52:56Z
category: reading
description: "关于\"PostgreSQL 内置全文搜索太慢\"的结论大多来自两处可验证的配置失误，而非引擎本身的能力上限。作者在 1000 万行数据上复现 Neon 的 benchmark 基线，只修了这两处问题，查询从 41.3 秒降到 0.88 秒——50 倍差距。"
source: "https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth"
---

## TL;DR
关于"PostgreSQL 内置全文搜索太慢"的结论大多来自两处可验证的配置失误，而非引擎本身的能力上限。作者在 1000 万行数据上复现 Neon 的 benchmark 基线，只修了这两处问题，查询从 41.3 秒降到 0.88 秒——50 倍差距。

## 核心洞见
两个失误独立存在，叠加起来放大了基线的劣势：

**失误一：查询时现算 tsvector。** 基线在 `WHERE` 子句里直接写 `to_tsvector('english', message) @@ ...`，强迫数据库对每个扫描行实时执行分词、词干化、向量构造。即便建了 GIN 索引，这个写法也无法有效利用索引（索引建在表达式上，但查询优化器不总能匹配）。正确做法是预计算一个 `message_tsvector tsvector` 列、在写入/更新时填充，查询时直接命中该列。

**失误二：GIN 索引保留默认的 `fastupdate=on`。** 这个选项把索引更新先缓存进 pending list，降低写入延迟，但搜索时必须同时扫描主索引和 pending list，在大规模静态数据集上会拖慢读性能并加剧索引膨胀。Benchmark 场景是读密集的，正确配置是 `fastupdate=off`，让索引更紧凑、搜索路径更干净。

## 具体机制
修正后的标准配置：
- `ALTER TABLE ... ADD COLUMN message_tsvector tsvector;`
- `UPDATE ... SET message_tsvector = to_tsvector('english', message);`
- `CREATE INDEX ... USING GIN (message_tsvector) WITH (fastupdate = off);`
- 查询改为 `WHERE message_tsvector @@ to_tsquery(...)`

作者的测试环境（4 vCPU / 8GB shared_buffers，Docker PG 16）甚至比 Neon 的并行度配置还低，优化后依然做到了 50 倍提升，说明增益主要来自配置修正而非硬件。

## 隐藏限制
文章解决的问题是"找到匹配文档有多快"，对"找到后按相关性排序有多准/快"没有提供方案。`ts_rank` / `ts_rank_cd` 需要对所有命中行计算权重，在命中集合很大时代价可观；更根本的问题是 PostgreSQL 内置函数缺乏 BM25 所需的全局逆文档频率统计。作者推荐的 VectorChord-BM25 用专用索引类型和 `bm25vector` 数据类型解决这个问题，但这已经是不同需求的不同工具——不是内置 FTS 的缺陷，是 ranking 需求本身的复杂度。

## 一句话总结
"PG 全文搜索慢"是把未经优化的基线当成能力上限得出的错误归因；真正的能力分界线在于：match filtering 原生够用，高质量 relevance ranking 才需要专用方案。
