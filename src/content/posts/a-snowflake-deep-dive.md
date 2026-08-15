---
title: "A Snowflake deep dive"
date: 2023-10-11T19:41:55Z
category: reading
description: "公司必须衡量和跟踪一切：来自销售的数据，来自营销活动的数据，来自供应链的数据，来自客户的数据，来自合作伙伴的数据，来自财务的数据，来自基础设施的数据，来自软件团队的数据，以及来自其业务所基于的每个SaaS应用程序和服务的数据。这些往往收集在单独的数据孤岛中，组织中的每个团队都在保存和访问与他们相关的数据。"
source: "https://hhhypergrowth.com/a-snowflake-deep-dive/"
---

公司必须衡量和跟踪一切：来自销售的数据，来自营销活动的数据，来自供应链的数据，来自客户的数据，来自合作伙伴的数据，来自财务的数据，来自基础设施的数据，来自软件团队的数据，以及来自其业务所基于的每个SaaS应用程序和服务的数据。这些往往收集在单独的数据孤岛中，组织中的每个团队都在保存和访问与他们相关的数据。

孤岛使得无法看到整个组织，因此企业最终必须创建一个集中式数据存储来包含所有这些不同的操作数据，并将其提供给组织内需要它的每个团队。但是，为了驯服这个庞大且不断增长的数据海洋，公司需要正确的工具来帮助他们理解事物，以期提取见解。获得这些见解对于组织的成功至关重要，可以查看他们的团队是否实现了目标，帮助管理层确定未来的战略，并帮助公司在竞争中占据一席之地 - 这反过来又导致更多的数据随着他们的扩张和成长。公司总是有越来越多的数据要添加到堆中。即使收集的数据点数量保持不变，数据也会随着时间的流逝而增长;他们将需要在下个月和后个月收集相同的数据点，然后继续。数据是宝贵的财产。企业可以将所有数据留给自己，也可以买卖数据。

Snowflake 是一种工具，可帮助公司管理其数据并帮助提取见解。
### Overview
我看到的绝大多数投资研究都将Snowflake标记为“数据仓库即服务”（DWaaS）。这可能是他们最初对自己的称呼（并且在旧的营销中仍然存在），但他们远不止于此。今天，Snowflake是一个数据云。

简而言之，Snowflake希望成为推动整个企业所有分析（包括商业智能（BI）和数据科学（ML / AI））的引擎。他们是数据库即服务（DBaaS）提供商，可在Amazon AWS，Microsoft Azure和Google Cloud Platform（GCP）的3个主要云基础设施即服务（IaaS）环境中使用。

重要的是要事先了解 Snowflake 的架构将数据存储与对其执行的计算密集型操作分开。该平台利用每个云提供商中的本机存储和计算方法。当存储和计算分开时，它们会位于同一位置，以便本机计算处理所有需要的摄取、查询和分析，这些摄取、查询和分析是通过它直接驻留在底层云基础架构中的本机数据存储执行的。其平台群集中的这些分离存储和计算层设置为可按客户单独扩展，这允许每个客户根据其需求进行调整。这允许每个客户考虑他们希望保留的数据量，而不是他们想要的性能、响应能力和并发性，以及他们想要支付的价格。客户可以缩减成本以提高性能和更多并发操作，也可以缩减成本以减少并发性、排队流程和延长等待时间。这种可扩展的内部架构使 Snowflake 成为云中云。cloud-within-a-cloud

我发现Snowflake非常关注数据的安全性和管理。对数据的所有访问都受到平台服务层的严格控制。数据在传输中和静态（存储在 S3、Azure Blob 或 Google Cloud Storage 中的底层压缩文件）都经过加密。用户身份验证和访问权限是其系统的核心，在如何与平台交互方面具有广泛的灵活性，包括典型的现代安全功能（单点登录和多因素身份验证），而且还能够让您的企业网络直接连接到他们的平台（绕过公共互联网）。

