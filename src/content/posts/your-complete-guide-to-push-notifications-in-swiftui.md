---
title: "Your Complete Guide to Push Notifications in SwiftUI"
date: 2026-03-18T10:48:45Z
category: reading
description: "SwiftUI 无法完全脱离 AppDelegate 实现推送通知——即使整个 App 是纯 SwiftUI 写的，仍必须创建一个 UIApplicationDelegate 子类来注册设备并接收 APNs token。"
source: "https://medium.com/@jpmtech/your-complete-guide-to-push-notifications-in-swiftui-8a13f5588662"
---

## TL;DR
SwiftUI 无法完全脱离 AppDelegate 实现推送通知——即使整个 App 是纯 SwiftUI 写的，仍必须创建一个 `UIApplicationDelegate` 子类来注册设备并接收 APNs token。

## 核心洞见
推送通知的完整路径是：App 向 APNs 注册 → APNs 发放唯一 device token → App 转发 token 给自己的推送服务器 → 推送服务器调用 APNs → APNs 中转到设备。开发者的服务器永远不直接联系设备，APNs 是不可绕过的中间层。

## 具体机制
- 权限请求（`UNUserNotificationCenter.requestAuthorization`）与注册远程通知（`application.registerForRemoteNotifications()`）是两步独立操作，缺一不可；前者仅影响系统弹窗，后者才触发 APNs token 的下发。
- `CustomAppDelegate` 需同时实现 `UIApplicationDelegate`（注册 + 接收 token）和 `UNUserNotificationCenterDelegate`（前台展示 + 用户交互响应），SwiftUI 侧通过 `@UIApplicationDelegateAdaptor` 桥接。
- 本地测试：在 `.apns` 文件中写入 `"Simulator Target Bundle"` + `aps` payload，拖入模拟器或用 `xcrun simctl push booted <path>` 触发——App 必须在后台。
- 远程测试：从 Xcode 日志取 `stringifiedToken`，在 developer.apple.com Push Notifications Console 填入 Device Token + 设置 `apns-priority: high`（否则通知可能因低电量被延迟）。

## 隐藏限制
- 每个 Apple 账号最多创建 2 个 APNs key，p8 文件只能下载一次；丢失则必须重新生成并同步更新所有依赖该 key 的服务。
- 使用 Fastlane 等不自动管理 Provisioning Profile 的工具时，添加 Push Notifications capability 后需手动重新生成 certificates 和 profiles，否则 Signing 区域会出现警告且推送无法生效。

## 值得注意
APNs key 是整个推送基础设施的单点：泄露即意味着任何人可以向你账号下所有 App 的用户发推送。这个风险多数教程只用一句话带过，但在多 App 共用同一 key 的场景下，密钥管理的优先级理应高于代码本身。
