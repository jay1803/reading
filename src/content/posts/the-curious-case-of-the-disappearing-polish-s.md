---
title: "The curious case of the disappearing Polish S"
date: 2026-06-28T08:02:48Z
category: reading
description: "四个跨十年的偶然叠加，让波兰语字母 Ś 在 Medium 编辑器里彻底无法输入。根本原因是 Windows 的一个兼容性决定：Right Alt 在系统内部等同于 Ctrl+Alt——Medium 拦截 Ctrl+S 时，顺手把 Ctrl+Alt+S 也拦掉了，而后者恰好就是波兰键盘输入 Ś 的按键序列。"
source: "https://aresluna.org/the-curious-case-of-the-disappearing-polish-s"
---

## Windows 把 Right Alt 映射成 Ctrl+Alt，是让 Ś 消失的真正原因

四个跨十年的偶然叠加，让波兰语字母 Ś 在 Medium 编辑器里彻底无法输入。根本原因是 Windows 的一个兼容性决定：Right Alt 在系统内部等同于 Ctrl+Alt——Medium 拦截 Ctrl+S 时，顺手把 Ctrl+Alt+S 也拦掉了，而后者恰好就是波兰键盘输入 Ś 的按键序列。

## 四个历史偶然的逻辑链

① 波兰语有 9 个附加变音字母，英文键盘原生不支持。

② 共产主义时期波兰无法进口商业定制键盘，程序员自发创造"程序员布局"：用 Right Alt + 拉丁字母输入变音版本（Right Alt+S = Ś）。即使 1989 年后商业键盘普及，这套布局依然是主流，一如 QWERTY 的惯性。

③ Medium 为了屏蔽浏览器"另存为"弹窗，拦截了所有 Ctrl+S 事件，但代码没有排除 altKey 标志位。

④ Windows 为了向后兼容只有一个 Alt 键的旧硬件，把 Right Alt 内部映射成 Ctrl+Alt——于是波兰人打 Ś 时，浏览器收到的是 Ctrl+Alt+S，被 Medium 的事件拦截器当作 Ctrl+S 吞掉。

修复只加一个条件：~ctrlKey && !altKey~，区分真正的保存快捷键与携带 Alt 的组合。

## 英语霸权的夹缝

作者（本身是波兰人）指出，这几行代码是美式计算机霸权的缩影。大量软件以英语 26 个无重音字母为默认假设，其他语言只能在约束条件的缝隙里求存——波兰语从打字机时代开始就在这种夹缝里谋生，Ś 不过是最新一个被挤掉的字母。那些让 Ś 能再次被打出来的工程师，正在为这种日常性的边缘化默默付出代价。
