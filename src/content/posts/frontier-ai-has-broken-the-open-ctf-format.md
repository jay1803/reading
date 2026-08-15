---
title: "Frontier AI has broken the open CTF format"
date: 2026-05-17T08:01:23Z
category: reading
description: "Frontier AI 把公开在线 CTF 从“人类安全能力阶梯”改造成了“模型编排 + token 预算竞赛”。关键变化不是 AI 能辅助解题，而是足够多 easy / medium / 部分 hard 题已经可被 agent 自动烧穿，导致 scoreboard 不再干净衡量人类技能、学习进步和挑战设计的艺术性。"
source: "https://kabir.au/blog/the-ctf-scene-is-dead"
---

## TL;DR
Frontier AI 把公开在线 CTF 从“人类安全能力阶梯”改造成了“模型编排 + token 预算竞赛”。关键变化不是 AI 能辅助解题，而是足够多 easy / medium / 部分 hard 题已经可被 agent 自动烧穿，导致 scoreboard 不再干净衡量人类技能、学习进步和挑战设计的艺术性。

## 核心主张拆解
### Scoreboard 已经失去原来的含义
作者的判断来自长期一线经验：他从 2021 年开始打 CTF，赢过澳洲大型赛事 DownUnderCTF，加入过全球高排名队伍 TheHackersCrew，并长期在顶级 CTF 中进入前 10。这个背景让他的论点不是“外部观察者唱衰”，而是一个受益于旧赛制的人在说：旧游戏已经不在了。

GPT-4 时期，中等难度题开始出现 one-shot：把 crypto 题贴进 ChatGPT，十分钟后可能拿到 solve 和 flag。那时 hard 题仍基本安全，AI 只是提速工具。Opus 4.5 / Claude Code 之后，变化变成结构性的：几乎所有 medium、部分 hard 可以被 agent 求解；CTFd API + CLI + MCP 工具让队伍能为每道题启动一个 Claude 实例，先自动跑一小时，再让人类处理残留难题。

结果是公开 CTF 的排名开始混合衡量三件事：安全能力、AI 编排能力、愿意投入多少 frontier model 资源。拒绝使用 AI 的队伍不是少了工具，而是在玩一个更慢的版本。

### Pay-to-win 化不是未来风险，而是当前趋势
作者认为 GPT-5.5 / GPT-5.5 Pro 已接近或超过 Claude Mythos 级别，能 one-shot HackTheBox 的 Insane active leakless heap pwn，并能解决很多小型 CTF 组织者现实可产出的题。若在 48 小时赛中把 Pro agent 持续砸向难题，拿 flag 的概率已足够高。

这会把公开 CTF 推向 token-burning 竞赛：谁能并行更多 agent、给更多上下文、跑更久，谁就更快清空 scoreboard。专用安全模型反而可能被通用 frontier LLM 吞没，因为通用模型已经足够强，且周边编排工具开源或 vibe-codeable。

## 被破坏的反馈循环
### 初学者失去可攀爬的梯子
CTF 不只是题库，而是一条可见成长路径：解更多题、排名上升、加入更强队伍、逐渐进入高手圈。若公开榜单被 AI 队伍占据，初学者会被迫过早使用 AI 才能看到进步；但这正好绕过了真正训练直觉的 active struggle。学习平台如 picoGym、HackTheBox 更适合作为新手入口，因为默认目标是教育，而不是假装公开榜单仍代表人类成长。

### 出题者的艺术动机被削弱
好的 CTF challenge 往往是安全技巧、审美和谜题设计的结合。若作者花数周打磨的题几分钟内被 agent 吃掉，创作动机自然下降。更糟的是，为了阻止 LLM，题目会被迫变得猜谜化、过度工程化、对人类也不友好。

### 招聘和声望信号变差
过去 CTF 表现能粗略代表安全实践能力；现在它越来越像“能否高效部署 AI 解题管线”。这既不纯粹衡量人类安全技能，也不特别衡量 AI 能力，因为基础编排已足够商品化。

## 为什么常见反驳不成立
### “顶级决赛 AI 还解不了”救不了公开赛制
DEF CON 等顶级 finals 仍有 AI 无法处理的题，但参与者极少，而且通常由更容易被 agent 攻破的 qualifier 筛选。若 qualifier 已被自动化，真正有资格的人未必能进入仍需要人类深度能力的题目。少数 elite finals 不能证明大多数人实际参与的 open online format 仍健康。

### “AI 增强 CTF”需要诚实改名
若未来赛制承认自己是 AI orchestration benchmark，那可以讨论新规则；但不能一边允许 unrestricted AI，一边继续声称 scoreboard 衡量的是旧式人类 CTF 技艺。作者用国际象棋类比：引擎可以训练、复盘、解说，但正式比赛中不允许选手边下边开最强引擎。

### 反 LLM 技巧只是临时摩擦
拒绝字符串、prompt injection、训练截止日期后的技术点、禁止 AI 的规则，都无法长期解决问题。模型越来越会绕过提示攻击，web search 削弱 cutoff 设计，开放线上赛也几乎无法强制执行 no-LLM rule。组织者陷入两难：正常题会被 agent 解太多；专门敌对 AI 的题又会伤害人类体验。

## 值得质疑
- 文章大量依赖作者和社区体感，例如 CTFTime 失真、老牌队伍减少参赛、作弊上升；方向可信，但缺少系统数据支持。
- GPT-5.5 / Pro 的能力描述如果不能外部复现，可能高估了短期普遍性；不过即便只对中等题成立，也足以破坏公开榜单信号。
- “公开 CTF 已死”可能过于绝对；更准确的说法是：未分离 AI-assisted / human-only / education-first 的旧开放赛制已经失去原本功能。

## 最后一层
这篇文章真正哀悼的不是 puzzle 数量减少，而是一个社区机制的坍塌：从好奇心到高手、从个人挣扎到团队声望、从出题艺术到公共排行榜的连续路径被切断了。CTF 社区仍值得保留，但它需要新的学习、竞技和线下连接形式；继续维护旧 scoreboard 的幻觉，只会让 AI 包装商更容易把社区遗产卖回给社区。
