---
title: "Krishna Rao - Anthropic's CFO on Compute, Scaling to $30B ARR, and the Returns to Frontier Intelligence - [Invest Like the Best, EP.471]"
date: 2026-05-14T08:01:36Z
category: reading
description: "Krishna Rao 是 Anthropic 的 CFO，加入约两年，负责资本形成、compute 采购与配置、财务团队运营等核心问题。他的位置特殊：既要向投资人解释 Anthropic 为什么需要巨额资本，也要在公司内部把 compute 当作最稀缺、最高杠杆的资源来管理。"
source: "https://colossus.com/episode/cone-of-uncertainty/"
---

## 嘉宾背景
Krishna Rao 是 Anthropic 的 CFO，加入约两年，负责资本形成、compute 采购与配置、财务团队运营等核心问题。他的位置特殊：既要向投资人解释 Anthropic 为什么需要巨额资本，也要在公司内部把 compute 当作最稀缺、最高杠杆的资源来管理。

## TL;DR
这场访谈最核心的线索不是“Anthropic 增长很快”，而是：frontier AI 公司正在把 compute 变成一种可在训练、内部研发、客户推理之间动态调度的资本资产。传统软件公司把算力看成边际成本，Rao 的框架则是“整包 compute 的 ROI”：今天服务客户、明天提升模型、内部加速产品开发，本质上都是同一套资本配置问题。Anthropic 的关键赌注是：只要 frontier intelligence 的回报继续上升，买算力、提高效率、释放新模型、新产品、解锁更多企业需求，会形成一个自我强化循环。

## Compute 不是成本项，而是 Anthropic 的生产画布
Rao 把 compute 称为公司业务的 lifeblood 和 canvas：买太多会烧穿资本，买太少会失去客户、掉出 frontier，同样可能失败。难点在于 compute 无法临时补货；一个 gigawatt 级别的决策必须提前规划，而收入、模型能力、客户采用又都处在指数变化中。

因此 Anthropic 用“cone of uncertainty”管理未来 1-2 年的情景区间：不是押一个点预测，而是看需求、frontier 研发、内部使用、客户服务在不同增长路径下会如何变化。Rao 说自己现在仍有 30-40% 时间花在 compute 上，说明这不是财务后台问题，而是公司战略核心。

非直觉处在于：compute 的价值不只取决于买多少，还取决于能否快速把同一批资源在不同用途间切换。如果今天上午用于 inference，下午晚上用于 model development，它就不再像传统软件的“服务器成本”，而更像一组可重配置的资本设备。

## 三类芯片的可替代性，是 Anthropic 的抗脆弱来源
Anthropic 同时使用 Amazon Trainium、Google TPU、NVIDIA GPU，并长期投入让三类平台在模型开发、内部使用、客户服务之间尽可能 fungible。Rao 认为这使 Anthropic 可能是 frontier labs 中最高效的 compute 使用者之一。

这不是简单采购多供应商，而是从芯片层、compiler、orchestration layer 到 workload 分配都做了深度工程化。Anthropic 还和 Amazon Annapurna Labs 等团队协作，影响芯片路线图，因为他们的 workload 会把硬件推到极限。

这带来的战略含义是：当外部市场出现短期 compute 机会，Anthropic 更可能迅速吸收；一两年前，异构算力突然增加还很难快速利用，现在 Rao 认为几乎任何类型的 compute 都能被较快部署到训练、内部或客户需求中。

## Frontier intelligence 的回报仍在上升，尤其在企业场景
Rao 反复强调：Anthropic 认为 frontier intelligence 的 returns 仍然很高，尤其是 enterprise。原因不是简单 IQ 分数变高，而是模型能力是多维的：长任务能力、工具使用、computer use、agentic task 速度、可靠性，都会打开之前无法成立的新用例。

他给出的商业证据很直接：Anthropic 年初 run-rate revenue 约 90 亿美元，一个季度后超过 300 亿美元；这类跃迁来自模型能力跃升与围绕模型构建的产品。企业客户不像消费者只是“感觉更聪明”，而是把更强模型替换进真实 workflow，扩大 token 使用和承诺规模。

