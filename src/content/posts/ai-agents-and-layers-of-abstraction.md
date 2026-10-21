---
title: "AI Agents and Layers of Abstraction"
date: 2026-10-21T05:17:08Z
category: reading
description: "AI 产品下一阶段将在用户与软件之间增加一层 agent 抽象，人们无需了解具体软件即可完成工作，Luke Wroblewski 以开源工具 Intent 为例说明管理大规模 agent 协作的新方式。"
source: "https://www.lukew.com/ff/2159/ai-agents-and-layers-of-abstraction"
author: "info@lukew.com"
---

AI 产品的下一阶段，是在用户与软件应用之间增加一层由 agents 构成的抽象，让人们无需了解或操作具体软件，也能完成工作。Luke Wroblewski 将这视为 AI 产品演化的延续：模型先在幕后提供能力，随后进入聊天界面，如今已经发展到多个模型相互协作、共同执行任务的 **agent orchestration** 阶段；当系统成熟、用户信任加深，应用本身的操作细节也将逐渐退到幕后。

开发者的工作方式已经暴露出这一转变带来的管理难题。Luke 接触的前沿开发者，正在同时监督多个项目中的数百个、甚至更多 agents，让它们协调完成软件构建、测试与交付。为聊天时代设计的开发工具难以承载这种规模：人们需要掌握大量并行工作的进展，理解异常发生的原因，并在必要时纠偏。

为此，Luke 的团队重新设计、重建并开源了开发工具 Intent。它把任务放进独立的 workspaces，每个 workspace 都有隔离的文件副本，避免 agents 相互覆盖修改；工作围绕持续更新的 **living spec** 展开，由 coordinator 拆解任务、委派给专门的 sub-agents，并持续推进执行，减少人工盯守。更高一层的 agent 则跨多个 workspaces 和多台设备检查、管理工作。这些机制共同提供两种能力：通过 **observability** 看清正在发生什么，通过 **introspection** 追查为什么会这样。

这仍是一个需要保留人工介入入口的过渡阶段。越来越多开发者已经愿意放弃逐项手动审查 agents 的代码修改，只与管理其他 agents 的 coordinator 交互；但他们仍需要足够的控制权，能够随时深入执行过程、查看状态并调整方向。随着系统可靠性提高、信任累积，用户需要直接接触的细节才会进一步减少。

这种变化延续了计算机已有的抽象路径：多数用户无需理解应用代码，也无需理解操作系统如何通过更底层的代码与硬件交互；同样，未来用户也将无需关心 agents 如何调用、操作电脑上的应用，甚至无需知道这些软件存在或掌握其用法。Luke 将这一方向与 Apple 的 Knowledge Navigator 愿景联系起来：那段受 John Sculley 与时任 Apple Fellow 的 Alan Kay 对话启发的视频，描绘了以人为中心的计算方式。沿着这一方向，软件可以继续承担执行工作，而人们与计算机交互时需要理解和操纵的层级，将从具体应用上移到任务与目标。
