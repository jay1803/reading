---
title: "SentimenTrader Research highlights for week of Nov 24, 2025"
date: 2025-11-30T20:20:35Z
category: reading
description: "这其实是一则很短的研究预告，核心内容只有一个：SentimenTrader 新推出了一个叫 TCTM Composite Washout Model 的市场“恐慌出清/洗盘”识别模型，试图用多指标组合的方法，系统化识别市场是否已经进入某种接近 capitulation 的阶段。它背后的卖点是：与其靠单一情绪指标猜..."
source: "https://newsletters.feedbinusercontent.com/ef8/ef8788eaaa4b16c76a2be68d7934fa826ae2465b.html"
---

## TL;DR
这其实是一则很短的研究预告，核心内容只有一个：SentimenTrader 新推出了一个叫 **TCTM Composite Washout Model** 的市场“恐慌出清/洗盘”识别模型，试图用多指标组合的方法，系统化识别市场是否已经进入某种接近 capitulation 的阶段。它背后的卖点是：与其靠单一情绪指标猜底，不如把 breadth divergence、volume washout 等多个信号合起来做 weight-of-the-evidence 判断，去寻找更高概率的市场底部。

## 关键洞察
虽然正文信息很少，但从这段介绍能读出的主要思路还挺明确。第一，它关心的是 **systematically identify market capitulation**——也就是把“市场是不是已经恐慌性砸到位了”这件事，从主观盘感变成可规则化、可重复的判断。第二，它不是靠一个指标，而是把 9 套算法合成一个 Composite Model，这说明作者想解决单指标容易失灵、市场 regime 变化时鲁棒性不足的问题。

文中点名的两个核心输入也很典型：
- **breadth divergences**：看的是下跌是否已经扩散到极致、内部结构是否出现背离；
- **volume washouts**：看的是不是出现了带有“甩卖式出清”特征的放量行为。

这类模型的直觉很像“极端情绪 + 结构性破坏 + 抛售强度”同时出现时，后面 6-12 个月的回报往往更好。换句话说，它试图抓的不是短线反弹，而是那种中期维度上风险收益比比较划算的 washout bottom。

不过因为这封 newsletter 本身只是摘要 teaser，没有披露 9 个算法的具体构成、样本期、回测细节、信号频率、失效率或 regime dependence，所以现在更适合把它当成一个研究方向，而不是一个可以直接执行的系统。

## 对你（行动层面）的启发
如果你看市场研究，这条内容最值得记住的是：**猜底最稳的方法通常不是找一个神指标，而是做多证据叠加。** 尤其是市场极端阶段，单一情绪、单一成交量、单一 breadth 信号都可能误导，但多信号共振更有参考价值。

如果你真要把这种框架用于实盘，后面最该追问的不是“这个模型听起来猛不猛”，而是：
- 9 个算法具体是什么
- 信号多久出现一次
- 过去哪些年份失效过
- 它适用于指数、风格还是个股层面
- 它给的是反弹信号还是中期配置窗口

## 一句话总结
这篇短讯的核心意思是：用多指标合成模型去识别恐慌性出清，可能比靠单一情绪指标猜市场底部更靠谱。
