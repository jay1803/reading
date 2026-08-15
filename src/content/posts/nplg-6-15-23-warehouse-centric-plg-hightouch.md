---
title: "NPLG: 6.15.23: Warehouse-Centric PLG (Hightouch)"
date: 2023-06-16T13:28:20Z
category: reading
description: "本文是 Notorious PLG 关于 Hightouch 公司如何利用以仓库为中心的策略来实施产品驱动增长 (PLG) 的文章。Hightouch 的联合创始人兼联合 CEO Kashish Gupta 分享了他们的 PLG 策略，解释了他们如何使用数据仓库和自家产品来将用户注册转化为收入。"
source: "https://notoriousplg.substack.com/p/nplg-61523-warehouse-centric-plg"
---

## 概述
本文是 Notorious PLG 关于 Hightouch 公司如何利用以仓库为中心的策略来实施产品驱动增长 (PLG) 的文章。Hightouch 的联合创始人兼联合 CEO Kashish Gupta 分享了他们的 PLG 策略，解释了他们如何使用数据仓库和自家产品来将用户注册转化为收入。

## 主题
- 🏠 数据仓库为中心: Hightouch 的 PLG 策略核心是使用数据仓库。Hightouch 将来自不同来源的数据统一到数据仓库中，并使用 dbt 进行转换和建模。然后，他们使用 Hightouch 平台将这些数据激活到业务团队日常使用的应用程序中，例如 Salesforce 和 Hubspot。

- ➕ 数据完整性: 这种方法有两个主要好处，其中之一是数据完整性。通过在数据仓库中使用 SQL 连接来自不同系统的数据，可以协调不同的对象类型，并对这些数据建模操作进行版本控制、组织、搜索和追溯。因为受众是在仓库中定义的，所以可以生成漏斗转化和实验报告。

- 🏃 业务团队速度: 另一个好处是业务团队的速度。将逻辑移动到仓库，然后通过 Hightouch 将其激活到下游工具，确保每个人都基于相同的客户定义进行操作。每个工具都会更新关键信息，如客户阶段和最近的操作。业务用户可以通过常规工具进行试验并与客户互动，而无需工程资源。

- 👨‍💻 PLG 团队: Hightouch 没有完全专注于 PLG 的人员，而是多个业务用户通过他们的常规工具和工作流程来影响增长。
