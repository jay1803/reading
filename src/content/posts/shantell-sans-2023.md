---
title: "Shantell Sans (2023)"
date: 2026-06-01T08:01:18Z
category: reading
description: "Shantell Sans 的核心价值不是“又一个手写字体”，而是把个人笔迹、可读性、开源分发和可动画的 variable font 能力压进同一个字体系统：它保留 Shantell Martin 手写线条的亲近感，同时用专业字体工程让这种亲近感可以被网页、应用、演示文稿、Google Docs 和多语言排版稳定调用。"
source: "https://shantellsans.com/process"
---

## TL;DR
Shantell Sans 的核心价值不是“又一个手写字体”，而是把个人笔迹、可读性、开源分发和可动画的 variable font 能力压进同一个字体系统：它保留 Shantell Martin 手写线条的亲近感，同时用专业字体工程让这种亲近感可以被网页、应用、演示文稿、Google Docs 和多语言排版稳定调用。

## 核心机制
- 设计起点来自 Shantell Martin 的真实手写与 dyslexia 经验：她把字看作 drawing，希望字体降低人们面对文字时的压迫感，尤其是对阅读困难者更友好。
- “new Comic Sans”不是复刻 Comic Sans，而是抽取它的有效部分：日常用户能接受、情绪上更开放、低门槛、适合普通沟通场景。
- Stephen Nixon 将 Shantell 的 felt-tip marker handwriting 数字化，但没有直接 auto-trace；他规范化了高度、宽度、spacing、cap-height、x-height 和默认 line-height，让它接近 Roboto 等常用字体的使用预期。
- 易读性来自具体字形区分：b/d/p/q、n/u、I/l/1 等容易混淆的字符被用 exit strokes、serifs、flags 等细节拉开差异；a 和 g 采用 single-story form，维持儿童书写里的熟悉感。
- 字体不只提供 Weight 和 Italic，还加入 Informality、Bounce、Spacing 等 variable axes，让文字可以在规范性、手写不规则性、上下跳动和字距之间连续调节。

## 关键设计取舍
- 项目一直在“像真实手写”和“像可用字体”之间折中：太原始会混乱，太规整会失去 Shantell 的线条生命力。
- Informality 轴把规范化字形与更不规则的手写来源做 interpolation；Bounce 轴通过脚本让字形上下偏移；多个字母、数字和符号 alternate 被 pseudo-random 轮换，形成更像活字书写的运动感。
- Google Fonts 的支持把项目从个人字体扩展成公共字体基础设施：加入 Italic、Spacing、Vietnamese 字符、更多 currency symbols，并扩展到 Cyrillic Plus。
- Cyrillic 不是机械补字形，而是“翻译手写风格”：Anya Danilova 需要判断哪些 Cyrillic 形状在 Shantell Sans 中“感觉对”，还针对 Bulgarian、Serbian 等语言咨询本地设计师，避免相似字母混淆。

## 更大意义
Shantell Sans 把一个高度个人化的笔迹释放成开放字体：OFL 授权、Google Fonts、Google Docs、GitHub 下载，使它能被儿童、创作者、品牌、web 工具和普通文档共同使用。它已经出现在 Whitney Museum shop key tags、Cash App Cash Card、tldraw 和 univer.se 模板里，说明“个人风格”只要经过足够严肃的系统化工程，也可以成为公共设计材料。

## 值得注意
这篇文章最强的部分是设计过程透明：它把情绪目标、可访问性、字体工程、多语言扩展和 variable font 实验放在一条链路里。薄弱处是它主要从项目参与者视角出发，缺少用户阅读测试或 dyslexia 群体实证数据，所以“更易读”更多是设计意图与字形判断，而不是被量化验证的结论。

## 最后一句
Shantell Sans 有趣的地方在于，它没有把“手写感”当装饰，而是把手写里的亲密、缺陷和节奏变成了一套可部署、可授权、可动画、可跨语言扩展的软件对象。
