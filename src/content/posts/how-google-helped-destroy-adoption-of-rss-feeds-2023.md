---
title: "How Google helped destroy adoption of RSS feeds (2023)"
date: 2026-08-18T00:16:00Z
category: reading
description: "Google 通过拥抱-扩展-消灭模式系统性地削弱了 RSS 生态：先整合 RSS 吸引用户依赖，锁定后再撤掉支持，五次核心废弃事件直接摧毁了普通用户对 RSS 的信任。"
source: "https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds"
---

## Google 对 RSS 消亡的结构性责任

Google 对 RSS 的损害不是偶然的功能废弃，而是一套完整的"拥抱-扩展-消灭"（Embrace, Extend, and Extinguish）模式：先将 RSS 整合进自家产品吸引用户依赖，等锁定成功后再撤掉支持，既不提供替代，也不给出理由。

### 五个核心废弃事件

- **Chrome RSS 按钮**：Chromium 早期内置 RSS 订阅按钮，可在地址栏自动识别当前页面的 Feed；无通知删除，无解释。
- **FeedBurner**（2007 年收购）：将原始 RSS Feed 替换为 Google 控制的私有 Feed，内嵌广告与追踪；2012 年关闭 API，2022 年削减绝大多数功能，导致大量订阅链接失效，订阅者无法迁移。
- **Google Reader**（2005–2013）：RSS 阅读器领域事实上的标准，终结时无替代方案、无迁移指引。负责该产品的工程师透露，项目存续期间内部"一直有人想干掉它"。Reader 的关闭直接导致大量用户不只是停用 Reader，而是彻底放弃 RSS。
- **Google Alerts RSS**：2008 年添加，2013 年删除（与 Reader 同期）；被批后短暂恢复，但此时用户信心已被 Reader 事件摧毁。
- **Google News RSS**（2002–2017）：2017 年 12 月完全移除，无理由。用户自定义 Feed URL 全部失效，而 Google 自有格式的链接继续正常工作。

### 为什么 Google 的行为比其他公司更有害

Google 的市场影响力意味着它对 RSS 产品的每一次关闭都会直接改变普通用户对"RSS 是否值得用"的判断。用户看到的不是某个小工具下线，而是一个信号：RSS 不可靠、不被支持、不值得迁移到。这种信任损耗是不可逆的。

### "重新支持"承诺不可信

2021 年，Google 宣布将在 Chrome 中重新引入 RSS 功能，但截至今日无任何进展。鉴于历史记录，即便该功能上线也不值得当作可靠基础设施来依赖。
