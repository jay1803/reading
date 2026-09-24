---
title: "AI Skills with Matt Pocock"
date: 2026-09-24T16:18:29Z
category: reading
description: "Matt Pocock 认为 AI agent 已能承担大量具体编码工作，工程师价值转向确定方向、组织上下文、校验结果，以及维护对 agent 友好、可读性强的代码库。"
source: "https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock"
author: "Gergely Orosz"
---

Matt Pocock 的判断是：AI agent 已能承担大量具体编码工作，工程师的价值因而更集中在确定方向、组织上下文、校验结果，以及维护一个让新接手者也能理解的代码库。

他的职业路径也围绕自主安排工作展开。做声乐教师时，Matt 为学习唱歌的学生自学 JavaScript，做了一个网页音频频谱分析工具；此后，他用大量两分钟的 TypeScript 技巧视频积累受众。收到 Vercel 的全职邀请后，他谈成每周工作三天的合同，把其余时间留给 Total TypeScript。课程成功后，他离开 Vercel，专注技术教育；Total TypeScript 的累计销售额超过 250 万美元。他说自己不在周末工作，也不认同"9-9-6"：事业安排的目标是有更多时间陪伴家人。

在 AI 辅助开发中，Matt 借用 John Ousterhout 对 **tactical programming** 与 **strategic programming** 的区分：agent 擅长执行局部任务，人则需要更多地决定做什么、如何拆解，以及何时纠偏。他的 **grill-me** skill 源于 Anthropic 的 Thariq Shihipar 分享的做法，指令很短，核心是让 agent 持续追问用户，先把含糊的想法问清楚。他也使用 **wayfinder** 辅助规划和调整，并通过拆分上下文，避免 agent 在长任务中离开其表现较好的"smart zone"。

给 agent 合适的软件工程概念，能直接改变它的实现路径。Matt 发现 agent 倾向于逐层搭建应用，层与层的接口容易出错；读到《The Pragmatic Programmer》中的 **tracer bullet** 后，他让 agent 先打通一条端到端的"golden path"，得到的代码质量更好。为寻找这类有效的引导词，他重新阅读经典软件工程著作。他还把代码库想象成要交给一位每天醒来都失去记忆的同事：人能靠经验记住坏代码的绕行办法，agent 却在每次会话中重新开始。因此，清晰的结构、可读性和可靠的约束，对 agent 尤其重要，也正是软件工程基本功长期试图解决的问题。

这种工作方式也改变了他的工具选择和验证标准。他正把编码会话迁往云端，让 agent 在合上笔记本后继续运行，并使协作成为可能。对于 TDD，他认为失败的测试能提醒容易分心的人类开发者还有什么没完成；agent 拥有更长的上下文窗口，他现在更看重它能否提供代码确实有效的证据，无论过程是否采用 TDD。编码越来越容易交给 agent，工程师仍须判断系统是否健康、结果是否可信；技术教育中的人与人之间的教学，也不会因此失去作用。
