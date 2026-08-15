---
title: "How to make a font."
date: 2026-07-15T08:01:49Z
category: reading
description: "一个字体文件不只是字形轮廓的集合——它是一个结构化数据库，其中只有一张表存字形数据，其余所有表编码字体正确渲染所需的全套机制：间距、字偶调整、Hinting 指令、元数据、跨平台兼容参数。"
source: "https://newsletters.feedbinusercontent.com/cf5/cf5c66da1c5f4948a39079d01e93279cb8f0979b.html"
---

## 字形之外：字体文件是排版引擎的数据库

一个字体文件不只是字形轮廓的集合——它是一个结构化数据库，其中只有一张表存字形数据，其余所有表编码字体正确渲染所需的全套机制：间距、字偶调整、Hinting 指令、元数据、跨平台兼容参数。

### 格式演化的逻辑

- PostScript Type 1（1984，Adobe）：三次贝塞尔曲线，上限 256 字形，早期专业印刷标准。
- TrueType（Apple，1980s末）：二次贝塞尔曲线（3 控制点，相邻两个控制点之间自动插入虚拟锚点，省去显式存储），内置 Hinting 系统，被 Microsoft 采用。
- OpenType（Microsoft + Adobe，1990s末）：统一容器，最多 65,536 字形，全 Unicode 覆盖；引入 GSUB/GPOS 表，支持连字、小型大写、上下文替换等。
- Variable fonts：单文件编码整个设计空间（字重、字宽、倾斜等轴），运行时插值——一个文件取代多个字重文件，减少 web 请求数。

### 关键表的分工

- ~glyf~ / ~CFF~：字形轮廓（TrueType 用坐标+标志位；CFF 用类 SVG 绘图指令，相对坐标，更易压缩；CFF2 在此基础上加字重偏移，用于 variable fonts）
- ~cmap~：Unicode 码位 → 字形内部 ID 的映射
- ~hmtx~：每字形的 Advance Width + 左/右侧承（LSB/RSB）
- ~hhea~：全局水平度量（最大 ascender/descender、最大 Advance Width）
- ~GSUB~：字形替换（fi → fi 连字）
- ~GPOS~：字形定位（T+o 字偶间距调整）
- ~OS/2~：字重范围、家族样式（衬线/无衬线等）、光学对齐数据（x-height、cap height）、跨平台渲染参数

### 文本排版的四步流程

文本先切分为 runs——共享同一字体、尺寸、颜色、语言的连续段。强字符（Latin A、Greek Δ）触发 run 切分，弱字符（空格、数字、标点）不触发。每个 run 独立执行四步：

1. 字典查询：Unicode 码位 → 字形 ID（via ~cmap~）
2. 字形替换：检查 GSUB 是否需要合并（如 f+i → fi）
3. 位置调整：检查 GPOS 做字偶间距微调（如 T 后面的 o 向左收拢）
4. 渲染：按字形 ID 取轮廓数据，在分配好的 box 里绘制

Run 之间相互隔离——跨 run 无法做字偶调整。

### Hinting：以失真换清晰

在低分辨率下（如 11px），100 单位宽的字干折算约 1 像素，几乎不可能恰好落在像素格上，导致 H 两竖粗细不一。Hinting 的目标不是保真——它是在特定尺寸下有意扭曲轮廓，强制字干对齐像素格，让两竖等宽、x-height 全行一致。

TrueType 用字节码程序（存于 ~fpgm~ / ~prep~ / ~glyf~ 表，运行在光栅化器内置的虚拟机里）实现逐像素控制；Verdana、Georgia 当年就是手工逐点 hint 的。CFF 用声明式方法：只标注字干位置和"蓝区"（baseline、x-height、cap height），由光栅化器自行决定如何对齐。

高分辨率屏普及后，macOS 基本忽略大多数 Hinting，手工 hint 已是失传技艺，多数字体改用 ttfautohint 自动处理。

-----
注：原文约 6,000 字，后半部分（字形尺寸与比例、字重设计、间距）在 paywall 之后，以上摘要覆盖文件格式、文本排版流程、Hinting 三节。
