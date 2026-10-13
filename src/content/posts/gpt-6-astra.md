---
title: "GPT‑6 Astra"
date: 2026-10-13T02:55:00Z
category: reading
description: "GPT-6 Astra 在安全任务、长上下文和编程代理成本效率上领先，但独立评测显示综合智能未必超过 Claude Fable，ARC-AGI 3 高分高度依赖专用 harness。"
source: "https://simonwillison.net/2026/Sep/3/gpt6-astra/"
---

GPT-6 Astra 在安全任务、长上下文处理和编程代理成本效率上展现出明显优势，但独立评测尚未支持它在综合智能上领先 Claude Fable，最亮眼的 ARC-AGI 3 成绩也高度依赖运行模型的 harness。OpenAI 于 2026 年 9 月 3 日开始向少数组织开放 Astra，并计划随后几天覆盖全部 ChatGPT Plus、Pro、Business、Enterprise 用户，以及 OpenAI API 和 AWS。API 定价与 Claude Fable 5、5.1 相同：每百万输入 tokens 10 美元、每百万输出 tokens 50 美元，明确将其定位为 Fable 的竞争产品；OpenAI 自报的多数基准成绩也高于 Fable。Simon Willison 当时尚未亲自试用，文中的判断来自已公布的测试结果。

Astra 在当年 3 月发布的 ARC-AGI 3 上取得了 99.9%，但这个数字必须连同测试条件理解：OpenAI 使用自定义 **Provider Adapter harness**，花费 19,000 美元才获得这一成绩；使用默认 ARC-AGI harness 时，成绩为 62.7%，花费反而达到 26,000 美元。自定义 harness 会在请求之间保留不透明的推理状态，并在长对话中进行 compaction，使模型能够复用之前完成的工作。同一模型在两套运行框架下的巨大差异，说明这项成绩同时反映了模型与状态管理机制的协同能力；Claude Fable 5 当时尚无公开的 ARC-AGI 3 成绩，无法据此直接比较两者。

安全任务上的提升覆盖漏洞利用与二进制逆向工程。Astra 在 ExploitBench 上达到 100%，GPT-5.6 Sol 为 78.5%；在 ExploitGym 上达到 42.4%，Sol 为 30.3%；在 SRE-Bench 二进制逆向工程测试中，允许最多四次尝试时，Astra 达到 99.2%，Sol 为 68.7%。长上下文也出现了强劲结果：在 OpenAI 的 eight-needle 测试中，Astra 在 256K–512K tokens 区间达到 100%，在 512K–1M tokens 区间仍达到 96.3%。这些成绩支持它在超长输入中检索多处目标信息的能力显著增强，但证据范围仍限于这项测试。

独立评测给出了更有边界的竞争图景。Artificial Analysis 的 Intelligence Index 中，Astra 得分为 61，与 GPT-5.6 Sol 持平，比 Claude Fable 5.1 的 max with fallback 配置低 5 分，也落后于新发布的 Meta Muse Spark 1.3 的 max 配置。因此，OpenAI 自报基准中的多数领先，并未转化为这项独立综合智能指标上的领先。

Astra 更明确的竞争力体现在 **Coding Agent Index 的成本效率前沿**：使用 max effort 时，它与 GPT-5.6 Sol 的 max 配置成本相近，得分高 2 分；达到与 Claude Fable 5 相同的分数时，每项任务成本不到后者的一半。API 上线后的模型名称将是 gpt-6-astra。综合这些结果，评价 Astra 的关键需要同时看能力、运行框架与完成任务的实际成本：综合智能分数未必领先，仍能凭特定任务上的能力提升和更低的执行成本形成优势。
