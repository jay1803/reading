---
title: "Talkie: a 13B vintage language model from 1930"
date: 2026-04-29T08:02:23Z
category: reading
description: "Talkie 的核心价值不在“复活一个 1930 年的人”，而在于把语言模型的训练时间切开：用严格历史语料制造一个天然低污染、可控知识边界的实验对象，从而测试模型到底是在记住现代网络，还是具备跨时代泛化、预测与发明能力。"
source: "https://talkie-lm.com/introducing-talkie"
---

## TL;DR
Talkie 的核心价值不在“复活一个 1930 年的人”，而在于把语言模型的训练时间切开：用严格历史语料制造一个天然低污染、可控知识边界的实验对象，从而测试模型到底是在记住现代网络，还是具备跨时代泛化、预测与发明能力。

## 核心主张拆解
Talkie-1930-13B 是一个只用 1931 年前英文文本训练的 13B “vintage language model”，训练语料约 260B tokens，来自书籍、报纸、期刊、科学论文、专利、判例等历史文献。作者还发布了 base checkpoint 与不依赖现代聊天/指令数据的 post-trained checkpoint，并用 Claude Sonnet 4.6 进行 24/7 live prompting 展示。

这个项目的研究意义有三层：第一，知识 cutoff 清晰，适合测试模型对未来事件的“惊讶度”和远期预测退化；第二，天然避开现代 benchmark contamination，能更干净地观察模型能否从上下文学习 Python、逆函数、现代任务格式；第三，训练数据不来自现代 web，因此可以研究 web 数据对现代模型人格、倾向、能力边界的塑形程度。

## 关键实验与数据
作者用近 5,000 条《纽约时报》“On This Day”历史事件描述，测量 pre-1931 模型对不同年代事件的 surprisingness。结果显示 cutoff 后惊讶度上升，1950s/1960s 尤其明显，之后进入平台期；这为研究模型规模如何改善 forecasting、以及预测能力如何随时间跨度衰减提供了实验框架。

在 HumanEval 风格测试中，vintage models 在没有代码预训练的情况下，通过上下文中的 Python 示例尝试生成新函数。结果远弱于现代 web-trained twin，但随规模提升缓慢改善；正确答案多是简单一行程序或对示例的小改动，例如看到 rotation cipher 的 encode 函数后把加法改成减法实现 decode，这至少显示了某种逆函数理解。

作者还训练了一个架构相同、FLOPs 相同、但基于 FineWeb 的 modern twin。Talkie 在知识类评测上明显落后；过滤掉从 1930 年视角看属于 anachronistic 的问题后，差距约缩小一半；在核心语言理解和数值能力上则更接近现代 twin。

## 技术瓶颈
最大问题是 temporal leakage。即使用了文档级 n-gram anachronism classifier，早期 7B 模型仍知道 Roosevelt presidency 和 New Deal，13B 版本也知道部分二战、联合国、德国分裂等 cutoff 后信息；这说明“历史模型”的实验纯度取决于极难的日期元数据、后世脚注、现代编辑材料过滤。

第二个瓶颈是 OCR。1930 年前文本多数来自纸质扫描，传统 OCR 在历史版式和低质量扫描上错误很多；作者的控制实验显示，使用传统 OCR 文本训练时，同等 compute 只有人工转录文本约 30% 的学习效率，regex 清洗可恢复到约 70%，但仍有巨大损失。现代 VLM OCR 虽更准，却可能 hallucinate 现代事实，反而污染 cutoff。

第三个瓶颈是 vintage post-training。直接用现代 instruction-response 会注入现代知识和助手风格，所以作者从历史结构化文本中生成指令数据，如礼仪手册、写信手册、菜谱、词典、百科、诗歌寓言；再用 synthetic prompts 和 Claude Sonnet 4.6 作为 judge 做 online DPO，使 held-out instruction-following rating 从 2.0 提升到 3.4；最后用 Claude Opus 4.6 与 talkie 的 rejection-sampled multi-turn chats 平滑对话能力。但作者也承认，AI feedback 本身不可避免地带来现代塑形，早期 7B 甚至被 RL 训练出 listicle 口吻。

## 值得质疑
Talkie 并不是一个真正来自 1930 年的认知体，而是现代 transformer 架构、现代训练流程、现代评测体系与现代 RLHF/DPO 机制包裹下的历史语料实验。它能隔离一部分 web-era contamination，却不能隔离现代研究者的任务设计、Claude judge、英文公共领域语料偏差，以及 cutoff filtering 的残留污染。

项目当前主要基于英文历史文本，因为团队需要熟悉源文档来验证数据管线；这让“1930 年世界”的覆盖更像英语公共领域文献中的世界，而不是全球历史经验。作者计划扩展到多语言，并把语料扩大到 1T+ tokens，目标是训练 GPT-3 级模型并接近原始 ChatGPT 能力规模。

## 最后一层
Vintage LM 最有价值的地方，是把“模型能力来自语言本身、来自世界知识、来自现代 web、还是来自 benchmark 记忆”这些纠缠变量拆开。Talkie 目前还粗糙，但它提供了一个少见的实验旋钮：改变模型的时代，而不只是改变模型的大小。
