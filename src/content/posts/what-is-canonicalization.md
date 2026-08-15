---
title: "What is canonicalization"
date: 2023-09-19T10:29:06Z
category: reading
description: "规范网址是 Google 从一组重复网页中选择最具代表性的网页的网址。"
source: "https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting"
---

规范网址是 Google 从一组重复网页中选择最具代表性的网页的网址。
网站可能有重复内容的原因有很多：
- Region variants: for example, a piece of content for the USA and the UK, accessible from different URLs, but essentially the same content in the same language
- Device variants: for example, a page with both a mobile and a desktop version
- Protocol variants: for example, the HTTP and HTTPS versions of a site
- Site functions: for example, the results of sorting and filtering functions of a category page
- Accidental variants: for example, the demo version of the site is accidentally left accessible to crawlers
### How Google indexes and chooses the canonical URL
(that is, if only the header, footer, and other non-critical text is translated, but the body remains the same, then the pages are considered to be duplicates).
## How to specify a canonical with rel="canonical" and other methods
若要向 Google 搜索指定重复网页或非常相似网页的规范网址，您可以使用多种方法指明您更愿意使用哪个网址。这些方法按照其对规范化的影响程度排列如下：
- 重定向：强信号，表明重定向的目标应成为规范网址。
- rel="canonical" link 注释：强信号，表明所指定的网址应成为规范网址。
- 站点地图包含：弱信号，有助于站点地图中包含的网址成为规范网址。
### 最佳实践
无论使用哪种规范化方法，都请遵循以下最佳实践：
- 请勿使用 robots.txt 文件进行规范化。
- 请勿使用网址移除工具进行规范化，它会在搜索结果中隐藏网址的所有版本。
- 请勿使用不同的规范化方法为同一网页指定不同的规范网址（例如，请勿既在站点地图中为某个网页指定一个规范网址，又使用 rel="canonical" 为同一网页另行指定一个规范网址）。
- 我们不建议使用 noindex 阻止选择单个网站中的规范网页，因为这样会完全阻止该网页显示在 Google 搜索结果中。rel="canonical" link 注释是首选解决方案。
- 在网站中提供链接时，请链接到规范网址（而非重复网址）。 始终链接到您认定的规范网址有助于 Google 了解您偏好的网址。
## 避免在 Google 新闻中出现重复的报道
如果您将报道转载到其他新闻网站或您自己的网络中的其他网站，其他网站可以向您的报道添加以下漫游器元标记：

<meta name="Googlebot-News" content="noindex">

此标记可阻止 Google 新闻将您的内容转载版本编入索引。

若要限制转载内容出现在 Google 新闻和 Google 搜索中，其他网站可以向您的报道添加以下漫游器元标记：

<meta name="Googlebot" content="noindex">
