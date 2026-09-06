---
title: "The asteroid currently hitting front end web development"
date: 2026-09-06T04:35:00Z
category: reading
description: "生成式 AI 正在把前端开发从需要长期积累的专业知识改造成可低风险交给代理执行的工作，冲击的是整个前端教育、工具设计与 Web 标准演进的价值基础。"
source: "https://nolanlawson.com/2026/08/23/the-asteroid-currently-hitting-frontend-web-development/"
author: "codechicago277"
---

生成式 AI 正在把前端开发从一门需要长期积累、传授和更新的专业知识，改造成一类可以低风险交给代理执行的工作；真正受到冲击的因此不只是一批开发者，而是整个前端教育、工具设计与 Web 标准演进的价值基础。

变化已经体现在知识生产者的去向上：Axel Rauschmayer、Salma Alam-Naylor、Josh W. Comeau 等前端教育者正在退出或减少投入，Kent C. Dodds、Addy Osmani、Rachel Nabors、Lydia Hallie 等人则把注意力转向 AI。Nolan Lawson 自己曾长期研究 CSS 性能、shadow DOM、浏览器样式引擎和 CSS-in-JS，但当他把一个经验丰富的开发者也容易答错的问题交给 Claude Sonnet——Chrome trace 中反复出现高昂的 "Style Calculation"，而 Layout 成本较低时该查什么——Claude 已能给出接近专家水准的诊断路径。

Claude 首先判断瓶颈更可能来自大规模 selector matching 与 style invalidation，而非几何布局计算，随后覆盖了复杂或深层选择器、范围过大的 attribute selector、CSS-in-JS 产生的海量规则、在 `<body>` 或顶层容器切换 class、继承属性与高层 CSS custom property 的传播、频繁 DOM mutation、每帧批量修改 class、强制同步 style read，以及 shadow root 之间无法共享 stylesheet 等来源。它还准确建议开启 Chrome DevTools 的 "Selector Stats"，检查慢选择器及匹配次数、Recalculate Style 的 initiator 和调用栈、每次重算影响的元素数量、mutation 在 DOM 中的位置，以及 "Forced reflow" 警告；对应修复包括缩小状态切换和 custom property 的作用域、简化选择器、批量执行 DOM 更新，并用 `content-visibility: auto` 或 `contain: style layout` 隔离子树。对 Lawson 来说，关键事实是：即使他曾在浏览器性能团队工作，现在遇到慢网站也可能直接把 Chrome trace 交给 Claude Code，而这种做法在真实工作中已经产生了不错的结果。

前端之所以比其他软件领域更早被代理接管，首先因为自动生成代码的失败成本通常较低。数据库迁移需要多轮 AI review、人工审查和 staging 验证，一个 React component 却更容易未经监督直接进入生产环境。代理仍可能破坏 accessibility、制造无限循环或阻塞用户，但前端代码总体更短命、更容易替换，因此开发者更可能接受 "yolo" 式部署。这会进一步削弱深入掌握浏览器机制、CSS 性能和框架细节的现实回报。

随之贬值的是长期主导前端讨论的 **developer experience**。Svelte 和 Solid 过去强调更少的代码、更好的性能和更符合人体工程学的开发方式，但 Cursor 把代码库从 Solid 迁到 React，Viget 也从 Lit 转向 React；代理让大规模重写变得便宜，却没有促使团队选择更精简或性能更好的框架，因为训练数据中过度代表 React，代理对它掌握得最好。由此产生的新评价标准是 **agent experience**：决定技术栈的逐渐不再是人类写起来是否优雅，而是模型能否稳定生成、理解和修改代码。

同一逻辑还会改变 Web 标准的优先级。让 CSS shorthand 更简洁、让 JavaScript syntax 更短，对代理几乎没有价值，因为写三行 CSS 和写一行的成本差异很小，新语法反而可能因训练数据不足而需要额外指导。Lawson 早年参加 TPAC、推进 Web Components 标准时，曾听 Chrome 团队成员指出 shadow DOM 和 custom elements 只改变代码的组织方式，并没有赋予浏览器新的能力；相比之下，Project Fugu 一类工作可以直接扩展 Web capability。AI 编码会强化这种取向：标准教育仍会存在，但内容将从"如何采用更新、更方便的语法"收缩到"浏览器获得了哪些新能力"，而后一类功能更少、在标准机构中也更容易引发争议，因此可供文章和会议演讲持续开发的素材会明显减少。

前端教育尚有三个可能的落点。其一是向代理提供架构层面的判断，因为模型和 agent harness 偏爱 React，尤其偏爱 SPA，却未必知道营销网站采用 Astro 或 Eleventy 这类 MPA framework 可以减少约一半代码，同时避免 back button、focus state 和性能问题。即使 Astro 因语法近似 React 而容易让代理误判，代码总量的大幅下降仍可能抵消这种摩擦。专家的价值将更多体现在选择正确的问题规模、页面架构和平台能力，而非亲手填写每个实现细节。

其二是让网站更适合代理访问，Vercel 的 `is-agentic` 就代表了这个方向。server-rendered content、正确的 accessibility 和良好的 page speed 本来就是公共网站应具备的基础，如今"AI 可用性"可能为这些实践带来新的组织动力。不过这个机会依赖于现有 Web 形态继续存在：查询 Seattle 到 Paris 的机票时，用户更愿意直接询问代理，也不愿在缓慢的网站上点击一连串按钮；目前代理做不到，主要因为网站主动封锁 bot 或没有提供 MCP，而不是网页界面天然不可替代。只要创业公司打通数据与交易接口，人类直接浏览网站的需求就可能进一步萎缩。

其三是修复大量 vibe coding 制造的系统。AI 正在持续生成缓慢、不合规、存在安全漏洞，却又逐渐成为 "load-bearing" 基础设施的前端代码；当业务收入依赖这些网站，而创建者对 Web 的理解仅停留在"托管在互联网上的 app"时，一句 "fix my website pls" 未必足以完成修复，性能、accessibility、合规与安全专家仍可能获得咨询市场。但这个窗口并不稳固：到 2027 或 2028 年，下一代 self-healing web app 完全可能在平均水平上超过人类专家。

这场变化真正令人不安之处，在于多年积累的知识可能迅速失去稀缺性，而许多人原本清晰通向退休的职业轨迹在最后几年突然被改写。Lawson 用小行星撞击地球来描述这一刻：撞击已经发生，所有人仍在勘察废墟，既不知道尘埃落定后的生态，也不知道哪些"小型啮齿动物"会开启新的哺乳动物时代。他也把它类比为 Covid 初期——当一种力量注定将在未来数年支配生活时，研究病毒、流行病学和口罩比宣布厌倦这个话题更有用。前端领域未来或许会面目全非，但眼下最危险的选择，是把对 AI 的疲惫和恐惧包装成超然姿态，从而拒绝承认决定专业价值的条件已经发生根本变化。
