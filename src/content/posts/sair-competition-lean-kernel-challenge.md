---
title: "SAIR competition – Lean Kernel Challenge"
date: 2026-10-03T16:12:52Z
category: reading
description: "SAIR Foundation 与 Lean FRO 联合发起 Lean Kernel Challenge 第一阶段，征集更快的算法与数据表示以加速 Lean 4 内核中的可验证计算，涵盖八项基础问题，截止 2026 年 11 月 20 日。"
source: "https://terrytao.wordpress.com/2026/09/16/sair-competition-lean-kernel-challenge/"
author: "Terence Tao"
---

Lean Kernel Challenge 要通过改进算法与数据表示，加快 Lean 4 内核中的可验证计算，让计算性能的提升能够直接服务于形式化证明。这里的 **verified computation** 指由 Lean 内核检查证明中使用的计算结果；参赛者既要开发计算算法，也要在 Lean 中证明算法对每一个输入都符合给定的规格，正确性要求覆盖全部输入。

竞赛采取多阶段形式，首阶段是从基础问题入手的实验阶段，后续将扩展到更广泛的数学与科学领域以及更复杂的问题。它受到 Lean Kernel Arena 的启发，但两者优化的对象不同：Lean Kernel Arena 对不同的 Lean 证明检查器进行基准测试，Lean Kernel Challenge 则在 **固定任务、固定 Lean 内核** 的条件下，探索更快的算法和更好的数据表示，将社区贡献积累为 Lean 用户可共同受益的计算能力。

首阶段包含八项任务：Fibonacci、integer partitions（整数分拆）、Mertens function、prime counting（素数计数）、matrix permanent（矩阵积和式）、Rule 110、SHA-256，以及 polynomial discriminant（多项式判别式）。每项任务都提供规格，参赛者需要提交与其对所有输入一致的算法及 Lean 证明。提交截止时间为 2026 年 11 月 20 日 23:59，时区为 AoE（UTC−12）；竞赛及提交入口位于 competition.sair.foundation，另有 SAIR Playground 和 GitHub 官方仓库 SAIRcompetition/lean-kernel-challenge。

竞赛由 Lean FRO 与 SAIR Foundation 联合组织，组委会成员包括 Joachim Breitner、Leonardo de Moura、Kim Morrison 和 Terence Tao。其核心目标是让"计算得更快"与"结果可由内核严格验证"共同成立，把算法和表示层面的优化转化为形式化证明体系中的共享基础设施。
