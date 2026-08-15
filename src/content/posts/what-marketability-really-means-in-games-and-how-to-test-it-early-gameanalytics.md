---
title: "What marketability really means in games and how to test it early — GameAnalytics"
date: 2026-04-23T08:02:20Z
category: reading
description: "这篇文章真正有用的点不是再说一遍“别只看 CPI”，而是把 marketability 定义成一个分阶段验证系统：原型阶段验证 attention，soft launch 验证 retention 和 monetization，规模化阶段验证 LTV、CAC 与区域扩张；如果团队不能判断吸来的用户是不是对的人、产..."
source: "https://www.gameanalytics.com/blog/what-marketability-means-in-games"
---

## TL;DR
这篇文章真正有用的点不是再说一遍“别只看 CPI”，而是把 marketability 定义成一个分阶段验证系统：原型阶段验证 attention，soft launch 验证 retention 和 monetization，规模化阶段验证 LTV、CAC 与区域扩张；如果团队不能判断吸来的用户是不是对的人、产品有没有兑现广告承诺、以及自己是否知道该怎么改进，那么所谓“低 CPI”只是廉价误判，不是可扩张性。

## 核心洞见
- 文中最重要的重定义，是把 marketability 从单一买量指标改成 product-market-channel fit：先看有没有人想点，再看来的是否是对的人，最后看产品能不能把兴趣兑现成留存与收入。
- 同样一组早期数字，在熟悉品类的团队和陌生品类的团队里风险含义不同。前者知道还能优化哪些环节，所以更愿意容忍暂时偏弱的指标；后者即便 top-funnel 漂亮，也可能因为不知道如何修正深层问题而直接砍掉。
- UA 测试不只是筛广告，还会反向暴露产品该更早兑现什么 fantasy。Farm Manager 里“马”素材吸来更多女性用户，说明问题不在流量，而在产品前段没有足够快地交付用户被广告承诺的内容。

## 具体机制
- Prototype 阶段只回答一个问题：概念能不能赢得下一次点击。这里该看的是 CTR、IPM、fake-store conversion、创意层面的即时反馈，而不是过早执着 ARPU 或完整商业模型。
- Soft launch 才开始把技术稳定性与经营指标放到一起看：crash rate、D1/D7/D30、payer conversion、CPI、ROAS、ARPU。文中给出的 “40/20/10” 更像方向性健康线，不是可以机械套用的判定器。
- Scale 阶段，市场性从“能不能吸引”切换成“能不能长期赚钱”：DAU/MAU、注册和转化漏斗、LTV、区域表现、CAC 效率、长期留存与流失才是决定能否放大的核心。
- Benchmarks 的正确用法不是拿平均值当答案，而是拆出成功创意背后的 recipe：哪些主题、承诺、视觉元素和玩法 framing 真正在驱动高质量流量，然后再用自己的产品去验证。

## 值得质疑
- 文章本质上是一次 masterclass 讨论整理，启发性强于证据强度。多数判断靠经验总结，没有给出系统样本、因果检验或跨品类对照。
- “低 CPI 可能吸来错的人”这个判断是对的，但文中没有展开如何在创意误导、 onboarding 错配、产品兑现失败之间做更精细的归因。
- 它强调 marketability 可以被“earn early and iterate”，但真正难点是团队是否具备持续改产品、改创意、改投放并正确解释信号的组织能力，这部分被明显轻描淡写。

## 最后一笔
最该记住的不是“别只看 CPI”，而是市场性从来不是营销部门末端的一个 KPI；它是产品承诺、创意 framing、受众匹配和组织学习速度的联合函数。低成本获客只是门口，能不能把承诺兑现成留存与 LTV，才决定游戏是不是一门生意。
