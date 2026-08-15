---
title: "Less is safer: Reducing the risk of supply chain attacks"
date: 2025-10-09T23:33:59Z
category: reading
description: "供应链攻击的根本解法不是审计依赖，而是少要依赖——Obsidian 将核心功能（Canvas、Bases）从零自研，中型模块在许可证允许时直接 fork 内化，只有 pdf.js / Mermaid / MathJax 这类大型库才保留外部版本，且版本锁死、只在有安全修复时才升级。"
source: "https://obsidian.md/blog/less-is-safer/"
---

## TL;DR
供应链攻击的根本解法不是审计依赖，而是少要依赖——Obsidian 将核心功能（Canvas、Bases）从零自研，中型模块在许可证允许时直接 fork 内化，只有 pdf.js / Mermaid / MathJax 这类大型库才保留外部版本，且版本锁死、只在有安全修复时才升级。

## 三层依赖策略

- **小工具函数**：内部重新实现，不引入外部包。
- **中型模块**：fork 入代码库，切断上游更新通道。
- **大型不可替代库**（pdf.js、Mermaid、MathJax）：version-pinned 静态文件，不随上游滚动升级；升级时逐行阅读 changelog + 新增子依赖审查 + 全平台手测。

同时禁止所有 postinstall 脚本——这一条单独就能堵住 npm 生态最常见的任意代码执行入口。

## 为什么慢升级是护城河

刻意滞后的升级节奏制造了一个"早期预警窗口"：当上游恶意版本被发布后，社区和安全研究者有时间在 Obsidian 纳入之前发现并曝光它。这把被动防御变成了群体免疫。

**值得质疑**：该策略对尚未被公开披露的零日攻击无效；版本锁死积累的技术债也是隐形风险，pdf.js CVE-2024-4367 说明即便是"已审查的版本"也能携带已知漏洞。

## 留下来的那个想法
大多数安全文章教你怎么检查依赖；这篇教你怎么不拥有依赖。两者是不同数量级的防御姿态。
