---
title: "What happened to Apple's legendary attention to detail?"
date: 2025-10-30T14:50:53Z
category: reading
description: "iOS 26 / macOS 26 的 Liquid Glass 不是审美分歧——作者枚举的 bug 指向一个更刻薄的结论：这套设计连深色模式都没正经测过，就出货了。"
source: "https://blog.johnozbay.com/what-happened-to-apples-attention-to-detail.html"
---

## TL;DR
iOS 26 / macOS 26 的 Liquid Glass 不是审美分歧——作者枚举的 bug 指向一个更刻薄的结论：这套设计连深色模式都没正经测过，就出货了。

## 核心主张拆解
Apple 跨 app 设计不一致的问题在 macOS 上早已存在（Calendar / Activity Monitor / TV 三款系统 App 的 Tab 组件形状各异），但 iOS 26 把问题从"丑"升级成了"坏"：

- Files 深色模式下文件夹名不可见；Settings 图标全部消失；开启 Reduced Transparency 解决一个 bug 的同时制造了新的黑条。
- iPad 上鼠标悬停后 Liquid Glass 效果卡住无法消退。
- WebKit viewport 在 iOS 26 中被搞坏——Safari 和所有第三方浏览器内容与 UI 控件重叠、按钮闪烁；Apple 又强制要求 iOS 上所有浏览器使用 WebKit，等于一刀切断了整个浏览生态。
- iMessage 新背景图让消息文字和照片几乎不可读；App Library 图标随机出现 / 消失。

作者的诊断：多设计团队各自为政，没有统一规范执行；更根本的诱因是 PM 为季度目标做了漂亮 Mockup 说服高层，却没人在流程中按停。

## 值得质疑
作者是 EU DMA 听证常客，对 Apple WebKit 政策长期持批评立场——WebKit 段落可信度高，但关于 Apple 内部文化（"PM 追季度"）是个人推断，无内部证据支撑。截图大量来自早期 Beta，部分 bug 已被第三方自行修复（如 Vivaldi）。

## 更大的讽刺
Apple 用大量透明效果重塑了设计语言，而这几年用户和监管者恰好一直在要求 Apple"更透明"——作者把这层反讽直接点出来了，言简意赅。
