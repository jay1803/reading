---
title: "Claude, Teach Me Something"
date: 2026-03-27T08:01:05Z
category: reading
description: "Socratic method 比直接解释更适合 LLM 教学：它迫使 Claude 先诊断你的知识边界再填空，而非倾倒信息——这让 LLM 的两个底层优势（非确定性选题 + 文本问答）同时生效。"
source: "https://hugotunius.se/2025/10/26/claude-teach-me-something.html"
---

## TL;DR
Socratic method 比直接解释更适合 LLM 教学：它迫使 Claude 先诊断你的知识边界再填空，而非倾倒信息——这让 LLM 的两个底层优势（非确定性选题 + 文本问答）同时生效。

## 核心洞见
作者把"无聊时刷 Reddit"替换成对 Claude 说"Teach me something"。关键不是"让 AI 讲课"，而是用 Claude 项目的持久记忆 + 自定义 prompt 构建一个阻力最小的学习拦截器：无聊时有地方去，且每次话题都不重复。

## 具体机制
- **Prompt 结构**：在项目 system prompt 中列出按熟悉度递减的兴趣领域（编程 → 计算机科学 → UX → 网络安全 → 机器学习 → 烹饪 → 物理 → 经济学 → 心理学……），Claude 选题时会参考这个权重。
- **每次流程**：Claude 先查项目历史会话避免重复 → 选题 → 用问答摸底已知知识 → 引导发现，而非直接讲解。
- **收尾机制**：每次结束时要求 Claude 提供一手资料（网页 > 论文 > podcast > 书），兼具防幻觉和后续延伸两个功能。

## 隐藏限制
- Claude 没有重命名会话的工具调用；每次需手动在客户端改名（否则所有会话都叫"Learn something new"，项目历史记忆失效）。
- 话题多样性依赖项目内聊天记录的积累，新项目初期重复率可能偏高。

## 这个工作流的真正价值
它解决的不是"如何高效学习"，而是**无聊时刻的默认行为**：把 Reddit 的位置替换掉。学习效率是副产品，拦截效果才是设计目标。
