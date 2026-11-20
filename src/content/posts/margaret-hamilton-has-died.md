---
title: "Margaret Hamilton has died"
date: 2026-11-20T16:58:09Z
category: reading
description: "Margaret Hamilton 为 Apollo 登月留下的核心遗产，是让软件能够预防人为失误、在系统过载时保住关键任务，并推动 software engineering 获得独立工程学科的地位。MIT 的讣告回顾了她贯穿航天项目与创业生涯的同一项追求：把错误和未知情况纳入系统设计，使任务安全不"
source: "https://news.mit.edu/2026/margaret-hamilton-computing-pioneer-dies-1007"
author: "muglug"
---

Margaret Hamilton 为 Apollo 登月留下的核心遗产，是让软件能够预防人为失误、在系统过载时保住关键任务，并推动 **software engineering** 获得独立工程学科的地位。MIT 的讣告回顾了她贯穿航天项目与创业生涯的同一项追求：把错误和未知情况纳入系统设计，使任务安全不必完全依赖操作人员永不犯错。

这一认识曾被她四岁的女儿 Lauren 提前验证。Lauren 在 MIT Instrumentation Lab 玩指令舱模拟器时，在模拟飞行过程中启动了发射前程序 P01，导致模拟器崩溃。Hamilton 随即在技术文档中加入飞行期间不得启动 P01 的警告，并提出修改软件，从系统层面阻止这种操作；后一个建议遭到否决，理由是训练有素的宇航员不会犯同样的错误。然而，1968 年 Apollo 8 飞行期间，Jim Lovell 意外启动了 P01，导致机载导航数据消失。Hamilton 与团队被召来处理事故，她此前提出的修改此后才被纳入程序。这次“Lauren error”暴露了仅靠培训与警告的局限，也体现了 **defensive programming** 的原则：软件应当具备预判错误、阻止错误或自行修复错误的能力。

Apollo 11 则检验了系统在无法避免异常时能否继续工作。1969 年 7 月，Eagle 登月舱即将着陆时，机载计算机发出 1202 警报：一个硬件开关故障造成计算机过载，威胁到复杂的着陆程序。Hamilton 与团队设计的 **priority-driven software** 能够关闭不必要的后台任务，把计算资源优先留给任务关键程序。Houston 因而决定继续登月，最终两名宇航员首次踏上月球。P01 事故要求软件约束危险操作，1202 警报则要求软件在资源不足时主动取舍；两者共同指向一种可靠性观念：系统必须为异常状态预先安排可行的行动路径。

Hamilton 在 Instrumentation Lab 继续工作至 1970 年代；随着 Apollo 项目收尾，该实验室脱离 MIT，成为独立的 Draper Laboratory。她随后把错误预防与容错方法带入商业软件，1976 年创办 Higher Order Software，十年后又创办 Hamilton Technologies，试图通过改进规划、系统工程和软件开发流程，提高可靠性、降低成本并缩短产品上市时间。后者的旗舰产品 **Universal Systems Language（USL）** 将这些原则发展为面向复杂软件系统的建模语言与工程方法，使错误预防成为设计过程的一部分。

这套技术实践也支撑了她争取软件专业地位的努力。Hamilton 使用“software engineering”一词，是为了让软件及其开发者获得与其他工程领域相称的尊重，同时把软件与硬件等工程共同纳入整体系统工程过程。这个称呼最初长期被同事当作玩笑，她的想法也被视为激进；随着软件承担越来越关键的任务，其工程地位逐渐得到承认。她后来获得的荣誉包括 2003 年 NASA Exceptional Space Act Award、2017 年 Computer History Museum Fellow Award、2019 年 Intrepid Lifetime Achievement Award，以及 2022 年入选 National Aviation Hall of Fame。

晚年的 Hamilton 还成为女性参与科学与技术的代表人物：她站在 MIT 团队 Apollo 程序打印稿旁的照片在网上广泛传播；她参与开发的 Apollo 软件于 2015 年完整上传 GitHub；2017 年，源于 MIT 科学传播者 Maia Weinstock 设计的 Women of NASA Lego 套装在全球上市，她成为其中的官方人偶。贯穿这些公共纪念与技术成就的，是她所说的“handling the unknown”：可靠的软件工程，要把人的失误、硬件的故障和资源的极限，都当作系统必须承担的现实条件。
