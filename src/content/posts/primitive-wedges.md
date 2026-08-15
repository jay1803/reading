---
title: "👓 Primitive Wedges"
date: 2026-06-03T08:01:13Z
category: reading
description: "AI dev tool 的机会不在“再造一个更大的 agent 平台”，而在先占住一个小而痛、会被其他工作流反复调用的底层动作：安全运行代码、取回正确上下文、验证输出、委托权限、观察 agent 行为、协调人和工具。生成能力变便宜之后，稀缺性会转向信任、边界、审计和可控交付；真正的平台通常不是先被宣布出来的，而是..."
source: "https://www.plg.news/p/the-new-primitives-of-ai-native-development"
---

## TL;DR
AI dev tool 的机会不在“再造一个更大的 agent 平台”，而在先占住一个小而痛、会被其他工作流反复调用的底层动作：安全运行代码、取回正确上下文、验证输出、委托权限、观察 agent 行为、协调人和工具。生成能力变便宜之后，稀缺性会转向信任、边界、审计和可控交付；真正的平台通常不是先被宣布出来的，而是先变成别人不敢轻易替换的依赖。

## 核心主张拆解
作者把“primitive wedge”定义成一种狭窄能力：它不是完整平台，也不是普通功能，而是开发者做某件重要事情时的默认接口。一旦其他系统开始依赖它，它就从 feature 变成 infrastructure。Stripe 先让支付 API 变干净，Twilio 先让发短信变成一个 API，Vercel 先占住部署与预览工作流，都是先拥有一个 verb，再扩展成更大的平台。

这篇文章的判断基础是：AI 让“可用的代码草稿”变得丰富，但没有同步解决“能不能信、能不能运行、能不能交付、谁授权、出了事怎么追溯”。Stack Overflow 2025 调查里，84% 的开发者使用或计划使用 AI 工具，但 46% 不信任 AI 输出准确性，只有 3% 高度信任；66% 的主要挫败是“差一点对但不完全对”，45% 提到调试生成代码更耗时。采用曲线已经跑到信任曲线前面，这就是 wedge。

## 六个正在成形的 primitives
### Secure Execution
AI 写出的代码需要地方运行，但不能直接碰生产环境、开发者本机 secrets 或高权限系统。sandbox 一开始像功能，随后会变成 agent 行动的容器：装包、改文件、跑命令、测试、eval、数据分析、教育环境、内部自动化都要在受控环境里发生。Vercel Sandbox、Cloudflare Containers / Sandbox SDK、Daytona、Modal 这类产品都在围绕“安全运行不可信工作”形成类别。

### Operational Memory
很多“模型很笨”的问题其实是组织记忆坏了：文档过期、架构决策在脑子里、路线图在 Linear、客户反馈在 Zendesk、事故历史在日志里。AI 要改系统，必须知道代码库、命名、依赖、历史决策和隐含约束。Sourcegraph 从代码上下文切入，Glean 从公司知识切入，Letta / Zep 从 agent durable memory 切入；共同目标是让系统在正确时间拿到正确上下文。

### Verification
当生成的边际成本下降，昂贵的问题变成“这个输出是否安全、正确、值得保留”。测试、静态分析、安全扫描、policy check、代码审查、回归检测、运行时验证和 eval 会前移，不再只是生成之后的下游环节。CodeRabbit、Qodo、Greptile 的价值不在生成更多代码，而在把 PR 审查变成可重复的质量层。

### Delegated Authority
当 agent 从“建议”变成“行动”，权限就从烦人的配置项变成产品本身。关键问题是：哪个 agent 能代表哪个用户、在什么范围内、多久、能读写什么、是否需要审批、留下什么审计记录。Arcade 用 OAuth scope 和用户授权处理 agent tool access，Keycard.ai 试图做 agent identity、policy enforcement、scoped credential、agent-to-agent delegation 和 audit trail 的控制平面。

### Agent Traces
传统 observability 看日志、指标、trace、错误和延迟；agentic software 还要看模型、工具、上下文、策略、人类审批和失败路径构成的完整工作轨迹。企业会问 agent 做了什么、用了什么上下文、忽略了什么、花了多少钱、碰了什么数据、为什么被允许、能否 replay。LangSmith 和 Anthropic Managed Agents 都在把 thread、tool call、session、sandbox、harness、memory 变成可观察对象。

### Durable Orchestration
AI workflow 不再只是 Zapier 式 trigger-action，而是人、agent、API、policy、retry、approval、exception、rollback 的协调系统。Temporal 的类比很准确：AI apps / agents 是“distributed systems on steroids”，需要能在崩溃后恢复、保留状态、重试 tool call、支持 human-in-the-loop，并把 chain、graph、agent loop 映射成 durable workflow。

## 平台化风险
最大威胁是 primitive bundling。前沿模型提供商不只卖 intelligence，也在包装 intelligence 周围的 runtime。Anthropic Managed Agents 已经把 session、harness、sandbox、bash/file/web/MCP tools、stateful history、async work 放在一起，这直接触碰 agent runtime 的所有权。

但 bundling 不是终局。创业公司更稳的位置通常在 model-agnostic、harness-agnostic、workflow-specific、compliance-heavy、深集成或掌握特殊分发渠道的层。好问题是：如果世界变得 multi-model、multi-agent、multi-harness，你的 primitive 会更有价值，还是更像模型平台迟早内置的默认功能？

## 值得质疑
作者列出的六个 primitive 方向都合理，但文章对“谁能捕获价值”的判断还偏概念化。安全执行、traces、orchestration 很容易被云厂商、模型厂商和现有 DevOps 平台吸收；memory 和 verification 也可能因为深度依赖既有代码托管、CI、ticket、docs 系统而被 incumbent 绑定。真正的创业机会不只是“这是重要 primitive”，而是能否在 distribution、trust boundary、compliance、switching cost 或 workflow ownership 上形成独立权力。

## 最后一层判断
这篇文章最有用的不是列赛道，而是提醒 founder 不要被“AI-native platform”叙事诱惑。AI 时代的大机会可能先长得很窄、很无聊、很底层：一个被反复调用的动词，一个别人懒得自建但不能没有的接口，一个坏了就让整个工作流停摆的依赖。