这解释了为什么 Anthropic 不愿降低 model development 的 compute 底线。即使短期客户服务更紧张，也必须持续投资 frontier，因为下一个模型能力跃迁可能解锁新的 TAM。

## 递归自我改进已经在研发与产品中出现，但人才仍是方向盘
Rao 说 Anthropic 内部 90%+ 的代码由 Claude Code 写，Claude Code 的很多代码也由 Claude Code 生成。这是他们愿意把 compute 分配给内部使用的原因：模型本身正在帮助公司构建下一代模型和产品。

但他没有把未来描述成“人才消失”。Anthropic 仍是 research lab，研究人才负责设定方向、提出问题、探索新发现；模型提升的是 talent density 的杠杆，而不是替代判断本身。公司的目标是聚集最高密度的 AI research 和 inference engineering 人才，再用最强模型放大他们。

这个观点对组织设计很重要：如果 AI 把优秀人才的产出大幅放大，公司需要的不是更大的人海，而是更高密度、更能和 agent 协作的人。

## 定价不是尽量涨价，而是让 Jevons paradox 发生
面对 compute 约束，直觉上可以大幅涨价；Rao 的回答相反。Anthropic 的 Haiku、Sonnet、Opus 定价相对稳定，最大的调整反而是 Opus 4.5 发布时降低 Opus 家族价格，因为客户常把 Opus 级问题塞进 Sonnet，导致高能力模型被低用。

降价后，Opus 使用量增长远超价格下降带来的损失，形成类似 Jevons paradox：单位成本下降，需求被释放，总消费上升。Anthropic 的目标不是榨取单次 token 价格，而是让企业把 frontier intelligence 更深地嵌入 workflow。

Rao 也反对把 margin 简化成“每个客户推理的边际成本”。在 Anthropic 看来，compute 支持的是整个收入曲线：今天的 inference、六个月后的模型能力、内部产品加速、效率突破，都应放在同一 compute envelope 里看 ROI。

## Anthropic 主要做平台，但会在模型领先处亲自做应用示范
Rao 把 Anthropic 的主战略类比早期 AWS：大部分价值来自平台，让客户在其上构建更多应用。平台不只是 raw model access，还包括 prompt caching、VM、Claude Code、managed agents、SDK 等访问智能的“向量”。

但 Anthropic 也会做自己的应用，条件主要有两类：一是他们对模型能力演进有独特视野，可以提前构建，例如 Claude Code；二是他们想向市场展示平台如何组合，例如金融、生命科学、安全等垂直方案。

这会让生态伙伴既受益又紧张。Rao 的回应是：模型能力发展速度太快，连 Anthropic 自己都会被新能力惊讶；他们会通过早期访问、合作伙伴式发布、生态共建来降低冲突，但“平台方也会做应用”的张力不会消失。

## Anthropic 内部财务团队是企业 AI 落地的样板间
Rao 描述的 finance team 用法很具体：法定财务报表可由 Claude 生成，人类审核；AntStats 平台能实时解释业务数据变化；团队有 70+ finance-specific Claude skills；monthly financial review 已可生成 90-95% ready 的版本。

关键变化不是“报表更快”，而是讨论焦点从“发生了什么、数字如何 tie out”转向“该做什么、资源如何动态分配”。每周报告从数小时降到约 30 分钟，信息生产速度变成战略反应速度。

有意思的是，最大 token 用户不是最年轻的工程背景员工，而包括 tax 负责人等资深角色。这说明企业 AI 采用不只是年轻人 vibe coding，而是专家把自己的工作拆成可被 Claude 放大的技能库和流程。

## 投资人最难理解的，是 compute 的可重配置性
Rao 说投资人最常卡住的点，是把 compute 当成传统软件的 variable cost，或者把 R&D 和 COGS 分开看。但 Anthropic 的 compute 可以在一天内跨用途重分配：上午推理，下午研发；服务客户和提高模型能力相互强化。