Combined with Snowflake's distributed & scalable architecture, these factors ultimately give its platform a lot of flexibility and optionality, from which, multiple use cases (each with a different set of audiences) have emerged: it can be a data warehouse, a data lake, an enterprise-wide search or analytical engine, a cloud-native database to develop data-driven applications on top of, a collective pool of shared data across a partnership, and a marketplace for monetized data access.
### Raw Numbers
SaaS公司的利润率很低，这在很大程度上受到他们必须向云提供商支付所有使用的存储和计算资源的事实的影响。但它正在大幅上升（同比+13个百分点）这一事实是一个很好的迹象。Snowflake正处于现代云时代的一个有趣的难题中 - 他们的平台建立在IaaS提供商之上，而IaaS提供商恰好是他们最大的竞争对手。
### History
Founded in 2012 by ex-Oracle data architects, it operated in stealth for a few years until CEO Bob Muglia (formerly of Microsoft) joined in June 2014.  A few months later, the Snowflake platform was finally opened to the public, with its original focus of being a "Data Warehouse-as-a-Service". Snowflake first ran only on AWS, then ultimately added Azure in mid-2018 and Google Cloud Platform (GCP) in mid-2019.

Along the way, the BOD decided it wanted a "power CEO" with expertise in taking the company public, so changed up the CEO role quickly in mid-2017.  Out was Bob Muglia and in was Frank Slootman, enticed out of retirement after his 6 years as CEO of ServiceNow ($NOW). Over his 6 year tenure (2011-2017), he not only took them public, but also grew their run rate from $75M to $1.5B. Before that, he was CEO of Data Domain, a data storage company ultimately acquired by EMC (now part of Dell).

he BOD is full of industry-aware high-level folks from ServiceNow, VMWare/Dell/EMC, BMC Software, Adobe, & Symantec. It also has some direct competitors on the board, between the CFO of Cisco and the CEO of Arista.
#### What They Set Out to Solve (aka More About Data Warehouses Than You Wanted to Know)
Transactional Database = What you typically think of as a database (from Oracle, SQL Server, Postgres, or MySQL) is one honed for online transactional processing (OLTP) workloads. This kind of database is highly tuned for relationships between data sets and for handling complex transactions between them. [An example of a database transaction is a bank transaction, such as transferring cash from your checking account to your mortgage as payment. The system must assure it either all gets processed (across multiple records and tables), or is all rolled back if something goes wrong.] This kind of database is built around create/read/update/delete (CRUD) actions on individual records, and for interlinking related records between data tables while querying (joins).  The primary users are the developers of APIs or apps that are accessing it, or business users for monitoring & reporting on operations.

Structured Query Language (SQL) = Special purpose programming language used to craft data queries and database manipulation commands. It is the defacto standard for querying relational databases.

Data Warehouse = Data Warehouse databases, on the other hand, are honed for online analytical processing (OLAP) workloads, in order to have vision into the entire enterprise's operations. This is a structured data store that is filled with pre-processed (refined) data, to be used for analyzing the business. Primary users are business analysts (with operational knowledge) that are tracking performance of business metrics and doing related actions around it, like forecasting, planning, budgeting, & financial reporting. Unlike transactional databases, this kind of database is not geared for working with individual records, but is instead optimized around isolating and grouping like data (e.g. analyzing sales totals per region, or per sales agent, or per product category, or per product).

Data Mart = Smaller data warehouses specially made-to-purpose for a specific team's use. If a Data Warehouse is the grocery store for your data, Data Marts are the corner markets. Companies might create separate mini-warehouses for sales, marketing, finance, HR, operations, or development teams -- whoever needed it. This could help offload the compute needed for all the queries being made, so that each team's needs were isolated from the other teams, and so could be spread across multiple database systems.

Data Refinement = To make best use of a data warehouse, the raw data from transactional databases and other sources is processed in advance around pre-defined business objectives, and is then imported into the data warehouse and analyzed from there, typically with BI tooling (like Tableau, PowerBI, or Qlik) for visualizations, dashboards, or interactive (ad-hoc) querying. The refining process would typically involve taking the raw data from multiple sources, merging it into a single dataset (blending), then cleaning, enriching, filtering, sorting, removing personal info (scrubbing), and/or de-duplicating it further. This data processing is typically done in a separate staging area (likely a separate database), then imported into the Data Warehouse once refinement is complete.

