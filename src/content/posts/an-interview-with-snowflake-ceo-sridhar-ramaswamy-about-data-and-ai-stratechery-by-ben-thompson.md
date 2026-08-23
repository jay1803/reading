---
title: "An Interview with Snowflake CEO Sridhar Ramaswamy About Data and AI – Stratechery by Ben Thompson"
date: 2025-03-31T17:58:14Z
category: reading
author: "Ben Thompson"
description: "这篇访谈记录了 Stratechery 对 Snowflake 现任 CEO Sridhar Ramaswamy 的采访。Ramaswamy 拥有在 Google 领导搜索广告业务 15 年的背景，并创办了后被 Snowflake 收购的搜索引擎 Neeva。访谈内容涵盖了他的职业经历、对 Google 现状的看..."
source: "https://stratechery.com/2025/an-interview-with-snowflake-ceo-sridhar-ramaswamy-about-data-and-ai/"
---

## TL;DR
这篇访谈记录了 Stratechery 对 Snowflake 现任 CEO Sridhar Ramaswamy 的采访。Ramaswamy 拥有在 Google 领导搜索广告业务 15 年的背景，并创办了后被 Snowflake 收购的搜索引擎 Neeva。访谈内容涵盖了他的职业经历、对 Google 现状的看法、Neeva 的经验教训、他出人意料地接任 Snowflake CEO 的过程、Snowflake 的核心业务演进（包括对开放数据格式的支持）、商业模式、市场策略，以及最重要的——Snowflake 在 AI 时代的战略定位、产品方向（如 Cortex Search、Cortex Analyst）、对 AI 的核心理念（易用、高效、可信），以及如何利用其数据平台优势在与 Databricks、超大规模云服务商 (hyperscalers) 和 SaaS 公司的竞争中胜出。Ramaswamy 的目标是将 Snowflake 打造成企业信赖的核心 AI 数据平台。
### 主题
#### 个人背景与经历
Sridhar Ramaswamy 在南印度长大，毕业于 IIT Madras，并在 Brown University 获得数据库博士学位。他曾在 Bell Labs 从事数据库研究，之后于 2003 年加入 Google。
在 Google 的 15 年间，他从个人贡献者做起，最终负责搜索广告及商业部门，经历了 Google 从桌面到移动的转型（应对 RPM gap 挑战），并推出了 Google Pay 等产品。
离开 Google 后，他希望重新开始，短暂加入 Greylock 后创办了 Neeva。Neeva 是一个基于订阅、无广告的搜索引擎，其理念是广告支持的搜索模式已达效用极限。Neeva 在技术上探索了 RAG (retrieval-augmented generation) 等早期 AI 应用，但在合适的 AI 技术（如大型语言模型和聊天界面）成熟前推出，时机稍早。Neeva 最终被 Snowflake 收购。
Ramaswamy 认为当前 Google Search 面临来自两方面的挑战：对于简单问题，ChatGPT 等对话式体验更优；对于复杂工作流，未来的 agentic systems 能做得更多。
#### 接任 Snowflake CEO
Snowflake 收购 Neeva 是看中了其在搜索和早期 AI（如模型微调、RAG）方面的专长。Ramaswamy 加入 Snowflake 的最初计划是短期负责 AI 路线图，并非接任 CEO。
在与前 CEO Frank Slootman 沟通后，考虑到 Snowflake 在 AI 时代需要更强的产品导向领导力，Ramaswamy 在 Neeva 被收购八个月后接任 CEO。
这一变动加上公司发布的较低增长预期（22% vs 市场预期的 30%），导致 Snowflake 股价大幅下跌。Ramaswamy 认为 Slootman 快速完成交接是正确的决定，他上任后加强了与投资者、分析师和团队的沟通，并对公司近期的产品推出速度和未来发展表示乐观。
#### Snowflake 核心业务与演进
Snowflake 最初的核心价值是作为云数据仓库，通过分离存储和计算，提供了高度弹性和效率的分析平台，解决了传统数据仓库固定资源配置和并发查询的限制。
之后，Snowflake 发展了数据共享能力，使企业间能实时、跨云地安全共享数据，无需复杂的 IT 项目（如 FTP 文件传输），成为企业数据的“循环系统”。许多数据提供商（如 NYSE, S&P Global）通过 Snowflake 分发数据产品。
近期的一个重要变化是全面拥抱开放数据格式，特别是 Apache Iceberg。虽然这可能减少 Snowflake 的存储收入（因数据可存储在外部云存储上），但 Ramaswamy 认为存储本应按成本收费。更重要的是，这使得 Snowflake 的计算引擎可以作用于企业存储在外部云存储中更大量的数据（可能是 Snowflake 内部数据的数百甚至数千倍），显著扩展了 Snowflake 的价值和应用场景（如数据工程、数据摄取）。Snowflake 还推出了开源目录格式 Apache Polaris，以促进数据集发现。
这种开放策略一方面增强了平台的吸引力和网络效应，但也带来了风险，即客户更容易更换计算提供商。Snowflake 的应对是依靠其平台的综合优势，如治理、协作、灾难恢复、跨云能力等，而不仅仅是运行 SQL 查询。
#### 商业模式与市场策略 (GTM)
Snowflake 采用基于使用量的消费模式（consumption model），主要针对计算资源。这种模式将 Snowflake 的收入与客户实际使用和创造的价值对齐。虽然有时会遇到价值创造远超使用成本的情况（错失价值定价机会），但核心模式被认为是稳固的。
管理该模式的挑战在于避免客户因意外的高额账单（如未优化的查询）而产生负面体验。Snowflake 的策略是主动帮助客户优化计算、建立治理流程（如项目启动审批、预算控制），并将生命周期管理等功能内置到平台中，视低效计算为需要解决的问题而非收入来源。
对于领导销售驱动型组织，Ramaswamy 认为其在 Google 的经验（Google 有多种销售模式，包括自服务、内部销售、大客户销售，并有成熟的激励机制）有一定借鉴意义，但也需要学习企业销售的特性。Snowflake 的销售模式结合了交易导向（客户签订合同以获取计算折扣）和推动使用量（通过用例创造价值），需要掌握新的技巧。他推崇使用布尔指标 (Boolean metrics) 来衡量团队效率。
#### Snowflake 与 AI
AI 对 Snowflake 带来两大变化：一是让数据更具互换性 (fungible)，例如通过多模态模型更容易从 PDF 等非结构化文档中提取结构化数据；二是改变了数据消费方式，AI 可以让终端业务用户通过自然语言查询直接与数据交互，而无需依赖传统的 BI 工具和分析师。
Snowflake 的 AI 战略核心是“Easy, efficient, and trusted”（易用、高效、可信）。
1.  易用性：通过 SQL 等简单接口让现有分析师也能使用 AI 模型；提供 Cortex Search（针对非结构化数据，带引用来源）和 Cortex Analyst（自然语言生成 SQL 查询结构化数据，带反馈和验证机制）等产品。
2.  高效性：利用 AI 提升平台能力，例如加速数据迁移等。
3.  可信度：强调结果的可靠性，如 Cortex Search 的引用和 Cortex Analyst 的 verified query repository（包含正反例，控制模型回答范围和精度），在精确度和召回率之间做权衡，避免 AI 幻觉。
Snowflake 不寻求成为基础模型公司，而是利用现有的（包括开源模型如 Llama）模型，专注于构建基于其数据平台的 AI 产品和能力，特别是组合不同数据元素和 AI 能力的 agentic workflows（智能体工作流）。AI 被视为加速实现“帮助客户调动数据”使命的工具。
AI 使得 Snowflake 需要扩展其关注范围，从传统的“黄金”分析层数据扩展到底层更广泛的数据（结构化和非结构化），通过拥抱开放格式和连接器 (connectors) 实现。

