---
title: "An Interview with Nvidia CEO Jensen Huang About Accelerated Computing"
date: 2026-03-18T08:02:09Z
category: reading
author: "Ben Thompson"
description: "Jensen Huang，Nvidia 联合创始人兼 CEO，GTC 2026 主题演讲刚结束即接受采访，是 Ben Thompson（Stratechery 创始人）与他的第五次对话。"
source: "https://stratechery.com/2026/an-interview-with-nvidia-ceo-jensen-huang-about-accelerated-computing/"
---

## 嘉宾背景
Jensen Huang，Nvidia 联合创始人兼 CEO，GTC 2026 主题演讲刚结束即接受采访，是 Ben Thompson（Stratechery 创始人）与他的第五次对话。

## TL;DR
Nvidia 真正卖的不是 GPU，而是一套统一理论：在任何应用上，将最快的加速硬件与最深的软件栈垂直整合——Vera CPU、Groq LPU 收购、五层蛋糕论，都是这套理论的展开，而不是方向漂移。

## 代码能"运行或不运行"让 AI 第一次真正值钱
过去一年 AI 跨越的关键门槛不是模型更聪明，而是出现了可验证的执行环境：代码要么编译、要么不编译。这个反馈回路让推理有了锚点，agent 得以无需人工干预地迭代——Nvidia 内部工程师已大量停止手写代码，只做架构和规格。Jensen 认为这才是 AI 从"有用"跨越到"值钱"的真正机制。

## Groq 收购：买的是极致低延迟端，不是云
高吞吐（服务所有用户）与高速率/低延迟（给 coding agent 喂最快 token）之间存在根本性的 Pareto 张力，Nvidia GPU 无法同时在两端做到极致。Groq LPU 覆盖的正是"极高 token 率+极低延迟"端；Nvidia 只收购了团队和技术授权，不要 Groq 的云服务；整合后甚至把 decode 阶段的 attention 计算也拆出来放到 Groq 上——这要求软件栈深度解耦。

## Vera CPU 是 GPU 在等 tool call 时的答案
传统超大规模云的 CPU 优化目标是"可出租核心数"，性能次之。但 agent 工具调用的瓶颈完全不同：GPU 在等待一个 tool call 返回时，任何 CPU 的迟缓都意味着巨额 GPU 闲置。Vera 的带宽/核心是现有任意 CPU 的三倍，专为"不拖慢 GPU"而设计——它是 agentic 时代的 CPU，不是一个更快的云 CPU。

## 五层蛋糕：美国不能把 AI 做成捆绑博弈
Jensen 最担心的政策失误是把 power、chips、infrastructure、models、applications 五层当作一个整体去博弈——那样总成绩受限于最弱那层。同样逻辑下，他力挺在中国市场保留美国技术栈：DeepSeek、Kimi、Qwen 产出的开源创新最终会向外扩散，若底层跑的是美国栈，美国生态是受益者；若底层是华为栈，则反之。H20 禁令期间 Huawei 创下公司历史新高，多家 AI 芯片公司成功 IPO，是这个判断的现实注脚。

## Doomerism 正在制造上一次工业革命里欧洲的处境
Jensen 明确点名 doomerism 在华盛顿的影响深度出乎他意料。他的历史类比：欧洲发明了上次工业革命的核心技术，但美国更快吸收、扩散并商业化——最终被甩在身后的是欧洲。他担心美国正在用科幻叙事吓到自己，而 AI 好感度在民调中的持续下滑是这个趋势的早期信号。

## 留下的那个想法
Ben 问 Groq 是否是 Nvidia 历史上第一次让 Jensen 觉得"这个 ASIC 真的不同"的时刻，他的回答是："不，是 Mellanox。"Mellanox 后来成了 NVLink 大规模化的基石，Groq 进入 Nvidia 栈的轨迹可能与此高度相似——不只是推理加速器，而是未来某个核心基础设施层的起点。
