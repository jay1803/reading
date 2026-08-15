---
title: "Fuma Nama | Some Nice Things with SVG"
date: 2025-04-15T18:52:13Z
category: reading
description: "\"动态连线\"和\"目录高亮滑块\"这两个看起来毫无关联的 UI 效果，底层是同一个配方：用 SVG <mask> 裁切一个动画块，形状随意换，动画照跑。"
source: "https://fuma-nama.vercel.app/blog/svg-art"
---

## TL;DR
"动态连线"和"目录高亮滑块"这两个看起来毫无关联的 UI 效果，底层是同一个配方：用 SVG `<mask>` 裁切一个动画块，形状随意换，动画照跑。

## 核心洞见
SVG mask 不是装饰语法，是通用视觉乘法器——任何你能画出来的 SVG 形状，都能变成一个"只露出这个形状"的动画窗口。文章的两个例子都是这个配方的变体：Animated Wires 用直线 mask，Clerk TOC 用折线路径 mask。

## 具体机制
**Animated Wires**：`<line>` 放入 `<mask>`，然后让一个带颜色 / 渐变的 `<rect>` 套上这个 mask 做 translateY 动画——视觉上看起来像光在线上流动，实际上只是一个矩形在 mask 后面上下滑动。

**Clerk TOC thumb**：TOC 折线轮廓在服务端渲染（SVG `<path>`，`d` 属性是 `M1 0 L1 20 L13 36…` 这样的坐标命令列表）。客户端拿到元素的实际渲染位置后，用相同逻辑重新构造一个 SVG，转成 `data:image/svg+xml` URI，作为 CSS `mask-image` 注入一个动画 div——thumb 就是这个被折线裁切后、随滚动位移的 div。

## 隐藏限制
折线坐标（`d` 属性）需要客户端实测 DOM 位置才能构造，所以 thumb 只能在 client 渲染，outline 骨架才能 SSR。两者渲染分层是这套方案的必要代价，不是可以消除的细节。

## 收束行
`<path d="...">` 里那串坐标一旦被当作"命令列表"而非"自动生成的字符串"来读，整个 TOC 构造思路就变得透明——SVG 的可编程性就藏在这个属性里，大多数人从没主动碰过它。
