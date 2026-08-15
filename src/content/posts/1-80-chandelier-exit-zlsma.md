---
title: "最佳剥头皮指标—1分钟到日内交易—准确度超80%的轻松买卖策略测试(Chandelier Exit+ZLSMA)"
date: 2024-12-20T23:22:44Z
category: reading
description: "指标："
source: "https://www.youtube.com/watch?v=LamLdvIKGKA"
---

指标：
1. Chandelier Exit
2. ZLSMA
K 线使用 Heikin Ashi

CE period = 1
CE = 2

ZLSMA period = 50
ZLSMA - Zero Lag LSMA，意思是最小二乘移动平均线，几乎零滞后版本。
给出当前价格行为的即时线性回归，方向显示趋势方向。
- 当价格向上穿过均线时，表示上升趋势
- 当价格向下穿过均线时，表示下降趋势
- 当价格反复穿过均线时，代表震荡趋势

同时满足是做多：
1. 移动止损指标发出买入信号
2. 关键 K 线：收盘价位于均线之上的阳线；
止损：关键 K 线下方，或者阶段性低点。
止盈：收盘价向下穿过均线的 K  线。

同时满足时做空：
1. 移动止损指标发出卖出信号；
2. 关键 K 线：收盘价位于均线之下的阴线。
止损：关键 K 线高点上方，或者阶段性高点上方。
止盈：收盘价向上穿过均线的 K 线。
