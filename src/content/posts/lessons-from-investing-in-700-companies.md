---
title: "Lessons from Investing in 700 Companies"
date: 2026-02-24T10:55:40Z
category: reading
description: "Gokul Rajaram，产品人出身，先后在 Google（AdSense 早期）、Facebook（广告产品）、Square（产品与风控）、DoorDash（产品）担任核心角色，均在公司最关键的规模化阶段参与其中，同时天使投资超过 700 家公司，现为 Marathon Management 创始合伙人。采访..."
source: "https://colossus.com/episode/lessons-from-investing-in-700-companies/"
---

## 嘉宾背景

Gokul Rajaram，产品人出身，先后在 Google（AdSense 早期）、Facebook（广告产品）、Square（产品与风控）、DoorDash（产品）担任核心角色，均在公司最关键的规模化阶段参与其中，同时天使投资超过 700 家公司，现为 Marathon Management 创始合伙人。采访者 Patrick O'Shaughnessy，Colossus 主理人，Invest Like the Best 播客主持。

## TL;DR

AI 时代软件的最大危机不是被新公司颠覆，而是被自己的 SaaS 模型蚕食：凡是按席位定价、数据半衰期短的公司，已经可以被旁边挂一个 AI Agent 慢慢吸走价值——而大多数公司还没意识到这正在发生。

## 产品开发已经发生结构性断裂

Gokul 认为过去几个月，长运行 Agent 的到来让产品开发逻辑彻底变了：PM 不再主导功能设计，只守住"为什么建"和"质量评估（evals）"这两个节点；设计师与工程师的比例从 1:3 压到 1:20；代码本身变为非确定性，PM 的核心职责变成写评估代码来评估 AI 产出物。六个月前他自己尝试用 Claude Code 做视频转写工具失败告终；两周前同一件事在一小时内看电视顺手做完——这就是 Agent 韧性变化的量级。

## 判断力是 AI 时代唯一真正不可替代的东西

无限生产力时代的真正瓶颈是"做哪些事"，而不是"能不能做"。Gokul 把这称为 editorial capability（编辑能力）：Jack Dorsey 管 PM 叫 product editor，因为最好的产品人是做减法的；Rick Rubin 说自己是 reducer 而非 producer——同一条逻辑。工程师写了大量 AI 代码，但谁来判断哪段值得要？谁来审 critical path 上的漏洞？这层判断无法外包给 AI。

## 按席位计价的 SaaS 已进入死亡区

Zendesk 类公司面临的威胁不是被替代，而是被稀释：不需要迁移，只需在它旁边放 AI Agent，把 50 个席位砍成 20 个。Slack 的数据半衰期短，不如 Salesforce/NetSuite 里的客户记录和交易数据那么难迁。相比之下，ERP（NetSuite）因为 rip-out 代价太高而暂时安全——但 Gokul 认为这些公司都需要去私有化才能完成商业模式转型，因为公开市场无法承受从按席位收费转向按结果收费的过渡期。

## 广告业的三条路和一个威胁

广告业只有三种赚钱方式：① 拥有第一方流量（Google/Facebook/ChatGPT）；② 交付可量化的结果（AppLovin 做 mobile app install）；③ 成为大广告主的独占代理（The Trade Desk）。ChatGPT 同时拥有 intent 数据和 identity 数据，是广告史上首次——Google 只有 intent，Facebook 只有 identity。真正威胁所有现有广告平台的，是用户将重复性行为交给 AI Agent 自动处理后，不再打开 App，广告曝光机会消失。

## 向伟大创始人学到的产品直觉

- **Larry Page**：要求所有内部工具对外部小客户同等开放，结果小客户反而比大客户更会用——最优秀的自助产品用户是小型代理和创业者。Sergey 推翻了 AdSense 整个审核系统：与其提前审，不如等 URL 曝光满 100 次再看，大多数连 100 次都到不了。
- **Zuck**：Facebook Custom Audiences 的核心想法来自 Zuck 听到 Zynga 想找"鲸鱼用户"后拍脑袋想到的"让广告主上传自己的鲸鱼名单让我们找相似人"——跨域连接是他最突出的能力。
- **Jack Dorsey**：好设计=零培训即上手。Square POS 之前，收银员入职要培训数周；Square 能从 App Store 下载直接用。他把这种"去除摩擦"延伸到 Square 的整个风控逻辑——入驻时几乎不审核，风险判断前移到每一笔交易级别。

## 留下的那个想法

Gokul 说真正好的 PM 候选人会拒绝题目本身的前提——面试题是"我们应该建这个产品吗？"，最好的答案是去外面问了 10 个用户回来说"不应该建"。这个反射弧——把面试官当成需要被说服的用户，而不是需要被取悦的权威——比任何方法论都难培养，也比任何 AI 都难替代。
