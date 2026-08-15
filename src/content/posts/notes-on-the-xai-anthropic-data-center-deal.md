---
title: "Notes on the xAI/Anthropic data center deal"
date: 2026-05-08T08:01:45Z
category: reading
description: "Anthropic 租用 xAI / SpaceX 的 Colossus 1，不只是一次算力采购；它暴露的是前沿 AI 公司在算力极度稀缺时，会被迫把品牌、安全叙事、环境争议和供应链主权一起押进同一个外部依赖里。"
source: "https://simonwillison.net/2026/May/7/xai-anthropic/#atom-everything"
---

## TL;DR
Anthropic 租用 xAI / SpaceX 的 Colossus 1，不只是一次算力采购；它暴露的是前沿 AI 公司在算力极度稀缺时，会被迫把品牌、安全叙事、环境争议和供应链主权一起押进同一个外部依赖里。

## 关键时刻
- Anthropic 在 Code w/ Claude 活动上最大的新闻，是与 SpaceX / xAI 达成协议，使用 Colossus 数据中心的“全部容量”。
- Colossus 1 的环境记录很差：为供电安装的燃气轮机曾以“临时设备”名义运行，未取得 Clean Air Act 许可，也没有污染控制装置；可信报道把它与空气质量恶化相关的住院增加联系起来。
- Andy Masley 的评价尤其刺眼，因为他平时常反驳“AI 数据中心用水、占地问题被夸大”的叙事；连他都说“不会把自己的计算跑在这个具体数据中心”。
- 外界一度误读为 xAI 放弃 Grok，把全部算力卖给 Anthropic；文章澄清：Anthropic 拿到的是 Colossus 1，xAI 自己保留更大的 Colossus 2。
- Anthropic 公布前一晚，xAI 对 Grok 4.1 Fast 等模型发出仅两周的下线通知，SpeechMap 等用户刚迁移过去就被迫再迁移；这让作者追问：这些模型是否原本就跑在 Colossus 1 上？

## 背后逻辑
- 算力约束已经强到足以压过品牌一致性。Anthropic 作为“安全优先”的 AI 公司，仍然接受了一个环境和政治争议都很高的基础设施来源。
- AI 数据中心正在变成地方政治议题，不再只是云成本或 GPU 数量问题；许可、排放、社区健康和地方反弹都会进入模型公司的经营风险。
- 这笔交易还引入了新的供应链主权风险：Musk 表示如果 Anthropic 的 AI “伤害人类”，他保留收回算力的权利；这个判断标准显然由他自己定义。
- 对 xAI 来说，这更像是基础设施资产再配置：旧的 Colossus 1 对外变现，新的 Colossus 2 留给自家训练，并不等于退出模型竞争。

## 值得质疑
- 文章没有披露合同期限、SLA、价格、退出条款，也没有证据证明 Musk 的“收回算力”说法在法律上如何执行；供应链风险成立，但具体强度未知。
- Grok 4.1 Fast 下线与 Colossus 1 出租之间只有时间线关联，作者明确是在提出疑问，不是给出结论。

## 更大意义
前沿 AI 的瓶颈正在从“谁有更好的模型”扩展为“谁能持续、合法、低争议地控制足够算力”。这笔交易让 Anthropic 的风险画像更复杂：Claude 的未来容量不仅取决于芯片和模型能力，也取决于地方许可、环境政治，以及一个外部供应商对“good for humanity”的个人定义。
