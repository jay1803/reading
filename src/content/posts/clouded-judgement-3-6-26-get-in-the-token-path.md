---
title: "Clouded Judgement 3.6.26 - Get in the Token Path"
date: 2026-03-07T17:40:36Z
category: reading
description: "云时代最大的基础设施赢家，核心不是“按量付费”这四个字，而是把收入绑定到平台最核心的消耗单位；当年这个单位是 compute，作者判断 AI 时代越来越像 token。谁站在 token 的生成、处理与消耗路径上，谁就更可能像 AWS、Snowflake、Datadog 那样，随着平台使用量扩张而自动长大。真正的..."
source: "https://cloudedjudgement.substack.com/p/clouded-judgement-3626-get-in-the"
---

## TL;DR
云时代最大的基础设施赢家，核心不是“按量付费”这四个字，而是把收入绑定到平台最核心的消耗单位；当年这个单位是 compute，作者判断 AI 时代越来越像 token。谁站在 token 的生成、处理与消耗路径上，谁就更可能像 AWS、Snowflake、Datadog 那样，随着平台使用量扩张而自动长大。真正的难点是：进入 token path 只是入场券，想拿到最大结果，还得在这层计量权之上叠加差异化与护城河，否则很快会被商品化。

## 关键洞察
作者先回看云时代的胜负手。AWS 直接卖算力，Databricks 卖 job compute，Snowflake 卖 query compute，Datadog 卖由 workload 产生的 telemetry，Cloudflare 和 MongoDB 也都把定价嵌进工作负载的执行路径。它们的共同点不是抽象的 usage-based pricing，而是计费单位恰好就是整个平台扩张时被持续放大的那个原语；世界生成更多 compute，它们几乎不需要重新教育市场，收入就会同步抬升。云时代很多重要公司失败，不是产品不关键，而是收入没有变成这个原语的函数。Docker 是最典型的例子：它让容器成为云原生默认工具，却没把自身收入绑定到容器所拉动的算力支出上，最后 Kubernetes 和云厂商吃掉了它创造的大部分价值。

作者据此把映射转到 AI：AI 系统真正的原子工作单位是 token。prompt 会变成 token，context 会膨胀 token，response 在消耗 token，agent 的多步执行会把 token 用量继续放大。于是 OpenAI、Anthropic 这类模型厂天然站在原语层；Cursor 这类 coding agent 也因为每次补全、代理动作和推理调用都会触发 token 消耗，收入越来越像 token volume 的函数；推理云则在卖“token 版 AWS”。这也是作者看好“token path”的原因：最大 AI 基础设施公司大概率会诞生在 token 被计量、转发、放大和优化的位置，而不是停留在传统 seat、license 或附着在开源之上的企业订阅层。

但作者也强调，站在 token path 上只是必要条件，不是充分条件。云时代的 CDN 就说明，站在流量路径上却缺乏差异化，最后仍会被价格压成商品。Limelight 流量暴涨时收入反而下滑，Cloudflare 则在相近起点上叠加安全、开发者工具和 edge compute，做出了切换成本和更高价值密度。映射到 AI，结论是：要么在 token path 上提供更强的开发体验，要么做垂直模型、安全合规、专有数据等护城河；否则你只是 token 经过的一段管道，最终会被成本下降吞噬。更紧迫的是时间窗口。推理成本正在快速下行，这会推高 token 总消费，但也会持续压缩单位价格；真正的赢家必须在 token 彻底商品化前先卡住路径、成为默认层，再把护城河加厚。

## 一句话总结
AI 基础设施最值钱的位置，不是“离模型很近”，而是把收入绑定在 token 流动上，并在这条路径上做出无法被轻易替代的增值层。
