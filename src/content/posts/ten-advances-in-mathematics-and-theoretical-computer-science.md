---
title: "Ten advances in mathematics and theoretical computer science"
date: 2026-08-20T23:34:26Z
category: reading
description: "OpenAI 用不足 $2,000 每道题解开十个悬置十年的数学难题，成本曲线已断裂，数学界正经历 AI 版 Deep Blue 时刻。"
source: "https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything"
---

## AI 数学研究成本曲线已断裂：OpenAI 用不足 $2,000 每道题解开十个悬置十年的数学难题

OpenAI 宣布，其内部版 Astra 模型对十道"至少十年没有实质进展"的数学问题给出了完整解答，每道题花费低于 $2,000（以 GPT-5.6 Sol 价格计）。对比背景：Anthropic 几天前让 Claude Mythos Preview 做密码学研究，单次实验花掉了 $100,000。成本差距不是噪音，是能力曲线性质改变的信号。

### 可验证性

openai/ten-proofs 仓库包含完整的 Lean 4 形式化证明，可独立核查。配套论文描述解题路径；另有一份 LLM 生成的"推理复盘"PDF，模型根据未公开的推理轨迹"重建证明如何形成"。两个空白仍然存在：提示词未公开，以及没有数据说明有多少题花掉 $2,000 后仍然失败。

### 数学界的 Deep Blue 时刻与 Tao 的"大数学"

Willison 把社区反应类比于 1997 年 Deep Blue 击败卡斯帕罗夫的集体冲击。Terence Tao 在 IEEE Spectrum 上将这一趋势定义为"大数学"：人类主导创造性部分，AI 承担技术性苦力；复杂数学任务将被分解，进行大规模去中心化的人机协作。
