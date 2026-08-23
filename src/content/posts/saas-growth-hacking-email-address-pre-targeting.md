---
title: "SaaS Growth Hacking: Email Address Pre-targeting"
date: 2026-03-09T22:24:55Z
category: reading
author: "Lincoln Murphy"
description: "冷邮件发出之前，先用同一份邮件列表在 Facebook / LinkedIn / Twitter 投不带 CTA 的曝光广告——目的只是\"让他们见过你的名字\"，而不是让他们点击。这一步不是可选优化，而是决定邮件打开率的实质前置操作。"
source: "http://sixteenventures.com/saas-growth-hacking-email?utm_source=rss&utm_medium=rss&utm_campaign=saas-growth-hacking-email"
---

## TL;DR
冷邮件发出之前，先用同一份邮件列表在 Facebook / LinkedIn / Twitter 投不带 CTA 的曝光广告——目的只是"让他们见过你的名字"，而不是让他们点击。这一步不是可选优化，而是决定邮件打开率的实质前置操作。

## 核心洞见
邮件打开率的瓶颈不在邮件本身，在于"熟悉感"。多渠道预曝光的底层逻辑：目标收件人先在信息流里见过你的 logo，收到邮件时行为从"陌生拒绝"切换到"似曾相识"。关键反直觉点：预投广告时**主动去掉 Call to Action**，此阶段目的是印象积累，去掉 CTA 还能大幅节省 PPC 费用。

## 具体机制
六个渠道，逻辑各异：

- **Facebook Custom Audiences**：将邮件列表上传为自定义受众，发邮件前 3-5 天投品牌曝光广告，无 CTA，仅刷存在感。
- **LinkedIn 人工连接**：用 Rapportive 在 Gmail 里每次处理约 20 封邮件，鼠标悬停发个性化连接请求（远比批量导入的模板请求成功率高）；建立连接后可顺手找到他们所在的圈子组群再渗透。
- **Twitter 邮件定向**：直接上传邮件列表到 Twitter 广告台（2014 年起支持，行为等同 Facebook Custom Audiences）；或用 FullContact API 把邮件转为 Twitter 账号，先关注建立直接触达。
- **CRM 再营销（LiveRamp 类）**：上传名单，供应商在对方注册过该邮件的网站上触发展示广告，或按人口属性预测其常访站点跟投。
- **Gmail AdWords**：针对竞品交易邮件关键词投展示广告，直接出现在目标用户收件箱视野内；此渠道不需要持有邮件列表，依赖关键词购买。
- **第三方邮件列表合作**：在目标受众可能订阅的外部通讯上投广告或联名发送；若能在邮件中埋 retargeting pixel，后续还能持续跟投展示广告。

## 隐藏限制
文章写于 2013 年，提到的所有平台接口（Facebook Custom Audiences、Twitter 邮件定向、LinkedIn 批量连接、Gmail AdWords）在今天的机制、成本和限制上均已发生重大变化；LinkedIn 对批量连接请求的检测和封号策略远比当年严格。更本质的遗漏：整套方法依赖持有一份邮件名单（自建、抓取或购买），文章完全未触及名单来源的合规性（GDPR、CAN-SPAM）——这块风险当时已存在，只是还没有系统性立法。

## 一句话留下
这套方法的本质是"在开口要钱之前先让对方见过你"，但这恰好暴露了冷邮件的根本弱点：它依赖陌生人的善意。预曝光是在用媒体预算掩盖渠道策略的缺陷，这份预算本可以拿去构建一个从一开始就不"冷"的出站渠道。
