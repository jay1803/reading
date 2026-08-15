---
title: "telecheck and tyms past"
date: 2026-03-30T08:00:23Z
category: reading
description: "支票担保服务 TeleCheck，不仅是美国最早的实时电信支付处理系统，更是第一个跨城市分布式数据库网络——它在 ATM 出现之前就已存在，并最终演化成 ACH 电子转账的前身。"
source: "https://computer.rip/2026-03-29-telecheck-and-tyms-past.html"
---

## TL;DR
支票担保服务 TeleCheck，不仅是美国最早的实时电信支付处理系统，更是第一个跨城市分布式数据库网络——它在 ATM 出现之前就已存在，并最终演化成 ACH 电子转账的前身。

## 关键时刻
- 1964 年，Harry Flagg 在火奴鲁鲁童子军聚会上推销"坏支票黑名单"，次年 TeleCheck 正式商用，核心是 IBM 1440 主机处理实时电话查询——三种返回码（1/3/4），向商家担保支票；若支票跳票，TeleCheck 自掏腰包，同时接管讨债权。
- 这个模型天然自我强化：商家为了索赔必须上报坏支票，数据因此源源不断地流入系统，而非依赖警察或银行。
- TeleCheck 迅速扩张为特许经营网络，跨州之间自动同步坏账记录，形成全国性"分布式数据库"；1969 年月处理 7 万通电话、月担保 675 万美元。

## 背后逻辑
- TeleCheck 的技术野心远超支票本身：IBM 1440 → Honeywell 200 → CDC 3100，两年内连换三代机；同期还涉足医疗账单、计算机配对相亲（Match-Mate）、教育、潜水艇研发……最终过度扩张，1972 年破产，创始人 Flagg 出局。
- 1980 年被 Tymshare 收购，获得了 Tymnet——这张"工业互联网"级广域网此后为 Visa、MasterCard、AOL 等跑流量，TeleCheck 从此拥有全国级网络基础设施。
- 1984 年转给麦道（F-15 制造商），1989 年卖给 First Data，1990s 将支票验证与 ACH 电子转账整合为"支票转换"（Check Conversion），让支票在 POS 机上即时变成 ACH 批量交易。
- 2019 年归入 Fiserv，如今网站仅剩监管合规页面，连营销都不做——成了一头不被宣传的现金牛。

## 更大意义
TeleCheck 走完了支付科技的完整弧线：1960 年代的理想主义（让所有人的支票都被接受）→ 债务征信的监管泥潭（Fair Credit Reporting Act 下的数十起诉讼）→ 2020 年代的暮年讽刺（Amazon 帮助中心告诉你"支付失败请致电 TRS Recovery Solutions"，而 TRS 就是从 TeleCheck 剥离出来专门追债的子公司）。

## 令人意外的收束
Flagg 在离开 TeleCheck 后，于 1997 年创立了传销公司 Trek Alliance，2005 年被 FTC 起诉并裁定败诉。这不是偶然的讽刺：他一生的逻辑始终如一——抓住一切看起来能"用计算机赚钱"的机会，快速扩张，然后等待机器把他甩出去。
