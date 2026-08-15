---
title: "Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML"
date: 2026-05-04T08:02:01Z
category: reading
description: "AI 编程的瓶颈正在从“让模型写代码”转移到“定义什么算合格”：当实现越来越便宜，最有价值的工程资产会变成可追踪、可验证、能被代码和测试反向引用的验收标准。"
source: "https://acai.sh/blog/specsmaxxing"
---

## TL;DR
AI 编程的瓶颈正在从“让模型写代码”转移到“定义什么算合格”：当实现越来越便宜，最有价值的工程资产会变成可追踪、可验证、能被代码和测试反向引用的验收标准。

## 核心主张拆解
- “Peak Slop” 之后，代理生成代码的质量和速度继续上升，但上下文窗口、会话切换、多人交接会持续吞掉需求细节；可行修复路径是减少对临场 prompt 的依赖，把需求稳定地写下来并持续维护。
- specs 并不新，README、AGENTS、testing guide、architecture doc、PRD、design doc 都是旧工程习惯的回归；新变化是 LLM 让“spec 是否足够明确”直接决定生成系统的质量上限。
- 关键抽象是 ACID（Acceptance Criteria ID）：每条验收标准有稳定编号，代码和测试用编号引用它，从而把 review 从“逐文件看 diff”转成“逐需求检查是否实现、是否测试、是否通过验收”。
- Acai.sh 的 feature.yaml 试图把这个流程产品化：spec 由 feature、components、constraints 和编号 requirements 组成，CLI / CI 把 specs 与代码引用推到 dashboard，人或代理再标记 Completed / Accepted / Rejected。
- Acai 把 spec 定义为系统“应该如何行为”；“当前行为”只是会被实现替换的暂态，产品意图和验收边界需要落在更稳定的载体上。

## 具体机制
- feature.yaml 把需求拆成可引用的功能项和工程约束，例如 AUTH.1、AUTH.1-1、ENG.2；这些编号可以出现在实现、测试、review 注释和 dashboard 里。
- 这种耦合会带来维护成本：改 spec 时必须同步代码引用；但这个成本正是价值来源，因为它强迫实现重新对齐需求，避免旧代码静默偏离新意图。
- 传统 test coverage 只能说明代码被执行过；acceptance coverage 追问每条验收标准有没有实现、有没有测试、有没有被接受，更接近产品质量的真实问题。
- 当 CI、测试、观测和代理循环足够强时，红灯测试或线上告警可以直接映射回 spec，代理获得更明确的修复边界，人工介入从“解释想要什么”转为“审查验收是否成立”。
- specs 不适合塞进低价值 UI 细节和表面打磨；它们更适合行为、约束、安全性、幂等性、权限、数据形状等决定系统正确性的要求。

## 边界与薄弱处
- Acai 没有覆盖端到端交付链路；它聚焦 spec、实现引用和验收状态，计划 / implement / review 的 agent pipeline 仍要外接。
- feature.yaml 比 markdown 更结构化，比 EARS / Gherkin 更轻，但也要求团队接受一个新格式；低风险、小体量产品可能不值得引入这套额外约束。
- 稳定编号是核心机制，也是迁移摩擦来源；spec 大改时，编号废弃、替换、重排都需要明确治理，否则 ACID 会变成另一种陈旧注释。
- 对 SpecKit、Kiro 等工具的比较带有明显 NIH 偏见；有效判断应落在实际团队是否减少返工、提升验收信心、降低 review 成本，格式美感不应成为判断标准。

## 最后留下的判断
如果软件生成继续变快，代码、diff、甚至测试都会逐渐变成中间产物；团队真正反复争夺和校准的对象，会是那份写明“什么才算对”的 spec。
