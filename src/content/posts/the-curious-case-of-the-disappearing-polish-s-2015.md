---
title: "The curious case of the disappearing Polish S (2015)"
date: 2026-06-30T08:04:46Z
category: reading
description: "四个跨越数十年的独立决策叠加，导致波兰语字母 Ś 在 Medium 编辑器里完全无法输入。作者 Marcin Wichary 是波兰人，亲历了其中每一步变迁，因此得以追溯完整因果链。修复只需一行条件判断。"
source: "https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/"
---

## Windows 将 Right Alt 内部映射为 Ctrl+Alt，是让 Ś 在 Medium 消失的关键链接

四个跨越数十年的独立决策叠加，导致波兰语字母 Ś 在 Medium 编辑器里完全无法输入。作者 Marcin Wichary 是波兰人，亲历了其中每一步变迁，因此得以追溯完整因果链。修复只需一行条件判断。

### 四个成因

*共产主义时代的键盘局限。* 1980 年代波兰禁止商业进口西方电脑，只能拿到美式英文键盘。无法改硬件，程序员改用 Alt + 字母输入波兰语 9 个额外变音字母——这套"程序员布局"（programmer's layout）沿用至今。Ś = Right Alt + S。

*Windows 的兼容性决策。* 为让只有一个 Alt 键的旧键盘也能触发快捷键，Microsoft 在系统层将 Right Alt 内部映射为 Ctrl+Alt 组合。Right Alt + S 在事件层面因此变成了 Ctrl+Alt+S。

*Medium 拦截 Ctrl+S。* 为消除浏览器默认的"另存为"弹窗，Medium 编辑器监听 Ctrl+S 并调用 ~preventDefault()~。代码未排除 Alt 同时按下的情况。

*致命交叉：* Ś → Right Alt+S → Ctrl+Alt+S → 触发 Medium 的 Ctrl+S 拦截 → ~preventDefault()~ 吃掉按键 → 字母消失。

### 修复

将条件从 ~e.ctrlKey~ 改为 ~e.ctrlKey && !e.altKey~：只在 Alt 未同时按下时才拦截 Ctrl+S。

### 更大背景

这个 bug 是系统性问题的缩影。英语 26 个无变音字母构成了美式计算机生态的隐性假设，波兰语（和更多其他语言）只能在这套体系留出的缝隙里变通。从打字机时代的 Alt 键变通方案，到共产主义导致的美式键盘普及，再到 Medium 拦截 Ctrl+S——每一步单独看都合理，叠加起来才暴露英语中心的盲点。
