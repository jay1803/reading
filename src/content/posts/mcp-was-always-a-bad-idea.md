---
title: "MCP was always a bad idea?"
date: 2026-10-07T20:59:05Z
category: reading
description: "MCP 的价值在于让 AI agent 的外部服务访问可控、认证隔离且可审计；完整编程 agent 不需要它，不代表 MCP 已经过时。"
source: "https://simonwillison.net/2026/Sep/20/hn-49779718/"
---

MCP 的现实价值在于让 AI agent 的外部服务访问可控、认证隔离且可审计，完整编程 agent 不需要它，并不能证明它已经过时。对于 Claude Code、Codex、Meta Muse、OpenClaw 这类拥有完整终端能力、可不受限制访问互联网的 agent，直接调用 API 就足够了，使用 MCP 几乎没有必要。

但如果要构建权限更受约束的系统，开发者就需要精确控制 agent 可以访问哪些外部服务，让它在无法直接接触 API keys 的情况下完成认证，提供方便用户连接新服务并授权的界面，同时用完善的审计日志记录操作。MCP 能显著降低提供这些能力的难度。以全权限编程 agent 的需求判断 MCP 的价值，会忽略其他 AI 产品对访问边界、凭据保护、用户授权和操作追踪的需求。
