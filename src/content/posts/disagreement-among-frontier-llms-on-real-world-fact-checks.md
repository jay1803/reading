---
title: "Disagreement among frontier LLMs on real-world fact-checks"
date: 2026-05-29T08:01:14Z
category: reading
description: "前沿模型在真实用户事实核查上不是偶发分歧，而是系统性无法稳定落到同一判定桶：5 个模型对 1000 条新近真实请求给出四选一 verdict，67% 至少有一个模型不同意多数，34% 出现跨 2 桶以上的实质分歧；在没有人类真值前，这不能证明哪个模型错，但足够证明单模型 fact-checking 会把模型间不一..."
source: "https://lenz.io/research/llm-disagreement"
---

## TL;DR
前沿模型在真实用户事实核查上不是偶发分歧，而是系统性无法稳定落到同一判定桶：5 个模型对 1000 条新近真实请求给出四选一 verdict，67% 至少有一个模型不同意多数，34% 出现跨 2 桶以上的实质分歧；在没有人类真值前，这不能证明哪个模型错，但足够证明单模型 fact-checking 会把模型间不一致伪装成确定答案。

## 发现
- 样本是 Lenz 平台 1000 条最近的真实用户事实核查请求，均不早于 2026-02-15；作者只使用经标准化后的 atomic claim 和提交日期，不使用 Lenz 自己的 verdict 作为真值。
- 5 个模型包括 GPT-5.4、Claude Opus 4.7、Gemini 3 Pro、Gemini 3 Pro + Search、Sonar Pro；前三个偏参数模型，后两个带检索增强。
- 67% 的 claims 出现非一致判定：至少一个模型偏离多数，或 5 个模型无法形成严格多数。
- 34% 的 claims 出现最大 pairwise bucket distance >= 2，即不只是 True vs Mostly True 这种校准差异，而是可能变成 True vs Misleading / False 级别的答案冲突。
- Krippendorff's alpha ordinal = 0.639，说明模型判定不是随机噪声，但也远不到可以把 5 个模型视为可互换裁判的程度。
- 如果最慈善地假设多数 bucket 就是真值，下界仍然是：67% 的 claims 至少 1 个模型错，45% 至少 2 个模型错，13% 至少 3 个模型错；若多数也可能错，真实错误数只会更高。
- 分歧最严重的位置不是两端的 True / False，而是 Mostly True 和 Misleading：当 panel 落到中间 bucket 时，几乎无法形成高度一致。

## 为什么重要
这篇文章的核心不是“某个模型更差”，而是给事实核查产品提供了一个结构性风险指标：当真实世界 claim 没有标准答案、语境有时间锚点、四档标签本身有模糊边界时，模型输出的确定性标签会掩盖背后的判定不稳定。

多数投票也不能解决根本问题。作者明确说多数 verdict 不是 ground truth，只是测量分歧的结构参照；如果一个产品把“5 个模型里 3 个同意”包装成事实真相，它只是把 epistemic uncertainty 压成了 UI certainty。

检索增强也没有消除分歧。Gemini 3 Pro + Search 和 Sonar Pro 被纳入同一 panel，但整体仍有 67% 非一致率，说明问题不只是“模型没查资料”，还包括 claim framing、rubric interpretation、时间语境、来源选择和中间标签边界。

## 破坏了什么常识
文章削弱了一个常见假设：只要换成更强 frontier model，事实性判定就会自然收敛。这里的样本不是公开 benchmark，而是最近 180 天的真实用户提交，且没有公开 gold label 可背诵；在这种分布上，强模型之间仍然大量分裂。

它也提醒“LLM-as-judge”在开放事实判断上有硬边界。模型之间 alpha=0.639 已经显示出某种共同结构，但这个结构不足以支撑单一裁判式自动化，尤其是涉及 Mostly True / Misleading 这类需要语境、程度和误导性判断的标签。

## 值得质疑
- 研究没有人类标注真值，因此不能推出任何单模型准确率，也不能判断 Lenz、模型多数、或 dissenting model 谁更接近事实。
- 样本来自单一事实核查平台，不是“所有现实事实核查问题”的概率样本；用户来源、热点事件、平台筛选和重复提交都会放大或缩小分歧。
- 四档标签被当作有序尺度计算 bucket distance，但 True / Mostly True / Misleading / False 之间未必等距；2 桶差异可能来自 rubric 解释差异，而不一定是同等幅度的事实错误。
- 检索增强模型实际查到什么来源不可控，文章没有审计 retrieval path，因此无法分离“事实推理分歧”和“检索来源分歧”。

## 最后判断
这篇研究最有用的结论是产品层面的：事实核查型 AI 不应只返回一个 verdict，而应暴露 disagreement、证据路径和中间标签的不确定性；否则越强的模型界面，越容易制造一种并不存在的事实一致性。
