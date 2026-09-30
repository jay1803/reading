---
title: "google.com/goto: Google's anti-scraping update"
date: 2026-09-30T15:45:52Z
category: reading
description: "Google 正把搜索结果链接改写为 google.com/goto?url=...，需读取 Location 响应头才能获得真实目标网址，进一步抬高批量抓取 SERP 的成本。"
source: "https://www.autom.dev/blog/google-search-goto-links"
author: "1e1a"
---

Google Search 正把自然搜索结果的链接改写为 `google.com/goto?url=...`，让批量抓取结果网址的人必须逐条向 Google 发起请求。旧版 `google.com/url?q=...` 会在参数里暴露经过 URL 编码的目标地址；新版 `goto` 的 `url` 参数无法离线解码，看起来更像指向 Google 索引记录的不透明标识。要取得真实网址，可以请求 `/goto` 并读取响应的 `Location` 标头，无须继续跟随重定向。搜索结果页仍需显示域名、favicon 和来源信息，因此页面其他位置也留有网址线索，但这与读取 `Location` 是两条不同的路径。

截至 2026 年 8 月下旬，这种链接已从少量搜索结果扩展到未登录和无痕浏览时持续出现；Autom 观察到，这些条件下的结果链接实际上几乎全是 `goto`。以前，抓取者解析一次搜索结果 HTML 就能收集其中的目标网址；现在，每条结果都要额外请求 Google。连续解析数百条链接会增加耗时，也让 Google 更容易识别批量抓取行为。结合此前移除 `&num=100`、收紧 BotGuard/SearchGuard 的措施，这项改动进一步抬高了 AI 爬虫和 SEO 抓取工具建立搜索结果索引的成本。

Autom 已更新其 Google Search 流水线：读取 `goto` 响应的 `Location`，再把目标网址放回 API 原有的结构化字段，现有客户无需修改集成。由于 `goto` 仍可能处于实验或持续调整阶段，Autom 表示会继续监测格式变化。
