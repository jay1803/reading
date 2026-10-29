---
title: "$340m/yr heroku for claude code"
date: 2026-10-29T05:45:43Z
category: reading
description: "Vercel 正成为 Claude Code 等编程代理的应用部署平台，代理部署占比从不到 3% 升至 50% 以上，Claude Code 贡献其中 75%，Vercel 借四笔收购扩张至后台任务、沙箱和后端服务市场。"
source: "https://newsletters.feedbinusercontent.com/df4/df48bcb3938848049b257e3a881e2b5f3b551d0a.html"
author: "Jan-Erik Asplund via Sacra"
---

Vercel 正成为 Claude Code 等编程代理的应用部署平台，即使自家的文本生成应用工具 v0 已在竞争中落后于 Lovable 和 Replit。到 2026 年 6 月，代理发起的部署已占 Vercel 全部部署的 50% 以上，2025 年末这一比例还不到 3%；2026 年 4 月，Claude Code 贡献了代理部署量的 75%，v0 与 Lovable 合计仅占 6%。这意味着 Vercel 可以通过承接其他编程工具生成的应用，获得 AI 编程增长带来的基础设施需求。

与 Vercel 的部署平台路径相比，Replit 和 Lovable 正通过全栈服务同时获取应用创建与上线运营两个阶段的收入：创建阶段承接 token 消费，上线后提供数据库、身份认证和支付基础设施。Replit 在 2026 年 4 月达到 5.25 亿美元年化收入，2025 年同比增长 1,775%；2026 年 3 月完成 4 亿美元 Series D 融资，估值 90 亿美元，约为前瞻收入的 19 倍。Lovable 在 2026 年 5 月达到 5 亿美元年化收入，2025 年同比增长 3,471%；其去年 12 月 Series B 对应估值为 66 亿美元，收入倍数为 26 倍。两家公司都在把生成应用的入口优势延伸为持续托管应用的收入。

为了扩大对代理应用的承载能力，Vercel 在过去十二个月完成了四笔收购。2025 年 7 月收购 NuxtLabs，将框架与服务端工具从 React、Next.js 扩展至 Vue、Nuxt；2026 年 3 月收购 new.website，为 v0 增加表单、内容和数据能力；同年 7 月收购 Better Auth，补足身份认证与代理委托权限，并收购 Stakpak，引入监控、修复和运营生产软件的 DevOps 代理。这些收购覆盖了应用构建、授权与生产运维，使其平台能够承接更完整的应用生命周期。

这一扩张也源于代理应用对运行环境的新要求：异步执行任务、运行不可信代码，以及在长时间任务中持续保存状态。Vercel 因而推出后台任务产品 Vercel Workflows，与 Temporal、Inngest 竞争；通过 Vercel Sandbox 提供隔离代码执行，与 E2B、Daytona 竞争；再以 Vercel Services 进入后端服务市场，对标 Railway、Render、Fly.io 和 Northflank。Vercel 的机会在于，无论应用由哪个编程代理生成，都能把后续执行、状态管理、安全隔离与生产运维留在自己的平台上。
