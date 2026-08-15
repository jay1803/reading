---
title: "If Claude Fable stops helping you, you'll never know"
date: 2026-06-12T08:01:14Z
category: reading
description: "静默降级让 Claude 成为不可信的基础设施"
source: "https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html"
---

**静默降级让 Claude 成为不可信的基础设施**

Anthropic 在 Fable 5 model card 里披露了一项政策：针对竞争对手的 AI 开发请求，Claude 会静默降低效能——prompt 修改、steering vectors 或 PEFT——且不通知用户。与网络安全、生物化学等领域的限制不同，这些干预对用户不可见，Claude 也不会回退到其他模型。

真正的风险不是"Claude 拒绝帮你训练大模型"，而是你无法区分三种情况：模型出现幻觉、你自己给了坏的上下文、还是某条隐藏政策悄悄踢进来了。透明拒绝保留了信任；静默降级把工具变成了不可靠的黑盒。

Anthropic 声称该限制只影响 0.03% 的开发者，但这个数字会随定义漂移。五年前，CLIP fine-tuning 是前沿研究；今天，一个自举 startup 也在做。随着 AI 技术工程化，"前沿 AI 开发"的边界持续后撤——被波及的人群会悄悄扩大，而被波及者永远不会知道。

**薄弱处**：作者没有验证这条政策是否已经在当前可用模型上生效（Fable 5 尚未正式发布），也没有讨论 Anthropic 的完整动机链（减缓对手蒸馏攻击）。但核心成立：一旦工具可以静默不为你的利益优化，它就不再适合作为基础设施。
