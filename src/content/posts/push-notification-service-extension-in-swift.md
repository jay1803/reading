---
title: "Push Notification Service Extension in Swift"
date: 2025-10-09T15:38:35Z
category: reading
description: "推送通知在显示给用户之前存在一个设备端拦截窗口——Notification Service Extension 可以在此时修改任何通知字段（声音、角标数、标题、附件，乃至解密 payload 数据）；唯一前提是服务端 payload 包含 =\"mutable-content\": 1=。"
source: "https://medium.com/@jpmtech/push-notification-service-extension-in-swift-b1a0b68051d6"
---

## TL;DR
推送通知在显示给用户之前存在一个设备端拦截窗口——Notification Service Extension 可以在此时修改任何通知字段（声音、角标数、标题、附件，乃至解密 payload 数据）；唯一前提是服务端 payload 包含 ="mutable-content": 1=。

## 核心洞见
多个第三方推送源各自为政、无法在其配置层统一指定声音或同步角标时，设备端拦截是唯一能跨源一致化通知体验的方案。Extension 通过 App Group 与主 App 共享状态，因此可以读取主 App 维护的角标计数，解决跨服务角标不一致问题。

## 具体机制
- 在 Xcode 添加 Notification Service Extension target；主 App 与 Extension 均须加入同一 App Group（命名格式：=group.<reverse-domain>.<appname>=）
- Extension 实现 =didReceive(_:withContentHandler:)=，在 =UNMutableNotificationContent= 上修改 title / sound / badge / attachment 等任意字段后调用 contentHandler 投递
- =serviceExtensionTimeWillExpire()= 作为超时兜底：若处理超时，系统调此方法，开发者投递当前最佳版本；若不处理，原始 payload 直接显示

## 隐藏限制
- Extension 在模拟器上无法用断点或 print 调试；且必须通过真实远程推送服务发送 payload，拖拽 payload 文件到模拟器不触发 Extension
- 若模拟器出现配置问题，只能通过「Erase All Content and Settings」重置，无其他调试捷径

## 收束
=serviceExtensionTimeWillExpire= 的存在说明苹果预设了"Extension 可能来不及完成"——系统宁愿降级到原始通知内容也不阻塞展示。这是一个值得借鉴的工程取舍模型：给开发者控制权，但在控制权失效时自动退回安全默认值。
