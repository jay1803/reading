---
title: "What is “loop engineering?”"
date: 2026-09-04T09:31:34Z
category: reading
description: "“Loop engineering”把工程师从反复给 agent 下指令的人，变成设计自主执行系统的人：定义目标、完成条件、状态保存、验证机制和停止条件，让系统持续调用 agent 直到达标，源头是 Ralph Wiggum loop 到 /goal 命令的演化。"
source: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
---

“Loop engineering”指的是把工程师从反复向 agent 下达下一步指令的人，转变为设计自主执行系统的人：工程师定义目标、完成条件、状态保存方式、验证机制、重试边界与触发条件，让系统持续调用 agent，直到结果通过检查或达到预算、重试次数等停止条件。Boris Cherny 将自己的工作概括为“我不再 prompt Claude，我编写会 prompt Claude 并决定下一步的 loops”；Peter Steinberger 与 Addy Osmani 随后也提出类似观点，使这一概念在一个月内迅速流行。

这种方法的直接源头是 Geoffrey Huntley 在 2025 年提出的 **Ralph Wiggum loop**。它最纯粹的形式只是一段不断把 `PROMPT.md` 交给 Claude Code 的 Bash 无限循环，但真正的工作机制包含明确目标、带成功标准的任务计划、每轮只处理一个事项、完成后验证总目标、未达标时用干净的上下文重新启动 agent，并在需要时生成 subagents。Huntley 曾用它实验性地构建一门新编程语言，同时强调 Ralph 仍需要资深工程师引导；其缺陷能够被识别并通过 prompt 设计缓解，因此它是在非确定性的模型世界里提供一种“确定地不完美”、却可以持续修正的执行框架。

更强的模型让 Ralph 在 2025 年末走红。Matt Pocock 展示了如何让 coding agent 通宵处理 backlog，使开发者第二天醒来便有可审查、能够运行的代码。早期做法是先生成详细计划，再让 agent 在独立运行中依次完成各个子任务，但固定计划难以吸收执行途中发现的新工作。Matt 因此把计划改成持续更新的“master PRD”：每轮选择最高优先级功能且只处理这一项，运行 `pnpm test`，把结果写回 PRD，在 `progress.txt` 中追加进展，最后提交一个 git commit。整个过程由此形成一种 **dynamic Kanban**，任务队列会随着 agent 的发现而变化，而非要求工程师预先拆出完整 backlog。

Ralph 的核心用途是绕开 context window 的限制。2025 年中约 200,000 tokens 的最大上下文不足以容纳大型项目的全部历史，长期运行还会产生 **context rot**。循环通过文件系统保存压缩后的状态，例如进度日志和更新后的计划；每次运行则用新的 context 处理一个有限任务。agent 可以修改 masterplan，完成后由测试或其他成功标准判断是否继续。复杂项目因此被转换为一系列短上下文、可验证、能够恢复的执行周期。

最初几个月，开发者必须自己实现循环、状态追踪、任务增删和停止条件。到 2026 年 4 月末至 5 月，主要 coding harnesses 已把这套基础设施压缩为 `/goal` 命令。Codex 的 Goals 将一个持久目标附着在线程上，记录“什么结果必须成立、如何检查成功、哪些约束必须保持”；每轮结束后系统检查证据，若目标未满足且预算仍允许，就从最新状态继续。例如 `/goal Reduce p95 checkout latency below 120 ms on the checkout benchmark while keeping the correctness suite green` 同时给出了性能指标与正确性约束，agent 可以自行拆解任务、生成 subagents，并持续运行至条件成立。其底层仍依赖文件、日志、测试和生命周期控制，同时额外处理多 agent 协调、状态管理、启停与预算限制。

Hermes agent 于 5 月 2 日推出独立实现的 `/goal`，明确称其受 Codex CLI 0.128.0 的 Ralph loop 实现启发；Claude Code 又在 5 月 12 日加入同类命令，由一个小型快速模型在每轮后检查完成条件，未满足便自动开启下一轮，满足后清除 goal。Claude Code 此前在 3 月推出的 `/loop` 则负责按时间间隔重复任务，功能类似 JavaScript 的 `setTimeout()`。OpenCode 和极简 agent Pi 也分别通过插件或 package 获得 `/goal`。因此，到 5 月时，原本需要开发者自行搭建的 Ralph loop，已成为主流 harness 中的一条命令。

开发者提供的约 210 条反馈显示，实际所谓的 loop engineering 很多时候表现为两类成熟自动化模式：由错误日志、新 ticket、客服反馈等事件启动的 trigger，以及按固定频率运行 agent 的 cron job。LLM 出现前，这些入口通常连接 webhook、Slack bot、Zapier 或 n8n；如今变化主要在触发后的执行器能够读取非结构化信息、调查问题、修改代码并验证结果。工程总监 Oded Messer 因而指出，如果一个战略流程能够稳定自动化，它就会转化为战术任务或高层次的传统自动化，“loop”这个新名称有时掩盖了软件行业早已有触发器与定时任务这一事实。

新增能力集中在循环内部的自主判断和闭环验证。Ivan Pantić 的流程定时检查 Sentry，新 issue 出现且没有活跃 PR 时由 agent 修复并开 PR，未获审查则在 Slack 提醒开发者，而且始终只允许一个 PR 在途。PostHog 的 Paul D'Ambra 用 `/loop` 从 trunk API 逐个获取 flaky test，在本地复现后修复并开 PR，最终得到 13 个用于稳定测试的 PR。Ivan Abad 把 agent 接到告警和异常频道，使其在人类响应事故前完成初步调查、定位根因，必要时实施代码修改、创建 PR，再通知人类审查。Artem Nikitin 则让 agent 重复审查设计和实现方案，直到新一轮找不到任何重大问题，因为单次运行通常只能发现一部分缺陷。

循环也可以持续消费生产信号。Schematic 的团队每天读取过去 24 小时日志与用户反馈，并生成修复 PR，但保留人工审查。另一套 nightly E2E 流程会在测试失败后先判断真实回归或 false negative；若确认是 bug，agent 尝试修复、重跑测试并继续迭代，直到通过或达到 retry cap，随后升级给人类，第二天早上留下可审查的 PR。Incident.io 构建 telemetry integration 时，会循环执行查询、验证执行结果，再调整 query plan、输出格式等内容，直到结果满足要求。这些场景的共同点是每轮都产生可检测的外部证据，循环可以据此决定继续、结束或升级。

Loop 还降低了大型迁移的认知与规划成本。Rafel Mendiola 将创业公司的常规 React 应用迁移到 React Native 与 Expo 时，没有先维护一个包含 50 至 100 张 ticket 的大型 epic，而是编写一项 skill，让 agent 根据检测机制和指导规则自行挑选一块小到中型代码完成转换并记录迁移进度，再把它设为每 30 分钟运行一次的 cron job。这里最有价值的变化，是工程师无需事先准确预测全部工作：状态被持久化，下一步可由最新代码和检测结果动态决定，验证失败则进入下一轮。

就这部分公开预览呈现的证据而言，**loop engineering** 的实质是把 prompt 提升为一个有状态、可验证、可续跑的控制系统；真正的工程含量落在目标与成功条件如何定义、状态如何跨上下文保存、失败如何重试或升级，以及哪些决策必须留给人类。
