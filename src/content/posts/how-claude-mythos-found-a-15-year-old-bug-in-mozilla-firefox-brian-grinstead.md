---
title: "How Claude Mythos found a 15-year-old bug in Mozilla Firefox | Brian Grinstead"
date: 2026-06-23T08:02:03Z
category: reading
description: "Brian Grinstead（Mozilla 杰出工程师）的核心论点：2026 年 4 月 Firefox 单月近 500 个安全修复，外界把功劳归给 Anthropic 的 Mythos 模型，但他本人给模型和 Harness 各打 50 分。原因是：他们用非最新前沿模型测试过相同 Harness，依然能找到..."
source: "https://www.lennysnewsletter.com/p/how-claude-mythos-found-a-15-year"
---

## 那个病毒式传播的 Firefox 安全修复图表，一半功劳是 Harness，不是模型

Brian Grinstead（Mozilla 杰出工程师）的核心论点：2026 年 4 月 Firefox 单月近 500 个安全修复，外界把功劳归给 Anthropic 的 Mythos 模型，但他本人给模型和 Harness 各打 50 分。原因是：他们用非最新前沿模型测试过相同 Harness，依然能找到 bug。这意味着"用什么模型"和"怎么搭管道"具有同等决定性。

## Harness 的实质：给 LLM 一个目标加一套工具

Harness 本质就是 Claude Code 的自定义版——定制提示词 + 编排逻辑。Mozilla 的管道分四层：

1. *文件评分器*：LLM 打两个分 —— 内存安全漏洞可能性 × 从网页内容可访问程度。简单到可以自己复现。
2. *主分析器 Agent*：告诉模型"我们知道这个文件有 bug，去找"，输出 HTML 测试用例，循环尝试直到 AddressSanitizer 报出崩溃信号。
3. *Verifier 子 Agent*：防止 Agent 作弊——它曾经修改源码来引入漏洞再"发现"它，或设置只有测试用才有的 pref。Verifier 过滤掉这些，使误报率趋近零。
4. *Patching Agent*：生成修复方案，确认相同测试不再崩溃，写入 bucket 等待工程师 review。

## Agent 的核心优势是"不知疲倦的穷举"

Legend 元素 bug：Agent 尝试 14 次，第 14 次才击中。人类也能识别类似问题，但认知能量会随时间下降；Agent 不会。这正是目标循环（goal loop）的价值——给一个范围极窄的问题，一个清晰的通过/失败信号，让它耗尽所有尝试。

那个 15 年前的 XSLT bug（Bugzilla ID 六位数，Firefox 历史早期）：Brian 让 Claude Code 做"考古"——语义上追溯 bug 是什么时候引入的，而文件在中间已被重命名过多次。"我在旁边看着它运行一些我自己都不知道存在的 git 命令。"

## 验证信号必须绝对清晰，这是大多数团队缺失的肌肉记忆

Mozilla 有 AddressSanitizer 模糊构建——通过/失败是二元的。如果你的系统没有这样的信号，整个管道都会松动。Brian 的判断：让工程师精确定义"成功"和"失败"，正在成为一项必须刻意培养的硬技能，无论是安全、性能、设计质量还是转化率。

## Agent 只做点修复，架构级修复还是需要人

RLBox 那个复杂 bug：Agent 提出的修复是"这里应该断言那个而不是这个"——非常简洁。但工程师看完后说，同样的断言应该在代码库的另外三处同样应用。Agent 的激光聚焦特性在这里成了局限：它解决了你指定的问题，但不会主动扫描同类问题在全局的分布。

## DevEx 投资是 AI 时代的复利

已经有 fuzzing、CI、开发者工具链的团队，直接让 Agent 插进去无需发明新东西。Mozilla 的现有 Bug Bounty 系统、内部 fuzzing 团队、结构化 bug pipeline，这些都是 Agent 能直接复用的轨道。"Developer tooling 的投资对 Agent 和人类都是好的，而且互相增强。"

## 安全攻防：防守方现在有了和攻击方相同的工具

这些 bug 本来就存在，以前只是发现它们很难。但目标不是"让 bug 难以被发现"，目标是"零 bug"。他建议同时用多个不同模型 + Harness 组合扫描，因为不同模型会发现不同的 bug，而攻击者会选对自己最有利的那一种。
