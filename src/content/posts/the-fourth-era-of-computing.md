---
title: "The Fourth Era of Computing"
date: 2026-05-21T05:49:55Z
category: reading
description: "AI agent 把“易用性”的判断标准从“人能不能顺手点击”改成了“机器能不能直接操作”。过去被视为丑陋、反人类、只适合高手的 CLI、配置文件、API、daemon、pipeable 工具，正在因为可被 agent 接管而变成更省力的路径；相反，漂亮但 GUI-only 的软件会把人重新拉回去当操作员。"
source: "https://danieldelaney.net/fourth-era/"
---

## TL;DR
AI agent 把“易用性”的判断标准从“人能不能顺手点击”改成了“机器能不能直接操作”。过去被视为丑陋、反人类、只适合高手的 CLI、配置文件、API、daemon、pipeable 工具，正在因为可被 agent 接管而变成更省力的路径；相反，漂亮但 GUI-only 的软件会把人重新拉回去当操作员。

## 核心主张拆解
作者把计算界面分成四个阶段：第一阶段是 terminal，所有东西都难，用户必须记命令、读手册；第二阶段是早期 GUI，用按钮和可发现操作把普通人从命令行里救出来；第三阶段是 late GUI，设计师与 user-centered design 让软件围绕人的体验竞争，很多优秀软件公司的声誉也建立在这套人本 GUI 上。

第四阶段的变化在于，操作软件的主体不再只有人。作者重装家庭影院 PC 时选择 Linux、Jellyfin、Caddy 等工具，不是因为 Linux desktop 本身终于对人友好，而是因为 agent 能处理 Linux 的文件、daemon、命令和配置。五年前这些东西意味着手动分区、改 config、查 PipeWire 错误；现在它们反而是 agent 最容易抓住的“hooks”。

这个反转改变了产品选择：过去的问题是“这个系统我用起来容易还是困难”，现在的问题是“这个系统是否容易到我根本不用亲自用”。Linux、开源工具、原始配置文件、terminal-first 应用，因为暴露了可组合、可读写、可脚本化的接口，变成 agent-native；macOS Settings 这类精致 GUI 反而像一堵墙，因为 agent 难以稳定操作，人必须去点击。

作者给用户的建议是选有 hooks 的 stack：Linux、开源、CLI、配置文件优先于封闭漂亮的 SaaS。给 builder 的建议更直接：如果产品只有 GUI，没有 CLI、配置、REST API、MCP 或类似接口，它服务的用户时代正在结束；能活下来的软件会是用户不必手工操作的软件。

## 值得质疑
文章强在判断方向，弱在边界条件。它默认 agent 足够可靠、可授权、可审计，但实际部署里权限、误操作、安全边界、状态可见性仍会决定哪些任务能交给 agent。GUI 也未必会消失，它可能退到监督、确认、异常处理和高语义编排层；真正被淘汰的不是 GUI，而是没有机器接口、只能靠人点击的孤岛式 GUI。

## 最后一层
第四时代的核心不是 terminal 复古，而是软件从 human-operable 转向 agent-operable；未来的“好界面”可能首先不是给人看的，而是给人的代理稳定执行的。
