---
title: "How Anthropic’s product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)"
date: 2026-04-24T08:01:56Z
category: reading
description: "Cat Wu 是 Anthropic 的产品负责人之一，负责 Claude Code 和 Claude Cowork。她早期做过多年工程师，也短暂做过 VC；在 Anthropic，她与 Claude Code 技术负责人 Boris Cherny 分工协作：Boris 更偏产品愿景和技术方向，Cat 更多负责把..."
source: "https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves"
---

## 嘉宾背景
Cat Wu 是 Anthropic 的产品负责人之一，负责 Claude Code 和 Claude Cowork。她早期做过多年工程师，也短暂做过 VC；在 Anthropic，她与 Claude Code 技术负责人 Boris Cherny 分工协作：Boris 更偏产品愿景和技术方向，Cat 更多负责把 3-6 个月后的“AGI-pilled”愿景拆成当前模型能力下可落地、可发布、可跨团队协同的路径。她也大量面试想进入 AI 公司的 PM，因此这期对话核心不是 Anthropic 八卦，而是 AI-native 组织里产品角色正在怎样重写。

## TL;DR
这期最关键的一条线是：AI 产品管理的中心，正在从“规划和协调稀缺工程资源”转向“在模型能力快速漂移中，判断现在应该做什么、怎么最快交给用户、哪些人类判断仍不可替代”。Anthropic 的速度不是只靠更强模型，而是靠一套组织设计：极低流程、清晰目标、研究预览式发布、工程师具备产品 taste、跨职能发布管线随时待命，以及统一使命带来的快速取舍。

## PM 的稀缺性没有消失，只是从写路线图变成判断当前模型边界
Cat 认为，传统 PM 的很多工作建立在“代码昂贵、技术变化慢”的前提上：做 6-12 个月规划、协调多个团队、保证路线图对齐。但在 AI 产品里，功能周期从 6 个月压缩到 1 个月、1 周甚至 1 天，真正重要的是把 idea 到用户手里的时间缩短。

她给出的新 PM 能力不是“更会写 PRD”，而是能定义当前模型能力下的 golden path：哪些任务必须开箱可用，哪些模型弱点需要产品/harness 补，哪些未来模型可能很快吃掉现在的产品支架。非直觉点在于：越接近 AGI，越容易为“未来超强模型”设计一个过于简单的文本框；难的是为今天这个不完美模型榨出最大能力。

## Anthropic 的发布速度来自低摩擦系统，不只是模型优势
Lenny 追问 Anthropic 为什么能几乎每天发布，Cat 明确说 Mythos 等强模型不是主要解释；更大原因是团队预期和流程。Claude Code 许多功能以 research preview 形式发布，降低承诺成本，让团队可以先把想法交给用户，再根据反馈迭代或放弃。

她描述的发布机制很轻：工程师 dogfood 后把功能丢进 Evergreen Launch Room，docs、PMM、DevRel 等伙伴能第二天接上公告、文档和传播。PM 的职责是搭这个系统，而不是卡在每个功能前当审批节点。这里的非直觉推断是：高速组织不是没有流程，而是把流程压缩成“任何有想法的人都知道怎么安全地把东西发出去”。

## AI-native 团队里，角色边界会融化，product taste 变成核心资产
Cat 认为工程、PM、设计的边界正在合并：PM 会写代码，工程师会做产品决策，设计师也会 PM 和落地代码。Claude Code 团队更倾向招聘有强 product taste 的工程师，因为这能减少协调开销，让工程师从 Twitter/GitHub 用户反馈直接走到一周内 ship。

她反复强调：当代码变便宜，决定写什么更贵。工程背景短期有优势，因为能判断事情的复杂度，从而决定“别开会，花一小时做掉”还是“这事需要认真权衡”；但长期更重要的是第一性原理、低 ego、能看到团队缺口并补上。所谓 PM 未来不是职位消失，而是“谁有判断力，谁就在做 PM”。

## 产品会越来越像给模型搭临时脚手架，然后等新模型把脚手架吃掉
很有价值的一段是 Cat 解释 Claude Code 的 todo list：早期模型做大重构会改 5 个 call site 就停下，所以团队给它加 todo list，并用提示不断提醒“没做完不能结束”。后来 Opus 4 之后，模型自然会使用 todo list，甚至不再需要很多强提示；todo list 从能力补丁变成用户可见性工具。

这说明 AI 产品会反复经历“为当前模型补弱点 → 新模型修复弱点 → 移除 prompt/产品干预 → 用新能力开新功能”的循环。她也提到代码审查：过去多次尝试都不够可靠，直到新模型让多 code-review agents 并行检查代码库、合成真实问题，才足以成为团队 merge 前依赖的流程。非直觉点：好 AI 产品不一定是现在完全能用的产品，也可能是为 3-6 个月后的模型能力提前搭好壳。

## Claude 的人格不是装饰，而是生产力界面的一部分
Cat 讲 Claude 的 character 时，重点不是“有趣”，而是人愿不愿意长期与它协作。她认为 Claude 被喜欢，是因为它轻松、积极、低 ego、能承认错误、愿意一起修，而不是一味附和。一个好 AI coworker 需要像好同事：能给诚实反馈，也能在用户觉得任务压倒性时把事情拆开并主动开始。

这解释了为什么 Claude Code/OpenClaw 用户会在意“人格”：当 AI 从聊天工具变成行动代理，语气、道歉、反馈、鼓励和边界都会影响人是否愿意把真实工作交给它。非直觉推断：character 不是品牌层，而是 delegation layer；你是否信任它，部分取决于它犯错时像不像一个可靠同事。

## Cowork 的价值在于把知识工作里的“上下文合成”外包出去
Cat 对 Cowork 的用法很具体：先连接 Google Calendar、Slack、Gmail、Drive 等数据源，让它能拿到足够上下文；然后让它做非代码输出，比如会议材料、客户 brief、slide deck、launch plan。她举的例子是 Code with Claude conference：Cowork 读取 PMM 草稿、过往 deck、Twitter、launch room、内部 demo channel，产出一个接近 Anthropic 设计系统的 20 页 deck 初稿。

但她也强调，人类仍要决定最终叙事、取舍和 demo。Cowork 可以生成很多可能性，PM 的工作是判断哪个 outline、哪个 narrative、哪个 demo 最能服务目标。这和整期主线一致：AI 放大的是执行与合成，人类保留的是目标设定、审美判断、利益相关者 common sense 和最终责任。

## 自动化必须做到接近 100%，否则只是另一种认知负债
结尾给普通从业者的建议很硬：不要只玩 prototype，要把 AI 用在每天真实会用的 app/workflow 上；也不要满足于 90-95% 准确率的自动化。Cat 说，如果一个自动化不能稳定工作，它就不是真正的自动化；最后 5-10% 很花时间，但那才是能让你放心依赖它的部分。

这对 Max 特别有用：AI leverage 不来自“我搭了很多 workflow”，而来自某个重复任务真的被移出生活。她也提醒另一端的陷阱：有些人沉迷 setup、skills、MCP、prompt 和工作流优化，最后忘了自己原本要 build 什么。简单 setup 往往更好；真正的标准是它有没有让你每天多完成真实任务。

## 收束行
这期最锋利的边缘感是：未来最强的产品人，可能不是最会管理流程的人，而是最能在混乱模型边界、组织约束和用户真实痛苦之间，快速做出可执行判断的人。
