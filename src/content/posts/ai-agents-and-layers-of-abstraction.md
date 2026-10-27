---
title: "AI Agents and Layers of Abstraction"
date: 2026-10-27T03:38:15Z
category: reading
description: "AI 产品的下一阶段，是让 Agent 成为人与软件之间的新抽象层，使用户无需了解或操作具体应用，就能完成工作；多 Agent 协作带来的管理负担正在推动产品继续演进。"
source: "https://www.lukew.com/ff/entry.asp?2159"
author: "info@lukew.com"
---

AI 产品的下一阶段，是让 Agent 成为人与软件之间的新抽象层，使用户无需了解或操作具体应用，就能完成工作。Luke Wroblewski 去年判断，AI 模型将从幕后提供能力，发展到相互协作、共同执行任务；如今，**Agent orchestration** 已经把这一判断变成现实，而多 Agent 协作带来的管理负担，正在推动产品继续演进。

这种压力首先出现在开发者身上。Luke 接触的前沿开发者已经同时监督多个项目中的数百个、甚至更多 Agent，让它们协调完成软件构建、测试和发布。诞生于 AI 聊天时代的开发工具，难以承载这种规模的并行工作：用户需要管理大量任务及其执行过程，仅靠与 Agent 对话已经不够。

为此，Luke 的团队重新设计、重建并开源了开发工具 Intent。它把任务拆入独立的 workspace，每个 workspace 拥有隔离的文件副本，防止 Agent 相互干扰；内部通过持续更新的 **living spec** 和 coordinator 管理工作，由 coordinator 分解任务、委派专职 sub-agent，并推进执行，减少人工盯守。更高一层的 Agent 则跨 workspace、跨设备检查和管理进度。这些机制共同提供两种能力：**observability** 让人看见正在发生什么，**introspection** 让人追查为什么会这样。

这种可见性与追查能力，是当前扩大委托范围的基础。越来越多开发者已经愿意停止逐项人工审查 Agent 的代码修改，转而只与管理其他 Agent 的 coordinator 交互，但仍需保留深入检查、理解状态和纠正方向的控制权。随着系统成熟、信任积累，用户才会进一步远离这些执行细节。

Luke 预期，这一变化将重演计算机已有的抽象过程：多数人使用应用时，并不关心应用运行的代码，更不关心操作系统如何通过更底层的代码驱动硬件；未来，人们也将不再关心 Agent 怎样使用计算机上的应用，甚至无需知道任务涉及哪些软件、这些软件该如何操作。Apple 的 Knowledge Navigator 视频所呈现的人本计算愿景，正是这一方向的先声；它受到 John Sculley 与时任 Apple Fellow 的 Alan Kay 之间讨论的影响。沿着这条路径，今天用于监督 Agent 的工具，将成为通往更高抽象层的过渡：人保留目标与纠偏权，把调用软件、协调执行的知识逐步交给 Agent。
