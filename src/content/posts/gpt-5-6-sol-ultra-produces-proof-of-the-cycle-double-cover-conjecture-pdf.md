---
title: "GPT-5.6 Sol Ultra produces proof of the Cycle Double Cover Conjecture [pdf]"
date: 2026-07-12T08:02:55Z
category: reading
description: "圈双覆盖猜想（Cycle Double Cover Conjecture）由 Tutte、Itai & Rodeh、Szekeres、Seymour 独立提出，断言每个无桥无向图都存在一族圈，使每条边恰好被覆盖两次。它在图论中悬而未决约 50 年。GPT-5.6 Sol Ultra 给出了证明，整篇 paper..."
source: "https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf"
---

## 真正的洞见：一个组合拓扑猜想被归结为 F₂ 上的初等线性代数

圈双覆盖猜想（Cycle Double Cover Conjecture）由 Tutte、Itai & Rodeh、Szekeres、Seymour 独立提出，断言每个无桥无向图都存在一族圈，使每条边恰好被覆盖两次。它在图论中悬而未决约 50 年。GPT-5.6 Sol Ultra 给出了证明，整篇 paper 仅 3 页。

证明路线不是找圈，而是找一个代数标注，再从标注中读出圈。

## 证明结构

**归约到三正则图（cubic graph）**：Jaeger 已知最小反例必须是 snark（不可 3-边着色的三正则图），因此只需对无环三正则图证明。

**利用 8-流定理**：Kilpatrick 和 Jaeger 证明每个无桥图有处处非零的 Γ-流（Γ = F₃₂，加法群）。这是现成工具，proof 直接调用。

**关键引理（Lemma 2.1）**：若每条边 e 都能分配一个二元集 Pe ⊆ Γ，使得对每个顶点 v 和每个向量 s∈Γ，满足「s∈Pe 的 e 中恰好 0 或 2 条与 v 相邻」，则图有圈双覆盖。构造方式：对每个 s 取 Ms = {e : s∈Pe}，Ms 每个顶点度数 0 或 2，所以是不相交圈的并；Pe 有两个元素保证每条边恰好属于两个 Ms。

**构造 Pe 的障碍**：给定处处非零 Γ-流 f，可在每个顶点局部定义满足条件的集合，但同一条边从两端定义的集合未必一致。一致性条件等价于一个线性方程组 (4)：对每条边 uv，有 tu + tv + ϵe·f(e) = de，其中 de 是局部定义引入的偏差量。

**Lemma 2.2：方程组 (4) 总有解**。用对偶性：(4) 无解当且仅当存在满足 (5) 的对偶向量族使 Σ ηe(de) ≠ 0。证明中把 Σ ηe(de) 改写为对每个顶点 v 求和 Σ_{e∋v} 1_{ηe≠0}，每条 ηe≠0 的边在两个端点各贡献一次，总和 mod 2 为 0。矛盾，故解存在。

## 为何这是非显然的

证明没有在图上直接找圈，而是把构型问题转化为一个 GF(2)-线性代数问题，再用奇偶计数结束证明。关键步骤（equation 9）将局部内积 ηe(gv,e) 与 ηe 是否为零的奇偶性等同，使全局求和崩塌成一个简单的 mod 2 = 0 计数。整个证明依赖于 Γ = F₃₂ 的特征为 2（flow 方程变成 x+y+z=0）和 "没有重数计数" 这两个代数意外。

## AI 使用声明

论文明确注明：证明完全由 GPT 5.6 Sol Ultra 给出，排版由 Codex（与 GPT 5.6 Sol 合作）完成。
