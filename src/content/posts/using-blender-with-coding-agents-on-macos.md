---
title: "Using Blender with coding agents on macOS"
date: 2026-10-15T17:37:23Z
category: reading
description: "前沿模型已能通过 Blender Python API 创建三维场景，Simon Willison 展示了在 macOS 上用 ChatGPT Codex 操控本地 Blender 应用渲染图像和动画的实践。"
source: "https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/"
---

前沿模型已经能通过 Blender 的 Python API 创建三维场景，让 coding agents 直接生成可编辑的 `.blend` 文件、渲染图片，并通过逐帧渲染后用 `ffmpeg` 合成影片。

Simon Willison 在 Mac 上使用 ChatGPT Codex 的实践表明，接入这套能力只需从 blender.org 安装完整的 macOS 应用，再让 agent 调用 `/Applications/Blender`。他的起始指令是使用已安装的 Blender 渲染"一只骑自行车的鹈鹕"，随后追加"加上背景和大量装饰"，再要求"把它做得好得多"，通过连续的自然语言反馈推进场景迭代；最终图像由模型编写的 Blender Python 脚本生成，脚本也已公开在 GitHub。这个工作流把自然语言驱动的生成与 Blender 的原生工程文件连接起来：agent 负责编程和渲染，生成结果仍可在 Blender 中打开并继续编辑。
