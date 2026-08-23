---
title: "Understanding Optimization Algorithms: Newton's Method"
date: 2025-11-04T10:47:18Z
category: reading
author: "Nick M"
description: "牛顿法的本质不是\"找最优解\"，而是\"找方程的根\"——把优化问题转化为 f(x) = 0，再用切线迭代逼近零点。4次迭代就能将√3逼近到16位小数精度。"
source: "https://photonlines.substack.com/p/understanding-optimization-algorithms"
---

## TL;DR
牛顿法的本质不是"找最优解"，而是"找方程的根"——把优化问题转化为 f(x) = 0，再用切线迭代逼近零点。4次迭代就能将√3逼近到16位小数精度。

## 核心洞见
牛顿1670年的原始做法没有通用公式：已知近似解 x ≈ 2，令 x = 2+p 代入方程，因 p 极小而丢弃 p² 和 p³，线性化后解出修正量 p，再迭代。这个过程每步都要重新推导新方程。

Raphson 1690年将其系统化为可重复公式：**x_{n+1} = x_n - f(x_n) / f'(x_n)**，彻底终结了手工推导的麻烦。所谓"牛顿-拉弗森法"，算法结构其实是 Raphson 的贡献。

## 具体机制
几何直觉：在当前点 (x_n, f(x_n)) 画切线，切线与 x 轴的交点即为下一个近似根 x_{n+1}。切线斜率 = f'(x_n)，代入"斜率 = 高度差 / 水平距离"的定义，直接推导出更新公式，无需额外假设。

## 隐藏限制
算法只在初始猜测已足够接近真实根时才快速收敛。初始点选错，切线可能将迭代引向错误方向甚至发散——文章没有正面讨论这个局限，只在结尾轻描淡写了一句。

## 收束
Raphson 比 Newton 更配叫"Newton-Raphson 法"。Newton 发明了思路，Raphson 发明了算法。这个命名的不公平，藏着科学史里一种常见的规律。
