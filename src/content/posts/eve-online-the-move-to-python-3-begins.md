---
title: "EVE Online: The Move to Python 3 Begins!"
date: 2026-09-21T09:33:21Z
category: reading
description: "EVE Online 启动从 Stackless Python 2.7 向 Python 3 的迁移，需处理 240 万行代码和约 2 万处 Python 2/3 行为差异，未来可能延伸到调度基础设施重构。"
source: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
---

EVE Online 正式启动从 Stackless Python 2.7 向 Python 3 的迁移，这项工程的特殊之处在于，它要改造一个自 2003 年上线以来持续运行、上一次重大语言升级已是 16 年前的超大型游戏代码库。EVE Online 二十多年来一直是 Python 大规模应用的重要案例：游戏发布时便采用 Stackless Python，直到 2010 年才升级至 Stackless Python 2.7，此后核心技术栈长期停留在 Python 2 时代。

迁移将首先对 240 万行代码运行 **futurize** 脚本，自动完成一部分兼容性转换；随后，开发团队还要人工审查约 2 万处 Python 2 与 Python 3 行为不同的代码。此类差异可能直接改变程序语义，例如 `1 / 2` 在 Python 2 中等于 `0`，在 Python 3 中则等于 `0.5`，因此自动改写只能作为起点，真正困难的是逐处确认旧代码原本依赖的行为，并保证转换后游戏逻辑不发生隐蔽偏差。

公告没有说明 EVE Online 将如何替代 Stackless，但 CCP 已在较新的游戏 EVE Frontier 中探索了迁移路径。团队在去年的会议演讲 **Scheduling in Carbon: Leaving Stackless Python Behind** 中介绍，他们已让 Carbon 引擎脱离 Stackless，并以如今开源的 **carbonengine/scheduler** 库接管调度功能。这表明 EVE Online 的 Python 3 升级不仅涉及语法和运行时行为兼容，也可能最终延伸到对运行二十多年的并发调度基础设施的重构。
