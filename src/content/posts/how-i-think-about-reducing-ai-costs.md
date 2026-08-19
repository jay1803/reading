---
title: "How I think about reducing AI costs"
date: 2026-08-19T00:04:29Z
category: reading
description: "AI 成本不再边缘——企业用过时模型和低效工具导致账单失控。四层递进框架：审计→换模型→换供应商→workflow 级优化，节省主力往往在后两层。"
source: "https://martinalderson.com/posts/how-i-think-about-reducing-ai-costs/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## AI 成本削减的四阶段框架

AI inference 成本不再是边缘问题——企业已大量使用"年迈"模型、过度强大的模型和设计粗糙的工具，导致账单失控。作者提出四层递进杠杆：审计→快速换模→换供应商→workflow 级优化，每层回报速度不同，规模最大的节省往往来自后两层。

## 第一层：先审计，再动手

需要全公司维度的两个关键拆分：
- **按模型**：大量团队仍在用 GPT-4o（$2.50/$10 / 百万 token）而非 GPT-5.6 Luna（后者成本为前者十分之一，Artificial Analysis 智能指数得分高 4 倍）。模型技术债真实存在。
- **按 token 类型**：cached input / uncached input / output 的分布与直觉通常不符，在 agent 场景尤甚。

常见盲区：只盯 API 账单，忽略开发团队的 coding agent 消耗（或反之）。

## 第二层：低垂果实——换模型与降配

同供应商内换更便宜的新模型，风险可控但需验证回归——旧的提示词 hack 在更智能模型上可能失效。另一个方向是"降配"：用小模型处理不需要旗舰智能的任务，但判断哪些任务可以降配需要相当经验。

## 第三层：换供应商——最大量级的节省

从 OpenAI/Anthropic/Google 切换到托管开源权重模型往往是最大节省来源。不必一次性全迁：先迁移消耗 token 最多的几个 workflow，其余保持不变。

关键认知障碍：内部团队常把"DeepSeek"等同于"中国数据"，但 US/欧洲供应商可在本地司法管辖内托管同款模型，满足数据驻留要求。

## 第四层：workflow 级深度优化——隐藏的最大浪费

从消耗最高的 10 个 workflow 入手，常见失效模式：

**Prompt 塞太多文档**：把大量可能不相关的文档全塞入 context，远不如给 LLM 一个按需搜索工具高效。

**工具返回数据爆炸**：MCP 经常返回数万字节的原始 JSON。QuickBooks 官方 MCP 的典型案例：
- 142 个工具定义，序列化后约 21,000 token，每次请求前就已消耗
- `search_invoices` 返回每条发票的每个字段，无过滤无摘要
- `get_invoice_pdf` 将 PDF base64 编码：100KB 发票 ≈ 33,000 token 噪音，模型无法读取也无法压缩

**工具失败引发重试风暴**：agent 失败后不断重试，token 消耗指数增长；在长 run 末尾尤其灾难性（此时 cache read 成本已积累）。

## 持续维护：季度审查

AI 迭代极快，"一年前的最佳实践往往现在有害"。建议每季度审查 token 消耗分布与模型格局变化。
