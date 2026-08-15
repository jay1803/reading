---
title: "From journalist to iOS developer: How LinkedIn's editor builds with Claude Code | Daniel Roth"
date: 2026-03-18T08:02:09Z
category: reading
description: "Daniel Roth，LinkedIn 主编，资深商业记者出身（曾任职 Fortune、Wired、Forbes），无软件工程背景。过去两年通过 Claude Code 独立开发了两款 iOS 应用并上架 App Store，周末是他的\"建造时间\"。主持人 Claire Voe 为产品负责人，How I AI..."
source: "https://www.lennysnewsletter.com/p/from-journalist-to-ios-developer"
---

## 嘉宾背景

Daniel Roth，LinkedIn 主编，资深商业记者出身（曾任职 Fortune、Wired、Forbes），无软件工程背景。过去两年通过 Claude Code 独立开发了两款 iOS 应用并上架 App Store，周末是他的"建造时间"。主持人 Claire Voe 为产品负责人，How I AI 播客主理人。

## TL;DR

非技术背景的人不需要学会编程，只需要找准一个角色：最挑剔的客户。AI agent 负责建造，你负责品味与判断——而这个角色，恰好是记者和编辑最擅长的。

## Bob + Ray：用角色分工解决 AI 的"永远 rubber stamp"问题

Claude 默认会认同你说的一切。Roth 的解法是拆出两个有角色约束的 agent：Bob the Builder 只管按计划建造、模块化推进、强制记录文档；Ray 是一个"痴迷安全的资深工程师"，被明确指示必须说不，负责在 Bob 出计划后进行代码里程碑审查。

关键机制：Bob 在构建前必须暂停并把计划递给 Ray 审核；Roth 本人作为"第三个 agent"负责在两者出现分歧时拍板。Bob 可以生成子 agent，但子 agent 不能再生成子 agent；Ray 没有任何下属，也不接受管理——这是有意为之的"唯一守门人"设计。

这个三角结构模拟的是 Roth 在 LinkedIn 观察到的真实工程团队动态：principal engineer 就是那个所有人都要去问"这行不行"的人。

## 非技术背景者的真实角色：最挑剔的客户

Roth 先后将自己定位为"蹩脚 PM"、"架构师"，最终否定了两者——PM 要能把整个 app 装进脑子里、懂得优先级；架构师要掌握真实细节。他做不到。他真正能做的是：走进这栋房子，指着墙说"我要这个房间是蓝色，我知道你不建议，但我要"。

这个角色的核心能力不是技术判断，而是清晰知道自己在意什么——品味、语气、UX 细节、app 的"声音"。他为自己的播客剪辑 app 亲自写了等待提示的文案，因为系统默认的"视频正在生成"语气不够有趣。

## 所有东西写进 .md 文件：上下文窗口就是记忆断层

Roth 只在周末写代码，每次开始都记不清上次做到哪里。解法：强制 Bob 把所有决策、计划、review 结果都记录进项目目录的 markdown 文件。这同时解决了两个问题——Claude 的上下文遗忘，和他自己的遗忘。

配套的是一个持续维护的功能优先级聊天窗口，按"构建时间"和"增长影响"两个维度自动排序，让他在有两小时空余时能立刻找到匹配体量的任务。

## 晚间"我今天搞砸了什么"提示词

工作流层面，Roth 把 AI 最高价值的时间点从早晨移到了下班前 30 分钟：用一个固定提示词问 Copilot"我今天在哪些事上没有跟进"，让它扫描 Outlook、Teams、近期文件，找出未回复的邮件、被遗漏的升级请求、自己关注但没有行动的项目线索。他认为这比早晨的日程摘要更有价值——因为你还有时间补救。

## 留下的那个想法

App Store 是 vibe coding 时代最后一道真正的摩擦。写代码、测试、上 TestFlight——这些 Claude 都能帮你搞定；但导航 Apple 的审核流程、截图规范、元数据要求，目前还完全靠人肉摸索。Roth 说他正在考虑用 Claude Code 建一个工具专门处理 App Store 截图生成。这个"最无聊但价值最高"的场景，可能是下一个被 AI 解锁的地方。
