---
title: "Quoting Steve Yegge"
date: 2026-08-17T17:54:46Z
category: reading
description: "Opus 4.7 引入的「还有两件事」tic 让 Steve Yegge 的 AI 编码工具 Gas Town 陷入永久自我打磨循环，无法执行真实任务，最终彻底报废。"
source: "https://simonwillison.net/2026/Aug/4/steve-yegge/"
---

## Opus 4.7 的"还有两件事"tic 直接摧毁了 Yegge 的 Gas Town

Steve Yegge 建造了 Gas Town——一个为 AI 辅助开发设计的工具，其特殊之处在于它用自身来构建自身。在 Claude Opus 4.6 及更早版本中，Gas Town 运转良好。但 Opus 4.7 引入了一个行为 tic：模型陷入"just two more things"的循环，永远觉得 Gas Town 本身还需要再打磨两件事，导致它始终无法切换到执行真实任务的状态。这种无法收敛的行为让 Gas Town 彻底报废。Yegge 承认 Gas Town 还有其他问题，但 4.7 是压垮它的最后一根稻草。

这个案例说明 LLM 版本升级并非总是改进：单次版本迭代可以引入破坏性的行为退化，直接让深度依赖该模型的工具失效。把特定模型版本嵌入产品核心的开发者面临真实风险——模型厂商的"升级"不保证行为向后兼容。
