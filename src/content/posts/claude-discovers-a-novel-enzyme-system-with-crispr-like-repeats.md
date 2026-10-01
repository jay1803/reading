---
title: "Claude discovers a novel enzyme system with CRISPR-like repeats"
date: 2026-10-01T00:03:46Z
category: reading
description: "Anthropic 生命科学团队的 Claude agent 在大规模基因组搜索中发现一套此前未被识别的噬菌体酶系统（ART），其功能尚未确定。"
source: "https://www.anthropic.com/news/claude-discovers-novel-enzyme-system"
author: "raahelb"
---

Anthropic 的 Claude 在大规模基因组搜索中发现了一套此前未被完整识别的噬菌体酶系统：它将一种已知的逆转录酶，与邻近的伴随基因和规则排列的 DNA 重复序列联系起来；但这套系统究竟做什么，目前仍未确定。

这一发现来自 Anthropic 于 2026 年春季组建的生命科学研究团队。科学家给 Claude 的高层任务是在海量 DNA 序列中寻找值得研究的逆转录酶（RT）；约 950 个 Claude agent 随后运行了 21 小时，使用约 2.1 亿 token，汇集超过 20 万种 RT，筛出 3,500 个新系统候选，并对最有希望的 20 个撰写分析报告。其中一个 agent 检查某种形态异常的 RT 周边原始 DNA 时，注意到一段此前无人报告的串联重复序列。它接着计算重复次数与间距、对照已知 RT 系统、检索文献，才将其提交给人类科学家审查。文中称，这类筛选通常需要专家花费数周至数月。

团队把这个主要见于噬菌体的系统命名为 **array-associated reverse transcriptases（ART）**。其三个组成部分是 RT、相邻的伴随基因，以及长串等间距 DNA 重复序列。相关 RT 本身已在先前研究中被发现；Claude 的贡献是辨认出与它相连、共同构成系统的重复序列和功能未知的伴随蛋白。重复序列的排列令人联想到 CRISPR，而初步实验显示，ART 的序列阵列也会表达为多种不同的短 RNA。已知少数兼具类似特征的系统能够被编程以切割、复制或粘贴 DNA，因此 ART 值得进一步研究；现有实验尚不能证明它具有这些能力，也没有确定其主要生物学功能。

Anthropic 的工作流程是让 Claude 先阅读文献、用公开数据复现已有结果，再寻找无法归入已知系统的蛋白或基因组邻居；它会为候选提出功能假说和证据，并在后续分析中淘汰大多数候选。通过人类审查的对象才进入实验室，由科学家完成人工表达、结构和生化测试，Claude 协助解释数据。团队表示，其湾区实验室只开展 BSL-1 和 BSL-2 级研究，不处理能感染人类的病原体。ART 的价值目前在于提供了一个经初步实验支持、可供继续验证的新研究对象，也展示了 AI agent 如何把海量序列中的异常转化为具体的生物学假说。
