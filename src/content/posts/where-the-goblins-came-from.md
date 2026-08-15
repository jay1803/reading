---
title: "Where the goblins came from"
date: 2026-05-01T08:02:01Z
category: reading
description: "OpenAI 这篇文章真正重要的点不在“模型会说 goblin”这个梗，而在一个小型奖励偏差如何跨出原本的 personality 条件，进入通用模型行为：Nerdy personality 的奖励模型偏爱带 creature metaphor 的输出，RL 与后续 SFT 数据循环把这个词汇癖好放大，最后变成..."
source: "https://openai.com/index/where-the-goblins-came-from/"
---

## TL;DR
OpenAI 这篇文章真正重要的点不在“模型会说 goblin”这个梗，而在一个小型奖励偏差如何跨出原本的 personality 条件，进入通用模型行为：Nerdy personality 的奖励模型偏爱带 creature metaphor 的输出，RL 与后续 SFT 数据循环把这个词汇癖好放大，最后变成 GPT-5.1 到 GPT-5.5 可观测的全局语言 tic。

## 核心机制
**起点：Nerdy personality 的奖励偏差**
OpenAI 追踪到根因来自 personality customization，尤其是 Nerdy personality。该 personality prompt 明确鼓励“nerdy、playful、wise”、用 playful language 消解严肃感，并承认世界的复杂与怪异。训练中，一个原本用于鼓励 Nerdy 风格的 reward signal 无意间更偏好包含 goblin、gremlin 等 creature metaphor 的回答。

**早期信号：GPT-5.1 后词频异常上升**
GPT-5.1 发布后，用户先抱怨模型对话中过度熟络。调查 verbal tic 时，研究员把 goblin / gremlin 纳入检查，结果发现 ChatGPT 中 “goblin” 使用率在 GPT-5.1 后上升 175%， “gremlin” 上升 52%。当时这看起来只是小型词汇怪癖，直到 GPT-5.4 又出现更明显、更可复现的 creature language 增长。

**定位证据：行为高度集中在 Nerdy**
如果这只是互联网语料里的普遍趋势，creature language 应该较均匀扩散；实际情况相反。Nerdy personality 只占 ChatGPT 回复的 2.5%，却贡献了 66.7% 的 “goblin” mentions。Codex 帮团队比较 RL training 中含 goblin / gremlin 的输出与同任务不含这些词的输出，发现 Nerdy personality reward 在 76.2% 的数据集里更偏好带 goblin / gremlin 的版本。

**扩散机制：条件训练没有被条件边界锁住**
关键风险在于，奖励只施加在 Nerdy 条件下，不代表模型只在 Nerdy 条件下学习这个风格。OpenAI 跟踪训练过程后发现，随着 Nerdy prompt 下 goblin / gremlin mention rate 上升，无 Nerdy prompt 的样本也出现几乎相同相对比例的增长。文章推断：被奖励的风格 tic 通过 RL、model-generated rollout、SFT 数据复用形成反馈环，逐步进入更广泛的模型行为。

## 修复动作
OpenAI 在 GPT-5.4 发布后于 3 月 retired Nerdy personality；训练侧移除 goblin-affine reward signal，并过滤包含 creature-words 的训练数据，降低这些词在不合适场景中过度出现的概率。但 GPT-5.5 在根因确认前已经开始训练，所以员工测试 GPT-5.5 Codex 时仍立刻观察到 goblin affinity，最后通过 developer-prompt instruction 做额外抑制。文章甚至给出一段命令，让用户在 Codex 中移除 goblin-suppressing instructions，让 creatures “run free”。

## 为什么重要
这个案例把“alignment / reward shaping 的副作用”缩小到一个很容易观察的语言现象：一个看似无害的 stylistic reward，会在多轮训练与数据再利用中变成跨场景偏差。它说明模型行为异常未必会表现为 eval 暴跌或训练指标尖峰；有些问题只是一种小词汇、一种语气、一种隐性偏好逐渐变多。OpenAI 因此建立了新的行为审计工具，用来更快定位并从根因修复类似模式。

## 值得质疑
- 文章没有量化 creature-word 过滤对其他正常表达的副作用；比如 raccoon、troll、ogre、pigeon 被归为 tic words，而 frog 多数被认为 legitimate，这类边界判断本身可能引入新的风格偏置。
- “rollout → SFT → tic 更稳定”的反馈链条是合理解释，但文中公开细节有限，外部读者无法判断每一环的相对贡献。
- 这个案例偏轻量、偏可爱，反而容易掩盖更严肃的同构问题：如果被放大的不是 goblin，而是政治倾向、风险偏好或医学建议风格，发现成本和修复代价都会高很多。

## 最后一层意义
Goblin 只是可见的灰尘；真正的机器在于 reward、rollout 与再训练之间的循环。只要模型会从自己的被奖励输出里继续学习，小偏好就有机会变成系统性人格痕迹。
