---
title: "After two years of vibecoding, I'm back to writing by hand"
date: 2026-02-14T20:39:06Z
category: reading
description: "逐行 review 过 AI 代码、甚至用详细 spec 驱动 agent，并不能防止烂代码积累——因为 agent 优化的是\"看起来合理的局部\"，不是\"结构完整的整体\"。作者通读 codebase 后发现是纯粹的 slop，随即回归手写；综合算下来，手写比 AI 更快、更准确、更有创造力。"
source: "https://atmoio.substack.com/p/after-two-years-of-vibecoding-im"
---

## TL;DR
逐行 review 过 AI 代码、甚至用详细 spec 驱动 agent，并不能防止烂代码积累——因为 agent 优化的是"看起来合理的局部"，不是"结构完整的整体"。作者通读 codebase 后发现是纯粹的 slop，随即回归手写；综合算下来，手写比 AI 更快、更准确、更有创造力。

## 两个失败路径

spec 驱动失败：设计文档在现实中是随实现动态演化的，agent 做不到这点——它在开头锁定决策，后续不修正，遇到失控的问题会强行推进而不是退回来重想。把一份一小时写完的规格文档交给 agent 并告诉它"不要问任何问题"，是对软件开发过程本质的误解。

review 流程失败：AI 写的代码在 PR 粒度上有说服力——合乎语法、自洽、符合 prompt。但 agent 对整体结构、跨单元关系、相邻模式没有任何尊重。作者把几个月的 agentic 代码一起通读，发现"我们以为是早期模型残留问题的 slop"其实一直在增长。

## 为什么 review 是错觉

slop 不是因为你漏审了某一行，而是在你批准每一行的过程中，在整体层面悄悄结构性地积累的。每一段都合理，整个章节却是乱的——用作者自己的比喻：AI 在给你讲一个好故事，而不是在帮你建一个能运转的系统。

## 留下来的那个问题
"把 review 做得足够细"这个假设本身就是错的——那个粒度恰好是 agent 最擅长欺骗你的粒度。
