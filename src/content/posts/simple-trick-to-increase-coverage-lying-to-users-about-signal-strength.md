---
title: "Simple trick to increase coverage: Lying to users about signal strength"
date: 2025-11-04T11:14:22Z
category: reading
description: "Android 内置了一个从未出现在官方文档中的 CarrierConfig 标志 =KEY_INFLATE_SIGNAL_STRENGTH_BOOL=，运营商启用后，用户看到的信号格数会被强制调高一格。AT&T 和 Verizon 均已在生产网络中开启。这不是运营商绕过系统做的事——是 Android 主动提供..."
source: "https://nickvsnetworking.com/simple-trick-to-increase-coverage-lying-to-users-about-signal-strength/"
---

## TL;DR
Android 内置了一个从未出现在官方文档中的 CarrierConfig 标志 =KEY_INFLATE_SIGNAL_STRENGTH_BOOL=，运营商启用后，用户看到的信号格数会被强制调高一格。AT&T 和 Verizon 均已在生产网络中开启。这不是运营商绕过系统做的事——是 Android 主动提供给运营商的 API。

## 具体机制
=KEY_INFLATE_SIGNAL_STRENGTH_BOOL= 存在于 AOSP 的 CarrierConfigManager Java 源码中，任何运营商均可通过 CarrierConfig 文件自行启用；底层测量值不变，仅显示层被调高一格。AT&T 和 Verizon 的公开 CarrierConfig 仓库中已确认启用；提案者无法在 git blame 中追溯，也没有被收入 developer.android.com 的公开文档。

## 这破坏了什么
信号格数是手机 UI 里最被动、最被信任的网络质量指标——用户不会去质疑它，因为它看起来是硬件读数。运营商在这里动手，比任何广告语更有效，因为它根本不被识别为营销行为。加上"假 5G"标签和夸大覆盖的惯例，这是一种系统性的显示层操控，而非偶发行为。

## 留下的那个想法
Android 选择将"允许运营商美化信号显示"做成一个有 key 名、有文档注释的正式配置项，而不是把它拒之门外——这个设计决策本身比 AT&T / Verizon 的具体选择更值得追问。
