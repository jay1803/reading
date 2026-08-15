---
title: "Why cultivating agency matters more than cultivating skills in the AI era | Max Schoening (Head of Product, Notion)"
date: 2026-05-04T08:02:01Z
category: reading
description: "Max Schoening 是 Notion Head of Product；此前做过 Google PM、Heroku 设计负责人、GitHub 设计领导者兼兼职工程师，也是两次创业者。他在 Notion 推动设计师和 PM 用终端、代码和 AI 原型工作，但他的核心观点不是“人人都要变工程师”，而是产品人必须..."
source: "https://www.lennysnewsletter.com/p/why-cultivating-agency-matters-more"
---

## 嘉宾背景
Max Schoening 是 Notion Head of Product；此前做过 Google PM、Heroku 设计负责人、GitHub 设计领导者兼兼职工程师，也是两次创业者。他在 Notion 推动设计师和 PM 用终端、代码和 AI 原型工作，但他的核心观点不是“人人都要变工程师”，而是产品人必须理解自己正在设计的材料。

## TL;DR
这场对话最硬的一条线：AI 没有让技能不重要，而是让“技能不足”不再是主要借口；真正稀缺的变成 agency、taste、对材料的理解，以及把便宜原型收敛成可靠产品的能力。AI 把每个项目最初的 10% 变得几乎免费，探索和试错成本暴跌，但最后的产品质量、系统可靠性、团队判断力和那个“tiny core”反而更难被外包。

## AI 时代的产品人要进入材料内部，而不是只把代码当交付工具
Max 让 Notion 设计师和 PM 写代码，重点不在于让他们把生产代码合进去，而在于让他们用最终产品的材料思考。静态 Figma 聊天界面像 Bret Victor 所说的“dead fish”：你看不到 AI 的反馈、延迟、agent loop 和交互质感。Notion 起初建了一个 LLM-friendly 的小 playground，让非工程角色克服终端恐惧；模型能力变强后，同一批人开始更自然地接触真实代码库。非直觉点是：会改 CSS 的 PM 不如真正理解 agent loop 的 PM，因为未来产品判断越来越发生在代码、上下文、工具调用和反馈循环里。

## Agency 是 AI 放大后真正分化人的变量
过去人们可以说“我不会做，因为我缺某项技能”；现在模型把很多技能放到手边，留下的问题是你是否真的会主动改变环境。Max 用“drive Notion like it’s stolen”形容高 agency：不是等角色定义，而是看见组织需要招聘、原型、策略或实现，就主动把边界扩过去。他认为培养 agency 的入口不是办公室政治式地绕过老板，而是持续 making：做饭、改椅子、写小工具、做 side project。做东西会反复提醒你：世界是由并不比你聪明的人造出来的，因此也可以被你改造。

## “第一个 10% 免费”让 demos-not-memos 变成默认工作法
AI 改变产品流程的关键，不是 PRD 自动化，而是早期探索从文字辩论变成快速可反应的原型。Max 说很多项目的第一个 10% 现在几乎免费；甚至可以同时派 10 个 agent 探索 10 条路线，再挑出值得收敛的方向。这延续了 GitHub 的“demos, not memos”：与其写文档描述想法，不如给团队一个粗糙但可触摸的版本。代价是 token spend、代码行数、feature count 都容易变成虚荣指标；真正该优化的是验证循环、代码审查、可维护性，以及人工干预是否暴露了软件工厂里的 bug。

## 角色融合会增加产能，也会吞掉真正的专业性
Max 反对把“人人都能写代码”理解成专家消失。硬件类比更清楚：3D 打印原型能说明方向，但量产 1 亿台设备需要完全不同的工程能力。软件里的工程专业性对应可靠性、扩展性、权限、安全、回归控制和长期维护；设计专业性对应 delight、craft、材料感和审美判断。当前行业软件数量明显增加，但质量没有同比提升，这说明瓶颈从“能不能做出来”移动到了“能不能做成 obviously good 且 durable 的东西”。

## Malleable software 不是人人重建 SaaS，而是重新拿回计算生活的所有权
Max 对 malleable software 的定义是：软件应更贴近使用者的利益，而不是只服从制造它的公司的利益。他反感现代 app 把 UI、数据和行为焊死在一个方块里；AI 让个人临时做工具变容易，但如果没有协作、权限、安全和平台层，最后只会变成每个人一堆孤立脚本。由此他认为 SaaSpocalypse 被夸大了：用户愿意为 as-a-service 付费，本质上是在买维护、规模化、权限、协作和专家持续打磨。更可能发生的是工具重新泛化，像 90 年代的 word processor、spreadsheet、FileMaker Pro，但仍以服务形态存在。

