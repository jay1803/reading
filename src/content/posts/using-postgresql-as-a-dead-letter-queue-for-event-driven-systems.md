---
title: "Using PostgreSQL as a Dead Letter Queue for Event-Driven Systems"
date: 2026-02-14T20:39:06Z
category: reading
description: "Kafka 做 DLQ 是常见模式，但不适合需要\"可见性\"的场景——失败事件进入死信 topic 后，按失败原因查询或选择性重试都需要额外 consumer 和工具。用已有的 PostgreSQL 表存储失败事件，失败立刻成为可 SQL 查询的一等公民，运维复杂度几乎不增加。"
source: "https://www.diljitpr.net/blog-post-postgresql-dlq"
---

## TL;DR
Kafka 做 DLQ 是常见模式，但不适合需要"可见性"的场景——失败事件进入死信 topic 后，按失败原因查询或选择性重试都需要额外 consumer 和工具。用已有的 PostgreSQL 表存储失败事件，失败立刻成为可 SQL 查询的一等公民，运维复杂度几乎不增加。

## 核心洞见
Kafka DLQ 的本质问题：消息在死信 topic 里是不透明的流数据，回答"昨天什么失败了、为什么"变成一个工程问题。PostgreSQL 让这个问题变成一条 SELECT 语句。失败从"流"变成了"状态"，可按 event_type、failure reason、时间范围任意切片，工程师用已经在用的查询工具就能操作。

## 具体机制
表结构核心字段：=payload=（JSONB，不约束 schema）、=status=（PENDING/SUCCEEDED，极简状态机）、=retry_count= + =retry_after=（防止持续轰炸不稳定下游）。重试调度器基于 ShedLock 保证多实例下单次执行，用 =FOR UPDATE SKIP LOCKED= 实现无争用的并发行选取——多个实例可以同时跑，各自锁各自的行而不互阻。消费者侧先做指数退避（初始 2s，翻倍，上限 30s，最多3次），只有真正持续失败的事件才写入 DLQ，防止瞬断事件把死信表淹没。调度器每6小时运行一次，每批最多处理50条，最大重试次数240次。

## 隐藏限制
=max-retries: 240= × 6小时间隔 = 理论最长60天重试窗口，文章没有讨论超限后如何处置（归档、告警、人工介入）。DLQ 表长期运行会积累，清理/归档策略同样未提。整套设计的前提是失败为异常而非常态——若系统本身失败率极高，PostgreSQL DLQ 反而可能成为新的写入瓶颈。

## 把失败变"无聊"的代价可以忽略不计
这套设计在 Kafka 已是主链路的系统里引入 PG 做 sidecar 存储几乎零增量——Postgres 本来就在那里，多一张表而已。代价极小，但收益是：失败有了可审计的生命周期，工程师不再需要"害怕失败"，因为每一次失败都有清晰的恢复路径。可靠性不是消除失败，而是让失败可预测。
