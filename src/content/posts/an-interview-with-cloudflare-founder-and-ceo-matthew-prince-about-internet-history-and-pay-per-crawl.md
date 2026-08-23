---
title: "An Interview with Cloudflare Founder and CEO Matthew Prince About Internet History and Pay-per-crawl"
date: 2025-10-10T00:35:28Z
category: reading
author: "Ben Thompson"
description: "Matthew Prince，Cloudflare 联合创始人与 CEO。犹他州长大，6 岁获赠 Apple II 起步，本科主修英语文学（同时担任学生网络管理员），后取得法学学位（John Marshall 法学院兼职讲师），再入哈佛商学院，并在那里与 Michelle Zatlyn、Lee Holloway..."
source: "https://stratechery.com/2025/an-interview-with-cloudflare-founder-and-ceo-matthew-prince-about-internet-history-and-pay-per-crawl/"
---

## 嘉宾背景
Matthew Prince，Cloudflare 联合创始人与 CEO。犹他州长大，6 岁获赠 Apple II 起步，本科主修英语文学（同时担任学生网络管理员），后取得法学学位（John Marshall 法学院兼职讲师），再入哈佛商学院，并在那里与 Michelle Zatlyn、Lee Holloway 共同创立 Cloudflare（2009 年）。此前创立反垃圾邮件公司 Unspam，并与 Lee 共同搭建 Project Honey Pot（全球垃圾邮件溯源蜜罐系统）。

## TL;DR
AI 答案引擎正在打破 Google 维系 25 年的"流量换内容"旧契约；Cloudflare 的应对不是向 AI 公司施压，而是在基础设施层制造"可计量的抓取稀缺"，逼出一个能让独特内容被持续定价的新市场——即便没有 Cloudflare，这件事也迟早发生。

## 每一个产品都是被问题逼出来的，不是规划出来的
Cloudflare 的初衷只是"把防火墙放进云端"。真正驱动产品扩张的是意外客户带来的意外攻击：NGO 入驻引来黑客压测，给出了大量真实攻击数据；黑客入驻后反过来持续测试安全边界，推动更严密防护迭代。域名注册商是因为 cloudflare.com 差点被劫持而自建；Zero Trust 是没有第三方能处理其自身规模；Workers 是为了内部构建沙箱。每个"问题→自研→产品化"循环形成今天的产品矩阵，Prince 总结为："我们制造一系列问题，然后自己解决它们。"

## "运行过冷的资源"比瓶颈更值得盯
每季度的 hot & cold 会议：团队不只问"哪里在瓶颈"，同样要问"哪里的已付费资源尚未充分利用"。Prince 把这比作发现吧台厕所里还能卖广告位——一旦意识到空间可被变现，存量就变成新收入流。Workers、R2 等均源于此类"冷资源"的盘活，而非自上而下的战略规划。

## 网络思维 vs. 数据库思维：超大云与 Cloudflare 是错位而非竞争
超大云的本能是 DBA 思维：留住数据，数据库是宇宙中心。Cloudflare 的本能是网络管理员思维：把数据搬走越快越好。两者目标天然相悖，因此超大云的网络产品一般，Cloudflare 的数据库产品也一般——这反而是生态位稳定的基础。多云格局（AI 时代加速出现）需要一个跨云的"网络合理层"，正是 Cloudflare 最有利的位置；AI Agent 的频繁跨网调用已成为 Workers 最大的增长驱动。

## Google 付了 25 年的账，Answer Engine 让这张旧账单作废
旧契约：Google 抓取内容，换给站点流量，流量变广告收入。Answer Engine 直接给答案，95% 的用户不再点击来源——体验更好，但流量不再产生。同等 token 量的 Reddit 授权费是传统媒体的 7 倍：Reddit 的用户生成内容不可复制，而《纽约时报》与《华尔街日报》对 LLM 而言事实基本可互换，溢价空间稀薄。Prince 的结论：独特性越高、本地化程度越深的内容，在新市场里将获得最大议价权——地方报纸可能会比此前更值钱。

## Cloudflare 制造稀缺，但拒绝裁判内容价值
Prince 明确划清边界：Cloudflare 可以阻止攻击、对爬取收费、构建可计量的访问通道；但"哪些内容有价值"不是它该做的判断。提议的市场框架：各 AI 平台按自己算法对内容排序（质量与信誉两个维度），基础设施层只做计量撮合；Perplexity 在被封锁后通过 Trade Desk 广告数据反向重建内容、加上作者署名发布的案例（Prince 称其为"直接的欺诈"），说明基础设施层必须具备执行能力——但这与充当内容编辑是两件事。

## 留下的那个想法
Prince 向每位 AI CEO 寄出亚里士多德《政治学》并签名。这个细节比整场 pay‑per‑crawl 讨论更耐人寻味：一个本来打算逃离父亲 Hooters 餐厅、误打误撞进入商业世界的人，最终用基础设施权力推动互联网内容秩序的重建。他一直在强调制度设计先于技术——这才是这场战役真正的主战场，而不是哪家公司的反爬策略。
