---
title: "How to build your marketing strategy in Claude"
date: 2026-03-20T08:00:45Z
category: reading
description: "营销人员用 Claude 做不好输出，根本原因是把策略文档和实际工作完全脱节了。解法不是补提示词，而是把整个营销策略写进 Claude 的 =/marketing-strategy= skill 文件，让 Claude 在每次任务中自动引用它——策略不再是\"写完就忘的文档\"，而是每次作业的真实上下文。"
source: "https://newsletter.mkt1.co/p/build-marketing-strategy-skill-in-claude-code"
---

## TL;DR
营销人员用 Claude 做不好输出，根本原因是把策略文档和实际工作完全脱节了。解法不是补提示词，而是把整个营销策略写进 Claude 的 =/marketing-strategy= skill 文件，让 Claude 在每次任务中自动引用它——策略不再是"写完就忘的文档"，而是每次作业的真实上下文。

## 核心洞见
- 策略文档和日常工作之间的断层才是根本问题，不是人力、工具、时间不够
- CLAUDE.md 应保持 <200 行，营销策略本身就超过这个上限——必须拆成独立 skill 文件
- Skill 文件可跨团队共享（推荐 GitHub），CLAUDE.md 是个人的，不可分发

## 具体机制——6 个串联练习，顺序执行，每步输出写入同一个 skill 文件
1. *公司概览*：阶段、商业模式、GTM 动作、ARR、客户数
2. *ICP 优先级*：角色 × 公司类型的细分矩阵，标注成熟度（proven / scaling / testing / not-priority）和时间分配比例
3. *营销优势*：4 类（产品 / 生态 / 燃料 / 引擎），评估当前强度与竞争差异化程度
4. *认知目标（Perceptions）*：3–5 个市场叙事，从受众视角写成"他们会复述的信念"
5. *定位*：4 问（为谁 / 是什么 / 对比谁 / 为何更好），当前版 vs. 一年后版并列
6. *收入杠杆排序*：新客获取 / 扩张 / 留存 / 效率，按当前最重要排序，并说明 marketing 如何具体拉动头部杠杆

完成后可加：KPI 目标、渠道策略、生命周期阶段、品牌语调、技术栈和负责人。

## 隐藏限制
- 6 个练习全部完成后才能输出质量稳定的 Big Bets（大赌注战役）；跳过上游练习，Big Bet 输出就是垃圾
- Skill 的价值完全依赖使用频率：必须在每次 brief、内容审查、优先级决策时显式引用 =/marketing-strategy=，否则等于没建
- GitHub 团队共享方案需要成员各自手动拉取和配置，不是零摩擦

## 收束行
这篇文章本质上是在卖一个观念转换：把 Claude 从"任务执行器"变成"策略操作系统"——但这个转换必须先付出大量前期策略梳理的代价，而大多数团队会在此之前就放弃。
