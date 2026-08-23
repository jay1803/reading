---
title: "Pluralistic: Georgia's voting technology blunder (18 Apr 2026)"
date: 2026-04-19T08:00:44Z
category: reading
author: "Cory Doctorow"
description: "这篇文章最重要的判断不是“投票机一直很烂”这件旧闻，而是美国自由派在 2020 年后为了反对 Stop the Steal，连原本合理的投票机批评也一起防御化了，结果反而给了官员继续采购和包装糟糕系统的空间。Georgia 现在把“禁用 QR 码直接计票”的修法，又偷偷绕回成 OCR 复核方案，就是这种认知错位的..."
source: "https://pluralistic.net/2026/04/18/dominion-sucks-actually/"
---

## TL;DR
这篇文章最重要的判断不是“投票机一直很烂”这件旧闻，而是美国自由派在 2020 年后为了反对 Stop the Steal，连原本合理的投票机批评也一起防御化了，结果反而给了官员继续采购和包装糟糕系统的空间。Georgia 现在把“禁用 QR 码直接计票”的修法，又偷偷绕回成 OCR 复核方案，就是这种认知错位的最新样本。

## 核心主张拆解
- Doctorow 先回顾 Bush v. Gore 之后的历史：厂商曾想把一堆本来就有缺陷的触屏机直接写成“标准”，Diebold 又用 DMCA 压 leaked memo，说明问题从来不是阴谋论，而是这个行业长期依赖封闭、脆弱、受政治庇护的差技术。
- 2020 年后的真正扭曲，在于 schismogenesis。因为 Tucker Carlson、MyPillow 阵营把 Dominion 编造成选举舞弊机器，很多原本长期批评投票机的人反而被逼到“机器其实没问题”那一边，仿佛只要批评机器，就是替阴谋论背书。
- 这种二元对立遮蔽了仍然存在的现实风险。Georgia 虽然已规定纸票上的可读文字才是官方选票，但州务卿 Raffensperger 仍想让 Dominion 触屏机生成带 QR 的纸票，再用同系统导出的 200dpi 图像交给外包 OCR 做“验证”。
- Andrew Appel 的批评点很硬：如果你都不信 BMD 输出的 QR 码和文字一致，就没有理由再信它导出的 ballot image；而图像打包、传输、交给外包商处理的整条链路，又新增了多处可篡改面。所谓“audit”并没有引入独立校验，只是在同一条不可信链路上再跑一遍。
- 更荒唐的是，替代方案几乎现成：直接用已有的 Dominion ICP 扫描器统计预印、手填的 bubble ballots，甚至连软件升级都不是必要条件。也就是说，Georgia 面对的不是高成本取舍，而是彻头彻尾的人为失误。

## 值得质疑
- Doctorow 的政治情绪很强，像“Raffensperger sucks”这种判断明显带立场，但技术批评本身并不主要靠情绪，而是建立在 Appel 列出的具体攻击面上。
- 文中默认“手写纸票 + 光学扫描”是更稳妥的均衡点，但没有展开残障辅助、投票便利性与人工复核成本之间的制度权衡。

## 最后一笔
真正危险的不是有人胡说投票机能替 Hugo Chavez 偷走选票，而是这种胡说把正常的安全审计也一起污名化，最后让官员能在“反阴谋论”的旗号下继续做最蠢的采购决定。
