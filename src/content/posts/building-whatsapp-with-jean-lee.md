---
title: "Building WhatsApp with Jean Lee"
date: 2026-03-19T08:00:38Z
category: reading
author: "Gergely Orosz"
description: "Jean Lee，WhatsApp 第 19 号工程师，参与公司从早期小团队扩张到数亿用户的全程，亲历 2014 年 Facebook 以 190 亿美元收购；此后在 Meta 担任工程师及管理职位。[补充：现经营职业发展平台 Exaltitude，面向软件工程师提供职业指导。] 主持人为 The Pragmat..."
source: "https://newsletter.pragmaticengineer.com/p/building-whatsapp-with-jean-lee"
---

## 嘉宾背景

Jean Lee，WhatsApp 第 19 号工程师，参与公司从早期小团队扩张到数亿用户的全程，亲历 2014 年 Facebook 以 190 亿美元收购；此后在 Meta 担任工程师及管理职位。[补充：现经营职业发展平台 Exaltitude，面向软件工程师提供职业指导。] 主持人为 The Pragmatic Engineer 的 Gergely Orosz。

## TL;DR

WhatsApp 用 30 名工程师服务 4.5 亿用户，不靠 AI、不靠流程，靠的是信任——而信任的最极端表现是"只审一次代码，然后永不再审"。

## 一次 code review 定终身

Brian Acton 对每位新工程师的第一个 PR 做极其详细的审查，此后再无代码 review。这个"一次定标准"机制替代了持续的流程管控：工程师对标那次高要求，自我执行，而不依赖外部审计循环。Jean 的第一个 PR 被 Brian 逐行审查，她从此内化了这套标准。

## 零流程胜过有流程

没有 Scrum、没有 Agile、没有 TDD，照样打败了拥有 1000 名工程师、完整 Scrum 体系的 Skype。Jean 对 Skype 靠流程"提速"的逻辑直接质疑："我很惊讶他们以为流程让他们更快。"流程往往是信任缺失的替代品，而非质量的保障。

## 说"不"是核心竞争力

CEO Jan Koum 拒绝团队 99% 的功能请求，标准只有一条："乡下老奶奶能用吗？"视频通话等功能被压后多年，经家人测试才上线。这是"反 launch early"策略在消费软件里奏效的罕见案例——竞争对手在堆功能，WhatsApp 在打磨可靠性。

## 可见指标替代问责文化

办公室屏幕持续显示距上次宕机的天数，出事后数字归零，没有邮件通报，没有责任会议。可见的集体指标制造了压力，但压力均摊给团队而非落在某个个体头上，这让"避免宕机"成为所有人不言而喻的首要任务。

## Meta 的可见性游戏

在 Meta，定期在内部 Facebook 发布工作进展的工程师，在绩效校准会上有显著优势。"被看见"本身是职业资产——与 WhatsApp 的文化形成直接反差：WhatsApp 靠结果说话，Meta 靠曝光博弈。

## AI 能替代工具，替代不了信任

Jean 认为 AI 可以接管 OKR 管理、文档、绩效数据整理，但解除工程师阻塞仍需要人对人的理解。她同时质疑"AI 让小团队跑更快"的前提：WhatsApp 的高效不依赖工具，依赖的是规模小本身带来的效率。

## 留下的那个想法

WhatsApp 故事里最意外的不是"30 人支撑 4.5 亿用户"，而是这套打法的核心资产——信任、简单、说不——恰恰是规模扩大后公司最容易主动放弃的东西。
