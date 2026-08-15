---
title: "HTML is the new Markdown: How Anthropic engineers are building with Claude Code | Thariq Shihipar"
date: 2026-05-19T08:01:42Z
category: reading
description: "“HTML 取代 Markdown”的核心不是模型更爱读 HTML，而是人类终于愿意重新读计划、改计划、审计划。长跑 agent 把产品/工程决策变成了算力分配问题：让 Claude 跑 8 小时，本质是在授权它花掉一大笔计算预算；真正该花心思的是先用更可视、可交互、可校验的规格把意图对齐。"
source: "https://www.lennysnewsletter.com/p/html-is-the-new-markdown-how-anthropic"
---

## TL;DR
“HTML 取代 Markdown”的核心不是模型更爱读 HTML，而是人类终于愿意重新读计划、改计划、审计划。长跑 agent 把产品/工程决策变成了算力分配问题：让 Claude 跑 8 小时，本质是在授权它花掉一大笔计算预算；真正该花心思的是先用更可视、可交互、可校验的规格把意图对齐。

## 核心洞见
Thariq 的判断是：Markdown 曾经适合短计划，因为人还会逐行读、直接编辑；但当 agent 输出变成上千行、执行时间变成几十分钟到数小时，Markdown 计划反而让人退出循环。HTML 的价值在于降低“读懂并介入”的摩擦，可以放 mockup、代码摘录、文件结构、组件示例、交互控件和多视图标签页。

这也重新定义了产品经理和工程负责人：他们不只是写 PRD，而是在决定哪些问题值得消耗 token、时间和验证资源。规格不是旧时代流程残留，而是计算预算的投资备忘录。

## 具体机制
第一步是让 Claude 用 HTML 做 brainstorm，而不是给一串文字想法。Thariq 的 demo 里，Claude 为播客演示生成了 8 个带视觉 mockup 的候选方案；因为信息密度高、可扫读，他真的会把它们看完并选择方向。

第二步是把选中的方向扩展成 HTML implementation plan：包括 demo 脚本、文件系统、`SKILL.md` 摘录、mood board、组件、逻辑、模板和 helper scripts。关键提示并不复杂，只要明确“生成 HTML 计划，包含 excerpt、mockup、code，以及任何能给我最大上下文的内容”。约束要足够具体，但要给模型留出判断空间。

第三步是把计划里的局部难题变成一次性 micro-UI。比如计划中有一张“CSV 数据类型如何映射到可视化”的规则表，Thariq 不想在终端来回改文字，而是让 Claude 为这一个问题生成可编辑 HTML 界面：字段可改、规则可隐藏、结果可复制回计划。这里的产物不是长期软件，而是为了让人更好地思考某个局部决策的临时工具。

第四步是把 HTML 计划作为实现和验证的 artifact。清空上下文后，把计划交给 Claude 执行；完成后，再让验证 agent 对照 HTML 里的 mockup、类型接口、测试标准或 rubric 检查输出是否符合原意。HTML 既是沟通界面，也是验收基准。

## 延展用法
Thariq 还把 HTML 用作 living design system：把颜色、字体、间距、圆角、核心组件和变体压缩成一个 `design-system.html`，随 repo 迁移。Claude 可以直接引用这个文件理解设计约束；团队也可以把组件可视化页面、可下载透明 PNG、Remotion 视频素材等营销/设计协作资产建立在同一套 HTML 表达上。

更大的趋势是 just-in-time documentation：当生成、查找、重组文档的成本下降后，组织不必过度执着于统一模板和单一文档仓库，反而应该关心计划内容是否清楚、可执行、可验证。

## 隐藏限制
HTML 计划更好读，但也更容易制造漂亮幻觉：界面精致不代表判断正确，mockup 丰富不代表需求清楚。真正的质量控制仍在类型接口、测试数据、rubric、验收视频、历史失败样本这些验证机制里。

协作上，HTML artifact 可以显著提高别人愿意阅读的概率，但它也会制造新的管理问题：版本、托管、权限、评论回写、长期可检索性。模型能“找回来”不等于团队治理可以完全消失。

## 最后一念
这集最值得带走的不是“以后都写 HTML”，而是：AI 时代最稀缺的不是生成更多内容，而是设计一种让人愿意持续介入、修正、验收的工作界面。
