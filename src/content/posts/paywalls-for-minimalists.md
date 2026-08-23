---
title: "Paywalls For Minimalists"
date: 2026-03-27T08:01:05Z
category: reading
author: "Ernie Smith"
description: "任何静态网站都能用一天时间搭出可用的付费墙：Ko-Fi 收款 + Activepieces 自动化 + Listmonk 邮件 + HMAC 验证码，总计不超过 $12/月，绝大多数环节可自托管，完全无需 CMS 或复杂的登录系统。"
source: "https://feed.tedium.co/link/15204/17295750/minimal-paywall-setup-idea"
---

## TL;DR
任何静态网站都能用一天时间搭出可用的付费墙：Ko-Fi 收款 + Activepieces 自动化 + Listmonk 邮件 + HMAC 验证码，总计不超过 $12/月，绝大多数环节可自托管，完全无需 CMS 或复杂的登录系统。

## 核心洞见
付费墙的三个硬门槛（支付处理、读者信任、个人信息管理）可以全部外包给 Ko-Fi：它绕开了 App Store 抽成陷阱、定价透明（月收入再高也只扣 $12/月 Gold 计划）、webhook 支持开放。剩下的自动化、邮件、鉴权环节都可以用开源工具拼完。

## 具体机制
完整链路：用户在 Ko-Fi 完成 $3/月订阅 → Ko-Fi 触发 webhook → Activepieces 调用 Listmonk API 将用户加入付费列表 → Listmonk 发送带 HMAC 令牌链接的邮件 → 用户点击链接并输入邮件中的验证码 → 写入第一方 cookie，解锁内容或关闭广告。验证码采用 HMAC 客户端哈希，有效期约一个月（含宽限期），可跨设备分享，不需要服务方存储密码或大量 PII。

## 隐藏限制
邮件发送层无法完全自主：Gmail 对自托管发件人存在信任问题，实际上仍需绑定 Amazon SES（$0.10/千封）或 Mailgun。RSS 分发需要额外配置 listmonk-rss 插件，邮件模板也需要自行设计（作者计划在 GitHub 开源一套 starter kit，部分内容会放在付费墙后面）。

## 那个问题
Substack 的护城河从来不是技术，而是"读者愿意在陌生网站输入支付信息"的信任门槛——这套方案把这个门槛转移到了 Ko-Fi，但对于没有既有受众基础的创作者来说，冷启动问题依然存在，Ko-Fi 解决的是摩擦，不是人气。