Business Intelligence (BI) = The process of analyzing operational data in order to extract actionable information, and help business users (typically executives and managers) measure operational performance, to make informed decisions and forecasts.

数据仓库专门针对 BI 分析进行了磨练。用户主要是数据分析师和具有特定业务目标的业务用户，他们希望从中获得愿景并从中提取见解。

有关如何构建数据仓库和工作流，有两种主要方法。在一个（Inmon 方法）中，您可以将所有优化的数据放入集中式数据仓库中，并选择性地创建数据集市供特定团队使用。在另一种方法（Kimball方法）中，您将首先创建更严格的数据集市，然后将它们全部汇集到一个集中的存储中，以查看整个业务。无论哪种方式，您最终都会得到一个有价值的、集中的精细数据池，管理层可以在其中全面了解业务，并将其用作跟踪运营指标的来源。

虽然高层管理人员喜欢它获得的可见性，但数据仓库对所有其他相关方都有一些重大负面影响。
在云时代之前，数据仓库是在本地构建的，并且必须在一个必须非常强大的系统（大量内核、内存和存储）上运行。

Why is it so hard to work with data warehouses?

Dimension = 维度 = 业务分析师想要分析的数据中的特定因素，并用作聚合（汇总）数据的分组。数据分析中的维度可以被认为是图形上的维度（x 轴、y 轴、z 轴等）。例如，在分析销售数据时，经理可能希望按地区、州、销售人员或产品计算和汇总销售额——这些都是一个单独的维度。开始添加其他数据源，如供应链、物流和库存数据，它可以大大放大维度的数量。随着数据查询变得越来越多维（例如，按产品、区域、销售人员聚合销售数据），它使数据越来越难以分析，这反过来又需要越来越多的资源（计算和内存）来完成。

Ingest Process = 引入过程 = 将数据从原始孤岛中取出并将其加载到数据仓库中。

Extract, Transform, & Load (ETL) = 提取、转换和加载 （ETL） = 典型的摄取过程，用于将数据从数据系统中导出，对其进行操作以优化数据以进行分析查询，然后导入数据库。对于数据仓库来说，这是一个困难的过程，因为它需要围绕特定目标优化数据集。数据集最终以最终格式结束，其中包含业务分析师想要查询、报告和分析的每个维度。

OLAP Cubes = OLAP 多维数据集 = 进一步细化数据仓库数据集的过程，以跨所需的每个多维分析组合预先聚合数据。通过创建 OLAP 多维数据集，分析师可以预先进行计算，从而帮助减少最终分析期间所需的计算量。如果您熟悉Excel，它基本上是创建一系列巨大的数据透视表 - 一个数组，每个数据透视表都填充了数据聚合数组上的数组，跨越数据中多个维度的每个组合。

在最初的ETL阶段，分析师必须将原始数据细化为重组数据的专用格式，以便使其更理想地提取他们关心的维度（业务目标）的见解。这样做的严重缺点是，它迫使分析师不得不做出许多前期假设，这反过来又使整个过程变得极其不灵活。

This workflow had 2 primary roles:

Data Engineer = The role responsible for cataloging and extracting data out of original sources and into the data warehouse, including the pre-processing (refinement) of data, and then helping move data through the Warehouse and Marts.

Data Analyst = The role responsible for extracting insights from the data. They focus solely on the specific business objections provided by business users, like upper management and managers. They work with the Data Engineers to refine the data for initial ingest, and then further refinement again into OLAP Cubes – as it all requires operational knowledge of the data, such as what dimensions & values are needed.

