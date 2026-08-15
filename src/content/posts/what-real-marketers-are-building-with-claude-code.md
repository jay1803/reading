---
title: "What real marketers are building with Claude Code"
date: 2026-03-03T23:53:57Z
category: reading
description: "把框架、评审流程、竞品情报等已有的营销工作直接编码成可复用 Claude Skill，比\"用 AI 写内容\"效率高一个量级——而且无需写一行代码。"
source: "https://newsletter.mkt1.co/p/real-marketers-claude-code-builds"
---

## TL;DR
把框架、评审流程、竞品情报等已有的营销工作直接编码成可复用 Claude Skill，比"用 AI 写内容"效率高一个量级——而且无需写一行代码。

## 核心洞见

五个真实构建案例：

1. **Homepage Positioning（作者自建）**：输入任意 URL，对照 MKT1 定位框架打分（Hero + 全页分别给字母等级），并输出具体改写建议。经过四轮基于真实客户案例的迭代，从 60% 完成度提升到 90%。

2. **Marketing Advantages（作者自建）**：两阶段 Skill——先通过四轮提问从 12 个优势类别中识别核心优势，再压测每条优势的具体性与成熟度。验证方式：拿课程学员的真实提交对比 Skill 输出与作者手写反馈，结论一致。

3. **Customer Lookalike Outbound（Elaine Zelby）**：每周自动从 HubSpot 成交记录中提取结构化数据 → 用 Clay 找 10 家同类公司 + 每家 3-5 个联系人 → 生成 4 封邮件序列 + LinkedIn DM 草稿 → 推送 Slack 供人工确认。接入 HubSpot、Clay、Slack 的 MCP Connector，可无人值守运行。

4. **Humanizer（Aditya Vempaty）**：对 AI 生成文案打四维评分（AI 感、真实感、读者价值、领域可信度，各 1-10 分），标出具体 AI 化模式后按本人语音风格改写；每次运行后要求 Claude 自动更新 Skill 本身，累积迭代。

5. **LinkedIn Ad Intel（Kamil Rextin）**：调用预建的 /competitors skill 获取竞品列表 → 抓取各公司 LinkedIn 广告 → 分析信息主题与投放量变化 → 自动生成 PDF 情报报告。通过 GitHub + Railway + Vercel 部署，每周定时运行，不依赖本地终端。

## 具体机制

- **Skill = .md 文件**：Claude 收到触发词时读取，相当于给它注入专属知识 + 行为规则；可以在 Chat / Cowork / Code 之间手动搬运，但目前没有自动同步。
- **构建路径**：先把 ICP / 人设 / 定位消息等基础 Skill 建好，再在上面叠加 workflow —— Elaine 把这一步视为构建 agent 的前提条件。
- **Plan mode 先于执行**：Kamil 的做法——复杂项目在 Plan mode 里把输出结构确认好，再切换到"Ask Permission"逐步执行，减少信用消耗和混乱。
- **用真实案例迭代**：每次 Skill 运行完，对比手工输出找差距，告诉 Claude 怎么改，然后让 Claude 更新 Skill 文件。

## 隐藏限制

Claude Code 在本地终端运行时，若终端关闭 agent 就停；托管到 web 需要额外配置 GitHub + Railway / Vercel，这步有真实技术门槛——虽然 Claude Code 可以协助配置，但不能完全替代理解。另：三个 Claude 产品（Chat / Cowork / Code）之间的 Skill 无法自动同步，现阶段仍需手动搬运 .md 文件。

## 值得关注

这篇的真正信号：营销人开始把「如何思考」而非「如何执行」编码进 AI——定位框架、竞品判断、语音风格都变成了可复用模块。当 Skill 开始调用 Skill（Kamil 的 /LinkedIn-ad-intel 先调 /competitors），这不再是"提示词工程"，而是知识工程。
