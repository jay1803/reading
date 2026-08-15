---
title: "How Intercom 2x’d their engineering velocity in 9 months with Claude Code | Brian Scanlan"
date: 2026-04-22T08:01:29Z
category: reading
description: "Brian Scanlan 是 Intercom 的 senior principal engineer，核心工作之一是把公司内部的软件交付流程改造成 AI-first engineering。Intercom 不只让工程师用 Claude Code，也让设计、PM、TPM 直接 shipping code，而他..."
source: "https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering"
---

## 嘉宾背景
Brian Scanlan 是 Intercom 的 senior principal engineer，核心工作之一是把公司内部的软件交付流程改造成 AI-first engineering。Intercom 不只让工程师用 Claude Code，也让设计、PM、TPM 直接 shipping code，而他负责推动这套能力从“个人会用”变成“组织级系统”。

## TL;DR
Intercom 真正翻倍的不是单个工程师的打字速度，而是把 AI 编程从个人技巧变成一套可观测、可治理、可复用的组织系统。指标、skills、hooks、session telemetry、权限边界、内部工具接口和高信任文化一起作用，才把模型能力兑现成 2x 吞吐，而且他们判断下一步不是继续微调 prompt，而是把几乎所有技术工作都重写成 agent-first 流程。

## “给工程师发 Claude”远远不够
- 他们把 R&D 当产品来运营，核心指标是 merged PRs per R&D head，而且这个口径覆盖工程师、设计、PM、TPM，因为所有角色都开始直接 ship code。
- 2x 并不是模型自己长出来的，而是全员 adoption、enablement 和明确预期共同作用的结果。CI 一度先变成瓶颈，修完 CI 后 bottleneck 又转到 code review，说明瓶颈只是在系统内部迁移，不会凭空消失。
- Brian 最强的判断是，技术工作会被整体改写成 agent-first。报警响应、计划、实现、调试、提 PR，都不该再把 agent 当附属助手，而是默认第一执行层。

## 真正可复制的资产是 skills、hooks 和隐性经验编码
- Intercom 发现 AI 生成的 PR 描述质量在下降，于是没停在“提醒大家写好一点”，而是把 CreatePR 做成 skill，再用 hook 强制拦截 GitHub CLI 的默认开 PR 路径，逼系统走标准流程。
- 关键不是某个 skill 本身，而是把资深工程师脑子里的隐性标准拆成可执行组件。flaky spec skill 的做法很典型，它先研究历史案例形成 checklist，再在修复新案例时反写 skill，自我增厚，并主动扇出到同类问题。
- 他所谓 software factory 的含义不是把工程师降格成流水线，而是让系统稳定地产出达到组织标准的结果。AI 的组织价值，来自把高水平习惯从少数人的头脑里抽出来，变成整个环境的默认行为。

## 没有 telemetry，就没有 AI 运营
- 他们给 skills 打 Honeycomb 事件，知道哪些 skill 被谁、何时、为什么调用；同时把 session 数据匿名化后存到 S3，再做个人和组织级分析。
- 这套系统让他们能看到 adoption、dropout、哪些 skill 真有效、哪些只是在 repo 里躺着，以及人究竟是在卡权限、卡接口、卡上下文，还是卡使用习惯。
- Brian 的核心意思很直接，别把 Claude Code 当 IDE 插件，要把它当内部产品平台。没有 usage telemetry、session analysis 和评估闭环，本质上就是在盲飞。

## 成本先当投资，质量靠释放内部修复能力反而变好
- Intercom 明知 token 账单会像 Anthropic 收入曲线一样上升，仍选择先开足 Opus，把优化延后，因为现阶段更在意吞吐和学习速度。
- 他们观察到，从第一行代码到上线公告的时间在缩短， shipped volume 在上升，而且和 Stanford 合作看的外部质量信号并未恶化，反而 code quality 还有提升迹象。
- 更重要的一层是，AI 让 tech debt、flaky tests、CI/CD、内部重构这些过去商业上“没容量做”的事突然可做了。不是工程难题消失，而是 business 终于有能力说 yes。

## SaaS 下一轮不是更好 UI，而是更 agent-friendly 的产品面
- 因为 agent 会天然倾向自己造 feature flags、绕开第三方 SaaS，所以产品如果不提供 CLI、MCP、ephemeral APIs、多步接口和明确提示，默认会在 agent 工作流里失去位置。
- 他最有意思的观点是，要在 help、docs、CLI 里主动给 agent 提供“提示词级线索”，帮助它知道下一步该查邮箱、该建文章、该走哪条安装路径。不是等 agent 自己猜，而是把产品改成可被 agent 顺畅发现和执行。
- 这意味着未来掉队的不一定是功能弱的 SaaS，而是 agent onboarding friction 太高的 SaaS。用户不再主要在网页漏斗里流失，而是在 agent session 里直接按 Escape，改用别的方案。

## 最后一层
这场变化先被压缩的不是写代码本身，而是组织里的等待、协调、说服和标准传递成本。等这些摩擦被 AI 吃掉后，真正稀缺的就不再是工程产能，而是方向判断、产品取舍，以及谁敢先给组织发那张“你可以这么干，出了事我担”的许可证。