最终，数据仓库系统变得集群化，这开始允许数据分析师能够更即时地执行这些操作，而不是做出许多预先假设。但是集群系统放大了成本和头痛 - 您仍然必须管理多个系统来运行集群，并且由于软件架构难以使用，维护是一场噩梦。这些系统成为IT管理以及数据工程师和分析师的巨大头痛，因为管理层需要越来越多的洞察力（添加新数据集，添加新维度）。
#### Send in the Cloud
云的近乎无限的规模彻底改变了可以实现的目标。围绕数据仓库的许多流程，如OLAP Cubes，都是围绕这些原始的本地需求构建的，当时用户受到可用计算和存储资源数量的高度限制。云的规模和弹性允许分析数据库的架构发展，并出现了一种新的范式。

Data Lake = Using a centralized database as a vast pool for holding all of an enterprise's raw data. It can contain structured (relational data) as well as semi-structured (NoSQL) data, and allows for a common query interface over it. This allows users to further refine the data to import into a Data Warehouse from there for BI. But better yet, the database could be running analytics directly over the raw data. The benefits of a Data Lake are that it enables data scientists to extract new insights from raw data collected from across the entire enterprise (analytics that are not just around specific pre-determined business objectives), and enables centralized data sharing across the entire enterprise (data could be viewed across all regions, segments, departments, or teams).

Extract, Load & Transform (ELT) = Changing the ETL process to eliminate needing a staging area. The load ("L") is done before the transform ("T"), meaning all of the raw data is now directly loaded into the Data Lake, which can then serve as the staging area to further refine the data from there, using SQL-based tooling.
提取、加载和转换 （ELT） = 更改 ETL 过程以消除对暂存区域的需求。加载（“L”）在转换（“T”）之前完成，这意味着所有原始数据现在都直接加载到数据湖中，然后可以作为暂存区域，使用基于SQL的工具从那里进一步细化数据。

Data Scientist = Analytical & statistical expert that tries to find trends and insights from vast quantities of structured and semi-structured raw data, in order to make predictions based on past patterns. This is different than data analysts, who are more focused on extracting metrics around specific business objectives.

数据湖的主要优势是显而易见的 - 它成为所有数据的集中存储。这消除了孤岛，但也可以作为您想要对这些数据执行的任何其他操作的跳板，尤其是数据分析。这不是一个静态的东西 - 数据湖的目标是自动不断提取数据。云近乎无限的规模使数据湖具有近乎无限的规模 - 它可以随着更多数据的流入而增长。旧数据可以保留，也可以在不再有用时存档。

数据湖不会取代数据仓库（就像数据科学家不会取代数据分析师一样）。对 BI 的需求 - 通过预先确定的业务目标查看数据 - 并没有消失！数据湖有自己的用途，但它也与数据仓库协调工作。拥有数据湖和数据仓库极大地简化了数据工程师的任务。在数据提取（ETL 的 E）期间，他们可以从集中式数据湖中提取所有原始数据，而不是从单独的数据孤岛中收集数据。在数据转换（ETL 的 T）中，它通过大大简化优化数据的方式，完全消除了对暂存区域的需求。相反，他们可以使用标准 SQL 查询来优化数据并将其写入新数据集，所有这些都直接在数据湖中完成。事实上，现在数据分析师可以直接完成这项工作，数据工程师可以只专注于数据移动（提取和加载）。
#### Age of Analytics
作为一个巨大的运营数据池，数据湖已成为数据科学的首选平台，尤其是机器学习 （ML）。像Apache Hadoop这样的开源分布式分析平台正在被利用，这些平台在关注点分离方面有更好的实践（将存储引擎与计算引擎分开，但将它们并排分布）。Hadoop使公司能够拥有一个数据湖（分布式存储），可以直接对该数据进行查询和分析（分布式计算）。大多数人涌向一个名为Hive的Hadoop模块，该模块允许对存储在Hadoop中的任何数据使用通用SQL查询接口。但是Hadoop再次需要运行极其复杂的软件集群 - 并且再次成为IT和数据科学家管理和使用的皇家头痛问题。使用Hadoop和Hive肯定比早期的数据科学工具更快（需要提前几天的数据细化），但仍然感觉很慢 - 洞察力可能需要数小时或数天才能从存储在其中的大量（并且不断增长的）数据中提取出来。

