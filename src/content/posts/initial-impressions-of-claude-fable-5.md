---
title: "Initial impressions of Claude Fable 5"
date: 2026-06-12T08:01:14Z
category: reading
author: "Simon Willison"
description: "Fable 5 的核心差异不是安全过滤器，而是模型\"知道更多\"——更密集的参数知识库让它在没有工具辅助的情况下就能解决 Opus 4.8 需要搜索才能处理的工程问题，数小时内产出相当于数天工作量的代码。"
source: "https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything"
---

## TL;DR
Fable 5 的核心差异不是安全过滤器，而是模型"知道更多"——更密集的参数知识库让它在没有工具辅助的情况下就能解决 Opus 4.8 需要搜索才能处理的工程问题，数小时内产出相当于数天工作量的代码。

## 关键发现
- 定价翻倍：$10/M 输入、$50/M 输出，较 Opus 4.5–4.8 贵一倍；订阅计划 6 月 22 日前包含在内，之后额外计费
- 1M token 上下文窗口，128k 最大输出，知识截止日 2026 年 1 月
- Mythos 5 是 Fable 5 的无安全过滤器版本，两款同日发布；Fable 的过滤器触发频繁，Anthropic 专门新增了自动 fallback API 选项
- "知识量"测试：Fable 能精确列出 Simon Willison 数十个开源项目及发布时间，Opus 4.8 仅能列出 4 个主要项目并主动说明不确定性

## 实际编码能力验证
- 在 Claude.ai 容器环境中，用两次提示将 micropython-wasm 升级为运行完整 CPython/WebAssembly 沙箱，并打包为 13.9MB wheel 文件
- 为 Datasette Agent 和 LLM 库构建了完整的"暂停-恢复"工具调用机制（LLM 0.32a3），包括：PauseChain 异常、ULID tool_call_id、异步并发工具执行的失败语义、从 pending tool call 历史恢复 chain——全部含测试和文档
- Simon 评价：感觉数小时内完成了数天的工作量

## 隐藏代价与局限
- 模型速度慢、成本高——单日 token 费用 $110.42（但在 $100/month 订阅内）
- 安全过滤器触发频率高于以往任何版本，是实际使用的摩擦点
- Anthropic 未公开参数规模，无法直接验证"最大模型"猜测

## 收束
"最大的模型"不是靠速度，而是靠把更多世界知识压进权重——这种知识密度才是让复杂编码任务无需搜索就能流畅完成的根本原因，而非单纯模型架构改进。
