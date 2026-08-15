---
title: "Anthropic's CFO on How It Buys and Allocates Computes | Invest Like The Best"
date: 2026-05-15T08:01:24Z
category: reading
description: "Krishna Rao 是 Anthropic CFO，加入时公司 run-rate revenue 约 2.5 亿美元；两年后对话中提到已到约 300 亿美元。他负责在极端不确定性下筹资、采购与分配 compute，并称加入以来已帮助 Anthropic 融资约 750 亿美元，另有 Amazon / Goog..."
source: "https://newsletters.feedbinusercontent.com/31b/31b8069587db0a36d6fa77add5f4ce71e336a007.html"
---

## 嘉宾背景
Krishna Rao 是 Anthropic CFO，加入时公司 run-rate revenue 约 2.5 亿美元；两年后对话中提到已到约 300 亿美元。他负责在极端不确定性下筹资、采购与分配 compute，并称加入以来已帮助 Anthropic 融资约 750 亿美元，另有 Amazon / Google 相关未来承诺资金约 500 亿美元。

## TL;DR
Anthropic 的核心资产不只是“更聪明的模型”，而是把 compute 当成一种可动态调度的资本：同一批算力可在训练、内部加速、客户推理之间切换，跨 Trainium、TPU、GPU 三个平台使用，并通过模型效率、产品形态、企业信任把前沿能力快速转化成收入。

## 算力采购是指数业务里的资本配置，不是云成本管理
Rao 把 compute 称为 Anthropic 的 lifeblood：买多会烧死，买少则无法服务客户、无法留在 frontier；而 gigawatt 级算力不能临时购买，所以必须提前 1-2 年按“cone of uncertainty”做场景规划。关键不是点预测，而是保留弹性：Anthropic 同时使用 Amazon Trainium、Google TPU、NVIDIA GPU，并把不同代际芯片按最适合的 workload 分配。这个能力不是采购技巧，而是多年投入编译器、编排层、芯片协作后的系统性效率优势。

## Compute 在 Anthropic 内部是可互换资本，因此 ROI 不能按传统软件毛利拆开看
访谈中最反直觉的一点：同一块芯片早上可能做 inference，晚上可能做 model development；训练、内部使用、客户服务并不是三类固定成本，而是在不同时间尺度上共同服务收入。Anthropic 会给 model development 设置不可跌破的 compute floor，因为 frontier intelligence 的回报尤其在 enterprise 极高；内部员工使用模型虽然会占用可服务数十亿美元收入的算力，但它能加速研发、产品、效率优化，形成下一轮收益。

## Frontier intelligence 的回报来自“解锁新 TAM”，不是 benchmark 分数上涨
Rao 明确反对把模型能力理解成单一 IQ 分数。真正重要的是现实任务能力：长时程任务、工具使用、computer use、agentic workflows、速度与可靠性。新模型不仅更强，还经常更便宜地处理 token；因此客户不是简单替换旧模型，而是把以前不可行的工作流变成可行。Anthropic 从年初约 90 亿美元 run-rate revenue 到季度末超过 300 亿美元，Rao 将其归因于模型能力跃迁、产品封装与 go-to-market 的共同作用。

## 定价策略偏向扩大使用，而不是在短缺期榨取最高单价
尽管 compute 稀缺，Rao 不认为应简单大幅涨价。Anthropic 更重视 pricing stability 与客户 ROI：Opus 4.5 发布时反而下调 Opus 家族价格，因为高能力模型被低估使用，降价后 consumption 增长远超价格下降，出现类似 Jevons paradox 的效果。公司衡量的是完整 compute envelope 的回报，而不是单次 inference 的传统毛利；模型开发、内部加速、客户服务都在不同周期支持收入。

## Anthropic 不是纯平台，也会在关键场景做应用来证明模型未来
Rao 将主线定义为 horizontal platform：API、prompt caching、VM、Claude Code、Dispatch、Agents SDK、managed agents 都是让企业接入模型智能的向量。但当 Anthropic 对模型下一步能力有特殊视野时，会自己做应用：Claude Code 是“Claude-led”而非 developer-led 的例子；金融服务、生命科学、安全等 vertical products 则更多是展示平台如何组合出价值。公司试图让生态获得大部分上层价值，同时在能推动 frontier adoption 的地方亲自下场。

## 安全研究在商业上变成企业信任资产
投资者早期质疑“AI safety”和“大生意”是否冲突；Rao 的答案是二者在 enterprise 场景里反而互相强化。Interpretability 像模型 MRI，alignment science 让模型更可靠；这些研究起初服务使命，但也帮助 Anthropic 更好地构建模型，并让九家 Fortune 10 企业愿意把敏感工作流、数据和客户交互交给 Claude。Mythos 的发布方式也体现这种逻辑：该模型在 cyber 能力上显著跃迁，可把一个开源代码库发现漏洞数从 22 提到 250，因此采用 phased release，让防御性用途先扩散。

## 组织文化是 Anthropic 抵抗人才市场和复杂决策的隐性护城河
Rao 描述的文化关键词是 collaborative、humble、rigorous debate、transparent。七位联合创始人仍在公司，culture interview 不是形式；不接受山头主义、sharp elbows、抢功劳。Dario 每两周给全员写短文并接受真实问题，内部在 compute allocation 这种高冲突议题上可以激烈讨论，但决策后保持对齐。Rao 认为这也是 Anthropic 在 Meta 等公司高薪挖人时只流失极少核心人才的原因之一。

## 下一阶段 frontier 是“virtual collaborator”，不是聊天机器人
Rao 认为企业 AI 的下一形态是能理解组织上下文、调用内部工具、拥有记忆、从错误中学习、并跨长时间范围推进想法的 virtual collaborator。Claude Code 已让 Anthropic 内部 90% 以上代码由 Claude Code 编写；finance team 也用 Claude 生成法定财务报表、月度财务 review、每日 revenue / compute utilization 分析，把数小时工作压缩到约 30 分钟。更重要的是，人从“整理发生了什么”转向“讨论应当做什么”。

## 主要下行风险不是单一事件，而是指数曲线被三处打断
Rao 给出的 premortem 很清楚：第一，客户内部扩散速度可能放缓，大企业改变工作方式很难；第二，scaling laws 可能不再按当前轨迹推进，虽然 Anthropic 目前没看到放缓；第三，Anthropic 可能无法持续定义 agentic AI frontier。换句话说，业务高端情景依赖模型能力、客户 adoption、compute execution、组织速度同时成立。

这场访谈最值得留下的边缘感：Anthropic 的 CFO 角色已经不像传统财务负责人，更像在指数时代管理一种新型生产资料的资本配置者。