Hadoop中的分析工具进一步发展，一个名为Apache Spark的模块最终作为一个独立的分析平台从该生态系统中脱颖而出。它是一个开源的分布式分析软件，使Hadoop的计算端变得更快。数据首先跨集群中的分布式节点加载到内存中，因此从那里对其执行的所有分析任务都可以完全在内存中完成，而不是在存储层上工作。这可以使某些操作比Hadoop / Hive快~100倍，并且突然之间答案可能会在几秒钟或几分钟内出现，而不是几小时或几天。Databricks公司是围绕开源Spark引擎创建的，以增强和支持它。

Apache Spark已成为当今使用的主要数据科学和机器学习工具之一。但除此之外，数据科学家仍然使用MATLAB等原始统计工具，或者使用Python，R，Java或C++等编程语言编写脚本，利用大量可用的分析库和框架（TensorFlow，Pandas，Numpy，Pytorch，Scikit-learn）。

What makes Snowflake so special?
### Platform Architecture
不要将Snowflake视为“只是一个云数据仓库”。这是两全其美的;它经过高度优化，既是数据湖又是数据仓库。它是一个数据湖屋 - 一种将两个工作负载的最佳功能与不同的用户群和用例相结合的新范例。

#### SQL Interface
Snowflake以 “snowflake schema”（结合创始人对滑雪的热爱）命名，这是一种数据仓库方法，将传统的市场仓库（Kimball）布局与关系SQL数据库相结合以进行维度查找。这完美地总结了该平台的双重用途——它是一个分析数据库，具有对整个数据湖的SQL查询功能。

What this means is that you can throw ANY data at it.
#### Analytical Data Cloud
Snowflake gives you all of these things in one single package.
However, all of the cloud providers are moving into this same direction, and now have data lake AND data warehouse AND analytical capabilities, AND have the near limitless scale of the cloud. But this is just the start of Snowflake's architecture. The platform has an incredible number of benefits it can leverage from here, that I believe are huge advantages over the other "all-in-one" data platforms that the individual cloud providers (who I consider are Snowflake's primary competitors) are creating.
#### Cloud-Neutral Vendor (Multi-cloud)
Snowflake的主要优势在于它可以在每个云提供商中运行。这最终使他们的客户能够采用多云战略
#### Leveraging the Native Features
Snowflake平台利用每个云提供商内的本地基础设施和工具，以尽可能提高性能。他们将平台的架构紧密设计到每个云提供商的本机服务上：他们使用每个提供商内的本机存储功能，以及尽可能靠近它的计算资源。

在所有3家云提供商中，他们维护自己的一组分布式平台集群，其下是共享存储和云服务层，而每个客户都有自己独立的计算节点。这使得多平台集群（在每个云提供商下运行，跨多个区域和可用区）尽可能高效 - 计算引擎位于它正在处理的存储层所在的同一数据中心。
#### Flexible Simplicity
Snowflake 是一个多云交钥匙 SaaS 提供商 - 无需维护基础设施，也无需系统集成即可使用它。他们大力吹捧这一点，并有意减少可以在平台内完成的配置和调整量。他们将其设计为非常易于采用和使用，从用户的角度来看，外观和感觉就像一个关系数据库。
### Optionality
#### Wide Number of Use Cases

#### Wide Number of Enterprise Users
Data Engineers (Ingest), for importing & managing the data, or pulling in datasets from others
数据工程师（摄取），用于导入和管理数据，或从其他人那里提取数据集
Business/Data Analysts (BI), tracking operational metrics for Mgmt, Sales, Marketing, Finance teams
业务/数据分析师 （BI），跟踪管理、销售、营销、财务团队的运营指标
Data Scientists (Analytics), using ML to extract further insights
数据科学家（分析），使用 ML 提取更多见解
Citizen data scientists (BI & Analytics), merging the business analysts with the data scientists
公民数据科学家（BI和分析），将业务分析师与数据科学家合并
Developers (DBaaS), using it as the data store of their app/service
开发人员 （DBaaS），将其用作其应用程序/服务的数据存储
Data Brokers (Data Marketplace), as publishers of data
数据代理（数据市场），作为数据发布者
Operational users, like sales & marketing (Data Marketplace), to manage subscribers to published or monetized datasets
运营用户，如销售和营销（数据市场），用于管理已发布或货币化数据集的订阅者

