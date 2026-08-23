---
title: "TBM 403: The Seduction (And Folly) Of Rollups, Points, and (Most) Time Tracking"
date: 2026-02-14T20:39:06Z
category: reading
author: "John Cutler"
description: "Rollup 越整洁，数据就越假。强制要求每个 story 都有 epic、每件事都能归类，结果只有两种：团队伪造汇报来喂养报表，或者扭曲工作方式让数字好看——而且这两种都很常见，不是边界案例。"
source: "https://cutlefish.substack.com/p/tbm-403-the-seduction-and-folly-of"
---

## TL;DR
Rollup 越整洁，数据就越假。强制要求每个 story 都有 epic、每件事都能归类，结果只有两种：团队伪造汇报来喂养报表，或者扭曲工作方式让数字好看——而且这两种都很常见，不是边界案例。

## 为什么 rollup 必然失真
知识工作天然跨切、探索驱动、由本地上下文塑造，这正好是 rollup 的失效条件（Stafford Beer：管理模型的"多样性"必须匹配被管理系统的复杂度；rollup 只在工作稳定、可分解、分类缓慢变化时才有效）。Story points 和工时借用了财务会计的权威感，却不是会计——它们是代理指标、猜测和社会契约。一旦把激励挂上去（"BAU 必须低于 30%"），相应数字就会神奇地从电子表格另一端出现。

真正需要工时追踪的只有一件事：法定资本化（CAPEX）。规划、依赖解决、规模估算，"大致够用的猜测"就足够了；story points 做完前期规划后理应直接扔掉，不需要留存。

## 实际有用的替代信号
变更吞吐量、developer experience、跨团队协作密度——这些比知道某张票花了多少点数更能反映团队实际健康状态。更值得投入的是 return 侧：上线了什么、客户在用吗、是否达到预期效果。Douglas Hubbard（《How to Measure Anything》）：先弄清楚这个度量是为了支持什么决策，再选能以最低成本减少不确定性的方式去量化。

**证据薄弱处**：文章对"不做任何 rollup 的公司"如何满足合规/资本化需求的描述较模糊（"坚持 first principles"），没有给出具体替代工具或实操路径。

## 边缘判断
我们对"投入侧"精确度的执念，本质上是在回避"产出侧"太难量化这件事。把注意力转向 rollup 的整洁性，是一种组织级别的拖延症。
