---
title: "A very tactical guide to ABM in 90 days"
date: 2025-03-14T19:45:55Z
category: reading
description: "Userpilot 的市场营销副总裁 Emilia Korczynska 分享了她在 90 天内实施 ABM（Account-Based Marketing，目标客户营销）的详细过程和经验。由于之前没有 ABM 经验，团队面临诸多挑战，但通过不断尝试和优化，最终将 ABM 转变为一个有利可图的渠道。在 90 天内..."
source: "https://www.growthunhinged.com/p/a-very-tactical-guide-to-abm"
---

## TL;DR
Userpilot 的市场营销副总裁 Emilia Korczynska 分享了她在 90 天内实施 ABM（Account-Based Marketing，目标客户营销）的详细过程和经验。由于之前没有 ABM 经验，团队面临诸多挑战，但通过不断尝试和优化，最终将 ABM 转变为一个有利可图的渠道。在 90 天内，ABM 产生了超过 65 万美元的 pipeline，每花费 1 美元产生了 12 美元的 pipeline。
### 主题
#### ABM 的挑战与准备
Emilia 团队在过去五年主要依赖 SEO 获取流量，但随着产品价格上涨，SEO 转化率下降。首次尝试 ABM 时，他们发现缺乏详细的战术资源，需要自行解决许多问题。
在开始 ABM 之前，团队需要回答以下问题：
- 目标客户是谁？
- 预算多少？
- 使用哪些渠道？
- 如何衡量成功？
- 如何进行客户评分？
- 如何将销售和市场团队协同起来？

#### ABM 实施步骤
Emilia 团队决定从“1:many”ABM 活动开始，通过广告定位大量具有共同特征的客户。
他们根据 Kyle Poyar 的 GTM metrics 2.0 文章，确定了 ABM 活动的阶段、阶段基准、收入目标和预算。
ABM 活动阶段如下：
1. Identified：所有目标客户。
2. Aware：广告展示超过 50 次的客户。
3. Interested/Engaged：广告点击超过 5 次或互动超过 10 次的客户。
4. Considering：预约演示或注册试用的客户。
5. Selecting：有开放交易的客户。

#### 客户评分与技术应用
最初，团队尝试结合多种因素进行客户评分，但发现网站访客匿名化数据不可靠。
最终简化为仅使用 LinkedIn 的定量广告互动数据和定性数据（参与的广告活动）来个性化 BDR（Business Development Representative，业务拓展代表）外展。
使用 Fibbler 和 ZenABM 将 LinkedIn Campaign Manager 的公司级互动数据推送到 Hubspot。
根据互动数据了解客户意图，例如对入职、分析或从竞争对手切换的兴趣。
在 Hubspot 中创建活跃客户列表，根据 ABM 阶段和 LinkedIn 广告互动/点击次数的阈值进行划分。

#### 预算与渠道选择
设定了 350 万美元的合格 pipeline 目标和 35 万美元的年度预算。
初期仅使用 LinkedIn Ads，并计划使用 Google Display 网络进行重定向广告。
使用 Clay 和 BuiltWith 的 API 构建目标客户列表。

#### 客户选择标准
根据不同的 ABM 活动重点，使用不同的选择标准。
例如，针对“Session Replay + Analytics”功能的活动，目标客户需满足以下条件：
- Firmographic fit：
  - 公司规模：SMB（50-500 名员工）或 Mid-Market（500-2000 名员工）。
  - 收入：年收入 500 万美元以上或相当的资金。
  - 行业：数字优先（SaaS、电子商务、EdTech、FinTech、HealthTech）且采用产品驱动增长模式。
  - 地点：美国、加拿大、澳大利亚、新西兰、爱尔兰、以色列和西欧/北欧。
- Technographic indicators：
  - 当前或曾经使用过{用例}竞争对手。
  - 当前或曾经使用过缺乏{功能}的直接竞争对手。
  - 同时使用{功能1}+{功能2}工具。

#### 人员与广告策略
使用 Apollo 和 Clay 寻找目标客户中的相关人员（如 PM、UI/UX、PMM、CXO）。
在 Hubspot 中创建活跃列表，用于 LinkedIn Campaign Manager 的动态广告定位。
根据 ABM 阶段更新客户列表，确保广告与客户当前阶段相符。
根据人员和 ABM 阶段构建 LinkedIn 广告系列组，并在组内关注特定消息主题。
由于 LinkedIn API 的限制，重新构建了基于共同意图而非人员的广告系列结构。

#### 广告类型与效果
使用的 LinkedIn 广告类型包括：单图广告、视频广告、思想领袖广告、DM 广告、文本广告和文档广告。
单图广告的 CTR 最高，每次点击成本最低。
思想领袖广告的 CTR 较高，但 LinkedIn 会计算所有点击，包括“阅读更多”、作者个人资料等。
每月在广告上花费约 2 万美元。

#### 团队与技术栈
团队成员包括 ABM 经理、营销运营经理、平面设计师和增长/绩效经理。
使用的 ABM 技术栈包括：
- 列表构建：HubSpot (CRM) + Clay + BuiltWith + Apollo
- 活动资产管理：Notion
- 意图识别和客户评分：ZenABM/Fibbler
- 广告活动管理、销售线索流、报告和销售外展：HubSpot Marketing
- 潜在客户挖掘：SalesLoft
技术栈每月花费约 2500 美元。

#### 报告与指标
监控的指标包括：
- 每周从一个阶段过渡到另一个阶段的客户数量与基准对比。
- 每花费一美元产生的 Pipeline。
- 广告效果基准（CTR、CPM、CPC、CPL）。
在 HubSpot 仪表板上监控指标、客户进展和每个客户产生的 Pipeline。

#### 首次 ABM 活动结果
首次 ABM 活动以在线会议（Product Drive）为“门户资产”。
结果如下：
- 接触客户：1417
- 总成本：约 52191 美元
- 产生的 Pipeline：约 65.5 万美元
- 每花费一美元产生的 Pipeline：12.55
- 资产：约 100 个广告，面向 8 种角色
- 单图广告：1172 次点击，0.35% CTR，19 美元 CPC
- 视频广告：313 次点击，0.28% CTR，24 美元 CPC
- 思想领袖广告：4.42% CTR，68 美元 CPC
- 团队：4.5 名全职人员

### 总结
Emilia Korczynska 的团队通过 90 天的 ABM 实践，成功将 ABM 转变为一个高效的营销渠道。虽然过程充满挑战，但通过不断优化和调整，实现了显著的 Pipeline 增长，证明了 ABM 的价值。
