---
title: "Why polynomial coefficients?"
date: 2026-08-20T14:26:00Z
category: reading
author: "John D. Cook"
description: "物理 PDE 的可分离性决定了多项式系数 ODE 的重要地位：分离变量后所得的方程，要么本身已具多项式系数，要么经换元可化为此形式。"
source: "https://www.johndcook.com/blog/2026/08/01/why-polynomial-coefficients/"
---

## 多项式系数方程的地位来自物理 PDE 的可分离性

二阶线性常微分方程（ODE）里有一类以多项式为系数，看似窄小，但在应用中极为关键。作者读完博士也不知道原因，直到读 Kristensson 教材第一章才补上这个认知缺口。

物理学中常见的偏微分方程（如 Helmholtz 方程、Laplace 方程）在多种坐标系下都是可分离的。分离变量后所得的 ODE，要么本身已具多项式系数，要么经换元可化为多项式系数形式。于是，整个多项式系数 ODE 理论实际上是"物理 PDE 分离变量"这条路径的自然终点——重要性来自此处，而非数学本身的任意选择。

作者同时点出这类知识的结构性缺失：本科课程只触及幂级数解法的简单案例；研究生课程因为该领域太成熟、缺乏论文方向而跳过。结果是一大块有用理论被系统性地排除在标准教育之外。
