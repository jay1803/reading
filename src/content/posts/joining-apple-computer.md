---
title: "Joining Apple Computer"
date: 2025-06-16T15:18:01Z
category: reading
description: "本文是苹果公司早期核心工程师 Bill Atkinson 在加入苹果40周年之际写下的回忆。他讲述了1978年，在 Steve Jobs 的亲自招募下，如何毅然放弃神经科学博士学业加入苹果的故事。文中回顾了他与 Steve Jobs 的深厚友谊，以及他在苹果工作12年间所做出的奠基性贡献，包括为 Apple II..."
source: "https://www.folklore.org/Joining_Apple_Computer.html"
---

## TL;DR
本文是苹果公司早期核心工程师 Bill Atkinson 在加入苹果40周年之际写下的回忆。他讲述了1978年，在 Steve Jobs 的亲自招募下，如何毅然放弃神经科学博士学业加入苹果的故事。文中回顾了他与 Steve Jobs 的深厚友谊，以及他在苹果工作12年间所做出的奠基性贡献，包括为 Apple II 引入 UCSD Pascal、推动 Lisa 项目标配鼠标和采用白底屏幕、开发核心图形库 QuickDraw、发明下拉菜单、创造 MacPaint 绘画程序以及 HyperCard 创作系统。
### 加入苹果的转折点
#### 放弃学业，投身初创公司
1978年4月27日，作者 Bill Atkinson 正在攻读神经科学博士学位，他的大学朋友 Jef Raskin 邀请他加入初创公司 Apple Computer。起初他因学业而拒绝，但在 Jef 的坚持和 Steve Jobs 的亲自招募下，他改变了主意。Jobs 用一个生动的比喻说服了他：“想一想在浪潮之巅冲浪是多么有趣，而在同一波浪的浪尾像狗刨一样挣扎又是多么无趣。” (Think how fun it is to surf on the front edge of a wave, and how not-fun to dog paddle on the tail edge of the same wave.) 这个比喻让作者下定决心，在两周内便放弃了学业，搬到硅谷加入了苹果。
#### 与 Steve Jobs 的友谊与合作
作者与 Steve Jobs 成为了挚友，他们经常在 Castle Rock 州立公园长时间散步，分享美食，并就生活和设计进行广泛的交流。Jobs 倾听并挑战作者的想法，激发了他的创造力。作者认为 Jobs 并非利用他，而是驾驭和激励了他，引出了他最好的创意能量。在 Jobs 的支持下，他得以在苹果实现改变世界的理想。
### 在苹果的核心贡献
#### 为 Apple II 引入 UCSD Pascal
作者认为当时 Apple II 使用的 Apple BASIC 语言功能不足（例如没有局部变量），无法以模块化的方式构建复杂的软件库。在他的经理否决了引入更强大语言的提议后，他直接向 Steve Jobs 争取。Jobs 虽然认为用户对 BASIC 已经满意，但被作者的热情打动，给了他两周时间来证明自己的观点。作者在两周内成功带回了一个可用的 UCSD Pascal 系统，该系统后来被用于启动 Lisa 项目的开发。
#### 推动 Lisa 项目的关键决策
##### 标配鼠标
作者说服了项目经理 Tom Whitney，认为 Lisa 电脑必须在包装盒中包含鼠标。这样，软件开发者才能设计出完全依赖于指针设备的图形界面，而无需为只使用光标键的用户做兼容性设计。
##### 确立白底黑字显示标准
作者主张屏幕显示应像纸张一样使用“白底黑字”，以便正确处理图形和照片的显示与打印。尽管硬件团队担心白底屏幕会导致闪烁，需要更快的刷新率和更昂贵的 RAM，但 Steve Jobs 在听取了所有利弊后，为了更好的图形表现而支持了白底方案。
#### 开发核心图形与界面技术
##### QuickDraw 图形库
Lisa 和 Macintosh 电脑都采用了全位图显示（full bitmap displays），这在提供巨大灵活性的同时也带来了巨大的性能开销。为了解决这个问题，作者编写了高度优化的汇编语言图形基元库 QuickDraw。所有 Lisa 和 Mac 的应用程序都通过调用 QuickDraw 来高效地绘制屏幕上的所有内容，这使得图形用户界面（GUI）在当时的技术条件下变得实用。
##### 窗口与菜单系统
作者编写了最初的 Lisa 窗口管理器（用于处理重叠窗口和图形裁剪）、事件管理器和菜单管理器。在此过程中，他发明了至今仍在广泛使用的下拉菜单（pull-down menu）。后来，这些代码与 QuickDraw 一起被 Andy Hertzfeld 移植到了 Mac 上，总共占据了初代 Macintosh ROM 近三分之二的内容。
#### 创造 MacPaint 与 HyperCard
##### MacPaint
作者开发了随每台 Mac 附送的位图绘画程序 MacPaint。这个程序直观地向人们展示了配备图形显示和鼠标的计算机是多么有趣和富有创造力。
##### HyperCard
1985年，受一次个人体验的启发，作者设计了 HyperCard，这是一个让非程序员也能创建自己的交互式媒体的创作系统。它使用卡片堆栈（stacks of cards）的比喻，包含了图形、文本、按钮和链接。其脚本语言 HyperTalk 也让普通人能轻松入门事件驱动编程。HyperCard 于1987年发布，比第一个网页浏览器 Mosaic 早了六年。为了完成这个项目，作者选择留在苹果，而没有跟随 Jobs 加入他新创办的 NeXT 公司。
### 离开与回顾
在苹果工作了12年，见证公司从30名员工成长到15,000人后，作者于1990年离开，与他人共同创立了 General Magic 公司，致力于发明个人通信设备。回首过去，作者对自己40年前所做的选择感到非常满意，认为在苹果的岁月里，他有机会通过创造工具来赋予人们力量，并为世界带来了积极的改变。
### 总结
作者 Bill Atkinson 在四十年前放弃博士学业加入苹果的决定，开启了他作为核心工程师的职业生涯，他通过创造 QuickDraw、MacPaint 和 HyperCard 等关键技术，深刻地影响了个人计算机的图形界面和交互方式。
