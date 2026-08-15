---
title: "Rel=Confused? Answers to Your Rel=Canonical Questions"
date: 2023-09-19T11:58:52Z
category: reading
description: "Officially, the answer is “no” – Google does not recommend this. They recommend that you either rel=canonical to a “View All” page (if having all results on..."
source: "https://moz.com/blog/rel-confused-answers-to-your-rel-canonical-questions"
---

### (1) Should I Use Rel=Canonical for Pagination?
Officially, the answer is “no” – Google does not recommend this. They recommend that you either rel=canonical to a “View All” page (if having all results on one page is viable) or that you use rel=prev/next.
### (2) Can I Use Rel=Canonical Cross-domain?
Yes – in late 2009, Google announced support for cross-domain use of rel=canonical. This is typically for syndicated content, when you’re concerned about duplication and only want one version of the content to be eligible for ranking.
### (3) Should I Use Rel=Canonical Cross-Domain?
That’s a tougher question. First off, Google may choose to ignore cross-domain use of rel=canonical if the pages seem too different or it appears manipulative.
### (4) Should I Use Rel=Canonical on Near Duplicates?
一般来说，我认为最好为重复项或非常接近的重复项保留 rel=canonical。
### (5) Can I Put Rel=Canonical on the Canonical Page?
yes
### (6) Is It OK to Put Rel=Canonical on My Entire Site?
Yes
### (7) Should I Use Rel=Canonical or 301 Redirects?
从SEO的角度来看，它们不可互换。这是关键的区别 - 301重定向将访问者带到规范网址，而rel=canonical标签则不会。通常，这些方法中只有一种适合您的访问者。如果您确实想永久合并两个页面并删除重复项，请使用 301 重定向。如果您希望两个页面都可供访问者使用，但只有一个页面只显示在搜索结果中，请使用 rel=canonical。
### (8) Does Rel=Canonical Pass Authority/PageRank?
这很难衡量，但如果你适当地使用 rel=canonical，并且如果 Google 尊重它，那么它的行为似乎类似于 301 重定向。我们怀疑它会为指向非规范网址的链接传递权威/PageRank，但会有一些少量的损失（类似于301）。
### (9) Can I Chain Rel=Canonicals (+301s, 302s, etc.)?
一般来说，这是一个坏主意。充其量，它是草率的。在最坏的情况下，它可能根本不起作用，或者您可能会在整个链中失去显着的PageRank。尽可能避免使用链并在单个跃点中实现 rel=canonical。
### (10) Are Non-Canonical Pages Indexed?
我想他们会的。但是，作为SEO，非规范URL不再以任何有意义的方式存在。
### (11) Can Someone Else Rel=Canonical My Pages?
您不能同时拥有它 - 如果您有重复的内容，请删除它，控制它或改进它。
