---
title: "Context Before Code: How Notion Put an AI Engineer on the Sales Floor to Discover What Actually Needed Building"
date: 2026-02-24T10:55:40Z
category: reading
description: "Notion 把 AI 工程师派到销售前线当 BDR 后发现：销售 AI 工具的瓶颈在于\"何时联系\"和\"联系谁\"这两步必须同时自动化——单独解决任何一步，对销售代表都没有实用价值。"
source: "https://www.firstround.com/ai/notion?ref=review.firstround.com"
---

## TL;DR
Notion 把 AI 工程师派到销售前线当 BDR 后发现：销售 AI 工具的瓶颈在于"何时联系"和"联系谁"这两步必须同时自动化——单独解决任何一步，对销售代表都没有实用价值。

## 核心洞见
两种建设模式：papercut（加速现有流程）与 new bet（重造流程），Bleier 各建一个。Chrome 扩展（papercut）把散落在多个标签页的联系人信息聚合到邮件草稿，三周内被整支团队采用。Salestino bot（new bet）由 SQL 查询驱动——当产品数据仓库检测到目标账户有新 workspace 创建，触发研究 agent 抓取公司与联系人信息，再生成三份定制邮件草稿，打包成一条 Slack 消息送到销售代表面前。

## 具体机制
研究 agent 选择开放网络而非内部有限数据集，但严格约束搜索轮次上限，防止在"找到正确的人"问题上无限发散。最棘手的部分是消歧：同名公司的区分，以及如何精确定义"值得关注的公司新闻"——定义含糊即撞墙。Chrome 扩展的部署障碍来自 MDM 配置变更，代码本身反而是次要问题。

## 隐藏限制
Bleier 刻意不预设指标——Notion 的产品哲学是先放入 beta 再看数据，但这需要组织有足够耐心和信任预算。**值得质疑**：30 名销售的非正式调研是目前唯一可见的效果依据，工具实际对转化率的影响未公开。

## 留下的那个想法
Bleier 说未来应该"假设自己写完代码后永远不会再维护它"——这条建议的前提，是工程师先用几周时间变成用户，才知道什么值得建。顺序颠倒了，原则就只是口号。
