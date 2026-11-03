---
title: "Inside the multiplayer AI setups at Mintlify, LangChain, and Buffer"
date: 2026-11-03T05:48:21Z
category: reading
description: "多人协作 AI 系统的关键，是让团队共享准确、持续更新的业务知识，并为能力开发、发布、使用和维护建立清晰责任；Buffer、LangChain、Mintlify 展示了三条不同路径。"
source: "https://newsletter.mkt1.co/p/multiplayer-ai-mintlify-langchain-buffer"
author: "Emily Kramer"
---

多人协作 AI 系统的关键，是让团队共享准确、持续更新的业务知识，并为能力开发、发布、使用和维护建立清晰责任；Buffer、LangChain 和 Mintlify 展示了三条不同路径：全员构建与集中发布结合、由专门团队运营生产级 agent，以及先把公司知识建设成可靠的基础设施。三家公司各自利用了已有优势：Buffer 的透明协作文化、LangChain 的 agent 开发技术、Mintlify 的知识管理产品，因此适合借鉴的是运作机制，整套架构仍需围绕本公司的人员和工作方式设计。

Buffer 把营销系统拆成**能力层**与**上下文层**：前者包含 skills、工作流、可复用提示词和参考文件，后者保存业务知识与策略。团队成员可以选择 Claude Cowork 或 Claude Code，skills 通过共享 GitHub plugin 分发，一次推送即可让所有人的 Claude 获得更新；业务知识则留在营销团队熟悉的 Notion，避免每次调整策略都要提交 pull request。各职能负责人按照 Simon Heaton 制作的统一模板记录自己的策略，相关 skill 每次执行时读取对应文档。例如，AEO 月报先读取 Buffer 的 AEO 策略，再通过 Profound MCP 获取数据，使报告围绕公司实际定义的成功标准展开。

这种分离让专业知识的维护者和系统发布者各负其责。每位领域专家负责自己的 skills 与上下文，先在本地构建并测试；Simon 及其 growth marketing 团队提供搭建模板、协助复杂开发，在输出达到要求后审核并发布到共享 plugin。开发中的工作在 Linear 跟踪，大家在 Slack 分享进展。营销技术、marketing ops 和数据职能都在 Simon 的职责范围内，因此他承担整体系统的维护责任，而其他成员仍能自主试验。共享 skills 还把一个职能的知识传递给另一个职能：growth marketer 使用内容营销同事建立的 skill 时，也能接触对方的判断标准。

Buffer 的实际能力覆盖报告、网站维护、社区运营和合作申请处理。营销人员可以通过 Claude Code 添加 FAQ、更换图片或上线 A/B test；Buffer 已约五年没有使用 CMS，这让设计师和工程师可以集中处理定制性更强的工作。社区团队使用 Profound MCP 与 Reddit API 找出最常被 AI 搜索引擎引用的 Reddit 讨论，决定参与哪些对话。一个连接 Screaming Frog、Google Search Console 和 Ahrefs MCP 的工作流，会判断失效链接应恢复、重定向还是删除，再由 Claude Code skill 实施修复，首次执行使内部失效链接减少了 87%。合作申请 agent 则处理每次数十份的申请，并保留每日人工复核。

Buffer 还为系统自身建立了维护能力。每月一次的上下文刷新工作流通过 Granola 等 MCP 检查信息变化，再在 Slack 提醒各职能负责人决定如何更新文档；新 skill 在全员发布前必须经过领域专家测试；部分每次都需要人工参与的内容工作流，会同时检查变化并把更新写回自身。这里包含三个持续性任务：规范新能力的构建、在使用过程中发现修复点与重复项，以及定期检查整个系统。与此同时，Buffer 对面向用户的内容保留严格人工控制，博客、社交帖子和 landing page 仍由人撰写，或由人深度参与。系统扩大了执行能力，没有取消内容责任。

