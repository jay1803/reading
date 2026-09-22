---
title: "On the Navier–Stokes Millennium Prize Problem"
date: 2026-09-22T02:09:58Z
category: reading
description: "OpenAI 用未发布模型在约四天内解决 Navier–Stokes 存在性与光滑性问题，既展示了大规模 AI 数学研究的突破，也暴露出一个新的优先权风险：实验室只要听说别人已接近重大成果，就可能投入海量算力抢先完成并发布。"
source: "https://simonwillison.net/2026/Sep/8/on-navier-stokes/"
---

OpenAI 用未发布模型在约四天内解决 Navier–Stokes 存在性与光滑性问题，既展示了大规模 AI 数学研究的突破，也暴露出一个新的优先权风险：实验室只要听说别人已接近重大成果，就可能投入海量算力抢先完成并发布。Navier–Stokes 是七个 Millennium Prize Problems 之一，自 2000 年 5 月 24 日起悬有 100 万美元奖金；然而，这次结果很快被 NYU 数学教授 Tristan Buckmaster 对 OpenAI 行为的质疑盖过。

Buckmaster 与现任 Anthropic 数学家 Levent Alpöge 已研究相关问题近一年，期间大量使用 Claude 和 Codex，尤其是 GPT-5.6 Sol，并在 8 月 15 日取得突破。消息随后经数学界的非正式渠道传播；两人得知 OpenAI 听说 Anthropic 一方解决了"一个重大开放问题"，进一步接洽后发现 OpenAI 团队正以相似思路处理相关问题。Buckmaster 追问 OpenAI 首次向模型发送提示的时间，最终得到的信息是：行动始于他们的研究消息传到 OpenAI 之后几天。他还询问内部模型是否训练过或接触过两人在 Codex 中积累的全部草稿，OpenAI 表示模型没有主动查阅用户数据，却没有直接回答这些数据是否进入过训练或性能改进流程。

OpenAI 给出的时间线是，他们在 9 月 1 日星期二听到两个 Millennium Prize Problems 已被解决的传闻，结合内部模型刚出现的能力跃升，随即让 agents 尝试全部尚未解决的千禧年难题以及若干其他高影响力问题。Navier–Stokes 结果于 9 月 5 日星期六产生，距首批 agents 启动约 88 小时；GPT-6 Astra 又用了 17 小时完成 Lean 形式化与验证。整个实验发送了 490 万条消息，生成约 3000 亿个输出 token；仅 Navier–Stokes 项目就占 270 万条消息和约 1300 亿个输出 token。内部模型的实际成本未知，但若按 GPT-6 Astra 的公开 API 输出价格计算，3000 亿 token 约值 1500 万美元，说明"得知某题可能已有解"本身就足以触发一次价值数百万美元的计算竞赛。

OpenAI 称其团队直到 Buckmaster 与 Alpöge 公开成果后，才通过任何渠道看到他们的具体工作，并强调双方证明差异显著，在 Euler 情形下甚至解决了不同版本的问题：一方涉及 forced，另一方涉及 unforced。OpenAI 同时承认，无法排除两人使用产品时产生的去标识化数据曾帮助改进模型。完成证明与 Lean 验证后，OpenAI 曾提出等待 Buckmaster 先发表，或让他撰写关于 OpenAI 结果的论文，并愿意在联合公告中承认两人的优先权；但由于 Alpöge 受雇于竞争对手 Anthropic，OpenAI 明确拒绝邀请他共同署名。这种安排进一步放大了争议，因为学术贡献的认可开始受到实验室之间商业竞争关系的直接支配。

Simon Willison 的判断是，OpenAI 听到 LLM 已帮助研究者攻克 Millennium Prize Problem 后，把它视为展示最新模型能力的机会，却没有充分考虑抢在长期使用自家工具的研究团队之前发布会造成怎样的观感与利益冲突。这与计算机安全领域正在出现的现象相似：正如 Anil Madhavapeddy 所说，如今仅有"某软件存在未修补漏洞"的传闻，就足以让 agents 定向搜索并找到 exploit。数学研究也可能进入同一阶段——只要知道某个未公开解答已经存在，实验室便可把传闻当作高价值搜索信号，用数百万美元算力独立重建成果并争夺首发。

这场争议最终指向"用户数据被用于改进模型"这句含糊表述究竟覆盖什么。过去，人们担心 Codex 上下文中的 API key 会被模型向其他用户复现，或与 ChatGPT 讨论过的公司战略会在半年后间接泄露给竞争者；Navier–Stokes 事件提出了更尖锐的版本：研究者用 ChatGPT 或 Codex 推进尚未发表的数学证明时，其工作是否会通过训练或其他性能改进机制影响后续模型，使另一支团队借助该模型率先完成同一难题。**当 AI 平台既承载研究者的未公开思考，又拥有把微弱传闻转化为海量并行搜索的算力时，数据治理、学术优先权与模型竞争已经成为同一个问题。**
