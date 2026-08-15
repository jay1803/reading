---
title: "from vibe coding to vibe doing"
date: 2026-04-09T08:01:35Z
category: reading
description: "这篇内容真正有价值的判断是：AI 从“vibe coding”走向“vibe doing”的关键，不是模型再聪明一点，而是能否在没有 Git 这种统一真相源的知识工作里持续保留上下文、维护状态并跨工具推进任务。编码场景已经被端到端系统吃掉，是因为代码世界有 repo、branch、merge；知识工作之所以更难商..."
source: "https://newsletters.feedbinusercontent.com/84e/84eec66acbdd489bc1eda4c38d57979ed3e6def2.html"
---

## TL;DR
这篇内容真正有价值的判断是：AI 从“vibe coding”走向“vibe doing”的关键，不是模型再聪明一点，而是能否在没有 Git 这种统一真相源的知识工作里持续保留上下文、维护状态并跨工具推进任务。编码场景已经被端到端系统吃掉，是因为代码世界有 repo、branch、merge；知识工作之所以更难商业化，不是需求不大，而是 email、chat、docs、calendar、项目工具彼此割裂，工作的产物本身就是那团不断变化的上下文。

## 核心主张拆解
作者把 2026 的新战场定义为三类“代做型”知识工作：chief-of-staff 类关系与收件箱维护、项目管理、以及文档和报告生成。Sauna 的切入不是再做一个聊天入口，而是把转录、Notion 文档、日常沟通串起来，持续判断一个项目正在偏离原文档，还是正在形成新共识。这里隐含的产品定义很清楚：知识工作 agent 的价值，在于长期跟踪“事情怎么演化”，不是一次性回答“这篇文档是什么意思”。

市场面上，文中把 players 铺得很开：Sauna、Lindy、Fyxer、Zo Computer 这类创业公司，试图复制 Claude Code、Codex、Cursor Agents 在编程里的 delegation 体验；同时又要面对 Claude Cowork、Perplexity Computer 这类平台级产品。作者想说明的不是“机会存在”，而是“入口正在从 prompt 走向 persistent workspace”。这也解释了为什么 Manus 式的一次性任务代理被归为上一阶段，它能解决离散任务，解决不了持续协作。

## 具体机制
文章最强的一点，是把编码代理和知识代理的基础设施差异讲透了。编码任务有 Git 作为 source of truth，agent 完成一个分支任务后可以被丢弃；知识工作没有“main branch”，同一个人可能在四个会议里给出四种不同偏好，agent 必须自己拼出当前真实状态。因此，知识代理要想可用，必须补齐三层能力：跨工具接入，长期记忆，以及对上下文漂移的判断。Sauna 的早期使用案例也围绕这三层展开，例如用户把会议转录与 Notion 文档喂进去，让系统每天在正确频道里报告项目是否偏离几天前的设想。

## 证据薄弱处
这篇内容更像创始人 thesis 加市场扫描，不像被充分验证的行业研究。它列了不少融资和 ARR 数据来制造赛道热度，但关于 Sauna 自身的留存、付费结构、任务成功率、误判成本几乎没有展开。另一个薄弱点是，它把“知识工作缺少 Git”当成核心瓶颈，这个判断大概率对，但真正的落地阻力可能更脏：权限体系、缺 API 的工具、企业流程责任归属，以及用户未必愿意长期交出代理权。

## 留下来的那个想法
AI 下一阶段最值钱的不是“替你回答”，而是“替你记住、对齐并持续推进”，谁先把知识工作的状态管理做成真正可依赖的基础设施，谁才更接近吃到“vibe doing”的大头。
