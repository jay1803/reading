---
title: "Four Horsemen of the AIpocalypse"
date: 2026-04-22T08:01:51Z
category: reading
author: "Ed Zitron"
description: "AI 泡沫真正先撞上的不是“能力上限”，而是供给、成本和会计现实：当 Anthropic 连稳定服务都做不到、微软和 Anthropic 开始把补贴订阅往 token 计费切、而 NVIDIA 宣称的销售额远高于在建机房能容纳的 GPU 规模时，“需求爆炸”更像被 VC 补贴、超前采购和财务叙事放大的假繁荣。"
source: "https://www.wheresyoured.at/four-horsemen-of-the-aipocalypse/"
---

## TL;DR
AI 泡沫真正先撞上的不是“能力上限”，而是供给、成本和会计现实：当 Anthropic 连稳定服务都做不到、微软和 Anthropic 开始把补贴订阅往 token 计费切、而 NVIDIA 宣称的销售额远高于在建机房能容纳的 GPU 规模时，“需求爆炸”更像被 VC 补贴、超前采购和财务叙事放大的假繁荣。

## 核心主张拆解
### 1. Anthropic 的问题不是暂时拥堵，而是商业模式和基础设施同时失真
- 过去 90 天 Claude chatbot 仅 98.79% uptime，API 99.09%，远低于成熟软件服务常见的 four nines。
- 服务不稳和模型退化一起出现：作者把 Opus 4.7 的口碑回落、token 消耗上升、推理变浅，与 Anthropic 的 capacity crunch 视为同一问题的表现。
- 更关键的是，Anthropic 没有因为供给不足而停止接客，说明容量约束没有阻止增长，只是把成本和不稳定性转嫁给用户。
- 作者引用估算：Anthropic 的订阅产品可能每赚 1 美元收入，要补贴 8–13.5 美元推理成本；如果这类补贴停止，增长叙事会立刻塌。

### 2. “安全克制”叙事，很多时候只是“算力不够”的公关版本
- Claude Mythos 延迟大规模发布，被作者判断主要不是 safety concern，而是无法稳定供应。
- 这篇文章的更大判断是：AI 公司频繁把 capacity shortage 包装成 capabilities management，把工程或财务问题讲成道德克制。

### 3. AI 数据中心需求被两家公司极度扭曲，行业并没有想象中那么多真实供给
- Sightline 数据里，至 2028 年底计划上线 114GW，但真正“在建”的只有 15.2GW，其中 2026 年可交付约 5GW。
- 仅 OpenAI 的 Stargate 就占 4.6GW；Anthropic 通过 Google、Microsoft、Amazon 等伙伴预订的容量至少又有数 GW。
- 作者因此认为，所谓全行业 AI 需求繁荣，本质上已被 OpenAI/Anthropic 两家高度集中化；如果它们的 economics 出问题，整个基建周期都会受冲击。

### 4. NVIDIA 的销售叙事和物理落地速度之间存在巨大缺口
- 按文中假设的 PUE、机柜功耗和每 MW IT 成本估算，15.2GW 在建数据中心对应的 GPU/关键 IT 价值约 2857 亿美元。
- 但 NVIDIA 对外给出的订单/可见收入是 2025–2026 年约 5000 亿美元、至 2027 年 1 万亿美元。
- 作者据此推断：大量 GPU 可能是被提前确认销售、在 ODM/仓库里堆积，而不是已经对应到真实可上线的机房需求。
- Quanta inventory 从 105.4 亿美元升到 163 亿美元，被拿来当成早期库存堆积信号。

### 5. 真正先结束的可能不是 AI 热情，而是 AI 补贴
- Goldman Sachs 提到企业 inference 预算正以数量级超支；Uber CTO 说全年 AI 预算几个月就烧完。
- Microsoft 已开始暂停 GitHub Copilot 个人付费注册、收紧 rate limit，并准备往 token-based billing 切；Anthropic 也已对企业客户改成 seat fee + per-token。
- 这意味着行业将从“先做大用户数”转向“把真实 compute 成本回收给客户”，而一旦如此，很多 today 的 adoption 可能并不成立。

## 值得质疑
- 文章的方向判断很强，但部分论证建立在作者自己的拼接估算上，例如在建容量如何映射到 GPU 销售、不同项目到底归属谁、库存上升是否足以证明渠道堆货。
- 对 AI 公司收入夸大、合同 ARR 虚胖、甚至接近误导的指控，有很多合理怀疑，但直接证据并不都在本文里。
- 即便如此，作者抓到的核心矛盾很硬：如果服务质量下降、单用户成本高企、客户预算失控、且物理供给跟不上，那“需求强劲”本身就必须打折看。

## 最后一笔
这篇文章最重要的提醒是：AI 产业眼下最危险的不是技术失败，而是“大家都默认别人已经验证过 economics”。一旦补贴退潮、token 真实定价、机房建设速度暴露上限，市场会发现自己追逐的可能不是生产力革命，而是一场被资本和会计口径撑大的过度消费。
