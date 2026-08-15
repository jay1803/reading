---
title: "From a $6.90 newsletter to $3M API: How a non-coder built Memelord | Jason Levin"
date: 2026-04-28T08:02:08Z
category: reading
description: "Jason Levin 是 Memelord 创始人兼 CEO。Memelord 是一个 AI meme 创作平台：从 $6.90/月的 meme 趋势 newsletter 起步，最早把用户导向 Google Slides；随后 Jason 用 Bubble 和 395 个 workflow 做到 $100K..."
source: "https://www.lennysnewsletter.com/p/from-a-690-newsletter-to-3m-api-how"
---

# BEGIN_SUMMARY
## 嘉宾背景
Jason Levin 是 Memelord 创始人兼 CEO。Memelord 是一个 AI meme 创作平台：从 $6.90/月的 meme 趋势 newsletter 起步，最早把用户导向 Google Slides；随后 Jason 用 Bubble 和 395 个 workflow 做到 $100K ARR，在没有工程师的情况下验证需求；之后融资 $3M，转向 API-first 产品，让品牌、个人和 agent 基于趋势 meme 生成语境化内容。

## TL;DR
这场对话最重要的不是“AI 会不会做 meme”，而是一个产品迁移信号：人类仍需要极强的人味、品牌、幽默和 onboarding 来建立信任，但高频使用会越来越从 UI 转到 agent/API/skill。Memelord 的策略是把两端同时做到极端：对人足够有趣，对 agent 足够低摩擦。

## “No UX is the best UX”正在从口号变成产品架构
Memelord 花大量精力做漂亮 onboarding，甚至被称为“互联网最好的 onboarding”，但 Jason 同时承认长期方向是“没人想按按钮”。他的投资人 Sam Lessin 直接说不想再用任何软件，Jason 的答案不是继续优化按钮，而是给 API。

更非直觉的是，API 不是藏在文档里的工程接口，而是和 OpenClaw skill 一起被包装成 agent 可消费的产品。对 PM/设计师来说，产品交付物开始从“按钮在哪里”变成“如何让一个 agent 明白什么时候、怎样调用能力”。

## 非技术创始人的瓶颈从“不会写代码”变成“有没有足够怪的问题”
Jason 不是典型 vibe coder：他先用 Bubble 硬做，395 个 workflow 支撑核心编辑器，并把产品推到 $100K ARR。融资后他雇了工程师，但自己和营销团队主要用 Cursor 继续做边缘功能、营销页和小工具。

他的内部规则是“每个 marketer 都必须 vibe code”。原因不是为了替代工程师，而是减少创意交接损耗：一个营销创意如果要经过 PM、设计、工程层层转译，通常会被磨平；现在 marketer 可以直接把想法做成小产品。

## 免费小工具正在取代 PDF 下载，成为更高转化的 lead magnet
Memelord 的 free tools 区不是装饰，而是获客机器：各种 meme/filter/generator 小工具给他们带来数十万 email，甚至因为土耳其用户做 TikTok 而在当地传播。Jason 两年前写过“free tools are the new PDF downloads”，现在照做并验证有效。

这里的实操判断很清楚：如果一个 PDF 是为了捕获需求，那今天更好的形态往往是一个小工具，先解决用户进入大问题前的第一个问题。AI 降低了小工具生产成本后，“优先级”开始变成更宽松的“可以都试”。

## Agent-first 工具栈会奖励可被自动化访问的系统
Jason 明确看好 Linear 和 PostHog：Linear 是因为 API 和任务结构适合作为 agent 的 task substrate；PostHog 是因为 AI 数据分析已经能直接回答“来自 Meta ads 的用户留存如何”这类问题。Claire 也补充，她自己几乎不再登录 Linear，而是让 agent 读写 Linear。

这指向一个产品标准：未来工具不只是给人类界面做得好，还要让 agent 能稳定理解、查询、修改、汇报。UI 仍重要，但可编排性正在变成核心竞争力。

## 最有价值的 AI 应用可能不是 SaaS，而是“只为自己做的怪软件”
Jason 的床边 keyboard/Raspberry Pi 项目是整场最强案例：他不带手机进卧室，但会半夜有想法；Google Home 会吵醒妻子；所以他做了一个无屏键盘，盲打后按 Enter，通过 Zapier/LLM 分流到 email、Linear 工程 ticket 或其他任务系统。

他不打算把它产品化，因为价值已经在“为自己解决一个极具体问题”里实现了。对话里还延伸到家庭摄像头找钥匙、检测播客里意外泄露的 API key、iPhone keyboard gun case、stopgivingmeadvice.com 这类半玩笑半工具的个人软件。AI 让 disposable software 和 hyper-personalized software 同时成立。

## AI 能生成笑话，但 meme 的核心仍是语境密度
Jason 以前公开认为 AI 不会好笑，现在修正为：AI 已经能替代前 3% 左右的普通搞笑能力，但顶尖 0.1% 的人类仍更强。就模型风格而言，他认为 Grok、Gemini 比 ChatGPT、Claude 更适合 meme，因为后两者过于安全。

关键边界是：slop 没有上下文，meme 是高度上下文化的信息压缩。AI 可以吐出笑话，但真正有效的 meme 仍依赖人类对场景、身份、时机、冒犯边界和文化语感的判断。Jason 因此不用 AI 替他写作或写 standup，他想保留自己的幽默肌肉。

## 证据薄弱处
- Memelord 的 free tools 带来“数十万 email”，但对话没有给出转化率、留存、CAC、AI credit 成本或付费转化质量。
- “让所有 marketer vibe code”适合强创意、强互联网文化团队，不一定适合合规重、品牌风险高或工程边界复杂的公司。
- “be mean to your AI”更像 Jason 的个人 prompting 风格，不应泛化成稳定方法；更可复用的部分是明确语气边界、降低模型的安全套话、给出更强风格约束。

## 最后一层
这集真正的创业信号是：AI 没有让“人味”贬值，反而让它变成更稀缺的入口；但一旦信任建立，产品就要准备好被 agent 使用，而不是只等人类来点按钮。
# END_SUMMARY
