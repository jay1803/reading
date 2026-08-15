---
title: "Please do not A/B test my workflow"
date: 2026-03-16T01:01:14Z
category: reading
description: "Anthropic 正在对 $200/月的付费 Claude Code 用户进行无声 A/B 测试，用户需要反编译二进制文件才能发现自己被分配到了哪个变体——而该变体直接决定了工具的核心行为。"
source: "https://backnotprop.com/blog/do-not-ab-test-my-workflow/"
---

## TL;DR
Anthropic 正在对 $200/月的付费 Claude Code 用户进行无声 A/B 测试，用户需要反编译二进制文件才能发现自己被分配到了哪个变体——而该变体直接决定了工具的核心行为。

## 核心主张拆解
作者在 Claude Code 二进制中找到了名为 ~tengu_pewter_ledger~ 的 GrowthBook 实验，控制计划模式（plan mode）的输出格式，分四个递进的限制变体：null / trim / cut / cap。被分配到 cap 的用户：计划硬上限 40 行，禁止背景说明，禁止散文段落，模型直接生成计划并呈现"既成事实"，没有问答环节。遥测同步收集计划长度、通过/拒绝结果、变体名称。整个过程无通知、无开关、无法从界面感知。

## 反驳或薄弱处
作者自己承认 Anthropic 的目的应该是优化而非恶意降级——这实际上削弱了文章整体的愤慨语气。文章没有提供不同变体对多数用户的实际效果数据，只是一个人的体验报告。"AI 安全公司却做静默实验"这个对比有情绪力量，但 AI safety 研究和产品 A/B 测试在逻辑上并不直接矛盾。

## 可观测性缺口
$200/月 专业工具的行为只能靠反编译来理解——问题的核心不是透明度态度，而是工具的可观测性设计从一开始就没有把用户纳入进来。
