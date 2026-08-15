---
title: "How Did DeepSeek Build Its A.I. With Less Money?"
date: 2025-03-19T10:19:30Z
category: reading
description: "DeepSeek 这家中国初创公司通过使用包括“混合专家”（mixture of experts）在内的多种技术技巧，显著降低了构建 AI 系统的成本。他们只用了大约 600 万美元的原始计算能力，大约是 Meta 构建其最新 AI 技术所花费的十分之一。"
source: "https://cn.nytimes.com/technology/20250213/deepseek-ai-chip-costs/"
---

## TL;DR
DeepSeek 这家中国初创公司通过使用包括“混合专家”（mixture of experts）在内的多种技术技巧，显著降低了构建 AI 系统的成本。他们只用了大约 600 万美元的原始计算能力，大约是 Meta 构建其最新 AI 技术所花费的十分之一。
### 主题
#### How are A.I. technologies built?
AI 技术基于神经网络（neural networks），这是一种通过分析大量数据来学习技能的数学系统。最强大的系统会花费数月时间分析互联网上的大量文本、图像、声音和其他多媒体，这需要巨大的计算能力。大约 15 年前，AI 研究人员发现，被称为图形处理单元（GPUs）的专用计算机芯片是进行此类数据分析的有效方法。像 Nvidia 这样的公司最初设计这些芯片是为了渲染电脑视频游戏的图形，但 GPU 也擅长运行驱动神经网络的数学运算。
#### How was DeepSeek able to reduce costs?
DeepSeek 采用“混合专家”方法，将系统分成许多较小的神经网络，每个专家专注于特定领域，例如诗歌、计算机编程、生物学、物理学等。DeepSeek 的诀窍在于将这些较小的“专家”系统与一个“通才”系统配对。专家之间仍然需要交换一些信息，而对每个主题都有一定了解的通才，可以帮助协调专家之间的互动。
#### And that is more efficient?
DeepSeek 还掌握了一个涉及小数的简单技巧。
#### There is math involved in this?
DeepSeek 在训练其 AI 技术时也做了类似的事情。神经网络识别文本模式所涉及的数学运算实际上只是乘法。通常，芯片会乘以适合 16 位内存的数字。但 DeepSeek 将每个数字压缩到只有 8 位内存，即一半的空间。本质上，它从每个数字中截去了几个小数。这意味着每个计算的准确性较低，但这并不重要，因为计算结果足够准确，可以产生一个非常强大的神经网络。
#### That’s it?
DeepSeek 在将这些数字相乘时采取了不同的路线。在确定每个乘法问题的答案时，它将答案扩展到 32 位内存。换句话说，它保留了更多的小数位，使得答案更精确。
#### So any high school student could have done this?
DeepSeek 工程师在他们的论文中表明，他们非常擅长编写告诉 GPU 做什么的复杂计算机代码。很少有人具备这种技能，但大型 AI 实验室拥有能够与 DeepSeek 相媲美的工程师。
#### Then why didn’t they do this already?
有些 AI 实验室可能已经在使用了至少部分相同的技巧。像 OpenAI 这样的公司并不总是透露他们内部的运作。尝试这种需要花费数百万美元，需要承担巨大的风险。许多专家指出，DeepSeek 的 600 万美元仅涵盖了启动时训练系统最终版本的费用。在他们的论文中，DeepSeek 工程师表示，他们在最终训练运行之前还花费了额外的资金用于研究和实验。但任何尖端的 AI 项目都是如此。

### 总结
DeepSeek 通过采用“混合专家”模型，结合减少参与计算的数字精度和优化 GPU 代码等多种技术创新，显著降低了构建大型 AI 模型的成本。
