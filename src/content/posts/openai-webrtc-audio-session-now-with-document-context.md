---
title: "OpenAI WebRTC Audio Session, now with document context"
date: 2026-06-14T08:02:30Z
category: reading
description: "Simon Willison 更新了他的 OpenAI WebRTC 浏览器端音频工具，新增两项能力：切换到 GPT-Realtime-2（OpenAI 首个具备 GPT-5 级推理能力的实时语音模型），以及粘贴任意文档上下文，用语音对话方式探索自定义材料。"
source: "https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything"
---

## TL;DR

Simon Willison 更新了他的 OpenAI WebRTC 浏览器端音频工具，新增两项能力：切换到 GPT-Realtime-2（OpenAI 首个具备 GPT-5 级推理能力的实时语音模型），以及粘贴任意文档上下文，用语音对话方式探索自定义材料。

## 具体机制

- **工具地址**：https://tools.simonwillison.net/openai-webrtc，2024 年 12 月首次发布，用于测试 OpenAI WebRTC API
- **模型切换**：用户现在可以在旧版模型和 GPT-Realtime-2 之间选择
- **文档上下文**：支持粘贴大段文本，在浏览器内针对该内容进行语音对话，无需打字

## 背景：GPT-Realtime-2

- OpenAI 上月发布，自称「首个具有 GPT-5 级推理能力的语音模型」
- 知识截止日：2024 年 9 月 30 日
- 在 ChatGPT iPhone 应用中尚未上线；Simon 因此重新启用了自己的 API playground 测试该模型

## 隐藏限制

GPT-Realtime-2 目前仅在 API 层可用，ChatGPT 消费端仍未跟进。这意味着新语音模型的探索窗口期只对开发者开放，普通用户暂时无法受益。
