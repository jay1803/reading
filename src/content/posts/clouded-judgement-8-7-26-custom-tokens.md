---
title: "Clouded Judgement 8.7.26 - Custom Tokens"
date: 2026-09-10T16:34:15Z
category: reading
description: "定制化开源权重模型是一套持续运转的训练、数据、评测、部署与升级系统，而非一次性获得更便宜、更专业推理能力的捷径。"
source: "https://cloudedjudgement.substack.com/p/clouded-judgement-8726-custom-tokens"
---

定制化开源权重模型会形成一个庞大市场，但它真正出售的是一套持续运转的训练、数据、评测、部署和升级系统，绝非把企业数据塞进模型后便能一次性获得更便宜、更专业的推理能力。

模型与 token 市场将同时容纳三类供给：OpenAI、Anthropic 等大型实验室提供的 **frontier tokens**，DeepSeek、Moonshot 等模型产生的通用 **open-weight tokens**，以及经过 RL 或 SFT 定制的 **customized open-weight tokens**。三者确实会争夺份额，但当前市场总量的扩张速度远高于彼此蚕食份额的速度，因此各类供给都能维持增长；只有当市场成熟后，份额才会趋于稳定，而在此之前，超高速增长可能持续得比多数人预期更久。

企业定制模型主要有三条路径。Custom pre-training 是从头使用自有数据训练模型，投入最重；SFT（Supervised Fine-Tuning）向模型提供"prompt + 理想 response"的示例，让它学习模仿；RL（reinforcement learning）则让模型反复尝试任务，用评分结果指导学习。多数企业采用后两种方法，因为从头训练所需的资本、算力和人才门槛过高，但 SFT 和 RL 本身仍依赖三个紧密耦合的支柱：训练基础设施、训练数据与 evals。

训练基础设施需要编排 GPU、跨设备切分模型、管理 RL sampling loops、维持高 GPU 利用率，并在每轮训练后把更新的模型权重从 trainer 传给 sampler，属于高度复杂的分布式系统工程；Thinking Machines 的 Tinker 试图把这些工作封装起来。数据侧的困难则在于企业拥有的客服记录、agent traces 和日志都无法直接用于训练，必须先清洗、转换并判断哪些样本代表"好结果"。SFT 通常能把数据整理为 JSON，但格式转换只是较简单的一环，决定保留什么、剔除什么才是核心工作；RL 更依赖为具体任务搭建 environment 和 reward function，缺少统一格式，也更难做成标准产品。Applied Compute、Trajectory 帮助企业处理这类工作，Handshake、Mercor、Micro1 则负责获取并交付 training-ready data，但每家企业的数据都有独特的混乱方式，使数据准备天然带有服务属性。

Evals 决定定制模型是否真正胜任目标工作流；在 RL 中，eval 还直接进入训练循环，作为 reward function 对每次尝试评分。横跨基础设施、数据和 evals 的是 **training recipe**：它规定采用 SFT、GRPO、PPO、DAPO，还是先 SFT 再 RL；选择哪个 base model；怎样设计 reward function；以及如何设定 learning rate、batch size 等 hyperparameters。市场目前有许多分别解决单个支柱的产品与服务，却缺少把整个流程连成一体的平台，因为 recipe 必须适应每家公司的数据、任务和质量标准，难以彻底标准化。

即使模型训练成功，生产部署仍是独立难题。许多训练平台尚不具备生产级 inference 能力；Tinker 的 sampling API 更适合测试，难以承载规模化流量。企业可以基于 vLLM 自建 inference stack，但工程复杂度很高，因此绝大多数会把模型交给 Baseten 或 Fireworks 托管，而这两家公司也在向 RL 和 SFT 环节延伸。定制模型通常保留 base model 的架构，所以 inference cloud 已为通用开源模型开发的优化可以继续复用，技术部署相对顺畅，真正的代价集中在经济性上。

托管平台运行通用开源模型时，可以让数千名客户共享同一批 GPU，以高利用率摊薄每个 token 的成本；企业专属模型缺少这种 multi-tenant 效应，往往需要 dedicated GPUs，闲置算力也由单一客户承担。这使定制模型最适合高吞吐、重复性强且任务边界清晰的场景：模型能够持续运行，较低的单位推理成本与专业化效果才足以覆盖专属容量和工程服务的费用。低频、需求波动大或任务类型分散的企业，更容易发现直接购买 frontier tokens 反而更经济。

部署之后还存在两个并行的升级周期。第一个来自企业自身：产品、客户需求和业务流程持续变化，几个月前训练的模型很快就会过时，因此数据收集、重训、重新评测和重新部署都必须反复执行，定制化带来的是经常性成本与经常性复杂度。第二个来自 base models：Kimi K3、GLM 5.2、DeepSeek v4 Flash 等更强的开源模型不断出现，企业刚完成一轮定制，就可能需要迁移到新的基础模型并重做整套流程。frontier labs 因而可以提出一个有力反问：既然定制工作必须持续重来，企业为何不直接购买持续升级的 frontier tokens？

这一复杂链条也解释了为什么参与者正从不同入口争夺平台位置：Baseten、Fireworks、Together 从 inference cloud 向训练延伸，Thinking Machines 从训练基础设施切入，Applied Compute 和 Trajectory 聚焦 RL，Handshake、Mercor、Micro1 从数据供给进入，CoreWeave 等 neoclouds 提供算力，Braintrust 与 Vals.ai 则从 evals 出发。最终胜出的巨型平台，很可能是能把这些割裂环节组合成可重复运行的生命周期系统，同时降低专属模型的闲置成本与升级摩擦的公司。

同期公开 SaaS 估值数据显示，整体 EV／NTM revenue 中位数为 4.1 倍，Top 5 中位数达到 31.8 倍，10 年期利率为 4.7%。按预期 NTM 增长率划分，增长超过 22% 的高增长公司中位估值为 19.3 倍，增长 15%—22% 的公司为 5.8 倍，低于 15% 的公司仅为 3.5 倍；22% 的分界线是为了让高增长组保留约十家公司，带有明确的样本构造因素。文章还用 EV／NTM revenue 除以 NTM growth 衡量相对增长的估值，例如一家以 20 倍 NTM revenue 交易、预期增长 100% 的公司，该指标为 0.2 倍；EV／NTM FCF 的统计只纳入倍数大于 0 且低于 100 的公司，负 NTM FCF 企业被排除。

这批 SaaS 公司的中位运营指标为：NTM 增长率 12%，LTM 增长率 16%，gross margin 76%，operating margin 3%，FCF margin 21%，net retention 110%，CAC payback 35 个月，销售与营销、研发、一般行政费用分别占收入的 34%、22% 和 13%。Rule of 40 由收入增长率与 FCF margin 相加，FCF 按经营现金流减资本开支计算；GM-adjusted payback 使用"上一季度销售与营销费用 ÷ 当季新增 ARR × gross margin × 12"的口径，其中 ARR 通常由季度订阅收入乘以四推算。由于不少上市公司不披露订阅收入，相关企业只能标记为 NA，这也限制了横向比较的完整性。

定制 token 市场的长期价值取决于能否把高度 bespoke 的模型工程转化为持续、经济且可升级的运营体系；当训练 recipe、生产 inference 和双重升级周期被真正贯通后，定制模型才可能从少数高流量任务的工程项目扩展为与 frontier tokens、通用 open-weight tokens 并立的基础市场。
