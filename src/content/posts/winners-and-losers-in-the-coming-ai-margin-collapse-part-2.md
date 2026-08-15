---
title: "Winners and losers in the coming AI margin collapse (part 2)"
date: 2026-07-14T08:02:35Z
category: reading
description: "好够用的廉价模型（GLM5.2、Grok 4.5 以 $6/MTok 输出定价）正在压垮纯推理毛利。Bezos 那句\"你的利润是我的机会\"在此精准成立——但吃掉这段利润的，不是同层竞争者，而是硬件层与用户层。"
source: "https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-2-winners-and-losers/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## 价值正在模型层两侧积累，而非模型层本身

好够用的廉价模型（GLM5.2、Grok 4.5 以 $6/MTok 输出定价）正在压垮纯推理毛利。Bezos 那句"你的利润是我的机会"在此精准成立——但吃掉这段利润的，不是同层竞争者，而是硬件层与用户层。

## 赢家：GPU 供应链 + 终端用户

半导体、内存、数据中心、电力冷却的供给仍严重不足。廉价模型让需求上升，但价值向硬件层沉淀——这与历史上软件主导利润分配的规律相反（苹果例外）。

终端用户是最大赢家：GPT4 时代的推理质量，如今以 5-10% 的价格可得。

Cursor 类编程 Agent 翻身：此前以接近零售 API 价格批发前沿推理，重度用户亏本。廉价"够用"模型一夜间让毛利转正。更重要的是其积累的真实 agentic 使用数据——哪些 prompt 有效、哪些编辑被开发者接受——恰恰是训练下一代模型所需的信号。xAI 收购 Cursor，买的不是 IDE，而是这个数据飞轮。

## 前沿实验室的两条逃生出路

Anthropic 约 80% 收入来自 API，理论上最暴露于模型切换风险。但前沿实验室有两条出路：

1. 将最强模型锁进托管 Agent 平台（无 API、无直接调用），让用户无法随意换模型，同时大幅降低蒸馏风险；
2. 持续拉开智能差距，让人们为高质量甘愿付溢价。

两者作者认为会并行尝试。最终取决于前沿智能领先是否能止住收窄趋势——目前看来并没有。

## 两个外卡

"够用"窗口可能是短暂的：下一轮前沿跃迁（速度、上下文、持续训练等）可能让当前格局再次失效，正如 Chat UI 到编程 Agent 那次切换。

B2C 广告变现几乎未被触动：ChatGPT 逾 10 亿 MAU，OpenAI 已试水，Anthropic 明确不做，Google 也迟缓。若某家破局，市场重心将重回 B2C。
