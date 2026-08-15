---
title: "Microsoft’s open sourcing of 86-DOS and what it means"
date: 2026-05-04T08:02:01Z
category: reading
description: "Microsoft 开源 86-DOS 的真正价值，不是给“MS-DOS 是否偷了 CP/M”这场老争论一个立即判决，而是把争论从回忆录、传闻和二手故事，推进到可审查的原始材料层面：早期 DOS 的起源史终于多了一份直接证据。"
source: "https://dfarq.homeip.net/microsofts-open-sourcing-of-86-dos-and-what-it-means/?utm_source=rss&utm_medium=rss&utm_campaign=microsofts-open-sourcing-of-86-dos-and-what-it-means"
---

## TL;DR
Microsoft 开源 86-DOS 的真正价值，不是给“MS-DOS 是否偷了 CP/M”这场老争论一个立即判决，而是把争论从回忆录、传闻和二手故事，推进到可审查的原始材料层面：早期 DOS 的起源史终于多了一份直接证据。

## 关键时刻
86-DOS 是 PC DOS 1.0 的直接祖先。IBM 当年没有和 Digital Research 达成 CP/M 授权协议，转而通过 Microsoft 获得操作系统；Microsoft 则从 Seattle Computer Products 以 5 万美元授权 Tim Paterson 写的 8086 版 CP/M 兼容系统，再把它授权给 IBM，同时保留向其他厂商授权的权利。这个安排解释了为什么 IBM 机器运行 PC DOS，而兼容机运行 MS-DOS，二者又大体兼容。

这次开源源自 Paterson 找到 45 年前的源码打印件。此前早期 PC DOS 已经有人反汇编并注释，但这次材料更接近作者本人留下的原始历史切片。

## 背后逻辑
围绕 86-DOS 的核心争议一直是：它到底只是 CP/M 的功能兼容克隆，还是包含了不当复制的代码或隐藏证据。Gary Kildall 曾暗示两者有只有他理解的“神秘相似性”，但没有展开；John C. Dvorak 又转述过早期 PC DOS 中可能存在 Kildall 版权彩蛋的说法，Jerry Pournelle 后来也声称见过类似东西，但从未公开可复现命令。

作者认为，过去的反驳也并不彻底。有人曾用源代码层面的差异来证明 MS-DOS 并非来自 CP/M，但这只能证明一个已知事实：MS-DOS/86-DOS 是 8086 汇编写成，而 CP/M 多由 PL/I 或 PL/M 写成。若真有抄袭，更可能来自行为复制、内存转写或接口模仿，而不是直接拷贝源代码。

## 值得质疑
开源 86-DOS 会削弱“原始代码里有明显赃物”的强版本阴谋论：如果 Paterson 明知里面有偷来的代码，主动释放原始材料并不合逻辑。但这不等于争议终结，因为代码相似性、接口兼容、商业机会截胡、以及 Gates 与 Kildall 之间的历史不公平感，是不同层次的问题。

作者也明确区分法律问题和历史评价：他不否认 Gates 在商业上双杀 Kildall，也不否认 Kildall 更像技术愿景家、Gates 更像抓住套利机会的人；但道德叙事不能替代证据。

## 更大意义
这份源码最重要的作用，是把早期个人电脑操作系统史从“谁背叛了谁”的传奇叙事，拉回到可研究的技术史。86-DOS 也许不能洗清所有争议，却让后来的判断更少依赖记忆、传闻和阵营立场。历史不会因此变得干净，但会变得更可检验。
