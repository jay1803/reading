---
title: "Dylan Patel - The Infinite Demand for Tokens, Claude Mythos, and Supply Constraints - [Invest Like the Best, EP.468]"
date: 2026-04-24T08:01:56Z
category: reading
description: "Dylan Patel 是 SemiAnalysis 创始人兼 CEO，长期跟踪半导体供应链、AI 基础设施建设和 token economics。这期是他第二次做客 Patrick O'Shaughnessy 的 Invest Like the Best，主题从 SemiAnalysis 自身的 AI 使用爆发..."
source: "https://colossus.com/episode/supply-demand-of-tokens/"
---

## 嘉宾背景
Dylan Patel 是 SemiAnalysis 创始人兼 CEO，长期跟踪半导体供应链、AI 基础设施建设和 token economics。这期是他第二次做客 Patrick O'Shaughnessy 的 Invest Like the Best，主题从 SemiAnalysis 自身的 AI 使用爆发，延伸到 frontier tokens 的需求、供给瓶颈、模型访问权与 AI 行业的社会叙事风险。

## TL;DR
这期最核心的一条线是：AI 竞争正在从“谁会写软件”转向“谁能拿到最强 tokens、把它们指向最高价值任务，并捕获由此产生的经济价值”。Dylan 的判断很激进：frontier model 的需求不是线性增长，而是被 implementation cost 崩塌后释放出的近乎无上限需求；同时供给侧从 GPU、HBM/DRAM、TSMC、设备、铜箔到 CPU 都被拉紧，导致 token 访问权本身可能变成新的稀缺生产资料。

## Token spend 正在从工具费变成生产资本
SemiAnalysis 去年 AI 支出还只是数万美元量级，今年 Claude/Anthropic 使用已经跑到约 700 万美元年化，相当于薪酬支出的 25% 以上；如果趋势继续，年底可能接近甚至超过薪酬支出。Dylan 并不把这看成 SaaS 成本失控，而看成一种生产资本再配置：少招人、更多买 tokens、用同一团队做出过去需要大型团队才能做的事。

他给的例子很具体：逆向工程实验室用几千美元 Claude tokens 做出芯片显微图像材料识别工具，过去像是 Intel 一个团队要维护的系统；经济学家独自拉取 Fed、就业、BLS task taxonomy 等数据，构建“phantom GDP”分析和 2000 个 eval；能源团队三周内抓取美国电厂、输电线和需求源，做出接近甚至局部优于传统能源数据公司的地图与 dashboard。非直觉点是：这些不是“写代码更快”这么简单，而是原本不值得立项或需要大团队的业务线，突然变成单人 + tokens 可试错的机会。

## 最强模型才有经济价值，旧能力降价并不会降低需求
Dylan 反复强调，用户不是想要“便宜的 GPT-4 级能力”，而是想要 frontier model，因为只有 frontier model 能打开新的高价值任务。旧能力层级会快速降价，可能一年内同等质量便宜 100 倍，但这不重要；真正的需求会迁移到更强模型上，因为更强模型能做此前不能做的事。

这解释了他为什么把 enterprise contract、rate limit 和早期模型访问视为战略变量。Anthropic 若拥有更强的 Mythos/Opus 级模型，即使单 token 贵 5-10 倍，也可能因任务完成效率更高而在 task level 更便宜。最稀缺的不是 API endpoint，而是“足够聪明、足够多、足够早”的 tokens。谁能把这些 tokens 指向高价值任务，谁就在做 token arbitrage；谁只能用落后一代模型，可能连竞争资格都没有。

## 当 implementation 变便宜，稀缺性转向 idea selection、资本和价值捕获
Dylan 对 Mythos 感到“有点害怕”的原因，不只是模型更强，而是 release cadence 和 implementation cadence 都在压缩。他认为 Anthropic 的目标从 L4 软件工程师能力跳到近似 L6 的速度，说明模型进步正在反过来加速模型研发本身：想法仍然便宜，但实现想法突然变得极快、极贵、极可规模化。

于是人的关键能力被重排：不再是亲手执行，而是选择哪个想法值得烧 tokens、如何销售/分发产出、如何拿到资本和模型访问权、如何捕获创造出的价值。他把问题拆成三层：使用更多 tokens、用 tokens 生成真实经济价值、捕获那部分价值。只想用 AI 把 8 小时工作压成 1 小时，是“无聊方式”；更强的方式是继续工作 8 小时，做出过去数倍的产出并把收益拿回来。

