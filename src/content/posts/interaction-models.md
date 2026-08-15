---
title: "Interaction Models"
date: 2026-05-13T08:01:53Z
category: reading
description: "Thinking Machines 的关键主张：AI 的瓶颈不只是能否独立完成长任务，而是能否在任务进行中保持实时共同在场。交互能力若继续依赖 VAD、ASR/TTS、前端 harness 拼装，会随着模型变聪明而成为协作瓶颈；它必须成为模型训练目标本身。"
source: "https://thinkingmachines.ai/blog/interaction-models/"
---

## TL;DR
Thinking Machines 的关键主张：AI 的瓶颈不只是能否独立完成长任务，而是能否在任务进行中保持实时共同在场。交互能力若继续依赖 VAD、ASR/TTS、前端 harness 拼装，会随着模型变聪明而成为协作瓶颈；它必须成为模型训练目标本身。

## 核心主张
- 当前通用模型仍是回合制单线程：用户输入时模型等待，模型输出时感知冻结，沉默、打断、重叠、视觉变化都被压扁成离散 turn。
- 真实工作常常无法一次性完整规格化，人需要边做边澄清、纠偏、展示、插话；过度强调 autonomous agent 会把人挤出协作回路。
- TML 要训练模型原生理解“何时听、何时说、何时等、何时打断、何时并发工具/后台任务”，让交互性随 intelligence 一起 scale。

## 技术机制
- 多流 micro-turn：音频、视频、文本被切成约 200ms 输入/输出块，按时间交织成同一 token 序列，使模型持续感知并持续回应。
- Encoder-free early fusion：音频用 dMel+轻量 embedding，图像拆 40×40 patch 经 hMLP，音频输出用 flow head，减少独立编码器/解码器边界。
- Streaming sessions：推理端把每个 200ms chunk 追加到 GPU 内持久序列，降低频繁小 prefill 开销；相关能力已 upstream 到 SGLang。
- 前台 interaction model 负责实时在场；后台 model 负责深推理、搜索、工具调用，结果流式回传并由前台择机织回对话。

## 证据
- TML-Interaction-Small 是 276B MoE、12B active；文章称它在 FD-bench 交互质量与 Audio MultiChallenge 智能/指令跟随组合上形成 frontier，并取得最佳响应性。
- 他们新增/改造 TimeSpeak、CueSpeak、RepCount-A、ProactiveVideoQA、Charades 等评测，测试按时说话、发音纠错、动作计数、视觉变化触发回应等能力。
- 关键差异：商业 realtime API 多靠音频 turn detection；交互模型把主动视觉/语音插话变成模型能力，而不是 UI 规则。

## 为什么重要
- AI 界面可能从 chatbox 变成“共享注意力层”：模型持续看、听、说、操作，用户随时介入，工作不再被 prompt/response 切碎。
- 对产品：coding、教育、翻译、会议、研究、创作工具的默认交互会更接近“并肩协作”。
- 对基础设施：低延迟多模态推理、持久 GPU session、实时安全、并发工具调用会成为核心能力。

## 值得质疑
- 证据主要来自自家 benchmark 和研究预览，缺少真实协作场景里的产出质量、误打断成本、疲劳感与长期信任数据。
- 276B MoE 加连续音视频对成本、网络和上下文管理要求很高，短期更像高端云端交互。
- 长会话里什么该记住、何时插入后台结果、如何避免打断，仍是产品和模型共同难题。

## 最后一层
这篇文章把问题从“AI 能不能自己做完任务”推进到“人类情境知识能否在工作进行中持续进入模型”。这可能比单纯拉长 agent 任务时长更接近真实协作的上限。
