---
title: "Old and new apps, via modern coding agents"
date: 2026-08-21T00:59:00Z
category: reading
description: "陶哲轩用 AI coding agent 数小时内将 1999 年搁置的 Java applet 复活、移植为 JavaScript，并将两个积压 27 年的项目当天落地，明确了 LLM 辅助编程的可接受风险边界。"
source: "https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/"
---

## AI coding agent 把数学可视化从"永久积压"变成数小时消耗品

陶哲轩的 1999 年 Java 1.0 applet 因浏览器标准变化而失效。他用 AI agent 在数小时内将约 24 个 applet 移植到 JavaScript，全部复活，且有图形升级（Besicovitch 集从单色变彩色）。

移植质量的实证评估：全程只发现 1 个 bug（某复分析 applet 的拖拽事件越界），但 agent 反过来识别出原代码中 2 个陶哲轩自己未曾察觉的 bug，净效果为正。

### AI agent 使两个搁置多年的项目成真

- **狭义相对论时空图**：1999 年的构想，目标是"Minkowski 空间中的 Inkscape"，当年因代码复杂性放弃，现在用 AI vibe coding 数小时后落地，附 making-of 对话记录。
- **Gilbreath 猜想可视化**：当天写完论文博文后即兴决定添加可视化工具，同日完成。

### 可接受风险的边界

陶哲轩明确了适用条件：工具必须是"次要视觉辅助"，不能是数学论证的核心组件。在此边界内，LLM 生成代码的 downside 风险可接受——他不会用同样方式处理证明验证或核心算法实现。

### 意义

AI agent 降低的不只是编程工时，而是一类创意摩擦：当实现成本长期高于创意价值时，好想法会永久搁置。这个案例显示，AI 有效降低了这个阈值，使 27 年前的构想可以在当天落地。
