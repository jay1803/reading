---
title: "A random variable visualizer"
date: 2026-07-14T08:01:56Z
category: reading
description: "Tao 2016 年提出用动画展示随机变量的想法，因编程复杂度一直搁置。本周用编程代理几小时内完成原型：一个 Web 应用，内置针对随机变量的小型自定义编程语言（Python 与 Excel 的简化混合），支持变量引入、算术运算、条件化操作，输出动画或文本可视化。"
source: "https://terrytao.wordpress.com/2026/07/12/a-random-variable-visualizer/"
---

## 编程代理让十年积压的可视化想法在数小时内变为可用原型

Tao 2016 年提出用动画展示随机变量的想法，因编程复杂度一直搁置。本周用编程代理几小时内完成原型：一个 Web 应用，内置针对随机变量的小型自定义编程语言（Python 与 Excel 的简化混合），支持变量引入、算术运算、条件化操作，输出动画或文本可视化。

### Berkson 悖论作为演示

截图展示的 demo 是 Berkson 悖论——两个独立变量在施加条件化后出现相关性。这是统计推断中常见但反直觉的陷阱，动画比公式更直观地揭示这个现象。

### 含义

Tao 明确定位为"次要视觉辅助"，不要求 100% 无 bug。这个定位判断值得注意：代理生成的原型质量足够用于教学演示，但不适合关键任务。更大的隐含结论是：数学家维护可视化工具的门槛已显著下降，那些"想法不错但写代码太费时"的积压项目现在可以批量实现。

- App: https://teorth.github.io/tao-web/apps/random-variables.html
- Making-of: https://teorth.github.io/tao-web/apps/random-variables-making-of.html
