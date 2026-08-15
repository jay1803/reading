---
title: "★ Nextpad++"
date: 2026-05-14T08:01:36Z
category: reading
description: "AI 让单人几周内把大型 Windows 编辑器移植到 Mac 变得可行，但 Nextpad++ 暴露的核心问题不是“能不能跑”，而是代码代理没有内化平台文化：它技术上是原生 Mac app，产品气质上却像 Windows 软件穿上了 Cocoa 外壳。"
source: "https://daringfireball.net/2026/05/nextpad"
---

## TL;DR
AI 让单人几周内把大型 Windows 编辑器移植到 Mac 变得可行，但 Nextpad++ 暴露的核心问题不是“能不能跑”，而是代码代理没有内化平台文化：它技术上是原生 Mac app，产品气质上却像 Windows 软件穿上了 Cocoa 外壳。

## 核心主张拆解
- Notepad++ 不是 Microsoft Notepad 的“小增强版”，而是 Don Ho 从 2003 年开始维护的 GPL 开源 Windows 编程编辑器，有成熟插件生态，更接近 Windows 世界里的 BBEdit。
- Nextpad++ 是 Andrey Letov 对 Notepad++ GPL 代码的 Mac 移植，最初叫 “Notepad++ for Mac”，因无权使用名称而改名；项目 3 月 10 日开始，几周内发出 1.0，速度本身就强烈指向 AI 辅助。
- 官网 About 页没主动强调 AI，但 Author 页承认“multi-agent AI development workflows”让单人完成这种规模项目成为可能；文章的判断是：可能可行，但很难称为 practical。
- 关键冲突在于：Nextpad++ 不是 Electron、Wine 或网页壳，而是 Objective-C++ + Scintilla + Cocoa、14MB、Universal Binary 的“真原生”实现；正因为它技术上原生，交互和审美上的不对劲才更刺眼。

## 证据与细节
- 官网截图里有 50 个难以理解的工具栏按钮，这不是 Mac 软件常见的信息架构。
- 文档标签在 mousedown 而不是 mouseup 时关闭，违背细节交互预期。
- 默认字体是 10pt Courier New，像把 Windows 默认习惯直接搬进 Mac。
- 设置里有 “Default / None / Antialiased / LCD Optimized” 四种字体抗锯齿选项，但默认值并不是 “Default”，暴露出移植逻辑与用户语义之间的错位。
- 这些问题不是“非原生技术栈”的问题，而是缺少真正熟悉 Mac 软件文化的人进行取舍、删减和品味校准。

## 值得质疑
- 文章主要评价产品气质与平台贴合度，没有系统测试 Nextpad++ 的稳定性、性能、插件兼容或实际编辑能力。
- 如果目标用户只是想在 Mac 上获得 Notepad++ 的肌肉记忆，Nextpad++ 的“怪异”可能反而是迁移价值；但这无法反驳文章对 Mac 原生体验的批评。

## 收束
Nextpad++ 最有价值的地方不是它本身，而是它提前展示了 vibe-coding 的边界：AI 可以快速搬运复杂软件结构，却不自动生成一个平台应有的 taste、克制和人类产品判断。
