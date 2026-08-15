---
title: "What is a database transaction?"
date: 2026-02-24T10:55:40Z
category: reading
description: "MySQL 和 Postgres 都宣称支持\"可重复读\"，但底层实现完全相反——Postgres 保留多个版本的行（MVCC），MySQL 直接覆写行但维护 undo log 供旧版本重建；这一分歧在高并发写冲突时导致截然不同的行为：乐观冲突检测 vs 悲观行锁。"
source: "https://planetscale.com/blog/database-transactions"
---

## TL;DR
MySQL 和 Postgres 都宣称支持"可重复读"，但底层实现完全相反——Postgres 保留多个版本的行（MVCC），MySQL 直接覆写行但维护 undo log 供旧版本重建；这一分歧在高并发写冲突时导致截然不同的行为：乐观冲突检测 vs 悲观行锁。

## 核心洞见
- 四种隔离级别（Serializable → Repeatable Read → Read Committed → Read Uncommitted）不是性能调优旋钮，而是"你愿意承受哪种数据错误"的主动取舍：Phantom read、Non-repeatable read、Dirty read 各对应一种被明确"允许"的不一致。
- Postgres 的一致读靠 xmin/xmax 元数据控制行版本可见性；MySQL 靠 undo log 在查询时按需重建旧版本——前者写放大（多版本行），后者查询时有重建开销。

## 具体机制
- **Postgres SERIALIZABLE（SSI）**：从不阻塞事务，用 predicate lock 追踪读写依赖；发现违反序列化时 kill 事务，属于乐观策略。
- **MySQL SERIALIZABLE（行级锁）**：事务更新行时必须持有 X lock；两事务争同一行时进入死锁，MySQL 检测后强制 kill 一方；锁等待本身也是吞吐瓶颈。
- Postgres 多版本行随写入不断积累"过期版本"，需定期运行 `VACUUM FULL` 清理压缩；MySQL undo log 在无活跃事务需要时自动截断，无需人工维护。

## 值得质疑
文章将 Postgres SSI 描述为"避免了死锁"，但被 kill 的事务同样是中断——只是触发条件变了，应用侧重试逻辑同样必需；"无死锁"的表述有一定误导性。

## 代价由谁承担
Postgres 把一致性代价推给存储清理（VACUUM），MySQL 把代价推给锁竞争；高读低写场景 MVCC 优势明显，高并发更新同一行场景 MySQL 的锁策略反而更可预测——选哪个取决于写模式，没有默认更优的一方。
