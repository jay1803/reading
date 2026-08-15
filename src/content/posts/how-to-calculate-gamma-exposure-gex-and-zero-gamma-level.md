---
title: "How to Calculate Gamma Exposure (GEX) and Zero Gamma Level"
date: 2024-11-10T20:34:24Z
category: reading
description: "首先，请注意，未平仓合约数据每天更新一次。几乎总是，这将是昨天的数据。尽管如此，我发现 CBOE 比其他来源更早地更新它，并且经常显示昨天的数据，而其余的则显示前一天的 OI。"
source: "https://perfiliev.com/blog/how-to-calculate-gamma-exposure-and-zero-gamma-level/"
---

### Calculating Spot Gamma Exposure
首先，请注意，未平仓合约数据每天更新一次。几乎总是，这将是昨天的数据。尽管如此，我发现 CBOE 比其他来源更早地更新它，并且经常显示昨天的数据，而其余的则显示前一天的 OI。

we'll assume that calls carry positive gamma and puts negative.

Let's now calculate the total gamma contribution from each option. The formula is:

Option Gamma Exposure = Option's Gamma * Contract Size * Open Interest * Spot Price ^ 2 * 0.01
