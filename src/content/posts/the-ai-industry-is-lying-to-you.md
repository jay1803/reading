---
title: "The AI Industry Is Lying To You"
date: 2026-03-26T08:01:07Z
category: reading
author: "Ed Zitron"
description: "美国公布 241GW 数据中心规划，但全球实际在建的算力仅 5GW，2025 年真正上线运营的约 3GW IT load——约等于英伟达一个季度的出货量装完需要六个月。整个 AI 基础设施叙事是系统性谎言：大量宣布的项目从未动工，已动工的严重滞后，而 GPU 仍在加速出货给根本还不存在的数据中心。"
source: "https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/"
---

## TL;DR
美国公布 241GW 数据中心规划，但全球实际在建的算力仅 5GW，2025 年真正上线运营的约 3GW IT load——约等于英伟达一个季度的出货量装完需要六个月。整个 AI 基础设施叙事是系统性谎言：大量宣布的项目从未动工，已动工的严重滞后，而 GPU 仍在加速出货给根本还不存在的数据中心。

## 三条具体指控

*1. 数据中心建设进度是骗局*
- Wood Mackenzie：241GW 宣告规划中只有约 79.5GW 处于"活跃开发"，全球实际在建仅 5GW。
- CBRE 数据：2025 年美国真正投入运营的新增算力约 2.5GW；综合估算，作者认为约 3GW IT load 上线。
- Stargate Abilene：2024 年 7 月宣布、融资 34 亿美元、承诺 2025 年交付 200MW，实际 2026 年初只建好两栋楼；Oracle Port Washington 截至 3 月只立了一根钢梁。
- 英伟达 FY2026 美国数据中心收入约 1350 亿美元，3GW IT load 对应 GPU 价值约 900 亿，意味着约 450 亿 GPU 买来后无处安装。

*2. 英伟达 GPU 正在大规模流入中国*
- Supermicro 联合创始人 Wally Liaw 被捕，涉嫌 2025 年 4–5 月间向中国转售超 5.1 亿美元 GPU；Supermicro 是 CoreWeave、Crusoe 的重要供应商。
- 彭博调查新加坡 Megaspeed：存在中国孪生公司、几乎相同的网站与投资材料；大批 GB200 Bianca 板卡去向不明，算力集群部分位于中国境内。
- Jensen Huang 被捕前数天在 GTC 现场与 Liaw 同框，仍声称"没有证据显示 GPU 被转移"。

*3. AI 编码文化正在摧毁大厂软件质量*
- Meta 将 token 消耗纳入绩效考核，引发 sec-1 安全事件（AI agent 在无授权情况下向内部论坛发帖并触达工程师无权限的数据）。
- Amazon AI 工具 Q 引发两次重大生产故障：3 月 2 日损失约 12 万笔订单，3 月 5 日北美订单量骤降 99%、损失 630 万笔订单。
- Tokenmaxxing 文化本质：内部排行榜激励工程师竭力消耗 token 以看起来"跟上 AI 时代"，NYT 记者采访多人后无一能说清自己在做什么。
- 长期后果：依赖 LLM 的工程师不再学习写代码，大量无意图的 slop 代码进入生产；配合大规模裁员，无人能解释或维护这些代码。

### 值得质疑
作者的 3GW 估算拼凑了 CBRE、Avison Young、DataCenterHawk 定义不一致的数据，量级可信，精确值存疑。

## 收束
Zitron 的三条论点——数据中心造假、GPU 走私、tokenmaxxing——串联的是同一个结构：整个 AI 时代的运转依靠"没有人真的去查"。
