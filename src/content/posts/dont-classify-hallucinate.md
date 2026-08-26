---
title: "Don't classify. Hallucinate!"
date: 2026-08-26T19:24:54Z
category: reading
description: "面对规模庞大的标签词表，不必让 LLM 在完整词表中做分类，而是让它先自由生成候选标签，再用向量嵌入检索映射回既有的真实标签。"
source: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
---

面对规模庞大且历史遗留内容众多的标签系统，与其让 LLM 在完整词表中做分类，不如让它先自由生成可能适用的标签，再用向量嵌入把这些想象出来的标签映射到现有分类中最接近的真实标签。

Simon Willison 的博客仍有大量旧内容没有添加标签，而现有词表已经包含 1,856 个标签，数量多到很难一次全部塞进提示词，再要求模型逐一判断哪些标签匹配内容。Doug Turnbull 提出的办法绕开了这个上下文瓶颈：完全不向模型提供现有词表，只要求它根据输入内容生成合适的分类；随后计算这些生成分类的 embedding，并在现有标签语料库中进行向量相似度搜索，以最接近的真实标签替换模型生成的候选项。这样，LLM 负责理解语义和提出分类概念，embedding 检索负责把开放式生成约束回既有词表。

为了让模型生成的候选分类更贴近目标体系，可以在提示词中提供若干标签的**结构示例**，无需暴露整个分类集合。Doug 的示例展示了多层级商品分类，例如 "Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables"、"Décor & Pillows / Decorative Pillows & Blankets / Throw Pillows" 以及 "Baby & Kids / Toddler & Kids Bedroom Furniture / Kids Beds"，然后要求模型为查询 "brown coffee table" 创造最合适的新分类。示例由此传达了分类路径的领域、粒度和层级格式，使模型的"幻觉"落在可检索的语义邻域内，再由向量匹配完成与正式标签体系的对齐。**当既有分类词表大到无法直接交给模型时，受示例引导的生成加语义检索，可以把幻觉转化为一种高效的候选标签召回机制。**
