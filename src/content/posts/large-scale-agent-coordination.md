---
title: "Large Scale Agent Coordination"
date: 2026-11-16T01:54:03Z
category: reading
description: "大规模 AI agent 协作的关键，是通过隔离的工作环境、持续更新的任务说明、明确的角色分工和按需交接，让大量独立执行过程始终服务于同一个目标。Luke Wroblewski 以 OpenAI 同时运行 10,000 个 agent、提出 Navier–Stokes Mille"
source: "https://www.lukew.com/ff/2161/large-scale-agent-coordination"
author: "info@lukew.com"
---

大规模 AI agent 协作的关键，是通过隔离的工作环境、持续更新的任务说明、明确的角色分工和按需交接，让大量独立执行过程始终服务于同一个目标。Luke Wroblewski 以 OpenAI 同时运行 10,000 个 agent、提出 Navier–Stokes Millennium Prize Problem 解法的尝试引出这一问题，但明确表示自己不了解 OpenAI 的协调机制；他介绍的是开发工具 Intent 的实现方式。

协调要解决的是多个 agent 同时工作时的具体障碍：避免彼此覆盖成果，告知任务完成状态，委派工作并相互审查，在需要时向人类提问或申请权限，以及让任务能够并行、串行或异步推进。每个 agent 都在与具备工具使用能力的 AI 模型反复交换消息，协调机制需要把这些分散的往返过程组织成朝统一目标推进的工作流。

Intent 首先通过**隔离与共享任务记忆**控制协作中的冲突和上下文混乱。每项任务在专属 workspace 中运行，持有一份独立的文件副本，避免 agent 相互覆盖修改。每个 workspace 同时维护一份持续更新的 living spec，记录已经做出的决定及其原因，让后来接手的 agent 能够知道此前发生了什么、接下来需要完成什么。文件隔离保护执行成果，living spec 则维持任务的连续性。

在这个基础上，Intent 用角色划分明确责任：coordinator 拆解工作并委派任务，implementer 编写代码，verifier 根据验收标准检查实现。团队还可以把自己的要求编码为可复用的 specialist 角色，例如执行特定测试方法或负责安全审查，使团队规范成为协作流程中有明确承担者的工作。

任务的推进顺序和交接方式也由协调机制管理。coordinator 在编写 spec 时说明工作由谁执行、按什么顺序开展、如何完成；执行中的 agent 可以判断自己是否需要等待其他事件，并在必要时才被唤醒。例如，一个 agent 可以在后台监控 pull request，随着 review comments 到来逐条回应，等条件齐备后再 push。agent 完成自身工作时，还可以与新 agent 往返沟通，把后续任务交出去，使接手者只携带继续工作所需的重要信息。

这些机制让扩展可以沿多个层次发生：同一 workspace 中运行多个 agent，多个 workspace 并行推进，再把 workspace 分布到多台设备上。软件开发目前提供了较成熟的实践环境，但 Intent 底层系统已经被用于降低电费、预订餐厅等任务。其可迁移的核心，是把工作组织成边界清楚、状态可追溯、能够等待和交接的执行单元；协调质量决定了增加的 agent 能否真正转化为共同任务的进展。
