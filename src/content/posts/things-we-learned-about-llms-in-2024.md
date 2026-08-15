---
title: "Things we learned about LLMs in 2024"
date: 2025-01-02T11:08:28Z
category: reading
description: "在我 2023 年 12 月的评论中，我写了关于我们如何还不知道如何构建 GPT-4 ——OpenAI 的最佳模型当时已经发布了将近一年，但没有其他 AI 实验室生产出更好的模型。 OpenAI 知道哪些我们其他人不知道的事情？"
source: "https://simonwillison.net/2024/Dec/31/llms-in-2024/"
---

### The GPT-4 barrier was comprehensively broken
在我 2023 年 12 月的评论中，我写了关于我们如何还不知道如何构建 GPT-4 ——OpenAI 的最佳模型当时已经发布了将近一年，但没有其他 AI 实验室生产出更好的模型。 OpenAI 知道哪些我们其他人不知道的事情？

在过去的十二个月里，情况已经完全改变了。

其中最早的是谷歌二月份发布的 Gemini 1.5 Pro 。除了生成 GPT-4 级别的输出之外，它还向该领域引入了多项全新功能 - 最引人注目的是其 100 万（后来是 200 万）令牌输入上下文长度以及输入视频的能力。
### Some of those GPT-4 models run on my laptop
### “Agents” still haven’t really happened yet
### Evals really matter
### Apple Intelligence is bad, Apple’s MLX library is excellent
### Synthetic training data works great
我见过的对此最好的描述之一来自Phi-4 技术报告，其中包括：
> 合成数据作为预训练的重要组成部分变得越来越普遍，Phi 系列模型一直强调合成数据的重要性。合成数据不是有机数据的廉价替代品，而是比有机数据有几个直接的优势。
>
> 结构化和渐进式学习。在有机数据集中，标记之间的关系通常是复杂且间接的。可能需要许多推理步骤才能将当前标记连接到下一个标记，这使得模型很难从下一个标记预测中有效学习。相比之下，语言模型生成的每个标记根据定义都是由前面的标记预测的，从而使模型更容易遵循生成的推理模式。
