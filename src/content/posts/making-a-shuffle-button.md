---
title: "Making a Shuffle Button"
date: 2026-07-07T08:02:30Z
category: reading
author: "Jim Nielsen"
description: "当每个页面都内嵌 974 个 note ID 时，发布新文章会让全站 HTML 文件的 hash 全部失效——Netlify 须重新上传每一个文件。无论是注入 ID 还是在构建期写死随机 href，问题根源相同：把会变的数据散布到每个页面。"
source: "https://blog.jim-nielsen.com/2026/notes-shuffle/"
---

## 把动态逻辑隔离到单独路由，是静态站点的部署代价最优解

当每个页面都内嵌 974 个 note ID 时，发布新文章会让全站 HTML 文件的 hash 全部失效——Netlify 须重新上传每一个文件。无论是注入 ID 还是在构建期写死随机 href，问题根源相同：把会变的数据散布到每个页面。

解法是把所有 shuffle 逻辑收进 =/shuffle/= 这一个 HTML 页面。其他页面只需一个稳定的 =<a href="/shuffle/">= 链接，永远不需要更新。只有这一个文件在 note 数量变化时失效。缓存有效，部署只重传一个文件。

顺带：shuffle 变成了一个可直接导航、可分享的路由（=notes.jim-nielsen.com/shuffle=），而不是只能通过 GUI 按钮触发的行为。

## 刻意的人工延迟是有意义的 UX 信号

点击 shuffle 后立刻跳转到随机页面，用户感知不到"发生了什么"。作者在 =/shuffle/= 页面加了 300ms 延迟 + "Shuffling..." 文案 + 旋转动画。这模拟了旧 CD 播放器的硬件行为：点击 shuffle 键后屏幕显示"Shuffling…"，光头在 CD 轨道上移动到新位置——硬件约束催生了明确的意图确认反馈。作者将其移植为纯软件实现：人工延迟不是 bug，是用户与系统之间的确认握手。
