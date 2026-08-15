---
title: "Spanish legislation as a Git repo"
date: 2026-03-29T17:23:59Z
category: reading
description: "Git 的版本控制模型和立法修订语义几乎完全吻合：每部法律是一个 Markdown 文件，每次修正是一个 commit（时间戳 = 官方发布日期，message 含修正标识符和原文链接）——legalize-es 用这一对等性把 8600 部西班牙法律塞进了标准 Git 仓库，不需要专用数据库或自研查询接口。"
source: "https://github.com/EnriqueLop/legalize-es"
---

## TL;DR

Git 的版本控制模型和立法修订语义几乎完全吻合：每部法律是一个 Markdown 文件，每次修正是一个 commit（时间戳 = 官方发布日期，message 含修正标识符和原文链接）——legalize-es 用这一对等性把 8600 部西班牙法律塞进了标准 Git 仓库，不需要专用数据库或自研查询接口。

## 具体机制

- 数据来源：BOE 官方开放数据 API，文本本身是公有领域；项目只增加了结构、版本历史和 YAML frontmatter（标识符、发布日期、最后更新、vigente/derogado 状态）
- 覆盖范围：宪法、刑法、劳工法等全部国家级"合并"立法，共 8600+ 部，完整修订链从 1960 年起
- 用法：`git log` 即修订史，`git diff <commit>^..<commit>` 即精确法条对比，`grep` 即全文检索——工具链是所有懂 git 的人的公共知识

## 隐藏限制

- 仅覆盖国家级 consolidada 文本，不含地方/自治区法规
- legalize.dev API 尚未上线，目前唯一使用方式是本地 clone（仓库体积未披露）
- 数据准确性上游依赖 BOE API；发现错误只能开 issue，无法在 repo 内自行修正

## 收束

这不是个演示——仓库已上线、8600 部法律、历史从 1960 年起。真正的问题是：为什么其他国家的官方立法数据还不是 Git 仓库格式。
