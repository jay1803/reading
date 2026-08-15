---
title: "Waste Tokens, Save Time"
date: 2026-05-28T08:01:44Z
category: reading
description: "这是一场 Naval Podcast 对话。主持人 Nivi 和 Naval 与三位创始人讨论 AI agent 正在如何改变工程、公司组织和创业护城河："
source: "https://nav.al/tokens"
---

## 嘉宾背景
这是一场 Naval Podcast 对话。主持人 Nivi 和 Naval 与三位创始人讨论 AI agent 正在如何改变工程、公司组织和创业护城河：

- Guillermo Rauch：Vercel 创始人，正在把 Vercel 做成面向 agent 和后续形态的 AI cloud。
- Blake Scholl：Boom Supersonic 创始人，做超音速飞机、工厂和自研喷气发动机。
- Max Hodak：Science 创始人，做把活体神经元长在硅上的 biohybrid brain interface，用于恢复视觉等感官功能，并探索新的脑区与感官。

三人的共同点不是“都在用 AI 写代码”，而是都在构建某种自己的工厂：软件工厂、硬件工厂、神经接口工厂。对话真正关心的是这些工厂背后的新知识和 alpha。

## TL;DR
这场对话最重要的线不是“AI 会让工程师提效”，而是：当模型把写代码这件事商品化以后，稀缺性从“亲手实现”迁移到“判断、架构、选择 building blocks、定义 factory”。所以 token 花费不是核心成本，人的时间、品味和系统组织能力才是核心成本；真正的 100x 不再只是写出更多代码，而是能生产出会继续生产输出的工厂。

## Token 消耗不是 ROI，时间和最终产物才是 ROI
Guillermo 提到很多人仍在看 token leaderboard，好像 token 数量能衡量 AI 工程效率。Blake 直接把这类指标类比成过去按 lines of code 衡量工程产出：它们可见、可计数，但不直接等于价值。

Naval 的立场更激进：不要太盯 token，应该“waste tokens, save time”。即使模型生成了低质量代码，只要最后要上线时再投入更多 token 让它审查、重写、修复，整体仍然比人力便宜。这里的前提不是 token 没有成本，而是在人类时间面前，模型推理成本仍是低价杠杆。

非直觉点在于：AI 使用中的“浪费”可能是理性策略。传统工程文化把计算资源、代码整洁、一次写对看得很重；但在 agent 工作流里，更重要的是把人从卡点中解放出来，让问题持续向可验证结果推进。

## 新的 100x 工程师不是高产代码作者，而是软件工厂设计者
Guillermo 把变化概括为“software factories”：过去评价工程师是看他能不能直接 ship output B；现在更关键的是他能否生产一个 factory，让它持续产出 B through Z。这让 10x 工程师争论变成过时问题，因为 AI leverage 让 100x、1000x 工程师重新变得可见。

Naval 补充说，在 idea domain 和 digital domain，本来就存在巨大的能力差距：Satoshi、Notch、Brendan Eich、John Carmack 这类人不是线性更强，而是选择方向、判断问题、构造系统的能力产生了数量级差异。选对问题与选错问题之间甚至是“infinity difference”。

这意味着 AI 没有消灭能力差距，反而可能放大能力差距。会用 agent 的工程师不只是更快写代码，而是更快建立可复用的生产系统；不会判断的人则可能只是更快地产生噪音。

这里的“软件工厂”可以更精确地理解为 Software Factory：由 agents、spec、上下文、工具、eval、review loop 和人类判断共同组成的可验证生产系统。

## 模型越像 principal engineer，人的 taste 越成为接口
Max Hodak 观察到，Claude 或 ChatGPT 在某个领域里大致会“像你一样好”：资深开发者会把它用得很强，初级开发者得到的也更像初级输出。关键不只是初始 prompt，而是过程中那些零散反馈和 reprompt，它们决定了模型走向。

Guillermo 说自己现在给同事的新型支持，是告诉他们应该怎样重新 prompt 模型；而模型近期也开始主动给出路线、trade-off 和架构建议，像 principal engineer 一样回到你面前讨论方案。比如当你让它把高基数 telemetry 数据塞进 Postgres，它会反过来建议 ClickHouse 或 Athena。

但这里仍有一个未解决问题：资深架构师是不是能从模型获得 10x，而 junior 只能获得 2x？对话没有给定答案，却指出了差异来源：技术选型、架构边界、性能预期、系统 taste。模型可以给矩阵，但人仍要知道什么时候说“不，我要另一个东西”。

## Agent 不会从零重造宇宙，building blocks 会变得更值钱
Naval 提出一个尖锐问题：纯软件是否正在死亡？如果模型已经会说英文，也会写代码，那么“经典软件工程”还是否可投资、可组织、可形成护城河？

Guillermo 的反驳是 building block economy。Agent 不应该每次为了发邮件就重造 queue infrastructure，而应该按任务选择合适的模块，比如 BullMQ、Postgres、ClickHouse 等。复用现有 building blocks 不只是省 token，也是为了和社会已有系统协作：大家都依赖 Postgres 13.2 这种共识，本身就有大规模合作价值。

他把既有软件比作“token cache”：文明已经花过巨量 token、时间和协调成本创造出来的东西，模型不应该每次重新生成。未来有价值的基础设施软件，可能正是 agent 会反复调用、组合和 fork 的高质量积木。

## 写代码手艺在下沉，系统理解在上浮
Max Hodak 说自己小时候学编程，年轻时会连续写二十小时代码，但现在已经很久没手写代码；从去年十二月以来，他建了大量自己每天使用的软件，却几乎不是亲手写出来的，而且很难想象回到手写代码。

Guillermo 认为这并不矛盾：真正有用的是理解 API、数据流、输入输出、性能预期，以及如何把模型 orient 到你期望的操作水平。过去优秀工程 leader 已经在通过 Slack、1:1 和团队管理“vibe coding through people”，本质是传递意图、经验和约束；现在只是把对象换成 agents。

Naval 的经历则从另一个方向印证：他二十年没写代码，现在通过 agents 又开始大量构建软件。基础的软件工程原则和算法理解足够让他重新获得创造力，因为 agent 消除了过去最痛苦的环节：追语言、追框架、拼基础设施、卡在窄小 debug 问题里。

## 编程教育里“卡住是必经之路”的信念正在失效
Max Hodak 最后指出，过去学习编程的内在挫折感来自随机卡点：大部分事情顺利推进，但一个很窄的问题可能让人无限期 debug。以前大家会说这就是学习过程的一部分。

现在 agent 改变的是“不再那么容易卡死”。它们能相对快速地找到正确做法，让构建过程持续往前流动。这不只是效率提升，也是心理结构变化：学习者不必把痛苦误认为深度，把卡住误认为成长。

边缘感最强的想法是：AI agent 不是把软件工程变简单，而是把软件工程从“亲手穿越摩擦”改写成“设计可验证的意图传递系统”。未来最稀缺的人，可能不是最能忍受 debug 痛苦的人，而是最会把判断转化成 agent 可执行工厂的人。
