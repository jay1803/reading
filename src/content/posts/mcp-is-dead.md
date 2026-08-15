---
title: "MCP is dead?"
date: 2026-05-31T08:00:59Z
category: reading
description: "MCP 最大的问题不是“协议错了”，而是它把很多本来可以按需调用的工具能力，提前变成持续占用上下文、增加进程依赖、降低可调试性的常驻层；但 Claude Code 后来的 Tool Search / Deferred Loading 已经削弱了作者最强的上下文膨胀论点，所以更准确的结论是：MCP 不适合作为开发者..."
source: "https://www.quandri.io/engineering-blog/mcp-is-dead"
---

## TL;DR
MCP 最大的问题不是“协议错了”，而是它把很多本来可以按需调用的工具能力，提前变成持续占用上下文、增加进程依赖、降低可调试性的常驻层；但 Claude Code 后来的 Tool Search / Deferred Loading 已经削弱了作者最强的上下文膨胀论点，所以更准确的结论是：MCP 不适合作为开发者工作流的默认入口，CLI + Skills 更适合大多数可脚本化任务，MCP 只在权限隔离、团队统一认证、无 CLI 服务和生产数据库 guardrail 场景里成立。

## 核心主张拆解
作者把 MCP 的成本拆成三类：上下文占用、运行可靠性、与既有 CLI/API 的功能重叠。Quandri 实测 4 个 MCP server 共 77 个工具定义，约 84,308 字符 / 21,077 tokens，占 Claude 200K 窗口约 10.5%，占 GPT-4o 128K 窗口约 16.5%；Linear 单独 42 个工具就约 12,807 tokens，即使实际只常用少数几个操作也会一起加载。

性能与稳定性问题来自 MCP 的中间进程层：服务要初始化、认证、维持进程、处理外部 round trip，还可能在会话中崩溃。文章引用 Jira MCP 对 REST API 的 benchmark：单次调用慢 3 倍，包含首次初始化时慢 9.4 倍；作者认为这不是 Jira 特例，而是协议架构天然多了一层。

CLI/API 的优势在于人机同构和可组合性：人和 LLM 用同一套命令，失败可以直接在 terminal 复现，输出能用 jq、grep、管道继续处理。作者用 Linear issue lookup 做 token 对比：curl + GraphQL 约 200 tokens，MCP 路线因为先背负 42 个 Linear tool definitions，总成本约 12,957 tokens，约为 CLI 方案的 65 倍。

## 更合理的替代路径
文章推荐的不是“去工具化”，而是 CLI-first + Skills：优先把已有 CLI/API、认证方式、常见命令、schema 和安全注意事项写成按需加载的 skill。这样模型只在需要 Linear、Postgres、AWS、GitHub 等具体任务时加载相关说明，而不是在整场会话中携带所有工具 schema。

Quandri 的实际策略是混用三种模式：gh、psql、aws 这类日常工具走 Bash + CLI；commit drafting、PR review 这类多步重复流程走 Skills；Slack、Linear、Notion 这种 CLI 不强或需要团队级 auth / permission scoping 的服务保留 MCP。这个分层比“全面 MCP 化”更接近工程现实。

## 值得质疑
文章自己的 update 已经承认 Claude Code 的 Tool Search with Deferred Loading 可把 MCP context usage 降低 85%+，这直接削弱了 Problem 1 的时效性。剩余的性能、调试、进程可靠性问题仍成立，但“MCP eats context”不再能作为当前 Claude Code 用户的决定性证据。

测量也偏工程经验样本：只来自 Quandri 的 4 个 server，token 用 4 chars/token 估算，工具定义大小从已加载 server schema 外推；它足以说明 MCP 的成本形态，但不足以证明所有 MCP 生态都低效。真正的判断标准应是：这个 MCP server 是否比 CLI/API 提供了额外的权限边界、认证封装、交互能力或非开发者可用性。

## 最后一层判断
MCP 没死，死的是“为了接入而接入”的 MCP 崇拜；当工具本质是一次 API 调用或 CLI 命令时，最强接口往往仍是可复现、可组合、按需教学的文本命令。