#### 竞争格局与定位
Snowflake 面临来自不同方向的竞争：
1.  与 Databricks 等公司的竞争：Snowflake 从结构化数据仓库起家，易用性强；对手可能从非结构化数据和数据湖 (Lakehouse) 起家，对 AI 更友好。双方都在向中间地带扩展。Ramaswamy 认为 Snowflake 的优势在于其从一开始就构建的统一、紧密集成的产品体验，这比将松散的产品组合变得易用要更容易。
2.  与超大规模云服务商 (hyperscalers) 的竞争：Hyperscalers 强于基础设施，但其平台往往由多个独立产品线构成，缺乏统一性。Snowflake 定位在更上层的、统一的数据平台。
3.  与 SaaS 公司的关系：Snowflake 与 SaaS 公司合作，进行双向数据集成。同时，SaaS 公司自身也在大力投入 agentic AI，这可能改变用户与 SaaS 平台的交互方式。Snowflake 通过 Native Application 等方式，允许第三方（如 S&P Global）在客户的 Snowflake 环境中安全地部署应用，结合双方数据提供价值，并探索 agentic AI 层面的互操作性（如与 Microsoft Copilot 集成）。
数据迁移仍然是一个巨大的市场机会，AI 有望大幅缩短迁移时间。这对 Snowflake 有利，因为迁移最终通常是为了更好地组织和利用结构化数据。

#### 未来愿景
Ramaswamy 的目标是带领 Snowflake 在未来十年实现高速增长（以 Google 的增长作为参照），成为企业不可或缺的数据合作伙伴，帮助它们像顶尖科技公司一样高效、深刻地利用数据。这需要 Snowflake 持续提供卓越的产品，帮助客户在 AI 带来的变革和机遇中导航。成功意味着 Snowflake 真正帮助客户调动了他们的数据，并通过 AI 释放了更大价值。

### 总结
Sridhar Ramaswamy 致力于将 Snowflake 从领先的云数据仓库发展为企业核心的 AI 数据平台，通过整合 AI 能力、拥抱开放标准、并依托其统一易用的平台优势，帮助客户在 AI 时代更有效地调动和利用结构化及非结构化数据。
