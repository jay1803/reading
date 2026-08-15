---
title: "European digital ID wallets rely on safety services of Google and Apple"
date: 2026-07-01T08:03:03Z
category: reading
description: "欧盟一方面高喊打破大科技垄断，另一方面在最关键的公共基础设施——身份钱包——中嵌入了 Google Play Integrity API。这不只是技术选型问题：该 API 在验证设备安全性的同时，强制要求运行 Google 授权的 Android 版本、通过 Google Play Store 安装应用、使用 G..."
source: "https://waag.org/en/article/european-digital-id-wallets-are-gift-google-and-apple/"
---

## 欧盟数字身份钱包把主权让给了 Google

欧盟一方面高喊打破大科技垄断，另一方面在最关键的公共基础设施——身份钱包——中嵌入了 Google Play Integrity API。这不只是技术选型问题：该 API 在验证设备安全性的同时，强制要求运行 Google 授权的 Android 版本、通过 Google Play Store 安装应用、使用 Google 账户登录。政府采用后，实际上成了 Google 生态准入规则的执法者。

## Google Play Integrity API 的真实机制

该 API 名义上是免费安全工具，用于防止 bot 欺诈与应用篡改。但它以 Google Play Store 作为"可信源"——不仅检查应用完整性，还检查安装渠道和设备授权状态。结果：e/OS、GrapheneOS 等去 Google 化操作系统的用户被直接排除在政府身份服务之外。这违反了《数字市场法》（DMA）。

## 现成的开放替代被忽视

Android 原生 Hardware Attestation API 提供基于硬件的安全验证，不绑定 Google 生态系统。瑞士以数据主权和自由选择为由放弃 Play Integrity，转用该替代方案。而荷兰和意大利无条件强制使用 Play Integrity，将欧盟架构参考框架中的"推荐"解读为"强制"。

## 治理层面的碎片化

欧盟架构参考框架本身只推荐而非要求使用 Google 认证，但这导致成员国执行标准不一：部分强制绑定 Google，部分不绑。可互操作的统一身份框架目标因此被内部撕裂。

## 结构性出路

从架构参考框架中彻底剔除 Google 和 Apple 认证，改为强制使用开放的硬件级认证机制。这不只是技术选择，也是让公共基础设施真正对公众负责的治理问题。