采用这些能力还需要让成员获得真实的构建经验。Buffer 在公司级 Build Week 前设置了 AI 能力评估与分层课程；原本自认非技术人员的 communications director Hailley Griffis，在那一周提交了 50 个 pull request、交付了 6 个内部工具，位列内部 makers 榜第三。随后，Buffer 又部署了运行于 Slack、Linear 和 GitHub 的 Roo，Simon 认为通过 Slack 与 Roo 协作的使用量可能超过 Claude Code。工具入口会变化，但让所有人能够贡献、同时保留统一发布标准的机制可以继续沿用。

LangChain 则把共享系统建设成云端运行的**生产级 agents**。其 GTM Engineering 职能于 2026 年 6 月成立，最初希望通过移除重复劳动，使 SDR 团队效率至少提高到原来的三倍，并把经理管理 SDR 的人数比例从约 1:3 提升至 1:10；之后服务范围扩展到营销及整个销售周期。文中描述的四人 GTM Engineering 团队负责团队级 agent 的开发与运营，每位工程师对接一段 funnel 和相应业务团队。Claude 在这里是可选模型提供商，员工主要通过 Slack 或专门界面调用能力，无须进入各自的 Claude 会话。

这套系统使用 LangGraph、Deep Agents 等产品构建 agents，通过 LangSmith 托管、追踪和监控，并有意保持模型无关性：Claude 与 OpenAI 的 Luna 被用于不同子任务，Danny Lambert 表示，切换到更好或更便宜的模型只需一个下午。Agents 直接通过 API 读取 CRM、数据仓库、Apollo、Reo.dev 和 Centralize 等权威数据源，把答案带到员工日常工作的地方，同时继续利用现有工具的底层功能。每次运行都会重新获取业务数据，例如新线索进入后，系统通过网络搜索和数据供应商补充信息，再写回记录，减少手工维护数据的负担。

实时获取的数据仍需配合人类编写的业务规则。起草外联邮件前，agent 会读取描述如何区别处理 warm lead 与 cold lead 的“outbound skill”；品牌、产品 messaging 和博客写作等知识，也由最了解内容的成员直接维护。系统还保存 SDR 对 Slack 草稿的修改，让后续草稿吸收反馈，并支持个人设置邮件语气和格式偏好。共享业务知识、每次运行获得的新数据与个人反馈由此进入同一工作流。

LangChain 的 GTM agent 会接收每条新 Salesforce lead，先检查是否已有同事跟进，再研究账户，并把邮件草稿发送到负责人的 Slack 私信，由人选择发送、修改或取消。根据 LangChain 公布的数据，lead-to-qualified 转化提高了 250%，pipeline 增至三倍，低意向线索的后续跟进增加了 97%，销售代表每月约节省 40 小时，86% 的团队成员每周使用该系统。这些是公司报告的业务结果；团队另外发现，表现最好的 SDR 也是 agent 使用最频繁的人，但这一关联本身不能证明因果关系。

其他 agents 将相邻工作的能力组合起来：paid media agent 每周分析 campaign、ad group、keyword 和 landing page，提出建议后还可以修改广告平台设置；原本作为其子 agent 的 content studio，后来扩展为社交、field marketing 和户外广告团队提供长视频、配音短视频及展示广告。销售材料生成器则制作符合品牌要求的 one-pager 与 POV plan，并交付可编辑的 Google 文件。系统也处理账户健康预警、周度账户情报、会前会后简报及 CRM 信息补全，所有面向客户的输出仍需人工审核。

集中部署带来的重要差异，是可以记录运行情况和实际采用程度。Agent 可以由 Slack 请求、webhook 或定时任务启动，团队通过统一数据库生成 adoption heat map，查看谁使用了哪个 agent、使用了什么功能、频率如何。相比之下，在成员各自 Claude 中执行的 GitHub skills，若缺少额外的集中记录，就难以获得这种使用视图；仓库贡献统计只能说明谁提交了能力，无法说明谁实际使用。LangSmith Engine 进一步监测每次运行的失败，把问题归类、阅读代码定位原因并起草修复，交给人批准。Danny 表示，这一过程曾发现 contact-enrichment 工作流的改进机会，使单次运行成本降低近 60%。

