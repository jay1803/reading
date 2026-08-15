---
title: "Where Are All The Data Centers?"
date: 2026-05-13T08:01:53Z
category: reading
description: "AI 数据中心建设的真实瓶颈可能不是“需求太强所以供给紧”，而是市场把“规划、签约、破土、局部投产、实际可营收容量”混成了同一种容量；如果真实投产速度只有每年几百 MW 到约 1GW，而不是每季度数 GW，那么 NVIDIA、hyperscaler、Oracle、OpenAI、Anthropic 这条 AI 资本..."
source: "https://www.wheresyoured.at/where-are-all-the-data-centers/"
---

## TL;DR
AI 数据中心建设的真实瓶颈可能不是“需求太强所以供给紧”，而是市场把“规划、签约、破土、局部投产、实际可营收容量”混成了同一种容量；如果真实投产速度只有每年几百 MW 到约 1GW，而不是每季度数 GW，那么 NVIDIA、hyperscaler、Oracle、OpenAI、Anthropic 这条 AI 资本开支链的收入、折旧、RPO 与融资叙事都会同时失真。

## 核心主张拆解
作者的主张很直接：AI 泡沫里最关键的基础设施叙事——“巨量数据中心已经建好或正在快速投产”——缺少可验证的微观证据。公开报道里大量项目被称为 “operational”，但实际常常只是一个 phase、一栋楼、甚至只是部分设备通电测试；真正完整建成、装满电力/冷却/服务器、并产生收入的容量少得多。

他把问题压缩成两个问题：一个数据中心到底要多久建成？过去两三年到底有多少容量真正上线？他的调查结论是：50MW 以上的数据中心通常要 18–36 个月，越接近百 MW / GW 级别越容易拖延；“每季度数 GW 上线”的说法与公开可见的项目进度严重不匹配。

## 关键证据链
**Microsoft 的容量说法最可疑**
Satya Nadella 连续两个季度声称 Microsoft 各新增约 1GW capacity，并称两年内将整体 footprint 翻倍、约 4GW capacity 上线。作者逐项追踪公开破土、土地收购、地方许可、社区更新和卫星图后，能确认的主要新增投产线索几乎只剩 Fairwater Atlanta 与 Fairwater Wisconsin。

即使用非常宽松的估算，Fairwater Wisconsin 可能只有约 117MW 运行；Fairwater Atlanta 若假设三栋楼完成，也大约 225MW 级别。合计约 342MW，距离 Microsoft 声称的 2GW/6 个月或 4GW/2 年差距巨大。作者因此判断，Microsoft 所说的 “capacity” 很可能包含合同容量、规划容量、colo/第三方容量或尚未真正上线的容量，而不是 active revenue-generating capacity。

**已宣布项目普遍卡在施工或 phase 状态**
Microsoft 在 North Carolina、Quebec、New Albany、Cheyenne、Brazil、Wales、Texas、Germany、Indiana、Iowa 等地的项目，大多仍在施工、等待破土、社区沟通或 civil works 阶段。其他公司项目也类似：Edged、EdgeCore、CyrusOne、Vantage、Aligned、DataBank、Flexential 等多个 20–200MW 级项目，从破土到开放常常超过 18 个月，且“开放”经常只是第一期。

真正可确认开放的案例反而偏小：American Tower Raleigh 1MW 用了 11 个月；Edged Phoenix 36MW 用了约 20 个月；EdgeCore Santa Clara 36MW 用了约 32 个月。作者用这些案例反推：GW 级 AI campus 不可能像媒体叙事那样轻松快速上线。

**Blackwell GPU 可能大量滞留**
Jensen Huang 曾称过去四个季度 ship 了 600 万 Blackwell “GPU”，但作者认为这是按双 die 口径计算，实际约 300 万颗。若按 B200 约 1200W 估算，300 万颗需要约 3.6GW IT load。Stargate Abilene 用近两年才上线两栋约 103MW critical IT load 的楼；要容纳 300 万 B200，大致相当于 35 栋 Abilene 级建筑在 2025 年建成并投产。作者找不到这些建筑在哪里。

