---
title: "Palomar – a registry of Lean verified mathematics"
date: 2026-09-26T15:01:34Z
category: reading
description: "Terence Tao 宣布 Lean FRO 与 ICARM 孵化的 Palomar 注册库开放投稿，为 Lean 形式化证明建立可检查、可定位版本的公开最低标准，但不构成同行评审。"
source: "https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/"
---

Palomar 要解决的是：一份 Lean 证明即使能够运行，也不足以让非专家确认它真的证明了对外宣称的数学结论。近来 AI 生成的新旧定理证明迅速增多，其中一些已被形式化；核验者仍须分别确认代码中的证明通过类型检查、没有通过增添公理等方式作弊，以及形式化命题在语义上对应文字描述的结果。Terence Tao 宣布，由 Lean FRO 和 ICARM 孵化的 Palomar 注册库现已开放投稿，试图为这些核验建立一套公开的最低标准。

Palomar 近似于 Lean 证明的预印本平台，但它登记的是外部 GitHub 仓库在**特定 commit** 的快照。投稿仓库须有用简短 Lean 代码呈现所声称结果的 `challenge file`、给出完整证明的 `solution module`，以及用自然语言描述结果并披露相关信息的 `formalization.yaml`。注册库随后用 Lean 的 Comparator 机械检查证明模块是否通过类型检查、是否恰好证明挑战文件中的命题；另用大语言模型判断自然语言描述看起来是否与形式命题相符，并检查仓库是否达到基本收录标准。通过这两道关卡即可登记，但第二道判断并非确定性的验证，整个流程也不评价成果的新颖性、重要性或数学准确性，因此 Palomar 不是同行评审期刊。

Tao 已将自己近期对 Sendov's conjecture 证明的形式化成果成功提交，说明流程虽细致，却可实际完成；他也计划提交更早的形式化工作。注册库同时接收旧结果与新结果，以及人类、AI 或两者合作完成的证明；Tao 建议投稿前细读提交说明，机械性的准备工作可借助 AI agent，但仍应由人审阅。Palomar 的价值在于把"这份代码究竟证明了什么"变成可检查、可定位到具体版本的公开记录，同时明确保留了从形式核验到数学同行评审之间的距离。
