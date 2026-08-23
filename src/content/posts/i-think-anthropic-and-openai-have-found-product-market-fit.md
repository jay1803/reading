---
title: "I think Anthropic and OpenAI have found product-market fit"
date: 2026-05-28T08:01:27Z
category: reading
author: "Simon Willison"
description: "OpenAI 和 Anthropic 的真正产品市场契合点，正在从大众聊天订阅转向高消耗、高付费意愿的企业级编码/通用代理；价格上调、按 API token 计费、企业销售扩张和推理算力支出，都指向同一个事实：代理产品已经开始把模型能力转换成可观收入。"
source: "https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything"
---

## TL;DR
OpenAI 和 Anthropic 的真正产品市场契合点，正在从大众聊天订阅转向高消耗、高付费意愿的企业级编码/通用代理；价格上调、按 API token 计费、企业销售扩张和推理算力支出，都指向同一个事实：代理产品已经开始把模型能力转换成可观收入。

## 核心主张拆解
### 企业用户开始按 API 价格买代理能力
Simon 自己的 30 天用量估算显示，Claude Code 若按 API 计费约为 1,199.79 美元，OpenAI Codex 约为 980.37 美元，但他通过 Anthropic Max 和 OpenAI Pro 合计只付 200 美元。这解释了为什么个人订阅显得极划算，也解释了企业续约时会感到成本冲击。

Anthropic 在 2025 年 11 月前后把企业计划改成 20 美元/席/月加使用量 API 计费；OpenAI 在 2026 年 4 月 2 日先对 Plus、Pro、Business 和新 Enterprise 计划更新 Codex 定价，并在 4 月 23 日覆盖既有 Enterprise/Edu/Health/Gov/Teachers 计划。到 2026 年 4 月，两家公司在 Codex、Claude Code/Cowork 上都把企业价格拉回到标价 API 成本。

### 编码代理把收入密度拉高了
ChatGPT 的 9 亿周活里只有约 5,000 万付费消费者，10-20 美元/月的订阅很难支撑万亿美元级基础设施投资。相反，编码代理面向高薪知识工作者，单用户月消耗可以轻易达到数百到上千美元 API 价值，且使用场景已经接近日常生产力工具。

作者把 2025 年 11 月视为代理能力变得真正可用的拐点；2026 年 4 月则是收入拐点：新前沿模型更贵，企业价格机制也同步切到按 token 兑现价值。GPT-5.5 的 API 价格是 GPT-5.4 的 2 倍，Opus 4.7 按新 tokenizer 折算约比 Opus 4.6 贵 1.4 倍。

### 企业化组织投入在同步验证这个判断
OpenAI 当前 703 个开放岗位中，作者归类 229 个与企业销售和支持相关，占 32.6%；Anthropic 390 个开放岗位中，105 个看起来偏企业化，占 26.9%。这说明模型公司正在补齐传统企业软件的重人力 GTM 能力：账号销售、Forward Deployed Engineer、客户支持和部署服务。

### “AI 成本失控”新闻更像定价权信号
Uber 据称几个月内用完全年 AI 预算，主要来自 Claude Code；但如果预算在 2025 年制定，就很可能低估了 2025 年 11 月后编码代理的真实需求。Uber COO 提到上一季度 25% code commits 来自 Claude Code，但还难以把它直接映射成 25% 更多消费者功能。

Microsoft 取消部分 Claude Code license 也被解释为财务因素和推动内部 Copilot CLI dogfood。作者的判断是，这些案例不是需求崩塌，而是客户开始因为价格吸气、但仍承认产品有足够价值的阶段。

## 关键证据
SpaceX S-1 披露，2026 年 5 月 Anthropic 与其签署云服务协议，将为 COLOSSUS 和 COLOSSUS II 计算能力每月支付 12.5 亿美元，持续到 2029 年 5 月。Anthropic 随后称这将提高 Claude Code 和 Claude API 的使用上限，暗示这笔算力更偏推理而非训练。

Anthropic 过去 API 收入高度依赖 Cursor 和 GitHub Copilot 等大客户；2025 年 8 月的报道曾称 Cursor 与 Copilot 贡献了当时约 40 亿美元收入中的 12 亿美元。如今 Claude Code 直接与这些中间层竞争，说明前沿实验室正在把价值链往自己产品端收回。

## 值得质疑
文章的核心推理强，但不少财务数字仍来自传闻、招聘页分类和媒体报道，缺少 IPO S-1 级别的审计数据。Anthropic 是否真的接近季度盈利、企业代理收入毛利是否足以覆盖持续扩张的推理支出，还需要等 OpenAI 和 Anthropic 的正式上市文件验证。

另一处不确定性是 ROI 归因。企业会愿意为代理能力付费，但从“25% 代码提交来自 Claude Code”到“显著增加有效产品产出”之间仍缺少可审计链路。预算超支证明需求强，不自动证明单位经济模型已经健康。

## 最后一层判断
这篇文章最重要的判断是：AI labs 的商业化中心正在从“全民聊天入口”转向“高价值工作流里的计量式代理基础设施”，而 2026 年 4 月可能是这个转折开始在收入、价格和企业预算里同时显形的月份。
