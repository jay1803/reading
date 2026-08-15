---
title: "Who Runs the Ransomware Group 'The Gentlemen?'"
date: 2026-06-12T08:01:14Z
category: reading
description: "安全研究员通过一系列 OSINT 线索，将月均攻击超 240 家机构的新兴勒索软件集团 The Gentlemen 的幕后管理员 Hastalamuerte/Zeta88，定位为俄罗斯乌德穆尔特共和国伊热夫斯克市的 36 岁男性 Alexander Andreevich Yapaev——一个在攻击链上拿 10%..."
source: "https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/"
---

## TL;DR
安全研究员通过一系列 OSINT 线索，将月均攻击超 240 家机构的新兴勒索软件集团 The Gentlemen 的幕后管理员 Hastalamuerte/Zeta88，定位为俄罗斯乌德穆尔特共和国伊热夫斯克市的 36 岁男性 Alexander Andreevich Yapaev——一个在攻击链上拿 10% 分成、在 LinkedIn 以 B2B 营销总监身份公开亮相的人。

## 关键时刻
- The Gentlemen 自 2025 年中成立至今，已公开 332 名受害者，仅 2026 年就超 240 名；90/10 分成模式（行业标准 80/20）使其快速从竞争对手处挖走老手，成为今年受害者数量第二多的勒索软件集团。
- Check Point 发现该集团以暴露在公网的 VPN 和防火墙为入口，入侵后数小时内可加密整个网络。
- 集团后端基础设施遭泄露的聊天记录证实 Hastalamuerte 亲自组装 locker 与 RaaS 控制面板、管理所有赎金支付，是实质性的单一管理员。

## 背后逻辑（OSINT 追踪链）
- Intel 471：Hastalamuerte 在近十个俄语黑客论坛注册，2025 年 1 月在 Breachforums 和 2022 年在 Breached 分别以伊热夫斯克 IP 登录。
- 注册邮箱 hastalamuerte1488@protonmail.com（1488 为白人至上主义数字符号）→ Epieos 关联 Apple 账号与 GitHub 账号 SantaMuerte，后者持续追踪多种恶意工具与漏洞利用项目。
- Telegram 账号 @hastalamuerte18 → Flashpoint 确认 Telegram ID 为 30907522 → Constella 关联用户名 "bu4vs" 及俄罗斯手机号 79127650004。
- 该手机号在多份泄露的俄政府数据库中指向 Alexander Andreevich Yapaev，36 岁，伊热夫斯克。
- 邮箱 bu4vs@mail.ru → Epieos 关联到 LinkedIn 账号，Yapaev 在此将自己列为俄罗斯大型电气照明企业 Uralenergo Udmurtia 的 B2B 营销总监。

## 更大意义
俄政府对国内网络犯罪长期采取默许立场（前提：不攻击俄公民或企业），这使犯罪者几乎没有遮掩真实身份的动力。Yapaev 入行初期（2019–2020）在论坛上留下大量笨拙、公开的痕迹，这些记录如今被商业情报平台永久索引。"在 LinkedIn 公开、在暗网犯罪" 并非无知，而是在特定政治保护伞下的理性选择——其脆弱性在于该保护伞随政治变化而消失。
