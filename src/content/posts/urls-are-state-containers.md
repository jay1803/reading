---
title: "URLs are state containers"
date: 2025-11-04T11:14:00Z
category: reading
description: "URL 状态的价值远超\"刷新后不丢失\"：它是 CDN 缓存键、SEO 索引维度、分析漏斗路径、A/B 测试变量载体。这些附赠收益，Redux 和 Zustand 一个都给不了。"
source: "https://alfy.blog/2025/10/31/your-url-is-your-state.html"
---

## TL;DR
URL 状态的价值远超"刷新后不丢失"：它是 CDN 缓存键、SEO 索引维度、分析漏斗路径、A/B 测试变量载体。这些附赠收益，Redux 和 Zustand 一个都给不了。

## 哪些状态该进 URL
- 进：搜索词、过滤条件、分页排序、视图模式（列表/网格/暗色主题）、日期范围、选中 tab、功能开关
- 不进：密码/token/PII、modal 开关、正在输入的表单、高频瞬态（滚动位置、鼠标坐标）
- 判断标准：同一 URL，另一个人打开后应该看到一样的状态吗？是 → 进 URL；否 → 别放

## 实现要点
- ~URLSearchParams~ 原生读写；~history.pushState~（新增历史条目）vs ~replaceState~（覆盖当前条目，不污染 Back 栈）
- 默认值在代码里处理，不写进 URL：避免 ~?theme=light&page=1&sort=date~ 这类参数噪音
- 高频更新（搜索框逐字输入）用 debounce + ~replaceState~；用户主动切换过滤项用 ~pushState~
- React Router / Next.js 的 ~useSearchParams~ hook 封装了上述逻辑

## 隐藏限制
URL 长度理论上 2000–8000 字符，但真正的上限由浏览器、服务器、CDN、搜索引擎爬虫各自实现共同决定——没有统一标准。若需要 base64 编码一整段 JSON 才能塞进 URL，状态已超出 URL 应承担的边界；URL 作为合约的价值也就消失了。

## 留下的那个想法
PrismJS 把完整构建配置压进一行注释 URL，不需要 README，不需要截图，换台电脑打开就复原——真正好的 URL 设计是让 URL 自己说话，而不是让你去解释它。
