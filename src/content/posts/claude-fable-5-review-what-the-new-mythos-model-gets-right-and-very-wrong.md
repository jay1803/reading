---
title: "Claude Fable 5 review: what the new Mythos model gets right (and very wrong)"
date: 2026-06-10T08:01:08Z
category: reading
description: "Claire Vo，ChatPRD 创始人、产品经理，AI 工具长期测评者。Anthropic 在 Fable-5 正式发布前邀请其提前体验。播客：How I AI（howiaipod.com）。"
source: "https://www.lennysnewsletter.com/p/claude-fable-5-review-what-the-new"
---

## 嘉宾背景

Claire Vo，ChatPRD 创始人、产品经理，AI 工具长期测评者。Anthropic 在 Fable-5 正式发布前邀请其提前体验。播客：How I AI（howiaipod.com）。

## TL;DR

Fable-5 是 Mythos 穿了安全紧身衣的同款底层——给了大众一个"够用的"高智商模型，但真正的价值不是替换你所有的 workflow，而是作为 orchestrator 调度更便宜的模型去执行。让 Fable 指挥，让 Sonnet 写 PRD。

## Mythos 的真面目：Fable 是被套上 safeguards 的同款模型

Fable-5 与 Mythos 底层相同，区别仅在 safeguards：网络安全、生物、化学、蒸馏四类分类器会触发 fallback，将请求优雅降级至 Opus 4.8，而非硬拒绝。95% 的会话不会触发。Project Glasswing 合作企业拿到的 Mythos 没有这层限制，但对普通用户来说，Fable 是唯一通道。

## 基准碾压一切，但 token 消耗是其他模型的 2 倍

SWE-Bench Pro 达到 80%，大幅领先 GPT-5.5、Gemini 3.1 Pro 和 Opus 4.8。定价 $10/百万输入 token、$50/百万输出 token，新建一个高于 Opus 的价格层。Anthropic 官方说"high"是大多数任务的甜点，Claire 全程用 extra high，结论是：智商越高，token 烧得越猛，但产出质量是否值这个成本，仍不确定。

## 视觉能力意外拔尖，文字输出像工程师在写技术文档

视觉/文档格式化方面明显超越 Opus 4a——给 7 岁孩子设计手写练习纸，Fable 在间距、留白、可读性上更胜一筹。但写作风格是软肋：内部引用密集、长段落堆砌、无法 zoom out，PRD 审查输出"完整但几乎无法解读"。Claire 的建议：规格、策略、散文类工作退回 Sonnet 或 Opus。

## 太"工程师"了：严谨性反而成为产品交付的障碍

工程师式彻底性让它在技术审查和 edge case 挖掘上可靠，但让它独自跑 MVP 时，"minimal"被诠释得极其保守，产出没有实际用户价值。UI 设计更是翻车：一键生成的技术注册中心界面是灰黑红色简单轮廓，被 Claire 评为"从根本上就是烂设计"——即使追加更详细的 prompt 也改善有限。**证据薄弱处**：一次性 UI 测试样本极小，可能对提示词敏感度很高。

## 多智能体编排有成功有卡死，长日任务的技术承诺尚未兑现

成功触发了多智能体任务，但也遇到 3 小时后无声挂起的问题（Claude Code harness 问题，非纯模型问题）。days-long 会话的承诺在技术层面仍待验证——智能体够聪明，但配套 harness 的稳定性决定上限。

## 收束行

当"太聪明"变成用户体验的负担，真正稀缺的能力不是找到更好的模型，而是学会为每类任务匹配恰当的智商档位——这是 AI 时代最被低估、也最难系统化的工程判断。