## Token 访问权可能加剧资源集中，而不是天然民主化
对话里最有边缘感的部分，是 Dylan 对“模型访问不再广泛开放”的判断。AI 公司口头上说要让人人获得强 AI，但最强模型极其昂贵，也有蒸馏和安全风险，因此更可能先给少数高价值客户、银行、网络安全场景或超大企业使用。若某个金融机构能承诺购买最早一批数十亿美元 tokens，它就可能在市场、研究、交易或安全领域获得结构性优势。

这意味着 token economy 未必自动扩散财富，反而可能把优势聚集到能支付、能谈判、能组织高价值用例的公司手里。Dylan 的“permanent underclass”说法虽然夸张，但抓住了一个真实风险：如果最强 tokens 的边际价值远高于价格，而供应长期不足，模型访问权就会像资本、能源、算力和渠道一样，成为分层机制。

## 供给侧不是单一 GPU 短缺，而是整条 AI 供应链重定价
Dylan 对供应侧的判断是：任何“有脉搏且卖光”的环节都会涨价、拿预付款或提高 ROIC。GPU 的有用寿命被拉长，H100/A100 集群续约年限上升，云层和硬件层毛利扩张；Nvidia 仍能维持极高毛利，内存厂商则因 DRAM/HBM 供给紧张享受更剧烈的价格弹性。

他尤其强调内存不是“故事已经被市场充分理解”，而是可能还会从当前价格再翻倍甚至三倍。原因是新增产能低双位数增长，真正大规模增量要到 2027 年末或 2028 年；在此之前只能靠价格摧毁其他需求，把产能从别处挤出来。Logic 侧 TSMC 也很紧，但提价更克制；更上游的 ASML、Lam、Applied Materials、Carl Zeiss、铜箔、玻纤、PCB、激光器等环节会被 TSMC 未来可能接近 1000 亿美元级 CapEx 的尾鞭效应放大。

## AI 需求还会外溢到 CPU、ASIC 和物理世界
Dylan 不把需求局限在 GPU 推理。ASIC 会增长，FPGA、CPU 等“配角”也会被 AI rack、强化学习环境和 AI 生成应用拉动。强化学习里的环境、评分器、仿真、文件操作、CAD/物理模拟等很多环节运行在 CPU 上；AI 生成的 app、dashboard、脚本和服务最终也要部署在 CPU/云实例上。因此，AI token boom 会制造一串二阶计算需求。

机器人是另一个潜在需求曲线。他认为所谓“software-only singularity”不会停在软件里，因为一旦软件实现成本足够低，机器人控制、微控制器、执行器、动作学习和任务软件也会被更快迭代。当前 VLA/robot model 可能不是最终路线，但未来 6-18 个月可能出现 few-shot robot learning 的突破：买/租一个机器人，示范几次，它就能学会很窄但可商业化的任务。这会把 token demand 从数字劳动继续推向物理劳动。

## 最大未知数不是供给，而是 token 创造了多少“phantom GDP”
Dylan 认为供给侧相对更可建模，真正难的是需求侧的价值扩散：谁在用 tokens、用来做什么、创造了多少经济价值、这些价值如何进入或不进入 GDP 统计。SemiAnalysis 用 tokens 产出的更好信息，可能帮助客户做出远超订阅价格的投资或战略决策，但这部分价值很难被 GDP 捕捉；成本下降甚至可能让名义 GDP 看起来变小，却让真实产出上升。

这也是“phantom GDP”的核心：AI 可能同时制造更高产出、更低价格、更难测量的经济价值。若统计系统只看到软件/信息服务价格下降，却看不到决策质量、速度和新业务线的复利，就会低估 AI 的实际影响。

## AI 行业的社会叙事风险正在变成硬约束
结尾 Dylan 预测未来几个月可能出现大规模反 AI 抗议。他认为普通人对 AI 公司缺少连接感，只看到少数技术公司、数据中心、能源消耗、失业威胁和“改变世界”的宏大叙事；Sam Altman、Dario Amodei 这类领导者频繁上访谈，却未必让普通人更信任 AI，反而可能强化“神秘小圈子要重写社会”的感受。

他的建议很直接：AI 公司应该少谈未来能力如何颠覆世界，多展示当下 AI 如何改善生活；少制造恐惧，多建立普通人与 AI 工作者、AI 应用之间的具体连接。否则，能力越强、收入越快、资源越集中，社会反弹越可能从情绪问题变成政治和监管约束。

## 收束行
这期真正值得跟踪的不是某家模型公司的 ARR，而是“最强智能的分配机制”：谁最早拿到、谁买得起、谁知道怎么用、谁能捕获收益，以及供给链和社会系统能否承受这种新生产资料的突然稀缺化。
