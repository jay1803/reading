---
title: "Quests, token leaderboards, and a skills marketplace: The elite AI adoption playbook | John Kim (Sendbird)"
date: 2026-05-07T08:02:46Z
category: reading
description: "John Kim 是 Sendbird / Delight.ai 的创始人兼 CEO，正在把公司改造成“AI-first company”：AI 不只是员工工具，而被当作劳动力、内部软件生产力和组织学习系统的一部分。对话由 Claire Vo 主持，核心围绕 Sendbird 如何用内部平台、任务机制、技能市场和..."
source: "https://www.lennysnewsletter.com/p/quests-token-leaderboards-and-a-skills"
---

## 嘉宾背景
John Kim 是 Sendbird / Delight.ai 的创始人兼 CEO，正在把公司改造成“AI-first company”：AI 不只是员工工具，而被当作劳动力、内部软件生产力和组织学习系统的一部分。对话由 Claire Vo 主持，核心围绕 Sendbird 如何用内部平台、任务机制、技能市场和 token 仪表盘推动全公司 AI 采用。

## TL;DR
这场对话最有价值的一点：AI 采用不是靠培训、口号或采购工具完成，而是要像做产品一样设计一套内部操作系统。Sendbird 把需求发现、工具构建、安全上生产、激励、展示、度量和领导示范连成闭环，让非工程团队也能安全地产生内部软件；真正被放大的不是“效率”，而是组织里原本被排期、权限和工程资源压住的创造力。

## AI 采用要产品化，而不是培训化
Sendbird 建了内部 Automators 平台，任何员工都能提出一个“quest”：例如财务想自动化 AR/AP，销售想做客户查询，招聘想自动化流程。quest 不是普通工单，而是一个内部 AI 需求市场：有提出者、协作者、预估节省时间、风险等级、受益团队、交付物和演示记录。

这个机制绕开传统 roadmap 的拥堵。以前一个跨职能小工具必须进入 sprint、争夺工程资源；现在员工可以把内部痛点直接暴露给公司里的 AI builder、人类工程师，甚至 AI agent。John 提到新版本里 AI 能读 quest specification、生成 PRD 并开始写代码，这让“内部需求 → 可运行工具”的路径更短。

非直觉点：这里的关键不是“每个人都学会写代码”，而是把组织里的小痛点、小创意、小空档时间做成可流动的市场。AI adoption 因此从培训项目变成了产品化的供需匹配系统。

## 非工程团队变成内部软件团队，前提是先铺好安全生产路径
最直观的例子是 marketing team 在没有工程支持的情况下，用一两天做出一个带 Stripe 支付的 swag store，还包含活动入口和 Konami Code 彩蛋。Claire 的判断很准确：过去这种“有趣但不一定值得排期”的东西很难进入产品路线图；AI 让 fun 的边际成本下降，所以团队可以做更有野心、更贴近文化的客户触点。

Sendbird 没有放任员工把 vibe-coded 小工具随便丢到 Vercel/Netlify，而是预先做了安全模板：认证、环境、基础设施、合规、数据访问都封装好，业务团队只需要在模板上构建。这背后还有一个 “AI Engineer for Internal Operations” 团队，直接向 CEO 和 chief of staff 汇报，并与 CTO、工程、InfoSec 每周协作，清理权限、合规、日志、工具栈等阻塞。

这个设计的核心是：既承认员工一定会自己做工具，也承认公司必须给他们一条“安全上生产”的默认路径。否则 AI adoption 会变成影子 IT 和安全债。

## 技能市场让经验复用，而不是让每个团队重复造轮子
Sendbird 还做了 company-wide skills marketplace。员工可以上传 plugin 或单个 skill，例如 sales team 的 MEDDIC / MEDPIC advisor、设计技能、招聘技能等；其他人能下载并嵌入自己的工具或工作流。

这个市场解决的是第二阶段问题：当每个团队都开始构建内部工具，重复建设和知识孤岛会迅速出现。skills marketplace 把“某个职能怎么判断、怎么写、怎么卖、怎么设计”的隐性经验编码成可复用模块，形成跨团队共演化。

采用过程是 top-down + bottom-up 混合：CEO、CTO 和高管会推动，也会做一对一提醒；但真正扩散来自好奇的人在 Slack、周三 all-hands、同伴演示里看到别人做出漂亮结果，然后主动学习。

## Token 仪表盘的作用是辅导，不是绩效审判
Sendbird 跟踪公司、团队和个人层面的 AI token usage，并按层级标记使用阶段，包括 beginner、intermediate、expert、architect / catalyst，以及每天 1 亿 token 以上的 “AI god”。John 强调这不是绩效考核，而是管理者判断团队 AI 熟练度、决定如何 enable 的工具。

他们关心的不只是总 token 数，而是曲线是否平滑。John 的解释是：如果周末、休假或离线时 token 使用断崖式下降，说明 AI 还没有成为持续运转的伙伴；更平滑的曲线意味着公司开始让 AI 在人的空档里继续工作。

领导示范是强信号：公司 CTO、co-founder / chief architect 和业务高管本身就是高 token 消费者。John 自己平均每天约 3000-5000 万 token，峰值约 2 亿；工具偏好上大约 80% Claude Code、20% Codex，同时观察到 Codex 在公司里的占比快速上升。

**证据薄弱处**：token usage 只能衡量“是否在用”，不能直接衡量产出质量、判断力或业务 ROI。Sendbird 的做法成立，是因为它同时配套了 quest 交付、内部演示、工具使用和团队反馈；如果只抄排行榜，很容易退化成新的 vanity metric。

## 人才标准正在从资历转向 curiosity、agency、energy
John 说他们重写了许多 AI-first role 的 job description，降低对年限和传统经验的强调，更重视好奇心、主动性和能量。理由是：AI 把学习和构建的成本降到每月几十到几百美元，愿意深入探索的人能快速补齐知识、做出东西。

他的个人用法也体现这一点：他做了一个叫 Gardener 的开源项目，像每天到知识库里“园艺”一样整理 Obsidian / markdown notes，补人物与公司资料、修正文字、生成标题、聚类和交叉链接；他还用 Claude Code / Codex 为自己生成 neuroscience、quantum mechanics、fusion、startup research 等离线学习中心。

这部分的边缘启发是：AI 不只是工作自动化工具，也可能是个人学习环境生成器。John 和 Claire 都强调，AI 让人能把抽象兴趣变成定制化教材、图谱和练习场，而不是被现成网站、课程和书的形态限制。

## 组织复制这个模式，先找冠军而不是先写制度
John 给 CEO 的建议很明确：每个组织里已经有人在好奇、尝试、自己做东西。先找到这些人，给 spotlight，让他们展示有趣成果，允许他们 fail forward，再围绕他们制造能量。创新不是从纯理论结构开始，而是从有故事、有能量的人开始。

但这不能只靠 grassroots。领导层必须真实使用 AI，并用自己的行为告诉组织“这件事重要”。如果领导自己不能说出过去 30 天的 token usage，Claire 认为就是危险信号；John 的公司则反过来，用高管高频使用来降低组织怀疑。

## 收束
Sendbird 的案例最值得学的不是 Automators、排行榜或 skills marketplace 的某个功能，而是它把 AI 采用设计成了一套组织内的“创作许可系统”：让更多人有权提出需求、构建工具、复用技能、展示成果，同时让公司仍然看得见风险和产出。
