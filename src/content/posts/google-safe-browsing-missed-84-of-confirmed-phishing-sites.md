---
title: "Google Safe Browsing missed 84% of confirmed phishing sites"
date: 2026-03-06T08:53:42Z
category: reading
description: "Google Safe Browsing 在2月份漏掉了83.9%的已确认钓鱼站，其中包括托管在谷歌自家平台（Docs/Forms/Sites/Apps Script）上的16个钓鱼页面——无一被标记。这不是偶发漏网，而是blocklist机制的结构性盲区，且攻击者已有意针对它做了规避。"
source: "https://www.norn-labs.com/blog/huginn-report-feb-2026"
---

## TL;DR
Google Safe Browsing 在2月份漏掉了83.9%的已确认钓鱼站，其中包括托管在谷歌自家平台（Docs/Forms/Sites/Apps Script）上的16个钓鱼页面——无一被标记。这不是偶发漏网，而是blocklist机制的结构性盲区，且攻击者已有意针对它做了规避。

## 发现
- 254个已确认钓鱼站中，GSB仅标记41个（16.1%）；213个在扫描时未被识别。
- 149个（58.7%）托管在Weebly、Vercel、GitHub、IPFS等受信任平台：Weebly 51站GSB只标记2个（96%漏率），Vercel 40站标记8个，Wix 7站标记0个。
- 16个钓鱼站托管在Google自家域名（Docs/Forms/Sites/Apps Script），无一被GSB标记。
- 对比方Muninn：自动扫描命中率94.1%（6个误报）；深度扫描0漏报，但代价是9个合法页面全被误判为可疑。
- 最常被仿冒的品牌：Microsoft（28）、Google（21）、Netflix（19）、Amazon（16）、AT&T（13），另有14个针对加密货币平台。

## 为什么重要
钓鱼页面寿命极短——攻击者发起→收割凭证→下线，往往在被举报审核前已完成。Blocklist的致命限制是reactive的：必须先有人报告、审核，保护才能生效。攻击者已针对性规避：两阶段攻击（诱饵页托管在amazonaws.com，凭证收割kit在攻击者控制域名）、一次性token（安全扫描器重访时看到的是Wikipedia）、bot检测机制。钓鱼套件通常只实现"happy path"——其余按钮全部无效，但针对真实受害者已经够用。

## 破坏了什么常识
"托管在受信任平台 = 安全"：Weebly/Vercel/GitHub的域名根本不可能被封锁，反而成了攻击者的掩护。"VirusTotal扫描通过 ≈ 安全"：这些钓鱼站在VirusTotal上的结果均为clean。最荒诞的反例：Google同时是基础设施提供商（Docs/Forms/Sites）、钓鱼宿主，以及自称的检测工具提供商——三重角色同时失守。

**证据薄弱处**：本文是Norn Labs的营销博客，数据基于他们自家工具Huginn对"已确认钓鱼"的定义；Muninn的性能数字均为自报，未经独立第三方复现。但Google自家平台上16个钓鱼站无一被GSB标记这个细节，很难用方法论偏差解释。

## 一个难以回避的荒诞
安全工具能"保护"你的前提，是先有一个知道威胁存在的人——而攻击者的策略恰好是：在那个人出现之前，已经完成了全部工作。
