---
title: "和产品一起成长 - 从 AI 猫娘到 Prowl 终端"
date: 2026-06-08T08:01:29Z
category: reading
description: "当单人开发者把 AI agent 稳定跑起来，工作流的变化不只是\"提速\"：人的角色从\"执行者\"变成了\"调度者\"，设备边界消失，任务在一天的碎片里被持续推进，工具链从\"工具\"演变为\"环境\"。"
source: "https://onevcat.com/2026/06/develop-with-ai/"
---

## TL;DR
当单人开发者把 AI agent 稳定跑起来，工作流的变化不只是"提速"：人的角色从"执行者"变成了"调度者"，设备边界消失，任务在一天的碎片里被持续推进，工具链从"工具"演变为"环境"。

## 具体机制
- 三只喂不同模型的"猫娘" agent 并行干活，各有 GitHub 账号、邮箱和独立人格设定；夜里通过邮件互评，自主小幅修改 AGENTS.md/SOUL.md，人格漂移经多轮后收敛稳定。
- MeowHook：薄 webhook 网关，GitHub/Linear 的 mention 或 issue assign 直接触发对应猫娘，结果回写原平台，reaction 从 👀 翻成 🚀 或 😕；CI 红叉由触发该提交的 agent 自行修复。
- argue：将同一问题抛给多模型 agent，互相辩论、投票，由得分最高者汇总报告，解决单一模型的视角盲区。
- Prowl：fork 自 supacode，基于 libGhostty，专为并行多 agent + 多 repo 工作流定制，目前领先上游超 1000 个提交，已是完全不同方向的产品。

## 关键实践细节
- agent id 注入环境变量 → git/gh 身份自动映射，严格区分"人 + co-author"与"agent 独立提交"两种 attribution，事后审计清晰可追溯。
- 手机 + 电脑 5:5 分工：碎片时间（通勤、做饭、等红灯）用手机 IM 安排任务；大段时间坐下来用 Prowl 并行跑多个 agent。
- 最早练手项目 transcrab 实现"发链接 → 半分钟后读中文全文"，整个开发过程未打开任何代码编辑器——这是他的第一个"以 agent 为目标用户开发的项目"。
- Linear issue 直接 assign 给对应猫娘，将看板变成异步任务池；人不必盯着，碎片时间扫一眼即知大盘状态。

## 值得注意
自主、私有、可控是整套方案的设计哲学核心：agent 跑在自家 mac mini，凭证自有，OpenClaw 和 MeowHook 均为自维护 fork。但这也意味着上游 PR 难以被接受（agent id 注入 PR 就花了很多说服成本），个人维护负担不低，且整套方案难以直接复用——它是"以 agent 为工具定制出的私有基础设施"，不是通用解决方案。