我看到用户类型覆盖解决方案，如下所示：

#### Cloud-within-a-cloud
Snowflake平台具有高可用性（HA），因为它们在每个云提供商中利用多个平台集群，然后将它们分布在多个云区域和可用性区域以实现数据冗余（弹性和业务连续性），确保其平台始终可用并将其分布到全球。但这也提高了性能（因为在其上运行的工作负载是分布式的），并赋予平台弹性（新的平台集群可以根据需求向上或向下旋转）。

在任何平台集群中，客户都可以启动“虚拟仓库”（私有虚拟集群）来处理其特定的计算需求。

客户可以根据他们将要执行的摄取和查询量，从他们想要的特定级别开始。但他们可以随时调整大小（纵向扩展或缩减），以减小或增加其虚拟仓库中的大小（计算节点的数量）。如果由于任何原因需要闲置，用户可以暂停他们的虚拟仓库，这反过来又会暂停计费。所有这些结合在一起，为客户提供了巨大的灵活性和规模。

大多数客户在共享平台基础结构中为自己创建单个专用虚拟群集，并由平台处理其余部分。但更高级别的客户可以走得更远，创建“多集群虚拟仓库”，可以启动 2-10 个独立的虚拟集群，这些虚拟集群都充当一个大型连续数据库。这使较大的客户能够更多地利用冗余功能，确保访问冗余功能的数据服务具有更高的可用性，并在其数据湖屋的运行方式方面实现更大的灵活性 - 例如数据的地理位置分散，将某些工作负载与其他工作负载隔离，或者在单独的虚拟群集中将频繁使用的“热”数据与不常用的“冷”存档数据（每个存档数据具有不同大小的计算层）分开。
#### Single Copy of Data
As you create refined datasets for BI purposes (what the traditional Data Warehouse was for), the underlying data is not actually copied into separate places. A single source of the data exists in the storage layer – and that is it.
#### Data Sharing
他们的服务层控制其共享平台集群中的所有数据访问。这反过来又使客户能够轻松共享和发布数据。它不会制作数据的克隆或副本 - 它全部通过访问权限处理，并使用指针跳转到要共享的数据段所在的位置。这是 Snowflake 平台与竞争对手的巨大区别

