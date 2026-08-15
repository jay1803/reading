---
title: "How to sequence your own DNA at home"
date: 2026-07-08T08:04:03Z
category: reading
description: "作者用 Oxford Nanopore MinION 自己在家测了五次全基因组。结论直接：基因组本身不是魔法，它是参考层。有了 VCF 才能问真正的问题——哪些变异、哪些通路、哪些药物代谢异常、哪些罕见变异值得重视。作者特别推荐 PharmGKB，因为它直接给出药物代谢差异（而不是模糊的\"风险稍高\"）。"
source: "https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home"
---

## 基因组是静态参考层，价值在于把 VCF 变成可查询的 AI 接口

作者用 Oxford Nanopore MinION 自己在家测了五次全基因组。结论直接：基因组本身不是魔法，它是参考层。有了 VCF 才能问真正的问题——哪些变异、哪些通路、哪些药物代谢异常、哪些罕见变异值得重视。作者特别推荐 PharmGKB，因为它直接给出药物代谢差异（而不是模糊的"风险稍高"）。

### 成本与入门门槛

核心耗材：
- Oxford Nanopore SQK-LSK114：$720 / 6 次反应
- NEBNext Companion Module v2（末端修复 + 连接）：$760 / 24 次反应
- Qubit 荧光计、AMPure XP 磁珠、微量离心机、移液器全套

两个月备齐耗材，作者第一次低输入练习跑实际投入 DNA 只有 13.9 ng（推荐值 1000 ng），大幅低于标准，但视为端到端流程验证是成立的。成本目前超出普通人承受范围，但作者判断正在指数级下降。

### 操作链路（关键节点）

1. 颊细胞棉签采样 → Monarch gDNA 提取（捕获磁珠沉淀，56°C 裂解，isopropanol 沉降）
2. Qubit dsDNA HS 定量 → 判断是否有足够 DNA 进入文库制备
3. FFPE DNA 修复 + 末端准备（FFPE Repair Buffer v2 + N-Prep Enzyme Mix，20°C 5min → 65°C 5min）
4. AMPure XP 清洁 → 接头连接（LNB + LA + Salt-T4 DNA Ligase，室温 10min）
5. LFB 洗涤（不用乙醇）→ EB 洗脱最终文库
6. 流动槽检查（>1200 孔 = 优，800–1200 = 可用，<500 = 仅练习）
7. MinKNOW 启动 → Dorado 碱基识别（sup/hac 模式）→ minimap2 比对 GRCh38 → Clair3 变异检测 → VEP + ClinVar + gnomAD 注释

整个协议被作者明确设计为"AI 可读"——建议把页面 URL 直接丢给 AI 逐步引导操作，AR 眼镜更佳。

### 前景判断：DNA + RNA + 生物传感器 → 个人模型

DNA 是稳定参考，RNA 是当前状态。作者的判断是这两者终将与实时生物传感数据整合成一个"个人模型"。近期价值是把静态基因组变成可查询层；"根据 AI 建议用 CRISPR 编辑自己"大概率会来，但不是现在。当前不具备诊断级别，要清醒对待模型的知识盲区。
