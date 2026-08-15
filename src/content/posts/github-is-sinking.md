---
title: "GitHub is sinking"
date: 2026-05-12T08:01:38Z
category: reading
description: "作者真正要拆的不是 GitHub 的某个故障，而是“GitHub = Git”的集体幻觉：一旦中心化托管平台开始被可靠性下降、AI 垃圾流量、机器人经济和企业级复杂度吞没，继续把所有开发协作押在 GitHub 上就从默认选择变成单点风险。"
source: "https://dbushell.com/2026/04/29/github-is-sinking/"
---

## TL;DR
作者真正要拆的不是 GitHub 的某个故障，而是“GitHub = Git”的集体幻觉：一旦中心化托管平台开始被可靠性下降、AI 垃圾流量、机器人经济和企业级复杂度吞没，继续把所有开发协作押在 GitHub 上就从默认选择变成单点风险。

## 核心主张拆解
**GitHub 的信任资本正在被消耗**
作者用 GitHub 官方 uptime、第三方历史状态图、近期可用性问题和用户体感串起一个判断：微软收购后的 GitHub 已经不再像一个稳定的开发基础设施，而更像被大型平台惯性、Copilot 产品线和 AI 生成内容拖累的 Microsoft 服务。

**“Git is not GitHub”是迁移论证的地基**
Git 本身是分布式开源工具，每个仓库都有完整历史，中心化 forge 只是社交协作的便利层。GitHub 过去是有用附加层；当这个附加层开始制造可用性、治理和垃圾内容问题时，把它当成不可替代基础设施就是概念错误。

**网络效应正在变成劣质信号**
作者认为 GitHub 的 star、issue、公共项目发现机制正在被 fake stars、bots 和 slop 稀释。网络效应仍然强，但如果网络里的信号质量下降，平台规模反而会变成过滤成本和治理成本。

**CI 绑定放大了平台风险**
GitHub Actions 被作者视为另一个锁定点：很多团队把发布、测试、自动化都绑到 GitHub 上，迁移因此变麻烦；但正因为 CI 已经进入关键路径，GitHub 的不可靠性才更像业务风险，而不是网页偶尔抽风。

**迁移不必一次完成**
作者的实用建议是先启动退出计划：把 repo 推到另一个 upstream，逐步迁移项目，不必立刻搬走所有 issue、CI 和协作流程。核心动作不是宣布立刻离开，而是停止让 GitHub 继续成为唯一上游。

## 可选路径
**中心化替代品**
Codeberg 被作者视为最稳妥的非营利/社区选项，也是 Forgejo 的旗舰实例；Tangled 还在 alpha，但 AT Protocol 集成有实验价值；Gitea 提供云托管；GitLab 适合企业但臃肿；Bitbucket 只是“技术上符合非 GitHub”的备选，作者明显不推荐。

**自托管与更低层方案**
如果团队愿意承担运维，可以自托管 Forgejo、Gitea 或 GitLab，并把 actions、releases 放在自己的 forge 里。更极端的版本是直接用 Git over SSH，协作再用邮件、patch 或其他流程处理；Linux 的邮件列表模式被作者用来提醒：中心化 forge 是便利，不是必需品。

## 值得质疑
**证据链偏情绪化**
文章把 uptime、Microsoft 收购、Copilot、fake stars、AI slop、Actions 复杂度放进同一个“沉船”叙事，但没有严格区分哪些是可靠性问题、哪些是产品治理问题、哪些只是作者对微软生态的厌恶。结论方向有价值，因果链略粗。

**迁移成本被低估**
对个人项目和小团队，换 remote 很容易；对依赖 GitHub Issues、Actions、Packages、Security Advisories、PR review、SSO、权限审计和生态可见度的组织，迁移会触发真实的流程重构。更稳的策略应是先镜像、备份、抽离 CI，再决定是否主迁移。

## 最后一层
GitHub 最大的风险不是它马上不可用，而是开发者把一个可替换的协作层误当成不可替换的公共基础设施；真正该做的是保留可迁移性，让 Git 重新高于 GitHub。
