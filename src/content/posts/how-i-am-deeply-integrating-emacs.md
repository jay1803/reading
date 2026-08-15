---
title: "How I am deeply integrating Emacs"
date: 2025-11-08T10:15:45Z
category: reading
description: "Emacs 深度整合最大的速度收益来自系统级胶水层：一个 Go 脚本将任意 Emacs 函数暴露为 Hyprland 全局快捷键，替换 bash+sleep 旧方案后调用链速度提升 10 倍。"
source: "https://joshblais.com/blog/how-i-am-deeply-integrating-emacs/"
---

## TL;DR
Emacs 深度整合最大的速度收益来自系统级胶水层：一个 Go 脚本将任意 Emacs 函数暴露为 Hyprland 全局快捷键，替换 bash+sleep 旧方案后调用链速度提升 10 倍。

## 集成全景
~emacsclient~ + Go 脚本作调度，把 Emacs 功能以独立帧形式弹出到任意 Hyprland 工作区。覆盖范围：vterm（默认终端）、mu4e（邮件）、elfeed（RSS）、dirvish（文件管理）、EMMS（音乐）、password-store（密码）、全局 org-capture。作者自建 ~universal-launcher.el~，将 wofi/rofi 的应用启动、SSH、书签、emoji、TODO 搜索全部收入 Emacs 弹出层；另有 ~thanos/type~：在任意浏览器输入框激活 Emacs 编辑模式，C-c C-c 粘贴回去。

## 弃用 EXWM 的逻辑
两个硬约束：Emacs 单线程（任何 Lisp 卡顿会冻结整个桌面）；EXWM 仅 X11，与 Wayland 方向相悖。解法是在 WM 边界做快捷键集成，把 Emacs 限定在应用层——既绕开单线程风险，又保留了"一切可召唤"的体验。

## 边缘判断
"我已经获得了好处，所以不需要 EXWM"——前提是他愿意手工维护 Go 脚本 + Hyprland 配置的胶水层。换 WM 意味着从头重建整套快捷键体系，这套方案的可移植性其实很低。
