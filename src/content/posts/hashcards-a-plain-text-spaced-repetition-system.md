---
title: "Hashcards: A plain-text spaced repetition system"
date: 2026-02-14T20:35:18Z
category: reading
description: "间隔重复系统最大的瓶颈不是复习纪律，而是录入摩擦——每一张因嫌麻烦没写的卡片，都是永久丢失的一块知识。"
source: "https://borretti.me/article/hashcards-plain-text-spaced-repetition"
---

## TL;DR
间隔重复系统最大的瓶颈不是复习纪律，而是录入摩擦——每一张因嫌麻烦没写的卡片，都是永久丢失的一块知识。

## 核心洞见
Anki 与 Mochi 各解决了不同的问题，但没有系统同时解决两者：Anki 算法（FSRS）优秀、界面极差；Mochi 界面流畅，但算法（基于乘数的 SM-2 变体）在长期记忆衰退时几乎无效——忘掉一张 60 天间隔的卡片，算法只把间隔缩到 30 天，等于没有帮助。作者因此在 1700 张卡片过期后放弃了 Mochi。

## 具体机制
Hashcards 的核心设计：闪卡就是目录中的 Markdown 文件；调度历史存入 SQLite；卡片用内容 hash 寻址。格式细节全部服务于"减少录入摩擦"：cloze 用方括号（无需 shift），Q/A 格式用单字符前缀，单文件对应单个 deck，方便就地编辑和版本控制。Markdown + Git 带来 Anki note types 的 DIY 替代：可用脚本批量从结构化数据（如 CSV 词表）生成卡片，用 Makefile 串联整个流程；可用标准 Unix 工具查询和批量修改；可公开分享卡片库。

## 隐藏限制
内容寻址（hash 定位卡片）意味着编辑卡片文字会改变 hash，旧调度数据自动失效——对频繁修订的卡片，记忆曲线需要重新建立，文章未说明是否有平滑迁移机制。

## 本质
让知识真正固化的系统，必须把录入阻力压到接近零——hashcards 每一个设计决策（方括号、不用 shift、纯文本文件）都是在对抗人类在"再写一张"时的自然惰性。
