---
title: "Everyone is writing a pricing page for robots 💳"
date: 2026-06-30T08:04:46Z
category: reading
description: "AI 代理在推荐或采购产品时，会直接读取定价页面。但标准定价页面是给人类设计的——价格藏在 JavaScript 里，机器人读不到，就直接跳过。解法极简：在 =yoursite.com/pricing.md= 放一个机器可读的纯文本版本。"
source: "https://www.marketingideas.com/p/everyone-is-writing-a-pricing-page"
---

## 给机器读的定价页面，已经成为 AI 购买时代的基础设施

AI 代理在推荐或采购产品时，会直接读取定价页面。但标准定价页面是给人类设计的——价格藏在 JavaScript 里，机器人读不到，就直接跳过。解法极简：在 =yoursite.com/pricing.md= 放一个机器可读的纯文本版本。

## 成熟玩法的梯度

- *静态 .md 文件（入门）*：Buffer 的 =/pricing.md= 把量价关系用清晰表格展开，机器一次能读出任何数量的月费。无需设计，就是纯文本。
- *多文件 + 权威声明（复杂定价）*：Flowdown 针对 GEO 定价，提供 pricing.md + docs + 说明文字，明确告诉代理"地区 App Store 价格是最终权威"——防止机器报错价。
- *带链接的人机共用页面*：Resend 在正常定价页放了一行 "Are you an AI agent? See pricing."，同时服务人类和机器人。
- *专属代理区块*：Stacktree 在定价页设了整段 AI agent 专区，签名"the file is the data"——是目前原生代理感最强的静态方案。
- *动态 API（最高级）*：Promptfax 提供 =/pricing.json?page_count=13= 这类带参数的端点，代理传入用量，直接拿到精确报价。静态文件彻底失效的复杂定价场景的终极解法。

## 被动发现已在发生

Supabase 和 WorkOS 的 =/pricing.md= 已存在，但在主页上没有显式链接。说明代理已经在按惯例主动探测 =/pricing.md=——你不挂链接，机器也会去找。

## 最小可行动作

一张表（Plan / Price / Includes / Limit）+ Overage + Billing + FAQ，存为 =yoursite.com/pricing.md=，同时备一份 =/pricing.txt=。主页加一行可见链接。价格变了就更新。

IDC 预测 2028 年 70% 的 B2B 买家会在首次接触你的网站前就用 AI 完成决策。定价页的受众已经改变，读者优先级已经倒转。
