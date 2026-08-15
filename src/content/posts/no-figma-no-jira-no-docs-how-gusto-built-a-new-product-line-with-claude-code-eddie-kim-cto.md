---
title: "No Figma. No Jira. No docs. How Gusto built a new product line with Claude Code | Eddie Kim (CTO)"
date: 2026-06-30T08:04:46Z
category: reading
description: "Gusto CTO Eddie Kim 带领 4 名工程师和 1 名设计师，用 10 周从零代码做到 Gusto Cofounder 的一级发布。没有 Figma、没有 Jira、没有 tech spec、没有 standup、没有 retro——唯一保留的是一个 24/7 PermaZoom 和大量 Claud..."
source: "https://www.lennysnewsletter.com/p/no-figma-no-jira-no-docs-how-gusto"
---

## 核心论点：代码成本趋零时，所有过程性基础设施都可以抛弃

Gusto CTO Eddie Kim 带领 4 名工程师和 1 名设计师，用 10 周从零代码做到 Gusto Cofounder 的一级发布。没有 Figma、没有 Jira、没有 tech spec、没有 standup、没有 retro——唯一保留的是一个 24/7 PermaZoom 和大量 Claude Code token。他的核心主张：当写代码的成本接近零，整套"用文档和流程控制不确定性"的软件工程基础假设就失效了。PR 本身就是产品决策的单元，而不是执行文档决策的结果。

## 垃圾桶方法：好代码随时可删，PR 就是 PRD

他们开的不是 draft PR，而是真正准备好人工 review 的 PR。讨论功能值不值得存在，如果答案是否，就直接关掉这个 PR——哪怕代码质量完全合格。Eddie 把这叫做"垃圾桶方法"（trashcan method）。

更极端的版本：他带回来的原型，工程师当场建议从零重写用 TypeScript + Cloudflare Worker。他情感上不愿意（那是我的代码），但最终同意了。他回头看认为这是整个项目最正确的决定。现在他已经完全没有了删掉"好代码"的心理障碍。

## 设计师进全公司工程师前 6% 靠的是工程文化，不是天赋

Katie（唯一的设计师）在 DX 的 PR throughput 指标上达到全公司 R&D（1000+ 人）的第 94 百分位。她自己解释：技术好奇心稍强，但更重要的是团队愿意认真 review 她的 PR，给具体反馈，教她怎么判断 Claude 生成代码的质量。这个团队的中位 PR review 时间是 9 分钟，因为 PermaZoom 里随时有人，直接开 breakout room 当场讨论。

Eddie 的推论：多数工程团队对非工程师的 PR 优先级低于工程师——这是反模式。只要投入 review 和反馈，回报极快。

## 假前端先行：UI 先上生产，后端再注入

设计师先把 UI 推到生产（返回固定假数据的纯前端），工程师并行搭数据模型和 agent loop，逐渐把真逻辑接入同一个前端页面。任何时刻生产环境都有"哪里不对"，但它在持续收敛。这个做法让 prototype 不再是一次性展示品，而是可以直接 breathe life 进去的活体。

## Stack 极简：Cloudflare Worker + Vercel AI SDK，仅此而已

没有第三方 memory 框架，没有复杂 orchestration。Memory 就是一个数据库字段。他认为大多数人对"构建 agent"的恐惧是多余的——它就是一个 agent SDK 跑在云上，能用工具、能看文件，没有什么复杂的。Vercel AI SDK 连 while loop 都不用写，stream 函数自己处理循环。

## Eval-first 是 AI bug 修复的唯一纪律

Eddie 的实际工作流：找到一个 GitHub issue + 触发问题的真实用户对话 → 让 Claude Code 先写一个 failing eval 复现问题 → 再修复 → eval 通过 → 开 PR。他从来不是 TDD 信徒，但对 AI 系统的 eval-first 完全接受，因为对话型 bug 没有其他方式验证"真的修了"。趁 Claude Code 跑 eval 的时间，他去开第二个 terminal 做另一个任务。

## 领导者必须亲手 merge 生产代码，不能只停在原型

只拿原型来说"你们看，这很快"会让工程师感到被轻视——他们知道原型到生产之间有多少真实复杂度。Eddie 在这 10 周里进了 IC 模式，自己的 DX 数据是全公司 95th percentile。他的建议：如果你是领导者，把原型能力延伸到真实的、被 review 过的、进了生产的代码——这是理解团队节奏和 AI 边界的唯一方式。

## Gusto Cofounder 的起点是一次误机的候机厅

他从马德里飞旧金山，中转伦敦时晚点错过航班，多了 5 小时空档。掏出电脑，把一直在脑子里转的一个想法 vibe code 出来，落地旧金山时原型已完成。他事后去找妻子说：我们应该多去度假。

## Gusto Cofounder 的产品洞见来自亲手装 OpenClaw

Eddie 不是从文章或演讲里理解这类产品的价值的，而是自己接 Telegram 用了之后才有了 visceral 理解——同时发现了问题：太难装了，得买 Mac Mini。这直接催生了 Cofounder 的两个核心设计决策：云端运行（不用自己的机器）、SMS 和 Slack 作为一级交互渠道。
