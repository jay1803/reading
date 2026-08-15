---
title: "In memory of the man who put red and green squiggles under words"
date: 2026-06-23T08:02:03Z
category: reading
description: "Tony Krueger 近日去世。他参与了 Word 1.0、1.1、2.0、Word for OS/2、Word for Mac，以及 Word 6.0 及之后多个版本，大概是发布 Word 版本最多的工程师。让他的工作渗透进几乎所有现代软件的，是他把拼写检查从阻塞式操作改造成后台静默运行，并在发现问题时立即..."
source: "https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451"
---

## 他发明了你每天见到的那条红线，但没人知道他叫什么名字

Tony Krueger 近日去世。他参与了 Word 1.0、1.1、2.0、Word for OS/2、Word for Mac，以及 Word 6.0 及之后多个版本，大概是发布 Word 版本最多的工程师。让他的工作渗透进几乎所有现代软件的，是他把拼写检查从阻塞式操作改造成后台静默运行，并在发现问题时立即在原位画红色波浪线——无需用户主动触发，也不打断前台操作。绿色波浪线（语法）随后跟进。

## 真正的发明是"不打扰"，波浪线只是 UI

早期 Word 的 Auto Spell Check 虽已在空闲时后台运行，但一旦用户开始操作就会抢占前台，导致很多人直接关掉它。Tony 的实现让检测在完全无感的情况下完成，波浪线做到即时、就地、不阻塞——把"显式触发的批处理"变成了"持续在场的环境提示"。

## 这个模式今天已经溢出文字处理器

红/绿/蓝波浪线现在出现在几乎每一个有输入框的软件里：浏览器、IDE、邮件客户端。Penn Jillette 听说这件事后当场在剧场大声宣布："The red and green squiggles!? I love the red and green squiggles!"；"Weird Al" Yankovic 的《Word Crimes》MV 里也让红色波浪线出镜。Tony 还有一个鲜为人知的成就：在没有源码的情况下把《Chip's Challenge》逆向工程后移植到了 Windows。
