---
title: "Algorithms for Optimization (Explained Simply): Part 2 - Line Search and the Trust Region Method"
date: 2025-11-04T10:50:02Z
category: reading
author: "Nick M"
description: "Line search 与 Trust Region 处理步长的顺序相反：前者先选下降方向再优化步长，后者先划定「可信半径」再在其内同时确定方向和步长——这个顺序差异使后者在高度非线性函数中收敛更稳健。"
source: "https://photonlines.substack.com/p/algorithms-for-optimization-explained-f26"
---

## TL;DR
Line search 与 Trust Region 处理步长的顺序相反：前者先选下降方向再优化步长，后者先划定「可信半径」再在其内同时确定方向和步长——这个顺序差异使后者在高度非线性函数中收敛更稳健。

## 核心洞见
- **Line search 的本质**：给定下降方向（负梯度），用不同精度换步长。精确 line search 直接解方程求最优 α；backtracking 从 α=1 开始，若不满足 sufficient decrease（Armijo 条件：f(x+α·d) ≤ f(x) + c·α·∇f·d），则乘以衰减因子 β 直到满足——以牺牲精度换速度。
- **Trust Region 的本质**：在当前点用梯度 + Hessian 构建局部二次模型 m(s)，步长被约束在半径 Δ 内；用「预测下降 / 实际下降」的比值 ρ 动态调整 Δ——ρ≈1 则扩大（模型准），ρ 偏差则收缩（模型不可靠）。

## 具体机制
Line search 流程：① 计算负梯度方向 → ② 求最优步长 α（或 backtracking 近似） → ③ 更新 x = x + α·d → ④ 检查终止条件，否则重复。

Trust Region 流程：① 设初始信任半径 Δ → ② 构建二次模型 m(s) = f(x) + g·s + ½H·s² → ③ 在 ‖s‖≤Δ 内最小化 m(s) → ④ 计算 ρ → ⑤ 调整 Δ → ⑥ 重复到梯度≈0。

终止条件四类：最大迭代次数、目标函数变化量小、步长小、梯度模长小——互为补充，防止算法无限运行或在平坦区域浪费计算。

## 隐藏限制
文章用的示例函数 f(x)=(x−2)²+1 是标准二次函数，Hessian 为常数，二次模型等于精确模型，无法体现 Trust Region 在高维非凸函数上的真正优势；backtracking 中的参数（β, c）对收敛速度影响显著，但文章未讨论如何选取。

## 留下的那个想法
Trust Region 把「我能信任多远」当作优化变量来主动管理，而 backtracking 是走过了再回头纠错——前者是「先限制再优化」，是更成熟的不确定性处理范式。
