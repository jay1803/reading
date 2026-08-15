---
title: "Motorola GrapheneOS devices will be bootloader unlockable/relockable"
date: 2026-03-06T08:53:42Z
category: reading
description: "Motorola 成为继 Google Pixel 之后首个承诺原生支持 GrapheneOS 完整 unlock-flash-relock 流程的主流 OEM，打破了该系统六年来只能跑在 Pixel 硬件上的局面。"
source: "https://grapheneos.social/@GrapheneOS/116160393783585567"
---

## TL;DR
Motorola 成为继 Google Pixel 之后首个承诺原生支持 GrapheneOS 完整 unlock-flash-relock 流程的主流 OEM，打破了该系统六年来只能跑在 Pixel 硬件上的局面。

## 关键时刻
MWC 2026 上，Motorola 与 GrapheneOS Foundation 宣布长期合作：未来旗舰机将支持 bootloader unlock + relock 并维持 Verified Boot 链完整性——这是 GrapheneOS 安全模型的核心前提。首批兼容机型预计 2027 年上市，目标为 Edge 和 Razr 系列旗舰。

## 背后逻辑
GrapheneOS 的安全模型要求设备能在刷入自定义 OS 后重新锁定 bootloader，且整个固件/OS 镜像经过密码学验证并带降级保护。此前只有 Pixel 满足这一硬件要求。此次合作还包括：Motorola 将 GrapheneOS 的部分安全特性整合进 Moto Secure 工具，面向普通用户；双方联合开发新安全能力；以及 Motorola 承诺为目标设备提供至少五年（未来将升至七年）的长期支持。

## 更大意义
主流 Android OEM 中出现第二家支持 verified-boot 兼容自定义 OS 的玩家，意味着对高安全需求用户（企业、记者、隐私敏感用户）而言，硬件选择不再被 Pixel 独占。若 Motorola 交付兑现，可能推动其他 OEM 效仿，从根本上改变 Android 安全定制生态的格局。
