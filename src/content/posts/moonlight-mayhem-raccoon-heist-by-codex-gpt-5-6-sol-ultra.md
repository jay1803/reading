---
title: "Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)"
date: 2026-08-16T21:37:26Z
category: reading
author: "Simon Willison"
description: "同一份一次生成提示让 GPT-5.6 Sol Ultra 做出更完整的浣熊盗窃游戏，却仍放过极显眼的视觉故障，说明最终验收不能交给代理自身。"
source: "https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything"
---

## 更强的生成不等于可靠的验收

同一份一次生成提示让 Codex Desktop 的 GPT-5.6 Sol Ultra 做出更完整、也更贴近“浣熊盗窃团”设定的游戏；它却在开发过程中审阅截图后，仍放过每只浣熊头顶悬着巨大黑色球体的显眼故障。52 分钟的代理运行足以产出可玩的作品，最终视觉验收仍需独立执行。

## 同一前提被落实成了真正的盗窃关卡

先前 Claude Fable 5 的版本让单只浣熊在后院收集硬币和鱼；Sol 的版本把任务放进博物馆，玩家要救出两名同伴，三只浣熊叠起来从展柜中取走金色沙丁鱼。玩法目标、场景和角色协作由此对齐了原始“组队浣熊行窃”的前提。

## 产物可复查，修复却来自极短的人工反馈

仓库保存了可玩的游戏、用 gpt-image-2 生成的纹理与提示词，以及完整 Codex 转录。作者只问“为什么浣熊身上有巨大的黑球？”再下达“修复它”，就得到对应提交；这说明代理已经留下可审计的工作痕迹，错误识别本身仍是交付链中缺失的一环。