如果他站在投资人位置，会问三类问题：一是全口径 compute ROI 如何、何时体现；二是客户自身是否真实获得 ROI，还是仍在试点；三是未来 compute 从哪里来、供应结构如何变化。Anthropic 用高 NDR、Fortune 10 客户、大额 commit、三云和三芯片平台来回答这些问题。

这套叙事也解释了为什么 Anthropic 能持续融资。Rao 说加入以来公司已融资 750 亿美元，Amazon 和 Google 交易未来还会带来 500 亿美元；融资原因不是填补当前亏损，而是为了覆盖 cone of uncertainty 上沿的增长和算力需求。

## 安全不是品牌姿态，而是企业信任与模型能力的一部分
Rao 把 AI safety、interpretability、alignment 和商业结果连在一起。Anthropic 投入 interpretability 是为了理解模型内部，像给神经网络做 MRI；alignment 是为了让模型更稳定地按指令行事。这些首先服务使命，但也让企业客户更愿意把敏感 workflow、数据和员工交互放到 Claude 上。

Mythos 的发布是例子：它不只是 cyber model，但 cyber 能力显著突出，能把过去模型找到的 22 个漏洞扩展到 250 个。Anthropic 没有选择不发布，而是采用 phased release，让能力先用于防御性用途，再逐步扩大。

Rao 对监管的态度也不是单纯反对。他强调美国优先、民主国家合作、创新速度与责任框架之间的平衡。Anthropic 需要政府关系，因为这类模型的影响已经超出普通商业产品。

## 文化上，Anthropic 追求“高密度人才 + 高透明度 + 低政治性”
Rao 认为 Anthropic 的文化优势来自几件事：七位联合创始人仍在公司；culture interview 不是形式；公司不容忍山头、抢功和 sharp elbows；内部强调“competitors are capable and success is far from guaranteed”。

Dario 每两周会写短文并回答员工真实问题；内部有严肃辩论，但决策后强对齐。compute allocation 这样的资源冲突也必须在开放讨论后形成一致，而不是靠政治博弈。

这套文化也解释了 Anthropic 在人才争夺中的韧性。面对 Meta 等高薪挖人，Rao 说他们只流失了很少的人，因为研究者更在意影响力、人才密度、协作质量和使命可信度。

## 下一阶段的 frontier 是“企业虚拟协作者”
Rao 对未来的描述不是更强 chatbot，而是 virtual collaborator：有组织上下文、能使用公司内部工具、有 memory、能从自己和人的错误中学习、能围绕一个 idea 长时间工作。它不是单任务助手，而像组织中的持续协作体。

Claude Code 是先行样本，Cowork 则把这种形态推向更广泛知识工作。Rao 说 Cowork 在同时间点上的增长快于 Claude Code，这很重要：开发者通常是最快采用者，如果通用知识工作产品增长更快，说明模型能力和产品形态正在触达更大的劳动池。

最终指向的是全球约 40 万亿美元知识工作的生产率改写。真正难的不是模型“聪明”，而是把智能放进正确 form factor，让它理解具体组织、工具链和工作节奏。

## 低端情景仍可能发生：扩散放缓、 scaling laws 放缓、失去 frontier
Rao 没有把高增长当必然。他列出三个可能把公司推向 cone 下沿的风险：第一，企业组织中的采用扩散撞墙，模型能力已有但人和流程跟不上；第二，scaling laws 放缓，虽然 Anthropic 当前没有看到；第三，Anthropic 无法持续站在 agentic AI frontier。

这三个风险都很关键：一个是需求吸收问题，一个是技术供给问题，一个是竞争位置问题。它们也对应 Anthropic 当前最重的投入：产品化与 go-to-market、frontier research、compute 与人才资本。

## 收束行
这场访谈最值得带走的不是 Anthropic 有多大，而是 frontier AI 正在形成一种新型资本配置逻辑：最稀缺资产不是现金、代码或人头，而是能被高密度人才和模型递归放大的 compute。
