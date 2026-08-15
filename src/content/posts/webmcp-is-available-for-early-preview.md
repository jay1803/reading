---
title: "WebMCP is available for early preview"
date: 2026-03-04T00:22:27Z
category: reading
description: "WebMCP 通过 Declarative API 和 Imperative API 为网站提供“面向 AI agent 的结构化操作接口”，目标是替代低可靠的纯 DOM 操作，让代理在支持、购物、出行等流程里更快、更稳、更精准地代表用户执行任务；当前处于 Early Preview Program 阶段，适合尽..."
source: "https://developer.chrome.com/blog/webmcp-epp"
---

## TL;DR
WebMCP 通过 Declarative API 和 Imperative API 为网站提供“面向 AI agent 的结构化操作接口”，目标是替代低可靠的纯 DOM 操作，让代理在支持、购物、出行等流程里更快、更稳、更精准地代表用户执行任务；当前处于 Early Preview Program 阶段，适合尽早原型验证。

### 主题
#### WebMCP 的核心定位：让网站主动定义 agent 如何与自己交互
WebMCP 的关键不是再造一个自动化框架，而是让网站把“可执行能力”显式暴露给 AI agent。这样 agent 不再靠猜测页面结构和脆弱选择器执行操作，而是沿网站提供的结构化入口完成任务。

#### 两类 API 分工：简单流程声明化，复杂流程编程化
WebMCP 提出两种交互接口，对应不同复杂度的业务流程。

##### Declarative API
用于可由 HTML form 明确表达的标准动作，适合规则清晰、字段固定、步骤可预期的流程。

##### Imperative API
用于需要 JavaScript 执行的复杂动态交互，适合多步骤、条件分支、状态联动较强的任务。

#### 为什么比原始 DOM actuation 更可靠
在原始 DOM 驱动模式下，agent 易受页面结构变化影响。WebMCP 通过结构化工具接口降低歧义，提高执行稳定性与性能，并减少因 UI 微调导致的自动化失效。

#### 典型业务场景
- Customer support：自动补全技术细节，帮助用户更快创建高质量工单。
- Ecommerce：更准确地检索商品、配置选项、推进结账流程。
- Travel：更稳定地完成航班搜索、筛选与预订，减少参数错配。

#### 当前阶段与接入路径
WebMCP 目前对 Early Preview Program 参与者开放，重点在原型验证与能力探索。加入 EPP 后可获得文档与 demo，并跟进 API 变更。

#### 对产品与平台团队的直接启示
- 将高价值、高频、可结构化的用户任务优先暴露为 agent 工具。
- 先用 Declarative API 覆盖标准流程，再对复杂关键链路补 Imperative API。
- 把“agent 可执行性”纳入站点能力建设，而不只把 agent 当外部流量入口。

### 总结
WebMCP 的本质是把网站从“被 agent 解析”升级为“向 agent 提供可执行协议”，从而在 agentic web 中获得更高的交互确定性与任务完成率。