## Notion 的 AI 优势来自“连接工作空间”这一上下文结构
Max 对 Notion AI agent 的解释不是模型更神奇，而是 agent 需要能 roaming 的上下文。Notion 长期积累的 connected workspace 让权限、文档、数据库、协作记录和企业搜索在同一环境里被 agent 访问；这使 Notion 更像一个 OS，而不只是一个 SaaS app。这里和 malleable software 相连：如果 workspace 本身足够可塑，AI 才能把“替你做事”从单次问答推进到跨资料、跨任务、跨人的工作流。

## Taste 是能在脑中模拟某个 in-group 反应的能力
Max 对 taste 的定义很工程化：给定一个想法，你能否在脑中跑一个 virtual machine，预测某个目标群体会不会喜欢。taste 不是玄学天赋，而是高频 reps、反馈、暴露于好东西、持续 side project 训练出来的模型。优秀设计师通常同时有两个习惯：自己端到端做东西，并且不断试用新工具、吸收别人的解决方案。值得注意的是，他不完全认同“AI 之后只剩 taste 属于人类”，因为 taste 的训练过程本身也像反向传播：输入、反馈、更新权重。

## 伟大产品靠 tiny core，不靠继续堆功能
Max 认为成功产品通常有一个极小但异常强的核心超能力：iPhone 的 multitouch，GitHub 的 pull request，Notion 的 blocks 和 slash command，Heroku 的 `git push heroku master`，Dropbox 菜单栏图标的可靠同步。失败产品常陷入“再加一个功能就好了”的死亡循环；他自己 2014 年做过类 Notion 产品，过度打磨 markdown folding 和编辑体验，却没有找到真正强的核心。结论是：being first 被高估，being right 更重要；AirPods、Anthropic、Notion 都不是单纯靠先发，而是靠把关键核心做对。

## AI 经济学的下一阶段会从“花钱探索”走向 ROI 与模型层分化
Notion 现在倾向于不限制探索性 token spend，因为早期应该鼓励人找到新工作方式；但 Max 判断 6–12 个月后企业会更认真追问 ROI。若 frontier labs 与 open-weight/local models 的差距扩大，权力会集中在少数实验室；若差距不扩大，企业会像云计算时代一样追求多供应商、低锁定、便宜且足够好的模型。更深的判断是：许多知识工作任务可能存在“retina display”式智能饱和点；到达够用后，人们更在乎速度、成本、本地运行和交互形态，而不是永远更聪明的远端神盒。

## 软件会继续吃掉世界，但方式是“工程能力扩散到所有岗位”
Max 不觉得模型在写作、市场、销售等非代码领域的进步像 coding 那样显著；更可能发生的是软件工程本身进入所有职能。HR、运营、产品、设计不再等工程团队排期，而是用 coding-agent-like 的工具把业务流程编码出来。Lenny 提到 Codex 产品负责人也有类似看法：未来赢的 agent 往往是能按需写代码、扩展自己能力的 coding agent。非直觉点是，AI 改造其他行业的主通道可能不是“每个岗位都有一个聊天机器人”，而是每个岗位都多了一层可编程外骨骼。

## 他的工作观不是躺平，而是拒绝“最后一班车”恐慌
Max 半开玩笑说知识工作本身已经像 UBI：很多幸运的人坐在空调房里输入正确的字母就获得很高收入。若 AGI 让他不用工作，他仍会做同样的事：tinker、code、让周围世界更可塑。他担心硅谷越来越多人不是真的爱电脑，而是在“last train / permanent underclass”叙事里恐慌地追逐钱和地位。更稳的路径是降低焦虑振幅、读历史、理解计算机史、持续做东西；在不确定里，agency 比预测未来更可靠。

**值得质疑**
Max 对“模型在非代码领域进步不明显”的判断主要来自产品经验和审美偏好，不是系统性评测；如果多模态、长上下文、行业专用 agent 快速成熟，这个判断可能低估了非代码岗位的改造速度。他对 SaaSpocalypse 的反驳也带有 Notion 视角：服务、权限和维护确实有护城河，但中低端、表单型、薄封装 SaaS 仍可能被通用工作空间和自生成软件明显挤压。

## 收束
这场访谈真正留下的边缘感不是“AI 会让每个人更高效”，而是：当制造能力变得廉价，一个人是否真的爱材料、愿意反复做东西、敢于改造环境，会比他的职位名称更快暴露出来。
