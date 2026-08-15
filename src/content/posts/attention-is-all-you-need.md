---
title: "Attention Is All You Need"
date: 2023-04-10T13:58:38Z
category: reading
description: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best per..."
source: "https://arxiv.org/abs/1706.03762"
---

## Abstract
The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.
## Explained by ChatGPT
"Attention Is All You Need" 是一篇在 2017 年由 Google 的研究人员发布的论文，这篇论文提出了一个新的深度学习模型，被称为 Transformer。

在这之前的深度学习模型，如循环神经网络（RNN）和长短期记忆（LSTM）网络，通常需要对序列数据（如文本）进行逐个处理，这意味着信息必须按照特定的顺序（比如从头到尾）进行处理，这在处理长序列时会存在问题，因为模型必须"记住"过去的信息，而这在技术上是具有挑战性的。

而 Transformer 模型则通过所谓的 "注意力" 机制，能够在处理序列数据时，让模型同时考虑到序列中的所有部分，而不仅仅是当前处理的部分。这使得 Transformer 模型在处理诸如机器翻译等需要理解整个输入序列的任务时，具有显著的优势。

"Attention Is All You Need" 的标题就是强调这个注意力机制的重要性，即 Transformer 模型的基础。这个模型已经在各种自然语言处理任务中取得了显著的成功，包括在机器翻译，文本生成，和文本理解等任务中。
-----
在深度学习中，"注意力"（Attention）是一种机制，它能够让模型在处理数据时能够集中在数据的某些部分，而非全部数据。这种机制的灵感来源于人类的注意力机制——我们在处理信息时，通常会把注意力集中在某些信息上，而忽略其他信息。

在具体操作上，注意力机制通常被用在处理序列数据，如文本或时间序列数据。对于一个序列，注意力机制能够为序列中的每一个元素分配一个权重，这个权重表示了该元素在当前处理过程中的重要性。然后，这些权重会被用于计算一个加权和，这个加权和就是注意力机制的输出。

以处理文本为例，当我们阅读一段文本时，我们不会平等地对待文本中的每一个词，而是会把注意力集中在某些关键词上。比如在理解句子"我爱我的狗"时，我们可能会把更多的注意力放在"爱"和"狗"上，而较少关注"我"和"我的"。在这个例子中，"爱"和"狗"就会被分配到较高的权重，而"我"和"我的"则会得到较低的权重。

注意力机制的一个关键优点是，它使得模型能够在处理长序列时，忽略那些不重要的信息，从而把计算资源集中在重要信息上。这在处理如机器翻译这样的任务时，特别有用，因为在这样的任务中，输入序列（源语言的文本）和输出序列（目标语言的文本）通常会非常长，而且并不是所有的信息都是 equally important。
-----
注意力权重是由模型自己学习和决定的，而不是由人为设定的。具体来说，注意力权重是通过训练过程中的反向传播和优化来学习的。

注意力机制通常在模型的某个特定层中实现，例如在序列到序列（seq2seq）模型的编码器和解码器之间。在这个层中，会有一个被称为“注意力打分函数”的组件，用于计算注意力权重。这个打分函数会接收输入序列中的每个元素以及当前的状态（例如，在解码器中的当前隐藏状态），并输出一个“打分”。这个打分反映了输入元素在当前状态下的重要性。

打分函数可以有多种形式，例如点积、加性或者是多头注意力等等。不同的打分函数有不同的性质，适用于不同的场景。

一旦得到了每个元素的打分，就可以通过一个softmax函数将这些打分转化为权重。softmax函数可以确保所有的权重都在0和1之间，并且它们的和为1，这样就可以将这些权重理解为一种“概率分布”，反映了每个元素的重要性。

最后，这些权重会被用于计算一个加权和，这个加权和就是注意力层的输出，它将被送入下一层进行进一步的处理。

注意力权重的计算过程是完全可微的，这意味着我们可以通过反向传播算法来更新模型的参数，从而使模型能够学习到更好的注意力权重。
