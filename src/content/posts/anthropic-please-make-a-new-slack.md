---
title: "Anthropic, please make a new Slack"
date: 2026-03-07T17:40:36Z
category: reading
description: "Slack 是当今企业最重要的知识库，但它的 API 策略等同于\"不\"——这不是懒惰，而是蓄意的护城河。Fivetran 认为，Anthropic 是唯一既有技术（Claude）又有信誉（坚守原则的公众记录）来颠覆这个局面的公司。"
source: "https://www.fivetran.com/blog/anthropic-please-make-a-new-slack"
---

## TL;DR
Slack 是当今企业最重要的知识库，但它的 API 策略等同于"不"——这不是懒惰，而是蓄意的护城河。Fivetran 认为，Anthropic 是唯一既有技术（Claude）又有信誉（坚守原则的公众记录）来颠覆这个局面的公司。

## 核心主张拆解
Claude 的根本缺陷不是功能不足，而是架构限制：它只能 1:1 对话，而业务发生在群组里。把 Slack 上下文粘贴进 Claude 的用户实际上在扮演 sub-agent，手动中转信息——这个荒谬本身就说明问题。

Slack 的数据封锁让这个问题无法从内部解决：企业 Slack 消息是公司运作的实时流，但 Slack Connect API 极度受限，Slack 官方也没有开放的动力，除非来自竞争压力。

Slack 的护城河比想象中脆弱。其"网络效应"几乎只体现在 Slack Connect 的跨公司频道——数量有限，用户可以承受迁移成本。同时 Slack Enterprise+ 定价极高（Fivetran 支付给 Slack 的费用接近 G Suite 全套），性价比难以辩护。

NewSlack + Claude 捆绑包解决三个问题：为长尾轻度 AI 用户提供捆绑理由、通过同事示范效应化解 AI 怀疑论者、一次性推动开放数据生态。

## 值得质疑
这篇文章的作者是 Fivetran（数据管道公司）高管——一旦 Slack 开放 API，Fivetran 是最直接的受益者之一。"开放互操作性"的呼吁嵌在一家以连接器收费为核心商业模式的公司的博客里，利益取向相当明显。"网络效应很弱"的论断也只是断言，没有提供迁移成本的实证数据。

## 更大的赌注
这篇文章的真正赌注是：谁控制企业通信历史语料库，谁就控制企业 AI agent 的上下文——Anthropic 如果不进场，默认是让 Slack 永久锁住这个入口。
