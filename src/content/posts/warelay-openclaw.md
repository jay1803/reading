---
title: "Warelay -> OpenClaw"
date: 2026-05-17T08:01:23Z
category: reading
description: "这篇短文真正记录的不是 OpenClaw 改过几次名字，而是项目定位如何从“WhatsApp 转发工具”一路外扩成“个人 AI 助手”：README 第一行的命名史，比正式路线图更诚实地暴露了产品重心的迁移。"
source: "https://simonwillison.net/2026/May/16/openclaw-names/#atom-everything"
---

## TL;DR
这篇短文真正记录的不是 OpenClaw 改过几次名字，而是项目定位如何从“WhatsApp 转发工具”一路外扩成“个人 AI 助手”：README 第一行的命名史，比正式路线图更诚实地暴露了产品重心的迁移。

## 关键时刻
- 2025-11-24：最早形态是 `Warelay — WhatsApp Relay CLI (Twilio)`，定位非常窄，核心是 WhatsApp + Twilio 的消息中继。
- 2025-11-25：README 开始强调“send, receive, auto-reply”，并从 Twilio 走向 QR-linked WhatsApp Web，功能边界从单一 relay 变成自动回复网关。
- 2025-12-03：改名 `CLAWDIS — WhatsApp Gateway for AI Agents`，第一次把“AI agents”放进项目身份。
- 2025-12-08：加入 Telegram，渠道从 WhatsApp 扩到多消息平台。
- 2025-12-19：标题变成 `Personal AI Assistant`，项目从“消息网关”上升为个人 AI 助手。
- 2026-01-27：短暂出现 `Moltbot`。
- 2026-01-30：最终定名 `OpenClaw — Personal AI Assistant`。

## 背后逻辑
Simon 用 `first_line_history.py` 追踪 README 第一行在 Git 历史里的变化，得到完整链路：`Warelay → CLAWDIS → CLAWDBOT → Clawdbot → Moltbot → OpenClaw`。这个方法的价值在于抓项目自我描述的“第一句”，而不是抓发布稿或事后叙事；第一句通常最能反映开发者当时认为项目是什么。

## 更大意义
OpenClaw 的命名演化体现了一个常见产品轨迹：先从明确、狭窄、可运行的工具切入，再随着能力堆叠逐步抽象成平台级身份。名字变化不是品牌包装，而是抽象层级变化：从渠道工具，到 agent gateway，到 personal assistant。

## 最后一层
如果一个项目的 README 标题频繁变化，未必是方向不稳；也可能是项目正在快速找到更高一层的真实类别。OpenClaw 的名字史像一条小型产品化曲线：从“能做什么”走向“它到底是什么”。
