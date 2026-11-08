---
title: "Why has Shopify dropped React Native?"
date: 2026-11-08T00:24:03Z
category: reading
description: "Shopify 放弃 React Native 的核心原因，是 AI coding agents 大幅降低了分别开发和维护 Swift、Kotlin 应用的成本，让共享代码的收益缩小，而原生开发在性能、平台能力和工具链上的优势依然存在。Re"
source: "https://newsletter.pragmaticengineer.com/p/shopify-native-mobile"
author: "Gergely Orosz"
---

Shopify 放弃 React Native 的核心原因，是 AI coding agents 大幅降低了分别开发和维护 Swift、Kotlin 应用的成本，让共享代码的收益缩小，而原生开发在性能、平台能力和工具链上的优势依然存在。React Native 在 Shopify 的实践中取得了成功；这次转向反映的是技术选择的成本结构发生了变化。

2020 年选择 React Native，首先解决的是 Android 产品迟迟无法推出的业务问题。移动端当时已是 Shopify 的主要交易渠道：2019 年第三季度，71% 的买家通过移动设备购买商品，当年的 Black Friday 和 Cyber Monday 期间，移动端贡献了平均 69% 的销售额。但分别建设两套原生应用，需要应对 Android 更多的设备类型、旧版操作系统和低端机性能问题，iOS 产品成熟后，Android 用户仍可能长期得不到服务。Clubhouse 展示了这种延迟的风险：2020 年 3 月推出 iOS 应用，直到 2021 年 5 月才发布 Android beta，7 月才全球开放，错过了此前的增长高峰。优先服务 iOS 用户对主要面向美国市场的公司有商业合理性，面向全球、尤其是 Android 占主导地位的亚洲市场时，延迟覆盖的代价更大。

Shopify 在 2018 年底重写 Arrive，也就是后来的 Shop，已经验证了 React Native 的价值。这款拥有数百万 iOS 下载量的应用当时没有 Android 版本，重写后两端共享 95% 的代码，既推出了 Android 应用，iOS 崩溃也比原生版本更少，团队还能吸收非移动端开发者。2020 年全面采用 React Native，延续的就是这条路径：减少同一功能的重复实现，让工程师跨 Web、iOS 和 Android 工作，避免持续追赶两端功能一致性。彼时只有 iOS 版本的 Shopify Ping，后来的 Shopify Inbox，也计划借此推出 Android 版本。

到 2025 年初，这项策略仍然被 Shopify 视为成功。五年间，六款移动应用全部迁移到 React Native，各团队自行决定迁移时机和方式，期间继续交付功能。Shopify 报告其应用屏幕加载时间低于 500 毫秒，无崩溃会话比例超过 99.9%；其中 Shopify app 的屏幕加载达到 P75 低于 500 毫秒。React Native 的 hot reloading 还消除了大型原生代码库中一次微小修改也要等待数分钟编译运行的痛点，TypeScript 则降低了 Web 与移动端之间的人才流动门槛。这些收益解释了为什么 Head of Mobile Mustafa Ali 在 2025 年 1 月仍表示会继续投资 React Native。

这些成绩同时伴随着持续的抽象层成本。React Native 的调试不够稳定，在 VS Code 中正确配置也需要额外工作；原生 iOS 和 Android 已有成熟的一方调试工具。性能密集型代码、特定动画、长时间后台任务和 home screen widgets 等平台能力，仍需要原生代码与专业知识。React Native 框架覆盖范围小于原生平台，应用还必须引入更多第三方依赖。因此，共享实现减少了一部分开发工作，也增加了框架、依赖和平台之间的协调工作。

性能上的差异同样来自这层架构。React Native 维护 React Host Tree，再将其转换为平台上的 Host View Tree，通过减少昂贵的 UI 更新来控制渲染成本；原生实现则减少了中间层，并让团队更直接地控制渲染栈。2024 年推出的 New Architecture 改善了这条路径，但 Shopify 的实际迁移收益有限。Mustafa Ali 表示，Shopify app 和 Point of Sale 都已迁移，团队也是 Meta 之外较早采用的大型团队之一；应用启动速度在 Android 上提升约 10%，iOS 上约 3%，部分复杂页面甚至需要额外调优才能解决迁移后的性能下降。这些经验意味着，继续升级 React Native 并不能自动兑现团队期待的全部性能空间。

真正改变权衡的是 AI 开始承担足够多的实现、跨语言移植、测试和 review 工作。原生开发仍要维护两个平台，成本并未消失，但 Shopify 判断，这项成本已不再像 2020 年那样具有决定性。团队得以保留 React Native 时期形成的组织方式：同一名工程师负责一个功能在 iOS 和 Android 上的实现，无须重新拆成两支独立团队，也减少了上下文传递和跨团队沟通。Head of Engineering Farhan Thawar 将这种变化概括为：过去承担共享语言角色的 React，现在由 English 接替，开发者通过 LLM 跨越 Swift 和 Kotlin 的技能边界。

两套代码长期分化的风险，则需要由验证机制接住。Shopify 认为 agents 已能在 Android 和 iOS 之间移植功能、比较两端实现，并结合并排测试发现和修复差异。更关键的是，团队正在建设一套*共享测试套件*，用完全相同的测试验证 Swift 和 Kotlin 中的业务逻辑；一个功能必须在两个平台都通过，才能发布。这些逻辑可以在桌面环境中无界面运行，为 agents 提供快速迭代的反馈回路。跨平台一致性的保障，由共享实现进一步转向共享的行为验证。

迁移速度已经提供了一个具体结果：Shop 在 12 周内完成原生重建并发布，Shopify app 正在迁移，其余移动应用也将转向 Swift 和 Kotlin。团队要求每次重建都达到或超过现有的性能、稳定性、无障碍和产品质量标准，同时让代码更容易被人和 agents 理解、测试与修改。Farhan Thawar 预计，迁移后的持续优化还会进一步改善启动时间和交互响应；这些后续收益仍是预期，12 周交付则是已经发生的结果。

Shopify 的转向揭示了一种新的工程取舍：当重复实现变得便宜，减少代码重复就不再天然优先于减少抽象层；让双端行为可验证、让平台能力可直接控制，开始成为更有分量的架构目标。
