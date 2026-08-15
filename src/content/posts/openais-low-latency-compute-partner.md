---
title: "openai’s low-latency compute partner"
date: 2026-04-30T08:02:48Z
category: reading
description: "Cerebras 的新故事不是“另一个 Nvidia 挑战者”，而是用低延迟推理切走 GPU 架构最不擅长的一小块高价值需求：OpenAI、编码 Agent、多 Agent 工作流需要 1,000+ tokens/s 级别的近实时反馈，Sacra 认为这足以支撑 Cerebras 从硬件公司转成垂直整合的推理云公..."
source: "https://newsletters.feedbinusercontent.com/05e/05ec1f979a42937d9cfba49171770bc421651bd2.html"
---

## TL;DR
Cerebras 的新故事不是“另一个 Nvidia 挑战者”，而是用低延迟推理切走 GPU 架构最不擅长的一小块高价值需求：OpenAI、编码 Agent、多 Agent 工作流需要 1,000+ tokens/s 级别的近实时反馈，Sacra 认为这足以支撑 Cerebras 从硬件公司转成垂直整合的推理云公司。关键赌注是：低延迟推理会从小众性能指标变成 AI 产品体验和开发效率的核心瓶颈。

## 核心主张拆解
Cerebras 的差异化来自延迟，而不是泛化算力。文章把 OpenAI 合作放在中心：OpenAI 寻找比 Nvidia 更低延迟的推理基础设施，Cerebras 因此能承接 Nvidia GPU 架构触顶的 latency-sensitive workloads。

收入结构正在从一次性硬件销售转向云化推理。Cerebras Cloud 2025 年收入翻倍至 1.52 亿美元，推理占收入比例从 2023 年的 0% 升至 30%，说明增长来源不再只是国家实验室、药企和能源客户的硬件采购。

编码 Agent 是这轮需求的具体入口。文章提到 Claude Code、OpenAI Codex 等工作流推动快速迭代和子 Agent 探索代码库；Cerebras 支持的 GPT-5.3-Codex-Spark 可达到 1,000+ tokens/s，约为 GPT-5.5 的 13 倍。

## 关键数据
- 2025 年收入：5.10 亿美元，同比增长 76%，2024 年为 2.90 亿美元。
- Cerebras Cloud：2025 年 1.52 亿美元，同比增长一倍；推理收入占比约 30%。
- 估值：2026 年 2 月 Tiger Global 领投 10 亿美元 Series H 后估值 230 亿美元，约 45x 2025 收入。
- IPO 目标：据称希望以 350 亿美元上市，约 69x 2025 收入。
- 对标交易：Groq 被 Nvidia 以技术授权/团队收购方式拿下，隐含约 200 亿美元估值；Sacra 估计 Groq 2025 年收入约 5 亿美元，对应约 40x。
- 客户集中：Cerebras 曾因 G42 收入集中和监管审查在 2025 年 10 月撤回 IPO；2026 年 4 月重新申报后，仍有 MBZUAI 占 2025 年收入 78% 的集中度问题，但新增 OpenAI 与 AWS 叙事改善了投资人故事。

## 为什么重要
如果推理超过训练成为主要算力支出，Cerebras 的市场空间会从“替代部分训练芯片”变成“占据实时 AI 体验层”。这与 Nvidia 的优势区间不同：Nvidia 通过 CoreWeave、Crusoe 等 GPU 云覆盖广泛算力需求，而 Cerebras 选择垂直整合，只押低延迟、高交互、Agent 化推理。

Groq 被 Nvidia 吸收后，Cerebras 成为更稀缺的独立 AI 芯片纯玩家。稀缺性会推高资本市场定价，但也会放大执行风险：它必须证明低延迟需求足够大、客户足够多、云服务毛利足够好。

## 值得质疑
69x 收入的 IPO 目标非常激进。这个倍数隐含市场相信低延迟推理会快速扩张，并且 Cerebras 能把 OpenAI/AWS 级别合作转化成稳定、可续约、高毛利收入。

客户集中并没有真正消失。G42 问题被“新客户故事”稀释，但 MBZUAI 仍占 78% 收入，说明商业化广度还没完全证明。

文章数据来自 Sacra 模型与 newsletter 摘要，完整 Cerebras dataset/report 仍在会员墙后；因此这些数字适合作为跟踪线索，不应直接当作已审计事实。

## 最后一层
Cerebras 最值得跟踪的不是“能不能打败 Nvidia”，而是 OpenAI 这类客户是否真的愿意为低延迟推理单独配置一条非 GPU 供应链；一旦答案是 yes，它卖的就不是芯片，而是 AI 产品反应速度。
