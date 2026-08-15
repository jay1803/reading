---
title: "TypeScript, C# and Turbo Pascal with Anders Hejlsberg"
date: 2026-05-14T08:01:36Z
category: reading
description: "Anders Hejlsberg 是 Turbo Pascal、Delphi、C#、TypeScript 的核心设计者；早年在 Borland 做开发工具，1996 年加入 Microsoft，当前是 Microsoft Technical Fellow。Gergely Orosz 访谈的主线，是让 Anders..."
source: "https://newsletter.pragmaticengineer.com/p/typescript-c-and-turbo-pascal-with"
---

## 嘉宾背景
Anders Hejlsberg 是 Turbo Pascal、Delphi、C#、TypeScript 的核心设计者；早年在 Borland 做开发工具，1996 年加入 Microsoft，当前是 Microsoft Technical Fellow。Gergely Orosz 访谈的主线，是让 Anders 用四十年语言/工具经验解释：什么样的编程语言能被开发者长期依赖。

## TL;DR
这场对话最核心的线索：长寿的语言产品，胜负手不在单点语法，而在能否持续降低开发者的“思考摩擦”——IDE、编译器、运行时、类型系统、开源协作、语义服务都属于语言本体的一部分。AI 时代会放大这条规律：机器能更快地产出代码后，真正稀缺的变成架构判断、语义校验、局部性、可审查性，以及最终由人承担的责任。

## 语言的竞争单位是完整开发体验
Turbo Pascal 赢，不只是因为 Pascal 编译器快，而是因为它把编辑、编译、运行、调试、运行库打成一个交互式循环；当时竞品常是 500 美元级别的“单独编译器”，Turbo Pascal 49.95 美元、速度更快、体验更完整，形成了 Anders 说的“10 倍好、1/10 价格”。早期“调试器”甚至只是把 runtime error 的程序计数器地址打印出来，再让编译器以“停在这个地址”的模式重跑，由当前语法位置反推出出错行。

非直觉点：开发者爱上的往往不是语言抽象本身，而是工具在关键瞬间让他们保持 flow 的能力。Anders 后来做 Delphi、C#、TypeScript 都延续了这套判断：语言设计必须把 IDE 和工作流一起算进去。

## C# 是平台战略被迫重启后的语言设计
C# 的起点不是纯技术灵感，而是 Microsoft 的 Java 路线被 Sun 诉讼切断后，需要一个自有平台语言：既有 Visual Basic 的生产力，又有 C++ 的能力，还要有 Java 已经证明有价值的 GC、异常、托管运行时、对象模型。C# 与 .NET 几乎同步推进，因为 Microsoft 要的是一个可承载多语言的 runtime，以及一个能吸引 VB/C++/Java 开发者的新主力语言。

设计过程反而很小：六七个有语言经验的人，每周三次、每次两小时，围绕 specification 逐项攻防。Anders 强调这种团队需要的是“能快速进入深水区”的共同经验；新想法先被几个人集中挑错，能活下来才进入语言。

## async/await 的价值是让编译器替人写痛苦状态机
C# 推出的 async/await 后来扩散到许多语言，因为它抓住了一个很硬的痛点：人类讨厌手写跨 await 的状态保存、堆对象、switch 状态机和 callback 链；编译器很擅长自动改写。开发者得到的是顺序代码的心智模型，底层则由编译器生成状态机。

代价也清楚：async/await 带来 function coloring，一旦底层调用变 async，上层调用链往往也要 async。Go 的 goroutine/green-thread 路线避免了一部分颜色传播，但对 C#、JavaScript 这类已有事件循环与 runtime 约束的生态，async/await 是现实可行的改造。

## TypeScript 的关键选择是“修 JavaScript”，不是逃离 JavaScript
TypeScript 来自 Outlook.com 团队想把 Script# 产品化：用 C# cross-compile 到 JavaScript。Anders 拒绝了这个方向，因为要赢得 JavaScript 生态，不能要求最好的 JS 开发者改写另一门语言；更好的策略是给 JavaScript 加一个可擦除的类型系统，再用类型系统支撑 IDE 能力。

他的判断是：JavaScript 本身有函数一等公民等优秀基础，缺的是能表达意图、支持重构、跳转定义、引用查找、补全的大规模工具基础。TypeScript 的类型在运行时被擦除，目标不是生成更强 runtime，而是把开发期语义提升到足以服务大型团队。

## TypeScript 真正爆发，靠 GitHub 上的 open development
TypeScript 2012 年一开始就开源，但放在 CodePlex 上时基本是“源代码公开，开发仍封闭”；团队把外部 issue 抄回内部流程，社区参与弱。2014 年迁到 GitHub 后，工作流变成真正的 open development，Anders 认为这直接让 TypeScript 变成今天的产品。

VS Code 又把这条线放大：VS Code 用 TypeScript 写成，是早期重度使用者；TypeScript 与 VS Code 的互动也推动了 LSP 的成型。语言、IDE、社区协作三者互相喂养，解释了为什么 TypeScript 不是突然流行，而是多年逐步爬升到 GitHub 最常用语言之一。

## AI 时代更需要类型、局部性和语义服务
Anders 对“哪种语言更适合 AI”的回答很现实：AI 最擅长的语言，首先取决于训练集中有多少该语言代码，所以 TypeScript 和 Python 占优。他认为语言特性上，类型、类型推断、局部性会更重要：类型能减少歧义，推断能减少 token，模块边界和显式 import 能降低上下文窗口压力。

当前 AI 在 TypeScript 团队中的用途主要是 PR review、简单 issue、移植 backlog PR、生成测试等重复劳动；但在编译器这种 brownfield、低层、强算法约束代码里，AI 还难以掌握 types、symbols、binding、parsing 之间的大图。未来更关键的不是让 agent 用 grep/awk 找文本，而是让它接入 LSP/语言服务做语义查询、语义重命名和生成中校验。

## 软件工程师会更像架构负责人和审查者，但责任不会外包
Anders 认为 AI 会让工程师更像管理一群 junior programmer：agent 能吐出大量代码，但必须有人理解整体架构、审查变化、承担结果责任。vibe coding 在顺利时很爽，一旦偏轨，若人类不知道系统为何如此，就无法把它拉回来。

他也承认这会改变 craft 的快乐来源：他个人喜欢写代码，AI 会拿走一部分“亲手让东西跑起来”的满足感；因此 code review 本身需要被重新设计，例如由 AI 生成解释性导览，而不是只给审查者一堆按字母排序的 diff。

## 收束
最有边缘感的一点：Anders 把编程语言看成十年尺度的工程生命体——version 1 只是开始，version 2 修问题，version 3 才真正变好，然后还要说服世界采用。AI coding 也许正在进入同样周期：第一阶段让代码变多，下一阶段必须让验证、审查、语义工具和责任机制一起成熟。

模型：openai-codex/gpt-5.5
