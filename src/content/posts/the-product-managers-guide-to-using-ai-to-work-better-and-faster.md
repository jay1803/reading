---
title: "The Product Manager's Guide to Using AI to Work Better and Faster"
date: 2025-05-20T10:10:14Z
category: reading
description: "PM 被 AI 取代的风险低于大多数\"制造者\"岗位（John Maeda：PM 是\"talkers\"），但 AI 对 PM 的赋能也因此有一个严格前提：必须提供内部产品数据上下文，否则通用 AI 只能给出与实际产品无关的泛化输出。"
source: "https://www.prodpad.com/downloads/product-managers-using-ai-tools/"
---

## TL;DR
PM 被 AI 取代的风险低于大多数"制造者"岗位（John Maeda：PM 是"talkers"），但 AI 对 PM 的赋能也因此有一个严格前提：必须提供内部产品数据上下文，否则通用 AI 只能给出与实际产品无关的泛化输出。

## 核心洞见
AI 对 PM 七大工作场景均有切入点——产品战略（vision、OKR 生成）、发现（研究问题设计、数据主题提炼、代码原型）、反馈管理（自动转录→提取要点→归并 backlog）、优先级（去重、对齐战略、排序）、文档与 copy（PRD、user story、接受标准）、利益相关方沟通（回答 ad hoc 问题）、最佳实践辅导。覆盖面广，但质量上限由上下文质量决定。

## 具体机制
**WISER 提示框架**（Allie K. Miller）：
- **W** ho：为 AI 设角色（是谁 + 在做什么 + 为何而做）
- **I** nstructions：具体指令，避免"给我一些想法"式模糊请求
- **S** ubtasks：拆分大任务，用 prompt chaining 逐步深入，避免一次性过载
- **E** xamples：提供模板或示例（few-shot prompting），减少重复输出
- **R** eview：要求 AI 自评，检查清晰度、创意、可行性、遗漏

工具选型逻辑：通用 AI（ChatGPT）灵活但需手动喂入上下文；专项 AI 功能聚焦但不灵活；嵌入式工具（已内置产品 backlog、feedback、roadmap）免去上下文构建，输出最贴合产品实际。

## 隐藏限制
AI 在市场和竞品分析上有硬伤：训练数据有截止日期，竞品分析往往过时。文章建议：用 AI 生成研究框架或消化长篇行业报告，但核心竞品数据须手动核查最新来源。

## 收束行
"talkers vs makers"的分层，准确描述了为什么 PM 是 AI 最好的放大器宿主：能设方向、能做判断，但无法被纯粹自动化——AI 把做的部分变快了，判断的部分反而更值钱了。
