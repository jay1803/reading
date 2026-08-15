---
title: "How finishing what you start makes teams more productive and predictable"
date: 2022-11-11T00:09:59Z
category: reading
description: "why so many people won’t finish what they start and how to illustrate and quantify the impact of unfinished work."
source: "https://lucasfcosta.com/2022/07/19/finish-what-you-start.html"
---

why so many people won’t finish what they start and how to illustrate and quantify the impact of unfinished work.
## How finishing what you start increases productivity

in the software industry, both tasks take longer to deliver whenever you start a new feature before finishing the first. Moreover, the first task will be delivered later than it could have been.

instead of starting each feature as early as possible, you start it as late as you can afford to.
As Little's Law
$Avg.\ Cycle\ Time = \frac{Avg.\ Work\ In\ Progress}{Avg.\ Throughput​}$

If you wish to keep cycle-times low, you should limit work in progress.
### The cost of context switching
context-switching incurs a high cost.
## When to start without having finished
one about batch sizes and Transaction Cost .
That’s why you don’t buy a single egg whenever you go to the supermarket. Going to the supermarket has a significant transaction cost
whenever a transaction’s cost goes up, that transaction happens less frequently.

That’s also the reason why [Martin Fowler and Jez Humble](https://martinfowler.com/bliki/FrequencyReducesDifficulty.html) advocate that “[if something is painful, you should do it more often](https://www.goodreads.com/quotes/1314241-if-it-hurts-do-it-more-frequently-and-bring-the)”, especially when it comes to deploying software. If you’re forced to do something often, you’ll naturally gravitate towards decreasing the cost of doing it.

In the software industry, there are several problems with large batch transferrals:
- They delay feedback because features take longer to get to customers
- They make it more difficult to trace bugs because the delta between each version is larger
- They increase the overhead of change management because they make versioning and automatic rollbacks more difficult to do
These problems exponentially increase the costs of holding software tasks as opposed to pushing them forward.

Reducing transaction costs enables small batches. Small batches, in turn, reduce average cycle times, diminish risk, and enhance reliability.

You should only start without having finished when transaction costs are high, and it wouldn’t make economic sense to spend time decreasing them, either because you have agreed to a particular delivery date or because you don’t have the capital to invest.
## How finishing what you start makes teams more predictable
The lower you make WIP limits and stick to them, the less variability you’ll see in cycle times.
