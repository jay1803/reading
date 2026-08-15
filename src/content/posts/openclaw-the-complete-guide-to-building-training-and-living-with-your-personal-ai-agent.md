---
title: "OpenClaw: The complete guide to building, training, and living with your personal AI agent"
date: 2026-04-02T08:01:08Z
category: reading
description: "OpenClaw 的杠杆不来自于\"一个更强的聊天机器人\"，而来自于多代理协作：每个代理只做一件事、24 小时运行、能自我修复——本质上是把\"雇人\"的逻辑搬到了 AI 上，而单代理做不到这一点。"
source: "https://www.lennysnewsletter.com/p/openclaw-the-complete-guide-to-building"
---

## TL;DR
OpenClaw 的杠杆不来自于"一个更强的聊天机器人"，而来自于多代理协作：每个代理只做一件事、24 小时运行、能自我修复——本质上是把"雇人"的逻辑搬到了 AI 上，而单代理做不到这一点。

## 核心洞见
- **多代理才是真正的 unlock**：Claire 试过让一个 agent 处理所有事，效果差；拆分成 9 个专职代理（个人助理 Polly、家庭管理 Finn、营销 Max、销售 Sam、客服 Holly、课程运营 Sage、播客制作 Howie、开发 Kelly、教孩子的教授 Q）后，每个代理身份更窄，质量反而更好。
- **代理的"身份文件"就是它的操作系统**：SOUL.md（人格与边界）、AGENTS.md（核心指令）、USER.md（关于你的信息）、TOOLS.md（工具备注）——这几个 Markdown 文件决定了代理的上限，写得好不好直接影响实际效果。
- **整合（integrations）是关键**：没有整合，OpenClaw 只是更复杂的 Claude Code；接入 gog（Gmail/Calendar）、GitHub、Linear 之后，代理才能真正替代人力完成具体工作。

## 具体机制
- **架构**：本地 gateway 接收来自 Telegram/WhatsApp/Slack 等渠道的消息，分配给对应 agent；agent 通过 cron job 和每 30 分钟的 heartbeat 持续自主运行。
- **部署选项**：Mac Mini（$600 起）是最推荐的入门硬件；VPS 最便宜但最复杂；托管服务最简单但功能受限。**严禁装在日常使用的电脑上**——代理有完整文件系统访问权限，误操作代价极高。
- **多代理创建**：`openclaw agents add agent_name` 即可新建，代理之间可以互相转移记忆和 cron（"脑科手术"）。
- **成本**：Claire 全 API 模式每月接近 $1,000；用 ChatGPT/Claude 订阅（$100-200/月）可以大幅降低成本。

## 隐藏限制
- **安全漏洞面宽**：代理拥有完整电脑访问权限、可能被 prompt injection 攻击（读到含恶意指令的网页）、接入 Gmail 后可以冒充你发邮件——不要在群聊中暴露代理，给 read-only token 直到充分信任。
- **不可靠是常态**：cron 会自己坏掉，代理会忘事，需要像管远程团队一样定期 check in；Claire 承认自己经常"hellooo?"发消息进虚空。
- **学习曲线在管理，不在技术**：最难的部分不是安装，而是想清楚"这件事该给哪个 agent、它的 SOUL.md 里该写什么"——OpenClaw 要求用户具备基本的管理思维。

## 收束
OpenClaw 最值得注意的副作用：它第一次让人们用"雇员"的眼光看 AI——不是"这个工具能做什么"，而是"这个职位需要什么能力、边界、权限"。这套思维框架比任何具体功能都更值得带走。
