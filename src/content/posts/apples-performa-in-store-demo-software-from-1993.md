---
title: "Apple’s Performa in-store demo software from 1993"
date: 2026-11-09T17:16:00Z
category: reading
description: "一台未经清理就出售的 Macintosh Performa 410，意外保存了 Apple 在 1993 年用于零售门店的演示软件，也留下了官方系统恢复镜像无法还原的销售现场。Doug Brown 最初在 eBay 买下它，是为了寻找尚无人保存的 Performa 专用操作系统 System …"
source: "https://www.downtowndougbrown.com/2026/09/apples-performa-in-store-demo-software-from-1993/"
author: "Doug Brown"
---

一台未经清理就出售的 Macintosh Performa 410，意外保存了 Apple 在 1993 年用于零售门店的演示软件，也留下了官方系统恢复镜像无法还原的销售现场。Doug Brown 最初在 eBay 买下它，是为了寻找尚无人保存的 Performa 专用操作系统 System 7.1P3；真正稀有的发现，则藏在 Applications 文件夹末尾，一个名为 Performa 410 Demo 的程序里。

这台机器的原装 Quantum 硬盘仍能读取，尚未被老硬盘常见的橡胶劣化问题毁坏。Brown 将硬盘内容制作成镜像后，发现系统确实是 System 7.1P3，而且前任主人似乎主要用 ClarisWorks 做文字处理，几乎没有改动原有环境。他清除个人信息、移除软件注册信息，整理出接近出厂状态的安装镜像并上传到 Macintosh Garden。随后，另一位收藏者上传了完整的 Market Software Series Apple Restoration CDs，其中 Volume 1 已包含纯净的 System 7.1P3 恢复镜像，使他的系统重建工作失去独有价值；但这台电脑保留下来的门店演示程序，依然是另一类难得的历史材料。

运行这个程序还促成了一次模拟器修复。Brown 最初在 MAME 中启动它，整个模拟系统随即冻结。他与 Arbee 深入排查声音芯片模拟问题，最终开发出测试工具 ASCTester，推动 MAME 的 Apple Sound Chip 模拟得到改进。在问题尚未解决时，他改用 Basilisk II，才确认这台 Performa 410 原本是一台商店展示机：出售前没有恢复出厂状态，买家又一直没有删除演示程序，门店环境因此留存在硬盘上。

这套软件呈现了 Apple 当时如何向普通家庭消费者介绍 Macintosh。它既有鼠标使用教程、Apple 配件介绍，也演示随机器提供的 ClarisWorks、Quicken、Global Village 传真调制解调器、AOL、American Heritage Dictionary 和 SuperMunchers，并展示可另行购买的 Lotus 1-2-3、WordPerfect、Yearn2Learn 与 Battle Chess。程序还直接比较 Performa 410 和 Performa 466，Brown 据此判断，这两款机型当时应曾在同一零售商处并排销售。它保留下来的信息，覆盖了入门操作、家庭用途和后续软件购买选择，超出了机器规格本身。

程序由 MacroMind Director 制作，其 Lingo 代码留下了操作方式与开发来源。Brown 找到的退出组合键是 Option-P；相关处理代码在多个画面中重复出现，其中还保留着被注释掉的跳转至“quit”画面的语句。隐藏退出键可以减少顾客通过常规 Command-Q 离开演示环境的机会。代码注释标明版权归 Apple Computer, Inc. 所有，开发者为 re:Source Marketing，时间主要是 1993 年 7 月，部分画面标为 6 月。Global Village TelePort Fax/Modem 的演示另有署名，由 Tree Frog Studio 的 Chuck Walker 于 1993 年 5 月创作制作，说明整套展示内容也整合了配件厂商提供的素材。

这类软件难以集中找回，与它的分发方式有关。一位前现场代表告诉 Brown，这台没有 CD-ROM 光驱的机器，其演示程序很可能由工作人员随身携带的专用 SCSI 硬盘安装；硬盘里装有各机型的安装程序，使用后需要交还 Apple。这意味着，保存着大量不同机型演示程序的安装介质未必会流入收藏市场。与此同时，当年的硬盘空间有限，买回展示机的用户很容易优先删除这类占空间的软件。此次留存依赖于机器未被重置、主人极少使用且原装硬盘仍然可读，几个条件缺一都可能让它消失。

Brown 已将演示程序上传到 Macintosh Garden，并用这台实体电脑及其原装硬盘录制完整演示视频，没有使用模拟器。Apple 曾推出大量 Performa 型号，每款是否都需要单独制作 Director 演示程序，仍有待更多实物或亲历者补充。这次发现揭示了软件保存中容易遗漏的一层：出厂恢复盘能够保住标准产品，流落用户手中的旧硬盘则可能保住产品当年如何被展示、讲解和出售的具体历史。
