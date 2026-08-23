---
title: "What Was Matt Thinking?"
date: 2026-06-23T08:02:03Z
category: reading
author: "Ernie Smith"
description: "Matt Wright 1995 年高中时做了一套 Perl CGI 脚本放上网，出发点只是\"让别人也能有留言板和计数器\"。结果 WWWboard 成为互联网上第一个被大规模使用的论坛软件，他的网站 Matt's Script Archive 无意间成为早期 web 的基础设施之一。"
source: "https://feed.tedium.co/link/15204/17365463/matts-script-archive-retrospective"
---

## 普通人能用就是好软件，直到它不是

Matt Wright 1995 年高中时做了一套 Perl CGI 脚本放上网，出发点只是"让别人也能有留言板和计数器"。结果 WWWboard 成为互联网上第一个被大规模使用的论坛软件，他的网站 Matt's Script Archive 无意间成为早期 web 的基础设施之一。

但专业程序员看到的是另一回事：脚本充满安全漏洞。OpenCVE 上有多个 CVE，其中 CVE-1999-1479（textcounter 工具）评分 10.0 满分危急，允许攻击者以 root 身份在服务器上执行任意代码。密码文件放在根目录，URL 可以直接读取环境变量。2001 年 London Perl Mongers 专门建了替代项目 nms，目的就是做 drop-in 兼容但安全的版本。

作者的核心论点：普通人只要"能用"，不会花时间比较所有选项。这个模式就是今天 vibe coding 的前身。两者都是民主化工具，也都是安全团队的噩梦。把 vibe coding 批成"不懂代码的人制造的废物"或捧成"开发民主化革命"，都对，也都偏。

近期 worldwidemart.com 域名到期后被一个真正关心这段历史的人买下，重建成介绍 Matt's Script Archive 历史意义的页面——正是 vibe coding 做的，却做对了事。

Matt 只是想帮忙，而他确实帮了。
