---
title: "Your B2B product-led motion is more of a data problem than a product problem."
date: 2025-02-19T16:07:50Z
category: reading
description: "文章与 Clarify (AI-native CRM) 的联合创始人 Austin Hay 共同撰写，探讨了产品驱动增长 (Product-Led Growth, PLG) 成功的关键因素——数据可用性。许多公司因未能优先考虑正确的数据基础设施和特定数据类型而导致PLG策略失败。文章详细阐述了PLG所需的数据基础..."
source: "https://www.elenaverna.com/p/your-b2b-product-led-motion-is-more"
---

## TL;DR
文章与 Clarify (AI-native CRM) 的联合创始人 Austin Hay 共同撰写，探讨了产品驱动增长 (Product-Led Growth, PLG) 成功的关键因素——数据可用性。许多公司因未能优先考虑正确的数据基础设施和特定数据类型而导致PLG策略失败。文章详细阐述了PLG所需的数据基础、技术栈以及实施策略，并指出了常见问题。
### 主题
#### 理解产品驱动增长 (PLG) 与产品驱动销售 (PLS)
PLG不仅仅是提供自助服务产品或试用策略，而是一套完整的市场推广和产品策略。它依赖用户自行发现并喜爱产品，从个人价值延伸到团队采用，最终吸引拥有购买决策权的人。
PLS (Product-Led Sales) 是PLG与传统销售模式的结合。其销售漏斗从用户注册、获得价值、邀请团队开始，当用户使用行为触发产品合格账户 (Product Qualified Account, PQA) 和产品合格潜在客户 (Product Qualified Lead, PQL) 的识别后，销售团队介入，寻求扩张机会。PLS的核心在于利用产品数据判断接触潜在买家的最佳时机，PLG的作用在于收集客户购买意愿和转化可能性的信号。
#### PLG 成功的基石：不可或缺的数据基础
成功的PLG策略依赖于一系列关键数据点，缺乏这些数据将导致基础不稳。
##### 用户人口统计数据 (User demographics)
了解注册用户的基本信息至关重要，这些数据应在用户引导流程 (onboarding) 中直接询问，而非猜测或使用数据补充工具。核心信息包括：
- 用户的角色 (User's role)
- 公司规模 (Company size)
- 产品使用场景/目的 (Use case)
- 团队规模 (Team size)
##### 用户获取数据 (Acquisition)
传统的归因方法 (如Last touch, Multi-touch attribution) 效果正在减弱，URL参数易被清除，Cookies被阻止，IP地址被隐藏。通过“你是如何了解到我们的？” (How did you hear about us?) 这样的简单调研可以有效收集流量来源（自然、付费、口碑）、活动归因以及用户初次认知渠道等信息。
此外，需要追踪的关键指标包括：
- 流量来源 (Traffic sources)
- 活动归因 (Campaign attribution)
- 首次接触点 (First touchpoint)
##### “混乱的中间环节”：用户激活数据 (Activation “messy middle”)
用户激活是从注册到持续参与的关键阶段，是PLG工作的核心。需要追踪的数据包括：
- 设置完成情况 (Setup completion)
- “啊哈！”时刻的达成 (Reaching the "aha!" moment)
- 关键功能采用率 (Key feature adoption)
- 习惯回路的建立 (Habit loops)
客户数据平台 (Customer Data Platform, CDP) 和产品分析工具需要有良好的数据管理规范，包括正确的事件命名、一致的属性以及明智的客户端与服务器端追踪决策。
##### 用户参与度数据 (Engagement reality check)
通过用户参与度数据可以区分试用者和潜在付费客户。关键指标包括：
- 日/周/月活跃用户 (DAU/WAU/MAU)
- 会话时长和频率 (Session length/frequency)
- 功能采用的深度和广度 (Feature adoption depth/breadth)
一个常见的问题是，这些数据通常停留在产品分析工具中，未能同步到销售团队使用的CRM系统，导致数据价值无法充分发挥。
##### 商业化数据 (Following the money)
商业化信号对于触发销售和增长活动至关重要。这些数据包括：
- 达到使用限制 (Hitting usage limits)
- 套餐升级 (Plan upgrades)
- 支付失败 (Payment failures)
- 扩张潜力指标 (Expansion potential indicators)
这些信号应实时同步到CRM和应用内通知，以便增长和销售团队及时响应。
##### 数据整合的挑战 (The data integration challenge)
数据整合是许多PLG策略失败的关键点。增长、营销和销售团队需要能够基于整合的数据执行以下操作：
- 对自助服务增长：发送及时、情境化的应用内通知和邮件。
- 对销售增长：按功能采用率筛选账户、按使用强度排序机会、在账户触发扩张条件时获得提醒、在联系人信息旁查看使用趋势。
#### 构建支持 PLG 的技术栈 (The stack you actually need)
选择合适的工具并确保它们能协同工作是PLG成功的关键。
##### 核心必备工具
1.  客户数据平台 (Customer Data Platform, CDP)：负责收集、整合和分发数据。传统上Segment是热门选择，新兴工具如Hightouch不仅收集数据，还能以符合现代数据栈的方式轻松分发数据。CDP的功能正被营销技术领域商品化。
2.  产品分析工具 (Product Analytics Tools)：如Posthog, Amplitude, Mixpanel, June.so，用于追踪和分析用户在产品内的行为。
3.  现代CRM (A Modern CRM)：传统的CRM可能不适合PLG。需要能够让销售团队查看和操作产品使用数据的CRM。Salesforce和Hubspot可以调整适应，但新兴的AI原生CRM如Clarify能更好地支持。
##### 对专用 PLG CRM 的反思
专门的PLG CRM试图解决错误的问题。PLG并非孤立的运营，而是整个市场推广策略的一部分。将PLG CRM与主要CRM分开会制造更多问题。PLG能力应该是市场推广平台的一个功能，而非独立工具。Gainsight, Catalyst, Vitally等工具通过增强现有流程而非取代它们，找到了自己的定位。
##### “锦上添花”的工具
- 营销自动化工具 (Marketing automation tools)：如Customer.io, HubSpot，用于在合适的时间自动触达用户。
- A/B测试平台 (A/B testing platforms)：如Optimizely, LaunchDarkly，用于优化体验。
- 潜在客户评分工具 (Lead scoring tools)：如Madkudu。
##### 工具选择的核心原则
具体工具的选择远不如其能力重要。关键能力包括：
1.  能否为特定用例收集和定制事件追踪？
2.  能否构建结合营销、产品和销售数据的单一用户视图？
3.  能否基于产品使用模式创建和导出列表？
4.  能否在正确的时间触发正确的沟通？
5.  销售团队能否实际查看和使用所有这些数据？
工具间的可靠通信至关重要。
#### PLG 的有效实施策略 (Making it actually work)
实施PLG时应从小处着手，逐步扩展。
##### 从基础开始 (MVP)
1.  选择一个与成功客户相关的关键产品行为。例如，Ramp关注完成第一份费用报告，Miro关注五人以上的协作白板会话。
2.  确保这一两个数据点能从产品可靠地流入分析工具。
3.  为用户达到此里程碑制定一个清晰的行动手册。
4.  将其连接到CRM，以便销售和营销团队查看和执行。
5.  将其反馈到产品中，以触发应用内通知和沟通。
##### 奠定基础
- 为公司创建共享的PLG定义。
- 就PQL与PQA的标准达成一致并文档化。
- 在CRM中设置基本的对象模型以处理产品数据。
- 定义团队间的清晰交接流程。
##### 扩展有效的方法
- 在验证了最初的信号后，才添加更多的产品信号。
- 随着对重要因素的了解加深而扩展追踪范围。
- 自动化手动有效的流程。
- 保持技术栈简洁，每个新工具都是潜在的故障点。
#### PLG 实施中的常见问题与解决方案 (When things go wrong)
PLG基础薄弱的迹象包括：
##### 数据孤岛与不一致 (Your data lives everywhere and nowhere)
各团队数据来源不同，无法就基本指标达成一致。产品数据滞留在分析工具中，CRM无法处理PQL，获取完整的用户行为视图需要拼接多个电子表格。当团队不信任数据时，会产生变通方法，而变通方法会扼杀PLG。
##### 团队目标与语言不统一 (Your teams are speaking different languages)
营销、产品和销售团队对PLG的理解和目标不一致，缺乏共同的“产品驱动”定义。例如，对于合格潜在客户的定义各不相同。缺乏统一的团队和指标，PLG将难以成功。
##### 技术栈无法满足需求 (Your tools can't keep up)
CRM并非为产品数据构建，导致需要附加其他工具。跨多个系统同步用户行为数据困难，导致销售团队获得的数据滞后。最终，销售团队可能完全放弃PLG，不再跟进PQL。
### 总结
成功的PLG并非依赖最花哨的功能或最昂贵的工具，而是建立在坚实的基础上：干净的数据、清晰的定义以及团队间的有效沟通。
