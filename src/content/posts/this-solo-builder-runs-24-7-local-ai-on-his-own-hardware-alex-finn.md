---
title: "This solo builder runs 24/7 local AI on his own hardware | Alex Finn"
date: 2026-07-14T08:02:35Z
category: reading
description: "买 Mac Studio 最常见的质疑：一台机器够 11 年 ChatGPT 订阅费，为什么值？Alex 的答案不是算 ROI——而是用例边界。云端 API 按 token 计费，用量有上限；本地模型无限推理，允许 24/7 不间断烧 token 做事。这个差距让整整一类任务（持续安全扫描、社媒信号监控、自动代码..."
source: "https://www.lennysnewsletter.com/p/this-solo-builder-runs-247-local"
---

## 本地 AI 的核心逻辑：用例解锁，不是 ROI 对比

买 Mac Studio 最常见的质疑：一台机器够 11 年 ChatGPT 订阅费，为什么值？Alex 的答案不是算 ROI——而是用例边界。云端 API 按 token 计费，用量有上限；本地模型无限推理，允许 24/7 不间断烧 token 做事。这个差距让整整一类任务（持续安全扫描、社媒信号监控、自动代码审查）从经济上不可行，变成静默运行的背景任务。

## 三类硬件路线的真实取舍

Alex 自己拆了四象限：

- **Mac Studio 512GB**：统一内存可跑 GLM 5.2（接近 Opus 4/8 级别），但内存带宽极低，单个 prompt 要等 5 分钟。慢但聪明，适合对延迟不敏感的任务。
- **DGX Spark（$4,000-4,600）**：128GB 统一内存 + NVIDIA CUDA，甜蜜点。跑 Qwen 3.6 速度合理，即插即用，连显示器都不需要。
- **RTX 5090（32GB VRAM）**：带宽极高，接近云端速度，VRAM 小但够快，适合需要即时响应的任务，还能打游戏。
- **老设备（Mac Mini / 旧笔记本）**：跑小模型（Gemma 4、embedding）或作为并行节点分担 Claude Code 工作树。

## 模型分工：用 SDR/Closer 框架想清楚

精髓在错位匹配，而不是用最强模型做所有事。GLM 5.2（慢但聪明）每次跑安全扫描，结果汇成每日 markdown 报告（他今天的报告有 374 条 findings）。Claude Code 的 /loop 每天扫一次报告，核查哪些是真漏洞并修复。本地模型 = SDR（初筛），Claude Code = Closer（决策行动）。Qwen 3.6 则全天监控 Twitter / Reddit / Hacker News / Product Hunt 找市场信号——这个任务不需要高智力，只需要速度。

## 软件工厂：Build Loop + Review Loop + 火箭 Emoji

他把网上流行的 "vague loop posting" 拆开示范了：早晨与 Claude 对话生成当天任务 → 两条 Claude Code 循环自动运行（build loop 持续构建，review loop 让另一个 agent 复审并修代码）→ 完成后 Slack 推送，他留一个 🚀 = 合并，Vercel 自动生成 preview 地址供测试。开发模式从"全天手把手提示"变成"早晨对话，傍晚审批"。

他对 vague posting 的解释值得记：大公司刻意不分享 loop 细节，因为这是最后一条护城河——AI 工程基础设施效率直接决定代码输出量，分享等于主动放弃竞争壁垒。

## OpenClaw 感情上赢，Hermes 可靠性上赢

Alex 同时运行两者：2 个 OpenClaw + 3 个 Hermes = 5 个 agent，常态下 3 个同时挂掉，另外 2 个负责修复。OpenClaw 给他的 wow 时刻更多，但连续一段时间每次更新都需要花半小时修复，熬不住。Hermes 从未出过这个问题，但没有"aha 时刻"。他的最终架构：一个专属"救生员" OpenClaw 只负责监控其他 agent，轻易不升级，保持稳定。

Claire 的相似解法：一个 OpenClaw 充当 lifeguard，只负责维持其他 agent 存活，不承担实际业务任务。

## Tailscale 是多机本地 AI 的基础设施

即使只有一台机器也值得装（手机可以通过 Tailscale 访问本地 localhost，直接测试 vibe coding 出来的 app）。多机场景下，Tailscale 构建私有网络，OpenClaw / Hermes 作为 IT 工程师可跨设备安装模型、配置运行环境，整个过程零技术门槛。

## 当前最爱本地模型：Ornith 1.0

在 Qwen 3.6 上用了 5 个月，最近切到 Ornith 1.0（35B）——某团队在 Qwen 基础上做了强化学习优化，每个编码 eval 都超过原版，且更快。可跑 DGX Spark。Alex 注意到这个模型很新，对团队背景了解为零，但 eval 数据说话。