Blackwell 还需要不同的机架、冷却和供电条件，不能简单塞进 H100/H200 时代的数据中心。作者因此怀疑：不止一半 Blackwell 尚未真正安装，NVIDIA 可能在用某种“超大规模预售 / bill-and-hold 式提前确认需求”支撑收入曲线。

**折旧数据也不支持“1GW/季度”**
折旧只有资产投入使用后才会开始显著进入损益表。Google、Microsoft、Meta、Amazon 的折旧确实快速上升，但幅度与“每季度新增 1GW GPU capacity”不匹配。作者举例：Microsoft 单季折旧增加约 4 亿美元，按 6 年折旧折回约 96 亿美元资产；若按每颗 B200 约 5 万美元估算，约 19.2 万颗 GPU、约 230MW IT load，明显低于 1GW 级别。

## 为什么重要
如果数据中心没有按叙事速度上线，AI 产业链会出现三层错配：

1. **芯片错配**：NVIDIA 已卖出的 GPU 可能远超现有数据中心可吸收量，库存、取消订单、延迟交付与下一代产品节奏会互相踩踏。
2. **云收入错配**：Microsoft、Google、Amazon 宣称的 AI 需求和 RPO 需要真实 compute capacity 承接；如果容量不存在，收入确认和客户增长都会受限。
3. **融资错配**：OpenAI 与 Anthropic 承诺向 hyperscaler 支出约 7480 亿美元，Oracle 又要为 OpenAI 建 7.1GW、可能超过 3400 亿美元的数据中心。若建设延迟到 2030 年甚至永远无法完成，合同价值与融资基础都会被重估。

作者特别强调 Oracle 风险最大：它没有 Microsoft/Google/Amazon 那种庞大现金牛业务缓冲，却要承担 Stargate 等巨型数据中心资本开支；如果 OpenAI 在容量投产前耗尽融资能力，Oracle 的 AI 云增长故事会先断。

## 破坏的常识
市场默认“AI compute 供不应求”意味着“新 capacity 会不断上线并立刻被填满”。作者反过来说：也可能是需求叙事太强、物理建设太慢，导致企业被迫买旧集群、抢临时容量、签超长期合同，并把未建成的 capacity 当成未来收入来资本化。

Anthropic 租用 xAI Colossus-1 是关键反常信号：如果未来几个月真的有大量现代 GB200 集群上线，Anthropic 没必要急着接手一个混合 H100/H200/GB200、效率较差、还带政治和污染争议的旧设施。这个交易更像“真实可用 compute 紧缺”而不是“数据中心正快速投产”。

## 值得质疑
作者的证据强项是微观追踪：地方新闻、许可、卫星图、社区公告、公司措辞之间确实存在大量不一致。弱项是它仍主要依赖公开可见项目，因此无法完全排除 Microsoft 等公司通过 colo、SPV、未披露第三方合作或旧数据中心 retrofit 获得大量容量。

但反驳门槛也很清楚：如果数 GW 已经投产，应该能找到对应的电力接入、建筑、许可、折旧、服务器交付、地方报道或客户收入痕迹。作者不是证明“没有任何隐藏容量”，而是把举证责任推回给 hyperscaler：请说明 capacity 到底是 contracted、energized、installed、revenue-generating，还是只是 pipeline。

## 最后一层含义
这篇文章真正挑战的不是数据中心施工进度，而是 AI 资本市场的计量语言：当 “capacity” 可以同时指合同、电力、建筑、IT load、GPU、phase、campus 或未来计划时，整个产业都可以在同一个词里藏杠杆。真正危险的不是数据中心建得慢，而是市场可能已经按“它们已经建成”给整条链估值。
