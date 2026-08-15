---
title: "GPT-4 Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE"
date: 2023-07-28T15:02:12Z
category: reading
description: "First off, with the problem statement. From GPT-3 to 4, OpenAI wanted to scale 100x, but the problematic lion in the room is cost. [Dense transformers models..."
source: "https://www.semianalysis.com/p/gpt-4-architecture-infrastructure"
---

First off, with the problem statement. From GPT-3 to 4, OpenAI wanted to scale 100x, but the problematic lion in the room is cost. [Dense transformers models will not scale further](https://www.semianalysis.com/p/the-ai-brick-wall-a-practical-limit). A dense transformer is the model architecture that OpenAI GPT-3, Google PaLM, Meta LLAMA, TII Falcon, MosaicML MPT, etc use. We can easily name 50 companies training LLMs using this same architecture. It’s a good one, but it’s flawed for scaling.

首先，让我们来看看问题陈述。从GPT-3到4，OpenAI希望扩大100倍，但问题是成本。密集的Transformer模型将无法进一步扩展。密集的Transformer是OpenAI GPT-3、Google PaLM、Meta LLAMA、TII Falcon、MosaicML MPT等模型使用的模型架构。我们可以轻松地列举出使用这种相同架构训练LLM的50多家公司。这是一个不错的架构，但对于扩展来说有缺陷。

[See our discussion training cost from before the GPT-4 announcement on the upcoming AI brick wall for dense models from a training cost standpoint.](https://www.semianalysis.com/p/the-ai-brick-wall-a-practical-limit) There we revealed what OpenAI is doing at a high-level for GPT-4’s architecture as well as training cost for a variety of existing models.

Over the next few years, multiple companies such as Google, Meta, and OpenAI/Microsoft will train models on supercomputers worth over one hundred billion dollars. Meta is burning over $16 billion a year on the “Metaverse”, Google waste’s $10 billions a year on a variety of projects that will never come to fruition. Amazon has lost over $50+ billion on Alexa. Cryptocurrencies wasted over $100 billion on nothing of value.

The costs of inference exceed that of training by multiple folds. This is what OpenAI’s innovation targets regarding model architecture and infrastructure.

In the datacenter, in the cloud, utilization rates are everything.
Humans on average read at ~250 words per minute but some reach as high as ~1,000 words per minute. This means you need to output at least 8.33 tokens per second, but more like 33.33 tokens per second to cover all corner cases.

A trillion-parameter dense model mathematically cannot achieve this throughput on even the newest Nvidia H100 GPU servers due to memory bandwidth requirements.

OpenAI is achieving human reading speed, with A100s, with a model larger than 1 trillion parameters, and they are offering it broadly at a low price of only $0.06 per 1,000 tokens. That’s because it is sparse, IE not every parameter is used.
### #1 GPT-4模型架构
GPT-4的规模是GPT-3的10倍以上。据我们了解，它具有大约1.8兆参数，分布在120个层，而GPT-3具有大约1750亿参数。

OpenAI通过使用混合专家（MoE）模型，成功地控制了成本。
OpenAI在其模型中使用了16个专家，每个专家的MLP参数约为1110亿。其中有2个专家路由到每个前向传递。
此外，注意力机制共享大约550亿参数。
### #2 数据集成
OpenAI在大约13兆令牌上对GPT-4进行了训练。考虑到RefinedWeb的CommonCrawl包含大约5兆高质量令牌，这是有道理的。供参考，Deepmind的Chinchilla模型和Google的PaLM模型分别使用了大约1.4兆令牌和0.78兆令牌进行训练。甚至据称PaLM 2是在大约5兆令牌上进行训练的。
### #3 并行策略
### #4 训练成本
OpenAI在GPT-4的训练中，使用了大约25,000个A100芯片，在90至100天的时间内进行了约32%至36%的MFU（平均功能利用率）。这种极低的利用率部分是由于大量的故障导致需要从检查点重新启动的原因，上述提到的气泡代价非常高。

如果他们在云中的成本约为每小时1美元的A100芯片，仅这次训练的成本就约为6300万美元。这还没有考虑到所有的实验、失败的训练运行和其他成本，比如数据收集、强化学习和人员成本等。

目前，使用约8,192个H100芯片，以每小时2美元的价格，在约55天内可以完成预训练，成本约为2150万美元。
### #5 MoE 的权衡
### #6 推理的权衡
### #8 GPT-4的推理成本
与175B参数的Davinchi模型相比，GPT-4的成本是其3倍，尽管其前馈参数只增加了1.6倍。这主要是因为GPT-4需要更大的集群并实现了更低的利用率。
### #12 关于视觉多模态
视觉多模态能力是GPT-4中最不令人印象深刻的部分，至少与领先的研究相比。
它是一个独立的视觉编码器，与文本编码器分开，但存在交叉注意力。我们听说它的架构类似于Flamingo。

对于视觉模型，OpenAI原本希望从头开始训练，但这种方法还不够成熟，因此他们决定先从文本开始以减轻风险。
据称，下一个模型GPT-5将从头开始进行视觉训练，并且能够自己生成图像。此外，它还将能够处理音频。
