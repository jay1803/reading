---
title: "Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue"
date: 2026-05-30T08:04:01Z
category: reading
description: "这篇文章和 60 秒小游戏想证明：AI coding agent 的“人工确认”安全模型会被高频、相似、带时间压力的权限请求快速稀释，用户最终会变成机械批准者；真正的防线应转向沙箱、权限边界、网络/文件系统隔离、hooks 和受控自动模式的组合，而不能把安全责任主要压在用户逐条读命令上。"
source: "https://llmgame.scalex.dev"
---

## TL;DR
这篇文章和 60 秒小游戏想证明：AI coding agent 的“人工确认”安全模型会被高频、相似、带时间压力的权限请求快速稀释，用户最终会变成机械批准者；真正的防线应转向沙箱、权限边界、网络/文件系统隔离、hooks 和受控自动模式的组合，而不能把安全责任主要压在用户逐条读命令上。

## 核心主张拆解
作者用小游戏模拟 Claude Code 权限疲劳：在一分钟内连续判断命令是否安全，场景包含正常工程命令、越权读取、凭证泄露、外部上传、持久化修改、恶意依赖与 prompt injection。游戏的关键设计是把危险命令包装成合理工程理由，让用户体验“看起来都像正常开发动作”的判断压力。

文章列出的真实风险有四类：破坏性命令，例如误删 home 目录；凭证外泄，例如读取 AWS/SSH key；越界访问，例如离开项目目录读取个人文件；prompt injection，例如网页、邮件、README 或文档内容被 agent 当成下一步指令。作者还强调，仓库自带 Claude settings、外部 skills、MCP servers 和插件都可能成为可更新的攻击面。

文章对纯人工审批的批评很具体：Anthropic 遥测显示用户大约批准 93% 的权限提示，提示越多，单条提示获得的注意力越少。即使用户认真读每条命令，权限模型仍有盲点：agent 可以先改文件，再请求运行一个表面无害的 `npm run build`，真正危险行为藏在脚本链里。

## 可用防线
Auto mode 试图用本地 fast filters、服务端扫描和 agent 执行前复核减少提示噪音，但作者指出它仍有代价：Anthropic 报告存在 17% false-negative rate，且会把危险命令错误关联到此前的同意信号。它能减轻疲劳，却不能替代边界隔离。

PreToolUse hooks 可以拦截 `rm -rf /` 等典型破坏性模式，也能补足沙箱未覆盖的规则；限制是它本质上偏 blocklist，对 base64、shell 管道、间接脚本、混淆命令等绕过方式并不稳。hooks 更适合作为第二层，而不是唯一防线。

Claude Code 的 `/sandbox` 模式更接近结构性防线：只允许写工作目录、对新网络域名提示确认、阻止 bash 访问工作目录之外的文件。更激进的路线是把 agent 放进 devcontainer、云端托管环境或 hypervisor 沙箱，再配合代理检查外发流量；这样可以运行 `--dangerously-skip-permissions`，但前提是容器内凭证和可访问资源本身也被最小化。

## 反驳或薄弱处
文章把小游戏表现和真实工作流疲劳连接起来是合理的，但证据主要来自安全直觉、案例枚举和 Anthropic 公开数字，没有系统比较“人工审批、Auto mode、sandbox、hooks、devcontainer”在不同任务类型下的误杀率、漏报率和生产力成本。

一些风险例子偏安全教育型，适合训练用户识别危险模式；但真正困难的部分是供应链与间接执行，例如 `npm run build`、README 注入、依赖 postinstall、全局配置修改。这类问题无法靠肉眼审批单条 bash 命令稳定解决。

## 最后一层判断
这篇文章最有价值的提醒是：当 agent 能读写文件、执行脚本、安装依赖、接触凭证和访问网络时，权限提示只是交互层，安全边界必须落到执行环境、凭证范围和可观测外发流量上。
