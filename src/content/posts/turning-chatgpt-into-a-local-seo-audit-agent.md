---
title: "Turning ChatGPT Into a Local SEO Audit Agent"
date: 2026-09-07T13:48:37Z
category: marketing
author: "Sarvesh Shrivastava"
description: "本地 SEO 顾问 Sarvesh Shrivastava 把 Google Business Profile 审计、竞对拆解、文案生成打包成一套可以直接喂给带浏览器能力的 ChatGPT 执行的 prompt 合集，标题喊的是 20 个，正文实际交付的只有 12 个，其余是引导付费代运营的钩子。"
source: "https://x.com/bloggersarvesh/status/2095896040155340809"
---

这条帖子表面上是"白送 20 个 ChatGPT SEO prompt"，核心其实是把本地服务类小企业（水管工、HVAC、律师、清洁公司这类）的 Google Business Profile 优化和网站 SEO，改造成一套可以直接喂给带浏览器能力的 ChatGPT（作者称之为 "ChatGPT Astra"）去自动执行的标准作业流程——AI 打开 Chrome，去 Google Maps、竞争对手的 GBP 页面、SEMrush、Google Search Console 上现场抓数据、做对比、出报告和文案，而不是泛泛地问它"怎么做本地 SEO"。

作者 Sarvesh Shrivastava 经营 Alventra Marketing，自称 14 年本地 SEO 经验，判断大多数人只用了 ChatGPT 潜力的 10%，这份清单是他专门为 home-service 行业沉淀下来的"另外 90%"。使用前提是先把一段固定的 Business Context 模板整段贴进对话——公司名、地址、核心服务、目标关键词、当前排名、竞争对手清单、已经试过的打法都填进去——并明确告诉模型"以后每次都用这段信息，不要再问我"，相当于给 agent 建一份持久化的项目简报，后面所有 prompt 都建立在这个上下文之上。

Part 1 的 8 个 prompt 全部围绕 Google Business Profile 展开：先是分类审计和属性审计，让 AI 逐个打开竞争对手的 GBP 页面，抓主/次分类和"veteran-owned"、"24/7"这类标签，做成表格标出自己缺什么、哪些是三家竞对都有的"标配"、哪些只有一家有的"差异化机会"；接着是评论区拆解，读竞对最近 50 条评论，提炼评论速度、常被提到的服务和社区名、常见投诉主题，反推出该训练自己客户在评论里说哪些关键词；再往后是评论回复策略（按 5/4/3/1-2 星分别生成带关键词的回复模板）、GBP 动态发布策略（照抄竞对节奏后产出一份 8 周发帖日历，前 4 周给全文案）、服务栏优化（把每项服务改写成 40-60 词、带关键词和服务区域的描述）、简介优化（关键词向、转化向、信任向三个版本）、照片审计（按竞对上传节奏定一份带拍摄清单和地理标记说明的 8 周计划）。

Part 2 的网站部分完整展开了 4 个 prompt：用 SEMrush 做关键词缺口分析，专门过滤出"有本地意图"（带城市名、near me、emergency 这类词）且难度可控的机会词；用 Google Search Console 数据做"金矿页面"审计，找出排名 4-15 名只差临门一脚的页面，以及有曝光没点击的标题/描述问题；生成服务+城市组合落地页的完整文案（标题、meta、H1、正文、FAQ、CTA 一次给全）；以及针对排名 11-20 名、月曝光超过 100 的"第二页金矿"关键词，做一个 30 天冲刺计划，且明确要求 AI 直接给出可用的标题和 meta 文案，而不是泛泛的建议。

值得注意的是，标题喊的是"20 个 prompt"，但正文完整给出文案的只到第 12 个，第 13-20 个只在末尾"使用节奏"部分被提了个名字（比如 review sentiment），并没有实际内容——这更像是刻意留白的漏斗设计：先用 12 个高质量、可直接复制粘贴的 prompt 建立信任和"这人真懂"的印象，最后落到"大多数人会收藏但从来不会真的执行，不如直接花钱让 Alventra Marketing 帮你跑完整套系统"这个转化点上。评论区反馈也基本是正面认同，比如"原来我们只用了 10%"、"这个 GBP posting calendar 从没人真的做过"，没有看到对内容真实性的质疑，说明这套引流打法目前效果还不错。

这条帖子真正值得留意的不是清单里的具体 SEO 战术——分类审计、评论管理、关键词缺口分析都是本地 SEO 里的常规动作，Sarvesh Shrivastava 只是把它们系统化了——而是它示范的一种新的内容形式：把一个原本靠人工反复打开网页、抄数据、写文案的重复性审计流程，压缩成一套可以直接丢给带浏览器/agent 能力的 LLM 执行的指令脚本，本质上是把"SOP 文档"这个载体从给人看的清单，换成了给 agent 执行的 prompt。这类"能跑的 SOP"会不会取代传统的行业教程和模板文档，是比这套具体 SEO 打法本身更值得跟踪的方向。

来源：<https://x.com/bloggersarvesh/status/2095896040155340809>
