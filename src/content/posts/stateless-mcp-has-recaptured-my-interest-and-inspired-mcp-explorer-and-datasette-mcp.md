---
title: "Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)"
date: 2026-08-02T13:36:19Z
category: reading
author: "Simon Willison"
description: "Simon Willison 的核心论点：给 agent 开一个终端+网络的\"全局授权\"在安全上几乎无法推理；MCP 工具集明确边界，可审计，小模型也能驱动。MCP 2.0（2026-07-28 规范，即 stateless MCP）同时把协议实现的工程成本降到可接受，三件事合在一起让他重新押注 MCP。"
source: "https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything"
---

## MCP 比 shell 访问更安全，而 2.0 规范终于让实现成本足够低

Simon Willison 的核心论点：给 agent 开一个终端+网络的"全局授权"在安全上几乎无法推理；MCP 工具集明确边界，可审计，小模型也能驱动。MCP 2.0（2026-07-28 规范，即 stateless MCP）同时把协议实现的工程成本降到可接受，三件事合在一起让他重新押注 MCP。

## Stateless 改了什么

旧的"legacy MCP"：每次调用需两个 HTTP 请求——先 ~initialize~ 拿 ~Mcp-Session-Id~，再实际调用工具。服务端必须维护会话状态，无法无状态横向扩容。

新规范（MCP-Protocol-Version: 2026-07-28）：单次 POST，session 信息直接内嵌在 ~_meta.io.modelcontextprotocol/clientInfo~，服务端不再需要路由"同一会话到同一实例"。对 serverless 和无状态 CDN 友好。

## 本周三个实现

- *mcp-explorer*：Python CLI，用 uvx 免安装，支持 list / inspect / call，主要用途是交互式探查陌生 MCP server。
- *datasette-mcp*：Datasette 插件，暴露 ~/-/mcp~ 端点，提供三个工具：~list_databases()~、~get_database_schema(database_name)~、~execute_sql(database_name, sql)~（当前只读）。已在 datasette.simonwillison.net 上线，可对接 ChatGPT 和 Claude。
- *llm-mcp-client*（alpha）：给 ~llm~ CLI 工具的 MCP 集成，计划后续纳入 llm core。

## 安全优先的结论

2025 年初 Willison 写过 MCP 的 prompt injection 问题；几个月后 general agent（任意 shell+curl）上线，他觉得那比 MCP 的风险更难控制。现在的立场：对敏感应用，MCP 的可审计工具集是更可辩护的选择。
