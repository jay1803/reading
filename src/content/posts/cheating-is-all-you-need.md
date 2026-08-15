---
title: "Cheating is All You Need"
date: 2023-03-25T23:51:58Z
category: reading
description: "本文介绍了 Large Language Models (LLMs) 对软件工程产生的巨大影响，作者认为其重要性堪比 World Wide Web、IDEs 和 Stack Overflow。文章重点介绍了 LLMs 如何通过编码助手 (Coding Assistants) 提高开发者的生产力，并强调了拥有数据护..."
source: "https://about.sourcegraph.com/blog/cheating-is-all-you-need"
---

## TL;DR

本文介绍了 Large Language Models (LLMs) 对软件工程产生的巨大影响，作者认为其重要性堪比 World Wide Web、IDEs 和 Stack Overflow。文章重点介绍了 LLMs 如何通过编码助手 (Coding Assistants) 提高开发者的生产力，并强调了拥有数据护城河 (Data Moats) 对于构建成功的 LLM 应用至关重要。最后介绍了 Sourcegraph 的产品 Cody，一个利用 Sourcegraph 独特优势构建的 LLM 编码助手。

## 主题

### 🌋 Trillion-Dollar Money Volcano (万亿美金的火山)

LLMs 不仅是自社交、移动或云以来的最大变化，也是自 World Wide Web 以来最大的变化。在编码方面，它们是自 IDE 和 Stack Overflow 以来最大的事件，并且很可能会超越两者。许多伟大的技术突破最初都只是一个简单的 demo，例如 AWS、浏览器聊天、Kubernetes 和 Docker。LLMs 的技术突破也非同小可，其潜力巨大。

### 🤔 The Mehs Prevail (怀疑占上风)

尽管 LLMs 潜力巨大，但许多工程师对其持怀疑态度。Sourcegraph 内部调查显示，约 ⅔ 的工程师对 LLMs 用于编码持“Meh”或负面态度。许多开发者质疑 ChatGPT 是否能编写出可运行的代码。

### 💻 ChatGPT vs Emacs

为了反驳怀疑，作者用 ChatGPT 编写了一段 Emacs-Lisp 代码。ChatGPT 一次性生成了完全可工作的代码，并且代码质量很高。这证明了 LLMs 在编码方面的强大能力。除了编写代码，LLMs 还可以根据产品描述生成 Web 应用程序。

### 😠 Whining about Trust Issues (关于信任问题的抱怨)

作者批评了一些开发者对 LLM 生成的代码“不信任”的观点。他指出，软件工程的存在本身就是因为不能信任任何代码，所以才会有 reviewers、linters、debuggers、unit tests 等。LLM 可以帮助生成 80% 的代码，开发者只需修改剩下的 20%，这将带来 5 倍的生产力提升。

### 📜 A Brief Mini-History of LLMs (LLMs 简史)

2017 年，Google Brain 团队发表了名为《Attention is All You Need》的论文，介绍了 Transformer 架构。该架构取代了 AI 领域的几乎所有东西。随后，人们开始使用大量数据训练大型 Transformers，并称之为 Large Language Models (LLMs)。2022 年 11 月 30 日，OpenAI 推出了 ChatGPT，这是第一个基于 LLM 的聊天机器人。

### 🤖 A Brief Introduction to Coding Assistants (编码助手简介)

Coding Assistants 是位于 IDE 中的工具，可以与 LLM 通信。它们可以读取和解释代码、编写文档、编写代码、自动完成、诊断问题，甚至可以通过“代理”执行任意 IDE 任务。一些助手还具有对话/聊天界面。可以将 Coding Assistants 视为“实时的 IDE 内 Stack Overflow”，并结合了一组强大的样板自动化任务。

### 🧠 Training/fine-tuning vs Search (训练/微调 vs 搜索)

LLMs 在大量数据上进行训练，但不包括用户的代码。有两种方法可以让 LLM 更好地理解用户的代码：

1.  **Fine-tuning (微调):** 在用户的代码上微调 LLM。
2.  **Search Engine (搜索引擎):** 引入搜索引擎。可以将 LLM 比作一个了解编码的哈佛 CS 毕业生，微调就像让它仔细研究你的代码，而结合搜索引擎则使其更有效，因为它可以快速回答直接查询，并用于填充查询上下文。

### 📝 Cheating is All You Need (作弊是你所需要的)

Context Window 是传递给 LLM 的“备忘单”，用于告诉 LLM 关于用户代码的信息。目前，Context Window 的大小有限（最多约 100k 字符）。因此，如何填充 Context Window 至关重要。Data Moats 是指拥有他人无法访问的数据。在 LLM 领域，拥有 Data Moats 才能脱颖而出。因为 Data Moats 是填充 Context Window 的关键。拥有 Data Moats 的公司需要一个快速且可查询的 Sidecar Database，这是一个搜索问题。

### 🎉 Party Time (Sourcegraph 的优势)

Sourcegraph 已经花了十年时间构建了一个解决方案，正好满足了 LLMs 的需求。Sourcegraph 的平台具有四个难以复制的维度：

1.  **Universal (通用性):** 适用于所有代码托管和平台。
2.  **Scalable (可扩展性):** 适用于各种规模的企业。
3.  **Precise (精确性):** 在准确性和完整性方面可与 IDE 相媲美。
4.  **Open (开放性):** 公开透明地开发。

### 🤖 A Whirlwind Tour of Sourcegraph's Cody (Sourcegraph 的 Cody 简介)

Cody 是 Sourcegraph 新的 LLM 编码助手。Cody 了解用户的代码，具有模板化操作，例如编写单元测试、生成文档注释、总结代码等。Cody 具有聊天界面，这意味着它是完全开放式的，可以向它询问有关代码库或环境的任何问题。Cody 本身也是一个平台，可以用于构建自己的 LLM 工作流程。目前 Cody 是一个 VSCode 插件。Cody 的工作原理：

1.  用户要求 Cody 做某事（例如，“为这个函数编写一个单元测试”）。
2.  Cody 使用 Sourcegraph 的代码智能平台（搜索查询、嵌入检索、graphql 查询等）填充 Context Window。
3.  它将 Context+Query 发送到 LLM，并解析结果。
4.  它（可选）将结果插入回 IDE（取决于操作）。

## 总结

LLMs 将通过 Coding Assistants 极大地改变软件工程，而拥有 Data Moats (如 Sourcegraph 的代码智能平台) 是构建成功的 LLM 编码助手的关键。
