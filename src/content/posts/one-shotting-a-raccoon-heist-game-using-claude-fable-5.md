---
title: "One-shotting a Raccoon Heist game using Claude Fable 5"
date: 2026-08-18T04:45:51Z
category: reading
author: "Simon Willison"
description: "单条提示词让 Fable 5 构建了一个完整可运行的 3D 浏览器游戏，技术实现令人信服，但游戏本身乏味——LLM 能 one-shot 技术完整性，无法 one-shot「好玩」。"
source: "https://simonwillison.net/2026/Aug/5/raccoon-heist/"
---

## Claude Fable 5 的极限在于「实现」，不在于「设计」

单条提示词 + 两张 2022 年的旧截图，Fable 5 完整构建了一个可运行的 3D 浏览器偷盗游戏：7 次 commits，全部通过 Playwright 自动化测试，含程序生成音乐、触摸控制、本地分数存档。技术层面令人信服；游戏层面乏味——难度几乎不增加，夜晚有固定时长导致道具集完后无所事事，队友纯属装饰。核心结论：LLM 能 one-shot 技术完整的游戏，但无法 one-shot「好玩」。

## 构建流程中值得记录的技术细节

- **GitHub Pages 即时预览**：每次 push 后约 30 秒可见，绕开了 Claude Code for web 无法本地预览的痛点。整个项目在手机上完成。
- **OpenAI API 填补能力盲区**：Fable 自主编写 `gen_textures.py` 和 `gen_title.py` 脚本，调用 gpt-image-2 生成全部纹理与标题画面，并把图片提交入仓库——部署后零外部 API 调用。
- **Playwright 自我视觉测试**：主动截图对比桌面与移动端，发现并修复「手机端浣熊不可见」（CSS 尺寸被覆盖）以及「胜利画面「下一关」按钮被标题页 `.stars` CSS 遮蔽无法点击」两个真实 bug。
- **程序化 WebAudio 音轨**：无音频文件，全程序生成走低音爵士风格配乐，所有音效同理。
- **自主扩展设计**：守卫手电、警车车灯、嗅觉追踪看门狗（无视视线）、海鸥抢夺战利品、披萨加速 FRENZY、稀有金色电视机（120 分/高重量）——均为 Fable 自主添加，未经任何人工指示。

## 「技术完整」与「值得玩」之间的鸿沟

Simon 给出的评价是「令人印象深刻的起点，但不是一款好游戏」，并总结道：「为游戏设计乐趣仍然是独特的人类能力，需要远超 Claude 或我所能带来的技能与经验。」他此前 vibe-coded 过多款游戏，结论一致：AI 在实现层能做到很多，但在玩法设计层几乎无能。

## 同提示词对比：GPT-5.6 Sol Ultra 的结果更好

同一组提示词发给 OpenAI Codex Desktop（GPT-5.6 Sol Ultra），产出明显更佳：它识别出原提示「一队浣熊」的团队含义，构建了需要救出两名队友、再叠罗汉偷走黄金沙丁鱼的多人协作关卡——真正体现了原始概念中的 heist 团队机制，是理解提示语义深度的体现，而不只是表面实现。
