---
title: "Pluralistic: The web is bearable with RSS (07 Mar 2026)"
date: 2026-03-27T08:01:05Z
category: reading
author: "Cory Doctorow"
description: "Google 2013 年关闭 Reader，不是因为 RSS 失去价值，而是因为 RSS 的核心功能——帮用户发现和分享新页面——直接威胁 Google 正用 G+ 取代 Facebook 的战略：他们宁可杀死一个好工具，也要为一个死产品清路，结果两手落空，把用户推给了 Facebook。"
source: "https://pluralistic.net/2026/03/07/reader-mode/"
---

## TL;DR
Google 2013 年关闭 Reader，不是因为 RSS 失去价值，而是因为 RSS 的核心功能——帮用户发现和分享新页面——直接威胁 Google 正用 G+ 取代 Facebook 的战略：他们宁可杀死一个好工具，也要为一个死产品清路，结果两手落空，把用户推给了 Facebook。

## 核心主张拆解
- 网络"屎化"是可命名的具体政策决策，不是市场铁律：Google 的 G+ 押注、Meta/Twitter 对开放 web 的绞杀、EU 把 cookie 弹窗等同于 GDPR 合规——都有具体责任人。
- G+ bonuses 绑定 engagement 指标是 Goodhart 定律的教科书案例：所有产品被塞入 G+ 入口，数字好看，体验崩溃；今天 AI 功能强塞的逻辑与之完全相同。
- 移动端"简化体验"的承诺实质是剥夺用户定制权——这不是副作用，是对平台和广告商的开放邀请；App 更进一步，用 IP 把"改进"入罪。

## 个人去屎化工具包（Firefox Desktop）
RSS 阅读器（如 Newsblur，$36/年）是第一层防线——大量网站仍发布全文 RSS feed，可在阅读器内绕开广告/弹窗/登录墙直读。无全文 feed 时的降级链：
1. Activate Reader View 插件 → 强制所有页面进入阅读模式（部分网站需 reload 触发全文）
2. Kill Sticky bookmarklet → 删除不滚动的浮层元素（订阅弹窗/cookie banner）
3. JavaScript Toggle → 对 JS 地狱网站建脚本黑名单
4. Element Blocker → 最后手段，逐元素删除页面杂质

## 收束行
移动端没有这些出路：iOS 上所有浏览器都是 Safari 皮，App 以 IP 为盾将改进入罪——去屎化的技术自由始终是桌面端的特权，这本身就是一个关于谁真正拥有你设备的声明。
