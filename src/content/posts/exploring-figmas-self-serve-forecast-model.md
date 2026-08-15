---
title: "Exploring Figma's Self Serve Forecast Model"
date: 2025-01-10T14:39:29Z
category: reading
description: "我们最近与 Figma 的第 40 名员工和第二位战略财务员工 Craft Ventures 的 Sean Whitney 坐下来，了解 Figma 如何构建一个自助服务预测模型，该模型始终预测年度经常性收入 （ARR） 增长率在 5% 以内。"
source: "https://wrap-text.equals.com/p/exploring-figmas-self-serve-forecast-model"
---

我们最近与 Figma 的第 40 名员工和第二位战略财务员工 Craft Ventures 的 Sean Whitney 坐下来，了解 Figma 如何构建一个自助服务预测模型，该模型始终预测年度经常性收入 （ARR） 增长率在 5% 以内。
### Figma's forecasting model for Self Serve ARR
Sean 的团队构建的模型涵盖了整个客户生命周期，并分为五个部分：网站流量和注册，它们构成了漏斗顶部 （“ToF”），然后是新许可证、扩展许可证和客户流失许可证的突破，它们相当于总许可证和 ARR。

### Model Walkthrough
#### Top of Funnel
##### Website Traffic
##### Signups
网站流量和注册构成了 ToF，是任何自下而上的 SaaS 模型最敏感的驱动因素。由于现阶段的交易量很大，ToF 性能的微小百分比变化会在 ARR 层面产生巨大影响，并导致预测误差。为了帮助领先于这一点，Sean 建议与您的产品和营销团队合作，将 ToF 流量分解为更精细的级别，例如流量来源、广告活动或地理位置。
#### Bottom of Funnel
##### New Licenses
we get our first glimpse of the magic powering the model, cohorting.
1. 转化率趋势 - 按年龄对同期群进行基准测试，使用户能够随着业务的发展比较和对比性能趋势
2. 数量贡献 - 通过 ToF 群组创建付费许可证量瀑布流，在变现和漏斗老化之间建立了联系
##### Expansion Licenses
接下来，该模型概述了新注册队列如何随着许可证的老化（不包括流失）而添加或删除许可证。对于同时拥有月度和年度合同客户的企业，需要单独的突破，因为追加销售往往以不同的时间增量进行。
##### Churned Licenses
拼图的最后一块是了解整个许可证基础中有多少将续订或流失。与扩展建模类似，分别对月度客户和年度客户的流失进行建模至关重要，因为年度客户的大部分流失发生在其服务期的第 12 个月。
### Key Takeaways
此模型成功的关键有两点：
1. 它涵盖了完整的客户生命周期，清楚地列出了旅程中每个阶段的绩效。
2. 通过同期群分析，用户可以查看效果趋势随时间的变化，并了解为什么今天的效果会受到过去活动的影响。
