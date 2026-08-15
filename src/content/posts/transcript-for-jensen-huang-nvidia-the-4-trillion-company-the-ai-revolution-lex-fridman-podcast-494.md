---
title: "Transcript for Jensen Huang: NVIDIA – The $4 Trillion Company & the AI Revolution | Lex Fridman Podcast #494"
date: 2026-03-24T08:01:59Z
category: reading
description: "Jensen Huang，NVIDIA CEO 兼联合创始人，1993 年创立公司至今。[补充：NVIDIA 目前市值约 4 万亿美元，是全球最高估值的半导体公司，也是 AI 基础设施的核心供应商。] Lex Fridman 为主持人，麻省理工研究员，主理 Lex Fridman Podcast。"
source: "https://lexfridman.com/jensen-huang-transcript/?utm_source=rss&utm_medium=rss&utm_campaign=jensen-huang-transcript"
---

## 嘉宾背景
Jensen Huang，NVIDIA CEO 兼联合创始人，1993 年创立公司至今。[补充：NVIDIA 目前市值约 4 万亿美元，是全球最高估值的半导体公司，也是 AI 基础设施的核心供应商。] Lex Fridman 为主持人，麻省理工研究员，主理 Lex Fridman Podcast。

## TL;DR
Jensen 用同一套底层逻辑运营公司和设计芯片：不是在正确时机宣布正确决策，而是用数年时间持续在所有人的信念体系里埋下铺垫砖，直到宣布当天所有人的反应是"你怎么这么慢才说"——这套机制让 NVIDIA 能以其他公司无法维持的速度，同时完成工程和认知上的飞跃。

## CUDA 放到 GeForce：把公司全部利润赌在装机基础上
CUDA 上 GeForce 是 NVIDIA 历史上最接近自杀的决策——它把 GPU 成本提高了 50%，而公司当时毛利率只有 35%，最终市值从约 80 亿美元跌至 15 亿美元。Jensen 的逻辑只有一条：架构的存活不取决于优雅，取决于装机基础。x86 比 RISC 架构丑陋得多，但活下来了。开发者只在意有多少机器跑这套平台，所以把 CUDA 塞进每一台消费级 GeForce，才是培育开发者生态的唯一路径——哪怕没有一个游戏玩家为此多付一分钱。

## Amdahl's Law 决定了极端协同设计无法回避
NVIDIA 的 "extreme co-design"（从 GPU、CPU、内存到网络、散热、电力、机架整体协同设计）不是产品策略，是物理约束的必然结果。当你把问题分布到一万台计算机，Amdahl's Law 会让任何单点的局部加速都在整体层面快速失效——网络、存储、电力任一环节成为瓶颈，计算扩容就白费。Jensen 的解法是 60+ 直接汇报、没有一对一会议，每个问题开放给所有领域专家同时攻击——组织架构直接镜像了他们要解决的物理问题。

## 四条 Scaling Law 最终收敛到"算力即智能"
Jensen 列出四个相互叠加的扩展定律：预训练（数据驱动）→ 后训练（合成数据，已从数据瓶颈转为算力瓶颈）→ 测试时推理（"推理是思考，思考比阅读难"，算力极其密集）→ 智能体扩展（生成子智能体，相当于乘法式地复制 AI）。这四条形成闭环：智能体产生的数据和经验倒流回预训练，再循环放大。结论只有一个：智能的上限是算力，没有其他瓶颈。

## 计算从仓库变成工厂：NVIDIA 的增长逻辑
旧计算 = 人工预录制内容 + 文件检索，本质是仓库，不直接产生收入。新计算 = 实时生成上下文相关的 token，本质是工厂，token 直接对应业务产出。工厂比仓库赚钱得多，而且 token 正在 iPhone 化分层定价（免费、付费、专业版），Jensen 认为"每百万 token 收 1000 美元"已在眼前。据此他推论：世界 GDP 增速将加快，GDP 中用于计算的比例将是过去 100 倍，NVIDIA 的天花板"只是一个数字"。

## 信念前置，宣布滞后：领导力即信念系统工程
Jensen 从不突然宣布转向——没有年终宣言、没有大规模裁员重组、没有新 logo。他的做法是把每一个新洞察即时告知周围所有人，用外部里程碑、工程突破、客户进展持续塑造团队、董事会、合作伙伴的认知，直到他宣布"我们全力押注深度学习"时，所有人的反应是"早就该了"。GTC 是同一机制对外的版本——他用十年 GTC 演讲为 GPU 计算、AI 工厂、智能体系统铺垫，NemoClaw、NVIDIA GPU in space、Vera Rubin 架构宣布时都无人惊讶。

## 留下的那个想法
Jensen 在对话末尾说"我认为 AGI 已经实现"——他的定义是，一个 Claude 或 Agent 能构建一个病毒式传播的 10 亿美元 Web 服务。这个判断很可能被大多数人低估，因为他说的不是未来某天，而是现在已经发生，而且他补充说"就像我当年预测不到那些互联网公司一样，我也说不出它具体是什么"。
