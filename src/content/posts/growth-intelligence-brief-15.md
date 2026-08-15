---
title: "Growth Intelligence Brief #15"
date: 2026-03-18T08:01:19Z
category: reading
description: "GPTBot 会在零反向链接、零权威的全新域名上线后几分钟内自动爬取，爬取密度是 Googlebot 的 470 倍——但高爬取量与能否在 ChatGPT 答案中被引用完全无关，两者走的是不同逻辑链路。"
source: "https://www.growth-memo.com/p/growth-intelligence-brief-15"
---

## TL;DR
GPTBot 会在零反向链接、零权威的全新域名上线后几分钟内自动爬取，爬取密度是 Googlebot 的 470 倍——但高爬取量与能否在 ChatGPT 答案中被引用完全无关，两者走的是不同逻辑链路。

## 发现
- 一个 $10 成本、纯 AI 生成的统计数据站（60K 页面）在上线 12 小时内被 GPTBot 请求超过 29,000 次，Googlebot 只来了 11 次。
- GPTBot 使用 `ChatGPT-User` user agent 仅爬取 642 次（截至 3 月 8 日），而 `GPTBot` user agent 爬取 78,000 次——前者用于实时检索答案，后者用于模型训练。
- 客户端分析工具（如 GA4）对约 98% 的 bot 流量完全不可见，只有服务器端日志才能区分爬取来源。

## 为什么重要
GPTBot 爬取量不是 AI 可见度的代理指标，被大量训练爬取的内容在 ChatGPT 引用中几乎不出现。进入训练集和成为实时检索的"引用来源"是两回事，大多数内容只属于前者。

## 破坏了什么常识
"被 AI 爬虫大量爬取"不是优化目标，也不表明你在 AI 搜索中有曝光。想出现在 ChatGPT 答案里，需要的是让 `ChatGPT-User` user agent 爬取你，而不是 `GPTBot`；可以通过 `robots.txt` 分别控制两者权限。

## 值得关注的细节
文章建议"屏蔽 GPTBot、保留 ChatGPT-User"，但未提供任何证据表明允许 ChatGPT-User 爬取能切实提升引用率——这仍是推断，不是验证过的因果链。

## 那个留下来的想法
GPTBot 的真正功能是替 OpenAI 建索引，而非替用户找答案。大多数站长把爬取当成曝光的证据，但这批数据直接说明：被爬不等于被见，甚至可能只是给模型做了免费的语料捐赠。
