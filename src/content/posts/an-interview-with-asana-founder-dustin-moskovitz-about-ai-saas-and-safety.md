---
title: "An Interview with Asana Founder Dustin Moskovitz about AI, SaaS, and Safety"
date: 2025-10-21T13:37:09Z
category: reading
description: "Dustin Moskovitz，Facebook 联合创始人（哈佛与 Zuckerberg 同住一寝室，后出任 Facebook 首任 CTO 兼工程 VP），2008 年离开 Facebook 与 Justin Rosenstein 共同创立 Asana。Asana 于 2020 年直接上市，Moskovit..."
source: "https://stratechery.com/2025/an-interview-with-asana-founder-dustin-moskovitz-about-ai-saas-and-safety/"
---

## 嘉宾背景
Dustin Moskovitz，Facebook 联合创始人（哈佛与 Zuckerberg 同住一寝室，后出任 Facebook 首任 CTO 兼工程 VP），2008 年离开 Facebook 与 Justin Rosenstein 共同创立 Asana。Asana 于 2020 年直接上市，Moskovitz 担任 CEO 长达 13 年，2025 年初移交给 LaunchDarkly 前总裁 Dan Rogers，自任董事长。他同时通过 Good Ventures 资助生物安全与 AI 安全研究，现为 Anthropic 董事会观察员，也是 OpenAI 早期捐助者。采访者为 Stratechery 创始人 Ben Thompson。

## TL;DR
在"最好的 AI demo 都没有权限控制"的行业现状下，Moskovitz 的反直觉押注是：拒绝 chatbot 优先、走嵌入式工作流路线的 SaaS 才能真正赢得企业 AI 渗透——因为最大的落地阻力不是技术，而是企业被糟糕体验吓退后的幻灭感；而这套商业逻辑与他对 AI 安全的判断在底层是同一件事。

## "演示驱动竞赛"是当前 AI 最大的系统性风险
Moskovitz 观察到行业结构性矛盾：最能打动投资人和客户的 demo，恰恰是权限最宽、控制最少的版本，由此直接制造 prompt injection、数据越权等安全漏洞。他将此比作 AI 领域的 Moloch 困境——竞争压力迫使所有参与者做出对集体有害的单边决策。他预计将有"某件很糟的事"发生并引发行业冷静期，而这对 Asana 和整个 SaaS 都是伤害，因此"减速即是加速"对他既是商业判断也是安全立场。

## AI 渗透的真正障碍是行为改变成本，不是技术能力
以 Asana 内部实践为例：自动分类客户反馈、维护需求热度排行并生成可追溯 Backlink，AI 持续在后台运行，PM 和 UXR 不需要打开 chatbot 就能获益。他将此称为"有用即用（useful without volition）"——与 ChatGPT Enterprise 席位大量闲置相对，嵌入式路线绕过了"说服员工改变工作习惯"的最大落地阻力。计划中的绩效评估场景也是同理：Asana 将自动为每位员工生成工作档案交给评审者，无需用户主动触发 AI。

## 席位制定价正在被自己的成功侵蚀，但转型必须走小步
Asana 已引入"固定平台费 + 预配 Token，超额按量计费"混合模式，甚至对大客户直接赠送席位换取平台消费。Moskovitz 坦言席位制与 AI 自动化之间存在根本矛盾——AI 越有效，企业所需人员越少，座位收入也越少。但这是一个 7 亿美元的上市公司，策略是先引入非席位 SKU 并从新客户改变定价心理，而非在续约时激进替换。他认为席位单价长期可能趋零，平台费成为主营收来源。

## Moskovitz 持"短时间线"立场，但拒绝暂停派
他自述早年认为 LLM 只是"随机鹦鹉"且无法做数学，后来逐一检验这些假设并发现自己全错；现在他是短时间线支持者，认为重大 AI 事故将在不远的将来发生。他担任 Anthropic 董事会观察员，支持芯片出口管制，但明确与"暂停 AI 开发"阵营切割——他认为 EA 并非铁板一块，多数严肃研究者真正担忧的是"竞赛点燃起跑枪"而非 AGI 暴走。他对前特朗普政府借 AI 安全叙事仓促出手（尤其对华关系）持批评态度，认为忽视了 10-20 年的长程变量。

## 留下的那个想法
他说 Facebook 早期成功的秘诀之一是"不知道自己不该怀疑自己"——这套逻辑用在 AI 安全上完全反了过来：今天那些最自信地快速部署 AI 的公司，或许正因为不知道该怀疑自己，而埋下了代价最大的隐患。
