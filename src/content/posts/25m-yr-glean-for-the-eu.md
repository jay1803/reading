---
title: "$25m/yr glean for the eu"
date: 2026-04-18T08:02:51Z
category: reading
description: "Langdock 抓到的不是“欧洲也需要一个 ChatGPT”这层需求，而是“欧洲企业明明想用 LLM，但合规上不敢直接用”的断裂带。它卖的本质不是模型，而是一个让 IT 部门愿意放行的 AI 控制面：多模型接入、审计、权限、数据驻留和 no-training 保证。只要合规 friction 还在，底层模型越商..."
source: "https://newsletters.feedbinusercontent.com/4ca/4ca4cf1532b25cd23b9d040b81cf3dfd59affed6.html"
---

## TL;DR
Langdock 抓到的不是“欧洲也需要一个 ChatGPT”这层需求，而是“欧洲企业明明想用 LLM，但合规上不敢直接用”的断裂带。它卖的本质不是模型，而是一个让 IT 部门愿意放行的 AI 控制面：多模型接入、审计、权限、数据驻留和 no-training 保证。只要合规 friction 还在，底层模型越商品化，这类中间控制层越有机会抽税。

## 核心机制
欧洲企业此前关闭 ChatGPT 等工具，原因不是效果差，而是缺少 GDPR DPA、EU data residency 和审计控制。Langdock 因而把产品做成封闭式企业 AI 工作区，让公司能在内部数据上部署 agent 和 workflow，同时把底层模型选择权交给 IT 白名单，而不是交给员工个人。它接入 40 多个模型，但真正卖点是“可控使用”，不是“最强模型”。

## 商业模型说明它想占住控制层，而不只是助手入口
它的收入并不只靠 seat。文中给出的收费结构包括 €20–€25/人/月的席位费、workflow automation 的分层订阅费，以及对 LLM API usage 加 10% markup，再加 1000+ 席位客户的定制企业合同。这意味着它想同时占住三个税点：员工入口、自动化编排、模型调用结算。若企业 AI 使用深度继续上升，它的收入增长不必完全依赖 seat 增长。

## 值得质疑
这份材料更像高密度销售卡片，不足以证明护城河。文中没有客户数、净收入留存、毛利结构，也没解释 10% API markup 在大客户采购里能守多久。若微软、Google、OpenAI 逐步把合规、审计和欧盟部署原生化，这类控制层的议价权会被迅速压缩。

## 收束
这条案例最该记住的，不是 Langdock 能不能做成“欧洲版企业 AI 入口”，而是企业 AI 的早期利润池，很可能先落在把“不能用”变成“可以放心用”的那层控制面，而不先落在模型本身。
