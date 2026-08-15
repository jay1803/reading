---
title: "What is Gamma Exposure and Why Should Equity Investors Care?"
date: 2024-11-10T20:35:19Z
category: reading
description: "传统保险业务通常使用多元化作为风险管理工具。任何单一不良事件的风险都可以通过为其他未能发生的不良事件投保来对冲。有了足够多的不相关投注，就有可能获得正回报。"
source: "https://perfiliev.com/blog/wtf-is-gamma-and-why-should-equity-investors-care/"
---

传统保险业务通常使用多元化作为风险管理工具。任何单一不良事件的风险都可以通过为其他未能发生的不良事件投保来对冲。有了足够多的不相关投注，就有可能获得正回报。
然而，在对冲一$SPX期权时，多元化并不实用。
主要的风险管理技术是 delta 对冲，即期权交易者开始在股票市场上胡闹的时候。

他们尽最大努力用其他期权来降低风险，但剩余风险敞口用标的股票或期货进行对冲——这一过程称为 delta 对冲。
随着标的物的移动，delta 对冲要求也会发生变化。做市商被迫交易标的物仅仅是因为该资产的价格变化，而不是出于任何其他基本面或经济原因。
这形成了一个反馈循环，投资者交易的期权类型和数量会影响标的价格行为。如果购买火灾保险的行为影响了房屋被烧毁的可能性，那将是等效的。
所需的 delta 对冲数量主要取决于这个叫做 gamma 的东西。

Gamma 显示做市商潜在的 delta 对冲活动数量。它是股市最重要的结构性流动之一的来源。

目前，仅 $SPX 期权就占 $SPX 市值的 16% 左右。总流通总量为 80 亿美元，这意味着做市商需要交易价值约 80 亿美元的$SPX才能使指数上涨 1%。

由于其性质，gamma 可以加剧市场波动（“short gamma”）或抑制市场波动（“long gamma”）。这在很大程度上取决于 “the street” 的定位。

(The street == options market makers and dealers)
### Long Gamma and Short Gamma
A quick rule of thumb - you are long gamma when you buy options and short gamma when you sell.

When the street is long gamma, that means option market makers net-net bought options. Their delta-hedging activity forces them to "buy low, sell high". They are sellers when the market rallies and buyers when it drops, conveniently adding liquidity and reducing volatility.

When the street is short gamma, the opposite happens. Dealers' book is short options, and they "buy high, sell low". This exacerbates market moves and removes liquidity (frequently, when it's needed the most).

So how is the street positioned?
在指数层面，人们普遍认为投资者主要买入看跌期权以保护自己，卖出看涨期权作为覆盖策略的一部分。这在$SPX偏度中很明显，它显示看跌期权的隐含波动率高于看涨期权。
然而，这可能会高估 gamma，因为投资者还会卖出看跌期权以获得收益（结构性产品）并买入看涨期权以获得杠杆。

Still, under this assumption, puts carry negative gamma (not because they're puts, but because the street is short them), and calls carry positive gamma.

A closely monitored data point is where the gamma is zero - known as the gamma flip. At the moment, this is around 4,660 for $SPX.

If we're above the gamma flip, the volatility tends to be low, as the market has to swim against the current of the options flow.
But should the market drop into negative gamma territory, expect fireworks.

在这种情况下，delta 对冲流与市场沿同一方向移动，可能会放大价格行为。随着波动率上升，系统性/管理波动率基金往往会减少敞口，进一步增加抛售压力并引发更多的负面伽马流动。
### When is Gamma the Strongest?
Of course, gamma is just one of the market forces here, and its impact largely depends on several factors, such as:
- Time to Expiry
- Open Interest
- Market Liquidity
- Volatility
For any single option, gamma is a bell-shaped curve centered around the strike. And it's the highest for short-dated, at-the-money (ATM) options:

因此，如果市场围绕即将到期的行权价交易，且未平仓量较高，则其伽马流量更有可能影响市场。
The most open interest is frequently concentrated around large expiries and nice, round strikes:

$SPX期权在周一、周三和周五到期，传统的月度期权在每月的第三个星期五到期。
较长的期限债券往往仅按季度（3 月/6 月/9 月/12 月）和每年（12 月）列出。
由于这些到期日存在的时间更长，因此它们积累了相当大的未平仓合约。
然而，这些流动是否足够强大以推动市场？
嗯，这取决于当时可用的流动性。流动性越高，市场就越有可能在不知不觉中简单地吸收任何 delta 对冲资金。
然而，在流动性较低的时候，伽马流量可能会导致期权到期前后的重大价格走势。
有什么可以阻止 gamma 及其邪恶计划吗？
是的，gamma 在高波动率环境中往往会失去其力量，因为 delta 对潜在走势变得不那么敏感。这是因为短期期权在高波动率环境中表现为长期期权。
有关如何计算经销商 Gamma 风险敞口的详细信息，请查看此帖子： 如何计算 Gamma 风险敞口和零 Gamma 水平