LangChain 因此把易用、模型无关、可追踪和自我改进设为高质量 agent 的四项标准，其中可追踪意味着团队能够理解执行过程并修复故障。个人仍可开发本地工具，只有当需求足够普遍时，GTM Engineering 才将其整合为共享 agent；同一 agent 还会依据使用者身份与权限，装配不同的数据源和指令。入口也要适应用户：Danny 估计，一支 100 人的 GTM 团队中，可能只有 20 至 30 人能熟练使用 CLI，因此 Slack 是主要消费界面，熟练用户仍可通过 MCP 和命令行访问。这样的分工也限制了无人维护的局部工具扩散，否则开发者一忙或离职，业务便可能依赖一个持续损坏的系统。

Mintlify 的优先级集中在**上下文基础设施**。它的营销团队只有 7 人，对应超过 40 人的销售团队，团队级 skills 的分享方式仍在摸索，但公司已经把内部知识库从 Notion 迁移到自己的产品，与外部帮助文档共用基础设施，并通过权限控制区分访问范围。文档采用 Git 版本控制，全员可以编辑和发布；系统监测产品变化、代码提交、release notes 及其他工具中的更新，起草知识库修改，再交给人审核。迁移后的 66 天里，团队完成了 419 次贡献，每位成员都至少撰写过内容。

Mintlify 为此设立了专门的 knowledge engineer。Ethan Palm 最初是 technical writer，一年后转向同时管理内部知识库和外部文档，并建设、维护更新它们的自动化。这个岗位让知识的新鲜度有明确负责人，也让审核与自动化开发成为正式工作。Lauren Volpi 曾在营销活动讨论中让 Ethan 同步更新竞争对手相关文档，因为客户及其 agents 查找信息时，会访问公司多个知识入口，营销活动的准备范围也随之超出 landing page。

文档的重要性还延伸到获客。内部 agents 需要公司知识来执行任务，客户的 agents 和 LLMs 也会读取公开文档形成产品答案。Mintlify 平台的流量计数器显示，在其支持的文档站点中，agent 流量占比从 2026 年 1 月的 15% 升至文中所述约 66%；Lauren 预期年底会超过 90%，后者是预测。结构清晰、事实明确的文档适合机器读取，而 Mintlify 自己访问量最高的内容正是 documentation，因此营销团队即使不直接拥有文档，也需要参与检查内容和流量。内部知识管理与外部需求获取，在这里共享了同一套知识基础。

在这层基础上，Lauren 用 Claude Cowork 建立了读取 Mintlify 知识库的 shared marketing brain，成员再围绕它构建个人 skills；团队也能在 Slack 中询问 Mintlify agent，或通过 Claude Design 中的品牌设计系统加快销售素材制作。CRM、销售通话录音和产品 tracker 的 MCP 帮助团队寻找 case study 候选、汇总客户反馈，并把 GTM 计划与产品路线图对齐。GTM engineer Cole Gottdank 开发的 Signal 每 30 分钟扫描注册和网站活动，判断购买意向，再把有效信号发送给对应销售的 Slack；营销团队使用相同的客户、产品和意向数据建立受众、生成 buyer map 和检查 fit score。支持工单转 PR、邮件处理、每周情报和定时销售晨报等公司级 agents，也为营销团队提供能力。

三套系统共同要求上下文具备几个条件：连接团队已经使用的工具与文档，维持权威来源并避免重复副本，让人和 agent 都容易读取，支持便捷更新和版本历史，同时经过筛选，避免每次执行都解析过量内容。Buffer 选择 Notion 加月度负责人复核，LangChain 选择每次运行获取数据并配合人工规则文件，Mintlify 选择自动起草更新加专职知识审核；共享仓库或某个 AI 客户端本身，无法独立承担这些职责。

组织方式同样必须与责任对应。Buffer 让全员开发、由 growth marketing 把关发布；LangChain 让专职团队对共享生产系统负责，保留个人试验空间；Mintlify 为知识维护设岗，由营销负责人和团队推进其他能力。三家公司都把人工审核保留在面向客户的输出、共享能力发布或知识更新环节，并把维护逐渐嵌入自动化流程。个人试验要变成团队长期依赖的基础设施，关键就在于让知识更新、质量控制、使用反馈和维护责任，都能随着能力的共享一起延续。
