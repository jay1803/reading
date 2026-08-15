---
title: "Building the most AI-pilled engineering team in the world | Fiona Fung (Anthropic)"
date: 2026-06-24T08:01:36Z
category: reading
description: "Anthropic 工程师每季度代码量是 2025 年的 8 倍。Fiona 的核心主张不是\"效率提升\"，而是：代码不再是瓶颈，天花板已被抬起，限制因素变成了\"你敢多有野心\"。以前觉得\"太复杂做不了\"的功能，现在的答案变成了\"直接让 Claude Code 做，它能行\"。问题不再是能不能做，而是值不值得做、敢不敢..."
source: "https://m.youtube.com/watch?v=Ybrl4FYM57c&ra=m"
---

## 编码已被解决——天花板抬高，瓶颈变成了你敢多有野心

Anthropic 工程师每季度代码量是 2025 年的 8 倍。Fiona 的核心主张不是"效率提升"，而是：代码不再是瓶颈，天花板已被抬起，限制因素变成了"你敢多有野心"。以前觉得"太复杂做不了"的功能，现在的答案变成了"直接让 Claude Code 做，它能行"。问题不再是能不能做，而是值不值得做、敢不敢做。非工程师也在提交代码——PM、设计师都在 merge PR，这既是能力释放，也是验证压力的来源。

## 验证是新 TDD：把"什么叫好"写进 repo，让模型对照 spec review

代码生成速度极快，验证成了新瓶颈。Fiona 的解法：把"什么叫好"（设计规范、内容规范、质量标准）写进 repo，保持与代码同步更新，然后让 Claude Code review 对照 spec。这是 TDD 的进化版——不是写测试，而是写规格。同时引入"bad vs. sad"质量框架：bad = 不可恢复错误（如 CLI crash，用户丢失工作）；sad = 可恢复但有痛点（如界面闪烁）。每个团队定义自己 surface 的 bad 和 sad，不再用一刀切的 dashboard 衡量不同场景。sad 的积累可以升级为 bad。

## 高 agency 必须配高 accountability，否则只是运动感

Claude Code 和 Co-work 团队文化核心：高 agency（有想法就去做）必须配高 accountability（假设是什么、outcome 是什么）。Fiona 把 Claude 持续接入所有 repo 和 Slack 频道，每月与下属开会时直接回顾"这段时间上了什么、结果如何、出了什么 bug"——以代码产出为出发点，但问的是 impact。她的告诫："别把运动感当成进展"（don't forsake motion for progress）——token 用量、代码行数都是代理指标，不是 outcome。指标本身会随景象变化而失效，需要定期质问"这个指标还在服务我们真正想要的 outcome 吗"。Facebook Marketplace 早期按"卖家数量"扩张，结果某地区因有"超级卖家"反而不需要很多卖家，差点错误否决了这个区域——指标需要随理解迭代。

## 经理必须当 IC，不是仪式，是保持产品触感的唯一方式

新加入的经理，必须先做几个月 IC，再承担汇报责任。Fiona 自己在 Claude Code 上提 PR——不是因为 PR 本身价值高，而是只有每天使用自己的产品，才能保持"触感"，这是 dashboard 和演示文稿给不了的。她离开 Meta 时上一次提生产代码已是 2017 年；用 Claude Code 重新找回了自信。她上一个团队做 VR 时，自己的 dog fooding 反而复现了其他人都无法稳定复现的地板高度 bug。对于无法直接使用产品的领导者，建议用客户拜访替代——亲身接触总比看数字更快暴露真实问题。

## AI 工作带来孤独，解法是平行游戏而非配对开发

当所有人开始独自与 agents 工作，团队的社交纤维开始断裂。Fiona 的解法：pairwise programming lunch——不是配对开发，而是"平行游戏"，各做各的，但在一起。意外收获：每个人用 Claude Code 的方式都不一样，观察别人工作本身就是学习。Hackathon 在 AI 时代反而变得更重要，不是更不重要。

## 从同步 prompt 到异步 routine 编排，context switching 是未解问题

Routines（定时代理编排）让异步工作模式成为可能：例程在凌晨跑完，Fiona 醒来已有 PR 等待 review，不再需要每天早晨手动翻 Slack 频道。但随之而来：同时有 20 个 agents 运行时，context switching 的认知负荷暴增。她承认还没解决这个问题，已经开始重新 block 专注时间来消化异步工作积累——某种意义上是回到了"心流保护"，只不过是为了消化 agents 的输出而非自己写代码。

## 两类人值得招：产品感知构建者 + 深度系统专家

不再需要大型专职 iOS/Android 团队，但仍需要 iOS/Android 专家——"任何需要 trust but verify 的地方，就是需要深度专家的地方"。另一类：具有产品感知的创意构建者（dreamers），能从想法到 launch 全程负责、迭代反馈、打磨体验。两类人都需要，比例在变，但谁也省不掉。Fiona 最初加入 Claude Code 时发现缺少系统背景的人，补齐后才稳住了可靠性。
