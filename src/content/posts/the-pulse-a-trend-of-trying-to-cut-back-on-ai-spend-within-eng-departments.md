---
title: "The Pulse: a trend of trying to cut back on AI spend within eng departments?"
date: 2026-06-12T08:01:58Z
category: reading
description: "AI 编程工具产生的生产力数字（代码提交率、token 用量）与实际交付的有价值功能之间，目前没有可观测的直接连线；与此同时，公司的 AI 支出已飙升到与可观测性工具同一量级——下一个晋升机会可能不在于\"多用 AI\"，而在于\"用更少 token 做同样的事\"。"
source: "https://newsletters.feedbinusercontent.com/eaf/eaff2bc91240b77a9e964c440b2c2ec43dd7f247.html"
---

## TL;DR

AI 编程工具产生的生产力数字（代码提交率、token 用量）与实际交付的有价值功能之间，目前没有可观测的直接连线；与此同时，公司的 AI 支出已飙升到与可观测性工具同一量级——下一个晋升机会可能不在于"多用 AI"，而在于"用更少 token 做同样的事"。

## 核心主张拆解

Uber 总裁 Andrew McDonald 的播客发言是最清晰的问题表述：Uber CTO Praveen 因为三月中旬就烧完了 2026 全年 AI 预算而在网上走红，McDonald 本人也坦承——即便 25% 的代码提交通过 Claude Code 完成，也无法画出一条线连到"多了多少有用的消费者功能"上。

各公司的应对策略已经明显分化：
- *尖端科技公司*（两家匿名 CTO/工程总监）：无法证明 ROI，但感觉不用顶级模型就会多出 bug，正在研究基于 use case 的智能模型路由来降费
- *DoorDash*：月度 token 上限，超限需要向团队说明理由并分享下月降本方案，定期知识共享会以"高效 AI 用法"为主题
- *传统大公司*（美国最大退休储蓄公司之一）：一个月前上线了 GitHub Copilot 月度 token 限额，超额后自动降级到免费的弱模型（GPT-5 mini、GPT-4.1、Grok Code Fast）
- *创业公司*：不用 API，给开发者批量订阅 Claude Code Max / Codex Max，绕开高单价

## 背后逻辑

效率优化的驱动力是自下而上的——作者特别强调，这些知识分享会是工程师发起的，没有自上而下的命令。OpenCode 创始人 Dax Raad 透露，最近一个月每笔新的企业入单都是关于优化 AI 开支的。Sam Altman 在 Uber 播客的一周后也公开说 AI 预算管控是大问题，呼应了这篇文章的发现。

## 反驳或薄弱处

*证据薄弱处*：全文依赖匿名消息源，没有具体数字（节省了多少 token、节省了多少美元）。"无法建立 ROI 连线"本身也可能是短期认知问题，而非长期结构性困境。晋升靠"省 token"这个预测目前完全基于作者推断，没有任何公司已经宣布这类政策。

## 结

AI 预算管控能否像两年前降第三方 SaaS 成本那样，真正形成可量化的组织激励，取决于一个缺失的数字：省下 X 万美元 token 费用，等价于多交付 Y 个功能。这个数字一旦建立，行为就会立刻改变；在那之前，所有管控都只是防御性的限额，而不是进攻性的效率文化。
