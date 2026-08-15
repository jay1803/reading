---
title: "98%胜率的5分钟终极剥头皮交易策略—测试(UT Bot Alerts+STC Indicator)"
date: 2024-12-23T21:53:36Z
category: reading
description: "指标："
source: "https://www.youtube.com/watch?v=rOqCgwoTWCE"
---

指标：
1. UT Bot Alert : key value = 2, ATR perod = 6
2. STC Indicator : length = 80, fastLength = 27
3. Hull Suite : default

5min chart

做多：
1. UT 指标发出买入信号
2. STC 指标小于 25，显示绿色向上趋势
3. 价格在 Hull 船体 移动平均线之上

关键 K 线：同时满足以上 3 个条件之后的阳线
止损：关键 K 线低点下方；或者阶段性低点 下方。

做空条件：
1. UT 指标发出卖出信号
2. STC 指标大于 75，显示红色向下趋势；
3. 价格在 Hull 之下

关键 K 线：同时满足以上 3  点之后的阴线
止损：关键 K 线高点上方，或者阶段性高点上方。

// 测试结果看起来并不是很好。
