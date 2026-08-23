---
title: "Pluralistic: Google's new remote attestation scheme is every bit as terrible as its old remote attestation scheme (12 Jun 2026)"
date: 2026-06-13T08:01:52Z
category: reading
author: "Cory Doctorow"
description: "Google 的「reCAPTCHA 手机验证」是被公众舆论扼杀的 WEI（Web 环境完整性）的化身复活——本质是把远程认证（remote attestation）从浏览器层下移到 Android 系统级 TPM，用户无法拒绝或篡改，凡是运行 de-Googled Android 的设备都将被主流应用与网站直接..."
source: "https://pluralistic.net/2026/06/12/compelled-speech/"
---

## TL;DR
Google 的「reCAPTCHA 手机验证」是被公众舆论扼杀的 WEI（Web 环境完整性）的化身复活——本质是把远程认证（remote attestation）从浏览器层下移到 Android 系统级 TPM，用户无法拒绝或篡改，凡是运行 de-Googled Android 的设备都将被主流应用与网站直接拒之门外。

## 核心主张拆解
- **浏览器是「用户代理」，远程认证是对这一关系的根本颠覆**：浏览器原本代表用户与服务器交涉，用户可以指令它屏蔽广告、关闭自动播放、保护隐私；远程认证则把代理关系倒转——设备替服务器向用户施压，强制向陌生服务器汇报软件配置，且因 TPM/安全飞地的硬件隔离，用户无法干预汇报内容。
- **技术锁定是商业+法律锁定失效后的续招**：Google 已被美国法庭三度定性为垄断者（搜索、应用商店、广告技术），商业封锁受制于监管；技术封锁绕过这条路，使 CalyxOS、GrapheneOS 等 de-Googled Android 替代品在获取主流服务时面临系统性屏蔽——此前这些替代品靠 Android 开源性在「围墙」缝隙中存活。
- **广告拦截的权利不只是隐私问题**：拦截器也是光敏性癫痫患者、低对比度视力障碍者等失能用户的无障碍工具；远程认证让服务器有权拒绝「不服从」设备，实质是剥夺用户在信息获取中的反谈判能力。
- **数据采集与威权政府的乘数效应**：Trump 政府已借 Google 数据追踪抗议者与 ICE 追捕对象；让设备强制向服务器「说真话」的架构，在此政治环境下不是短视，而是不可原谅的设计选择。

## 反驳或薄弱处
- **值得质疑**：文章将 WEI 与 reCAPTCHA 手机验证直接等同，但前者针对整个网络浏览器层，后者目前仅限于 Android 应用内认证，且仍处于实验阶段；文章未区分潜在风险与已落地影响，论证力度因此有所打折。
- **证据薄弱处**：「Android 每五分钟向 Google 发送一次数据」引用自 2018 年研究，年代久远，但核心论点并不依赖这一数字。

## 收束
把监控权利代码化进硬件的深层意义：它将原本属于法律与政治博弈范畴的问题（谁有权知道你在做什么）转变成一个技术事实——法庭判决、监管限令、用户意志在 TPM 面前全部失效。
