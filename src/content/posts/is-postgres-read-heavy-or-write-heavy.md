---
title: "Is Postgres read heavy or write heavy?"
date: 2025-10-21T13:23:04Z
category: reading
description: "判断 Postgres 数据库的读写性质是调优的前提：读重 vs 写重决定了索引策略、副本架构、存储配置和 WAL 调优的优先级。读写并不对等——每次写都要走 WAL、更新索引、可能触发 full page write，且写操作必须先将目标页读进内存，因此写的代价远高于读。实际上大多数 Postgres 库是读重..."
source: "https://www.crunchydata.com/blog/is-postgres-read-heavy-or-write-heavy-and-why-should-you-care"
---

## TL;DR
判断 Postgres 数据库的读写性质是调优的前提：读重 vs 写重决定了索引策略、副本架构、存储配置和 WAL 调优的优先级。读写并不对等——每次写都要走 WAL、更新索引、可能触发 full page write，且写操作必须先将目标页读进内存，因此写的代价远高于读。实际上大多数 Postgres 库是读重的，10:1 的读写比才算真正开始走向写重。

## 关键洞察
作者给出一个基于 pg_stat_user_tables + pg_statio_user_tables + pg_class 的 SQL 查询，通过 tuple 写入数乘以页密度（relpages/reltuples）估算写影响的物理页数，再与实际读取的 block 数比较，配合可配置的 ratio_target（默认 5，即读页超过写页 5 倍才算读重）对每张表分类为 Read-Heavy / Write-Heavy / Balanced / Write-Only / Read-Only，按活跃度降序排列。pg_stat_statements 是更粗粒度的补充：按 SELECT vs DML 汇总行数，一行 SQL 给出全库读写行比。

写重调优的瓶颈是 I/O 和事务吞吐：NVMe SSD 提升 IOPS；Postgres 18 的异步 I/O 从根本上改善写路径；裁减非必要索引（每个索引在写时都要同步更新）；调整 fill factor 启用 HOT updates，避免索引页写入；调大 wal_buffers 减少 flush 次数；调整 checkpoint_timeout 和 checkpoint_completion_target 将 I/O 峰值平滑到后台。

读重调优的目标是让热数据留在内存：调大 shared_buffers 和 effective_cache_size；用 EXPLAIN ANALYZE 定位慢 SELECT 并补索引；用读副本将 SELECT 流量从主库分流出去，写压力不变但读吞吐线性扩展。

## 一句话总结
用 pg_stat 查询量化每张表的读写比，然后针对瓶颈侧精准调优——写重看 I/O 和 WAL，读重看缓存和副本。
