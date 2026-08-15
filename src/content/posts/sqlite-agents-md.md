---
title: "sqlite AGENTS.md"
date: 2026-05-29T08:01:14Z
category: reading
description: "SQLite 的 AGENTS.md 不是在邀请 AI 直接改 SQLite，而是在把边界写给外部 coding agents：可接受的是带可复现测试用例的 agentic bug report，不接受 agentic code；PR 最多作为 proof-of-concept 供人类维护者参考，并且还要满足 S..."
source: "https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything"
---

## TL;DR
SQLite 的 AGENTS.md 不是在邀请 AI 直接改 SQLite，而是在把边界写给外部 coding agents：可接受的是带可复现测试用例的 agentic bug report，不接受 agentic code；PR 最多作为 proof-of-concept 供人类维护者参考，并且还要满足 SQLite 对公共领域授权的法律要求。

## 关键时刻
- SQLite 近期新增 AGENTS.md，目标读者更像是把 coding agent 指向 SQLite 仓库的外部开发者，而不是 SQLite 内部团队。
- 文件明确说 SQLite 不接受未经事先同意或缺少法律文件的 pull request，因为项目要求贡献进入 public domain。
- 最新一次相关提交删除了 “currently” 这个缓冲词，提交信息是 “Strengthen the statement about not accepting agentic code”，把“不接受 agentic code”从临时态度变成更强硬的项目规则。
- SQLite forum 已经被大量 AI 生成 bug reports 淹没，质量参差不齐；项目方因此把这类问题拆到新的 SQLite Bug Forum。

## 背后逻辑
SQLite 的策略不是拒绝 AI 提供任何价值，而是只接受可验证、低信任成本的产物。可复现测试用例能把维护者的判断负担压到具体行为上；agent 写出的 patch 则会引入代码质量、版权归属、公共领域授权和维护责任等多重问题。

这也解释了为什么 proof-of-concept patch 可以“被看”，但不会直接“被收”。SQLite 维护者可以从外部补丁中理解 bug 形态或修复方向，再由项目内部重新实现，以保留代码所有权、风格一致性和责任边界。

## 更大意义
成熟开源项目正在被迫为 coding agents 建立明确入口规则。过去贡献规范主要面向人类开发者，现在还要处理机器批量生成的 issue、patch 和半成品诊断材料。SQLite 的做法给出了一个可能模板：接受机器辅助发现问题，但把最终代码路径牢牢留在人类维护系统里。

**证据薄弱处**
原文是短篇 link blog，只给出了 forum 被 AI bug report 淹没的判断，没有提供数量、样本分布或具体质量案例；因此它更适合作为一个开源治理信号，而不是对 AI bug report 整体质量的统计结论。

真正值得看的不是 SQLite “反 AI”，而是它把 AI 贡献拆成了不同信任等级：测试用例可以进入讨论，补丁只能当线索，最终代码仍由维护者掌控。