由于 Snowflake 允许您轻松地向其他人公开数据集，因此这为围绕“已发布数据”创建的全新业务类型打开了平台。数据集可以向所有人公开（例如最近的 COVID-19 数据和仪表板），也可以作为用户可以订阅的货币化数据集公开。
像Trade Desk（$TTD）和Zillow（$Z）这样的公司允许订阅者从各自的平台访问匿名数据集。自行车共享提供商Lime正在向城市公开乘客和路线数据，以帮助促进智能移动和自行车安全计划。
该平台还赋予了全新的客户类型。可以建立仅存在于Snowflake Data Marketplace上的新公司，这些公司仅专注于成为用于数据丰富的已发布数据集的提供商。这使得数据代理的兴起成为可能。像FactSet和Weather Source这样的公司可以围绕Snowflake Data Marketplace建立他们的整个业务。
#### Distributed Compute
but the most exciting part is the analytical engine.
Snowflake还允许将数据科学工具直接嵌入到分布式计算层中。[为什么我说Snowflake类似于Hadoop-as-a-Service。独特的是，这一切都是雪花的内联。对于其他平台，您需要使用外部工具来进行分析（通常将其连接到云平台中的本机Spark和ML引擎，如AWS SageMaker或Azure ML）。
#### Data Ingest
该平台具有丰富的数据管道功能，可以从批处理或实时数据导入。Snowflake 可以处理连续的数据，因为它可以不断扩展。
Alteryx是数据准备方面的合作伙伴，Datameer，Streamsets，Talend，AWS Glue，IBM DataStage，Informatica，Fivetran等也是如此。
#### Developer Tool
Snowflake平台确实支持符合ACID的事务，但让我们明确一点 - 它不是一个“普通”数据库，也不会取代关系或NoSQL数据库的许多用例。如果应用需要对大量单个记录进行查找和更新，则这不是首选数据库。但是，如果应用程序或服务本质上是分析性的（对单个字段进行汇总聚合，或分析大量数据），那么 Snowflake 是作为云原生数据库提供商的绝佳选择......一个可以根据需要扩展的。
MongoDB将自己定位为分析数据存储，并围绕这一重点推出了多种产品，包括Atlas Data Lake以及Atlas用户如何利用隔离的分析节点。Snowflake的主要目的很好地解决了这个用例 - 不仅在半结构化数据上，而且在结构化（关系）数据上也是如此。
### Unique Database Features
#### External Functions
它可以调用任何基于 HTTP 的服务，包括 AWS Lambda 上的无服务器函数等（因此可以用任何语言编写）。
#### Data Masking
Snowflake允许数据所有者通过称为动态数据掩码的功能动态控制谁可以看到哪个字段。
#### Data Recovery
Snowflake具有一项名为“时间旅行”的功能，该功能可跟踪设定的时间范围内（基于定价层）内数据的所有更改或删除。它充当历史审计跟踪，允许客户随着时间的推移向后退（类似于 MacOS 上的时间机器备份），因此他们可以恢复丢失的数据或还原对数据或数据库结构（架构）的错误更改。
### Platform Tiers
#### Centralized Storage
基础原始数据位于列式存储中，这些存储经过压缩和加密。客户无权访问共享存储中的原始文件 - 所有访问都由服务层管理并由计算层执行。
#### Compute
计算由用于引入、查询和分析的计算节点群集组成。与存储和服务层不同，该层中没有共享的内容 - 每个客户都有自己的专用计算集群，称为虚拟仓库。
计算层利用每个云提供商中的本机计算引擎，以便在物理上尽可能靠近其覆盖的存储。
#### Services
#### Data Sharing
#### Integrations
A sampling of the many partners & tools available:
- Ingest/Refine Tooling: Alteryx, Datameer, Streamsets, Talend, AWS Glue, IBM DataStage, Informatica, Fivetran, Rivery.io, Snowplow, Matillion, Segment, dbt.
- BI Tooling: Tableau, Azure PowerBI, Qlik, Sigma, ThoughtSpot, Looker (Google), AWS QuickSight
- Data Science Tooling: Qubole, Alteryx, Zepl, Dataiku, Databricks (Spark-as-a-service), DataRobot, Sisense, Domo, H20.ai, RapidMiner, BigSquid, AWS SageMaker
- Data Science Libraries (Inline in Compute): Apache Spark, TensorFlow, Pandas, PyTorch, scikit-learn, Jupyter, Zeppelin
#### Snowsight
Snowflake 于 2020 年 6 月发布了一个名为 Snowsight 的新分析 UI，该 UI 来自一年多前收购 Numeracy。它提供了一个带有可嵌入图表的交互式 SQL 编辑器，因此业务分析师可以创建自定义仪表板来监视数据并提供见解。
#### Pricing
每个客户根据他们想要的响应能力和性能来确定他们希望使用的存储和计算大小。客户只需为他们在存储和计算之间使用的内容付费。计算平面和存储平面的分离意味着您可以根据需要独立扩展任何一侧。

客户需要支付以下费用：
- A fee per terabyte of compressed data stored, averaged per month, billed in arrears.
- Virtual warehouse (the scaled compute layer each customer spins up for ingest and querying) is billed by the compute-second, with a one-minute minimum. Customers can deactivate it when not utilizing it.
- Cloud Services (the services layer that provides data management, coordination, security, and ancillary services) can also be billed. Typical utilization of the standard services is free, but heavy users will see incremental charges above the norm. A few ancillary serverless functions exist that cost by second of usage for the exact compute time used.
- Data transfer fees, to recoup cloud provider fees if transferring data between cloud regions or out of a cloud provider.
### Customers
Customers include Capital One, Square, S&P Global, Bankrate, Sony, Adobe, Akamai, Square, Blackboard, Lime, Instacart, Sainsbury's, Neiman Marcus, Boden, Cemex, Paccar, Micron, Hubspot, Coupa, Talend, Overstock, Office Depot, A&E, EA, LionsGate, McKesson, Logitech, Doordash, Penguin Random House, RueLala, Rent the Runway, Univ of Notre Dame, Oregon State, ... and a crap ton of startups and apps and data brokers that have been built on top of their data cloud or Data Marketplace. Largest customer is Capital One, at 11% of revenue and shrinking – it is lowering because Snowflake is growing so fast, even as Capital One nearly doubled its spend YoY!!

Gartner Peer Insights（在数据仓库和云数据平台类别下）和G2上的客户评论往往给予很高的评价。一些为数不多的负面因素集中在UI上 - 但他们显然已经开始通过新的Snowsight产品解决这个问题。
### Competitors
主要来自云提供商本身（Snowflake的所有基础设施都必须依赖他们）。
#### Data Warehouse (OLAP)
Snowflake competes against a  number of deep-pocketed stalwarts – the cloud providers themselves.
- AWS Redshift
- Google BigQuery
- Azure SQL Data Lake
- Yellowbrick Data Warehouse (pure SaaS)
- Panoply Data Warehouse (pure SaaS)
#### Data Lake w/ Analytical capabilities
### Partnerships
- Dbt was built to manage the lifecycle of data refinement through the use of materialized views. This is allowing data analysts to drive the refinement process, not data engineers.
- Rivery.io, Snowplow, Segment, Matillion, and Fivetran are all SaaS startups that serve as an integration provider for data ingest, creating centralized & easily managed pipelines for exporting data out of SaaS applications and into cloud databases. These are greatly simplifying how data movement is handled by data engineers.
- 但尤其是 Segment，它远远超出了摄取的范围。它们充当数据库两侧的数据管道，特别关注客户数据。除了数据摄取之外，它们还允许创建管道以从数据仓库中提取分析见解，并将其加载回销售和营销工具中。这使业务用户能够深入了解客户/购物者/用户行为，以帮助进行产品创新和营销工作。它还提供软件开发工具，以便与移动应用程序和网站用户集成并从中提取见解 - 这似乎类似于Datadog的真实用户监控（RUM）产品。
- Sigma，Sisense和Domo是SaaS提供商，提供现代BI分析和仪表板工具，可以位于外部云数据仓库上，并帮助提取见解。这让业务用户可以做更多的事情，最大限度地减少与数据分析师合作的需求。而且它还消除了制作数据额外副本的需要，因为它们直接与云数据库集成。
#### Analytical Tools
Databricks是围绕开源Apache Spark的企业公司。他们是Spark即服务提供商，简化了Spark的使用（允许用户通过无代码UI而不是脚本开发ML）。他们已经能够将其云服务插入AWS和Azure，作为供应商中立的工具，以帮助企业管理和运行分析。他们还与Snowflake建立了合作伙伴关系，后者将其强调为采集管道（用于数据处理的Spark）和分析平台（Spark for ML）。Snowflake用于所有数据处理，安全性，性能和计算，Databricks用于从中提取所有见解。

但Databricks并没有停止前进。他们创建了一个名为Delta Lake的开源引擎（云存储上的服务层，使其成为可查询的数据湖），并且还直接与BI工具（Tableau，Qlik，Looker）集成。这是在上面的图表中消除雪花！Databricks还具有Snowflake最大的优势之一 - 供应商中立，并支持多云战略。
#### Citizen Scientists
