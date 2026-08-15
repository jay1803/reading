---
title: "Designing a Language (2017)"
date: 2025-11-19T08:34:44Z
category: reading
description: "语言设计的核心工作量不在于发明语法，而在于处理三件分离的事：grammar 只管结构，但上下文合法性（scope、类型、参数数量）根本写不进 grammar——几乎所有真实语言的语法规则都故意\"过度宽泛\"，把 statics 和 dynamics 另行定义。"
source: "https://cs.lmu.edu/~ray/notes/languagedesignnotes/"
---

## TL;DR
语言设计的核心工作量不在于发明语法，而在于处理三件分离的事：grammar 只管结构，但上下文合法性（scope、类型、参数数量）根本写不进 grammar——几乎所有真实语言的语法规则都故意"过度宽泛"，把 statics 和 dynamics 另行定义。

## 三层定义的分裂
Java 的官方 grammar 会接受 ~int x = y;~（y 未声明）——因为"标识符必须先声明"这类规则需要知道上下文，超出上下文无关文法的能力。所以语言定义必须分三层：
- *Syntax*：纯粹结构，grammar 描述
- *Statics*：上下文合法性（类型检查、scope、参数匹配），通常用 prose 或 formal semantics 描述
- *Dynamics*：运行时行为，同上

实际上大多数语言规范的 statics / dynamics 都是自然语言——这是工程现实，不是懒惰。

## 歧义消解编进 grammar 本身
优先级和结合性不是"约定"，而是直接编码进 grammar 规则的层次结构中。~Exp → Term → Factor → Primary~ 这条链条本身就强制了运算顺序；没有这个层次，~9-3*7~ 会有两棵合法的 parse tree。关键直觉：parse tree 的叶节点是 token 流，而不是字符——词法层和短语层的分离正是让 parser 可以处理注释和空格的原因。

## 隐藏限制：设计决策的长尾代价
换行是否有意义、ASI 规则、函数调用语法——这些看似"风格选择"，实际上决定了 parser 设计难度、工具链可靠性和学习曲线。JavaScript 的 ASI 要求程序员主动学习十几条插入规则，而不是依赖直觉；~puts 5 + 3~ 在 Ruby 里是 ~8~，但分两行写就是 ~5~。

## 留下的那个想法
Candygrammar 的反直觉：让语言看起来像英语，并不能降低编程难度。难的不是语法，是"把算法精确描述出来"这件事。Hypertalk 和 COBOL 用了最接近自然语言的语法，却没人觉得它们好学——语法只是包装，认知负担在里面。
