---
title: "Transcript for DHH: Future of Programming, AI, Ruby on Rails, Productivity & Parenting | Lex Fridman Podcast #474"
date: 2025-10-10T00:34:38Z
category: reading
description: "DHH（David Heinemeier Hansson），Ruby on Rails 框架创作者，37signals（Basecamp、HEY）联合创始人兼 CTO，《Rework》《Remote》等四本 NYT 畅销书合著者，同时是 Le Mans 24 小时赛同级别冠军车手。Lex Fridman 主持，以..."
source: "https://lexfridman.com/dhh-david-heinemeier-hansson-transcript/?utm_source=rss&utm_medium=rss&utm_campaign=dhh-david-heinemeier-hansson-transcript"
---

## 嘉宾背景

DHH（David Heinemeier Hansson），Ruby on Rails 框架创作者，37signals（Basecamp、HEY）联合创始人兼 CTO，《Rework》《Remote》等四本 NYT 畅销书合著者，同时是 Le Mans 24 小时赛同级别冠军车手。Lex Fridman 主持，以技术哲学追问为主，本人少有实质立场介入。

## TL;DR

DHH 真正的核心主张只有一个：开发者生产力的黄金时代是 1990 年代末 PHP/Apache 时期，此后三十年的大部分复杂度都是自找的——无论是 JavaScript 构建管线、微服务、云账单、工程经理，还是会议。这个立场不是怀旧，而是他用 37signals 二十五年的财务数据和产品数据反复验证过的实验结论。

## 编程之美：语言是写给人的，不是写给机器的

Ruby 打动 DHH 的核心是 Matz 的设计前提截然不同：程序员幸福感第一。他用 ~5.times do~ 做循环、~user.admin?~ 做谓词、~user.downgrade unless user.admin?~ 做反向条件——所有这些对解释器来说只是额外负担，但对人类读者是诗。Java 的设计者 Gosling 则反其道而行之，把程序员当"平均水平低的危险生物"来防范，于是设计出了 ~__init__(self)~ 这种丑法。两种语言观的背后是两种截然不同的人性假设。

DHH 在 Rails 的 ActiveSupport 里为数字加了 ~.days~ 方法（~5.days~ 返回秒数用于缓存过期），Matz 允许他以完全平等的方式扩展基础类——读者分不出哪行是 Matz 写的、哪行是 DHH 写的。这种信任在其他语言里几乎没有。

## Rails 信条：用约定消灭配置，用整体对抗分裂

Rails 九条信条里 DHH 反复强调两点：一是 Convention over Configuration——系统应该开箱即用，默认值应该由专家替你做好；二是 Integrated Systems（整体优于微服务）。

微服务在 Netflix 规模或许合理，但把"方法调用"变成"网络调用"是分布式系统第一定律的反面：**不到万不得已，不要分布式**。Basecamp 和 HEY 各自约 10 万行 Ruby 代码，420+ 个屏幕，一个工程师完全可以理解整套系统；HEY 上线时前端 JavaScript 只有 40KB，Gmail 同功能需要 28MB——差距不是技术，是哲学。

## Vibe Coding 不能替代真正学编程

DHH 的论断：你不能通过看健身视频练出肌肉，也不能通过 vibe coding 成为程序员。Vibe coding 目前能造出"看上去能用"的外表，但 AI 会在自己编织的迷宫里迷路——修一个 bug 破坏五个其他地方，这恰好是初级程序员的典型错误轨迹。

对于"高水平提示工程师是否是未来职业"，他直接否定：好编辑必须首先是好作者，能发现别人代码问题的能力是做事能力的副产品，不是独立技能。他认为若 AI 真的完全胜任编程，那才是好事——届时就不需要提示工程师了，任何人都能直接表达意图。

## 云不是更便宜，只是让你以为更便宜

37signals 的 AWS 账单峰值约 340 万美元/年；退出云端后购置自有服务器，基础设施花费降低约一半到三分之二，五年预计节省约 1000 万美元，运维团队人数**没有增加一个人**。

云的三条销售主张中，DHH 逐条拆解：更便宜（假，AWS 运营利润率接近 40%）；更简单（假，AWS IAM 比 Linux 更难配）；更快（真，但被严重高估——需要在 15 分钟内上线 1000 台机器的场景极少，而自购服务器在相同预算下算力多出数倍）。互联网最初的 DARPA 设计是去中心化网络，如今 US-East-1 一挂，全球三分之一的互联网跟着挂——这是对原始设计的背叛。

## 管理者与会议是生产力的负熵

37signals 在某段时期引入了专业工程经理，两年后 DHH 得出结论：他最初的判断是对的。默认团队规模：一个程序员 + 一个设计师 = 一个功能。这个规模下根本不需要管理层。

工程师最想要的职业发展路径是"和比自己更强的人一起工作"，而工程经理通常无法提供这一点（他们很快就会失去对代码的感觉）。他把会议和管理类比成"可按需调用的云服务"——偶尔需要，但不应该常驻。Basecamp 24 年，Jason 与 DHH 每周直接沟通不超过 2 小时。

## 留下的那个想法

DHH 在节目里顺口说：Basecamp 第一版由他一人写成，账单是 400 小时、25 美元/小时、共 1 万美元。这个系统后来产生了数亿美元营收，且仍在运行。这让整集关于"AI 会不会取代程序员"的讨论显得有点尴尬——真正稀缺的从来都不是写代码的人力，而是知道要造什么、并把它造得足够好的判断力。
