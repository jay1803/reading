---
title: "Collaborative Steering"
date: 2026-05-19T08:01:42Z
category: reading
description: "AI agent 真正的团队问题不是“每个人能不能更快地产出”，而是个人化 agent 会把团队共识拆成多套隐形上下文；未来高价值工具会把 prompt、skills、memory、MCP、项目约束等 steering layer 变成团队共同维护的协作界面。"
source: "https://www.lukew.com/ff/entry.asp?2153"
---

## TL;DR
AI agent 真正的团队问题不是“每个人能不能更快地产出”，而是个人化 agent 会把团队共识拆成多套隐形上下文；未来高价值工具会把 prompt、skills、memory、MCP、项目约束等 steering layer 变成团队共同维护的协作界面。

## 核心主张拆解
Luke Wroblewski 认为，当前 AI 工具大多仍是“个人生产力”范式：工程师写更多代码，设计师生成更多图，PM 产出更多文档。这个方向有用，但一旦团队里的每个人都用自己的 agent、自己的上下文、自己的偏好去推进工作，产出速度会放大视角分裂。

分裂的根源在于 agent 的行为受一组分散要素影响：agent markdown、skills markdown、system prompt、agent prompt、memory、MCP server 等。个人使用时已经复杂；放到团队里，这些 steering artifacts 散落在不同电脑、代码库和服务上，默认优化的是个人意图，而不是共享产品判断。

文章把这个问题命名为 collaborative steering：一种由团队共同创建、编辑、维护的 agent 指导机制。它的目标不是让 AI 替代专家判断，而是把设计、工程、品牌、性能、可维护性、基础设施等不同专业经验沉淀为可复用的项目级上下文，使多个 agentic workflow 朝同一个产品方向收敛。

作者用设计负责人在 Design Futures Assembly 的观察作为关键警告：当任何人都能构建自己想要的东西，产品会体现出“十五个不同想法”，而不是一个统一观点。AI 降低了实现成本，却提高了保持 coherent product point of view 的管理难度。

## 具体机制
作者提到他们近期在多个项目里使用 Intent 定义 project-level context，让 agentic workflow 对齐共享目标，而不是各自偏航。这里的重点不是某个单一 prompt，而是把团队共识变成一个可操作、可维护、能影响 agent 输出的层。

协作式 steering 隐含了三类能力：第一，把分散上下文集中到团队可见的位置；第二，让不同角色能修改和维护这些上下文；第三，让 agent 在执行代码、设计、文档等任务时持续继承同一套项目判断。

## 值得质疑
文章提出的问题很准确，但论证仍偏方向性判断。它没有展开 collaborative steering 如何处理版本控制、权限、冲突解决、局部实验、个人偏好与团队约束的边界，也没有给出 Intent 在真实团队中减少分裂的具体案例或指标。

真正难点可能不只是工具形态，而是组织决策：团队必须先愿意把“什么是好产品”写成可执行上下文，并持续维护。没有这一层共识，collaborative steering 也可能只是把分歧从会议室搬进 prompt 仓库。

## 最后一层
Agentic workflow 会让团队协作从“同步人的行动”转向“同步机器继承的判断”；谁能把团队品味、约束和专业分工做成轻量可维护的 steering system，谁就能把 AI 从个人加速器变成组织级产品能力。
