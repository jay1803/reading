---
title: "Profiling Hacker News users based on their comments"
date: 2026-03-23T08:01:21Z
category: reading
author: "Simon Willison"
description: "把用户最近 1000 条 HN 评论喂给 LLM，让它「分析此人」，得到的画像精准到连本人都认可——用的不过是完全公开的 API 和一句 prompt。"
source: "https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything"
---

## TL;DR
把用户最近 1000 条 HN 评论喂给 LLM，让它「分析此人」，得到的画像精准到连本人都认可——用的不过是完全公开的 API 和一句 prompt。

## 具体机制
- Algolia HN API 开放 CORS，可直接从浏览器端抓取任意用户的历史评论
- Willison 用 ChatGPT 做了一个一键抓取 + 复制工具，然后粘贴到 Claude Opus 4.6，执行 "profile this user"
- 输出包含：职业身份、核心技术立场、工作方式、人格特征、反复出现的观点……精度和篇幅均超越一般简历
- 他拿自己的账号试了一次：LLM 准确识别出他是 Django 联合创始人、Datasette 作者、iPhone 编程、BART 通勤、养鸡…… 所有细节均准确

## 隐藏限制
- 方法依赖用户在评论中的自我披露程度：Willison 习惯在评论里引用自己博客链接，LLM 因此轻易关联到真实身份；评论量少或风格谨慎的用户，画像质量会显著下降
- 实名关联是额外风险，匿名用户不一定面临同等暴露
- Willison 的实际用途是：在陷入长篇争论前，先查对方是否有惯性恶意争辩的历史

## 边缘判断
一个一下午构建完毕的工具，已把「公开数据」与「可用的社会监控」之间的距离压缩到接近零。Willison 称之为「有点反乌托邦」，这个定性远比实际情况温和。
