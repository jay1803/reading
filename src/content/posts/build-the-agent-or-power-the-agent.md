---
title: "Build the Agent or Power the Agent?"
date: 2026-06-25T08:02:23Z
category: reading
author: "Tanay Jaipuria"
description: "水平 Agent（Claude Code、Codex、ChatGPT）已成为越来越多知识工作者的默认工作界面。对创业者而言，这制造了一个结构性选择：要成为某类用户每天打开的核心 Agent，还是接受他们活在水平 Agent 里、把自己的能力以 MCP/API 的形式暴露给它？"
source: "https://www.tanayj.com/p/build-the-agent-or-power-the-agent"
---

## "Power the Agent"的真正价值是扩大你的用户规模，而不只是一种次优退路

水平 Agent（Claude Code、Codex、ChatGPT）已成为越来越多知识工作者的默认工作界面。对创业者而言，这制造了一个结构性选择：要成为某类用户每天打开的核心 Agent，还是接受他们活在水平 Agent 里、把自己的能力以 MCP/API 的形式暴露给它？

"Build the Agent" 有两个成立条件：一是你已经是用户的 system of record，他们整天都在你的产品里，原生 Agent 体验优于跳出去；二是领域推理本身就是产品，专业度高到水平 Agent 无法胜任（Harvey 对律师的赌注就是这个逻辑）。两条路都意味着足够垂直，才能支撑用户每天来找你而不是去找 Claude。

"Power the Agent" 的价值有两个杠杆：**数据与上下文**（Granola 把会议记录暴露给外部 Agent 消费）、**能力与动作**（Higgsfield 发布 MCP Server，让水平 Agent 调用它的图像视频渲染能力）。Salesforce "Headless 360"、HubSpot 远程 MCP 服务器表明连老牌巨头也在走这条路——"API is the UI"。

### 四个判断维度

1. **用户在哪里工作**：整天在你产品里还是整天在水平 Agent 里？越偏后者越应该 Power it。
2. **你拥有完整工作流还是一个切片**：完整拥有才有资格做 Agent；只拥有切片，编排权在上游 Agent 手里。
3. **价值在推理还是在数据/动作**：推理密集且高度垂直→Build；数据与动作→Power。
4. **工作是否必须在单一 App 里完成**：高管控、多步骤判断→Build；可组合、单一能力→Power。

### 两条路同时走，但面向的是两种用户

多数公司最终会做两件事：对核心重度用户（活在自己产品里的）内嵌 Agent，对边缘用户（只需要你一个切片的）暴露 Headless MCP 层。这不是妥协，而是精准分层——Salesforce 的销售 power user 用原生 Agent，其他角色通过 ChatGPT 拉 pipeline 数据。

最不显然的结论：Power the Agent 这条路不只是防守性选择，它的天花板更高——它能触达那些本来永远不会打开你产品的用户，因为他们不需要再学一个新工具，直接在自己的 Agent 里调用你就行了。
