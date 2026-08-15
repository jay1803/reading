---
title: "Why Superhuman is built for speed: applying the 100ms rule to email"
date: 2025-06-03T14:39:54Z
category: reading
description: "为了提升用户体验，数字交互的响应时间应控制在100毫秒以内，即“100毫秒规则”。Superhuman 通过一系列技术和设计优化，将此规则应用于其邮件客户端，旨在打造全球最快的邮件体验，帮助用户节省时间。"
source: "https://blog.superhuman.com/superhuman-is-built-for-speed/"
---

## TL;DR
为了提升用户体验，数字交互的响应时间应控制在100毫秒以内，即“100毫秒规则”。Superhuman 通过一系列技术和设计优化，将此规则应用于其邮件客户端，旨在打造全球最快的邮件体验，帮助用户节省时间。
### 主题
#### 100毫秒规则 (The 100ms Rule)
100毫秒规则指出，每一次数字交互都应该快于100毫秒。这个概念源于 Gmail 的创造者 Paul Buchheit，他认为100毫秒是“交互感觉即时”的阈值。将延迟控制在100毫秒或更少，能让网站或应用感觉信息传输和显示是瞬时的。
#### 延迟 (Latency)
延迟是衡量用户在网站上发出的请求从用户端到服务器再返回到用户端所需的时间。延迟与带宽 (bandwidth) 不同，带宽是指在特定时间内站点可以传输的最大数据量。低带宽可能导致高延迟，但并非唯一因素。
##### 造成延迟的原因
- 传播 (Propagation): 信息传播所需的时间。例如，光速在纽约和旧金山之间的传播时间约为14毫秒。
- 传输媒介 (Transmission mediums): 承载信息的线缆类型，从铜缆到光纤。例如，光纤电缆从纽约到旧金山传输信息约需21毫秒，而4G网络可能给每次信息传输增加高达100毫秒的延迟。“最后一英里”由于传输媒介的限制，通常耗时最长。
- 网络跳数 (Network hops): 数字信息通过路由器 (router)、网桥 (bridge) 或网关 (gateway) 等设备。网络跳数越多，延迟越高。例如，信息传输100英里但经过五个设备，会比传输3000英里但只经过两个设备耗时更长。
#### 100毫秒规则的有效性
研究表明，延迟对用户行为和业务有显著影响：
- Amazon 发现其网站上每增加100毫秒的延迟，销售额就会损失1%。
- Google 发现生成搜索页面每多花500毫秒，流量就会下降20%。
随着互联网速度的提升，用户对即时响应的期望越来越高，如果页面加载不即时，用户可能会放弃。新的研究甚至质疑100毫秒是否仍然足够快。因此，Superhuman 将100毫秒规则视为最大值，并尽可能将延迟目标设定在50毫秒以下。
#### Superhuman 如何应用100毫秒规则打造极致速度
Superhuman 致力于成为世界上最快的邮件体验，其方法分为两部分：
1. 测量所有希望提速的方面：持续跟踪和测量[性能指标](https://blog.superhuman.com/performance-metrics-for-blazingly-fast-web-apps/)，以发现可优化的点并追踪进展。
2. 实现加速：结合通用的延迟降低最佳实践、Superhuman 特有的UI特性以及一些专有技术。
##### Superhuman 的技术实现
尽管 Superhuman 运行在 Gmail 和 [Outlook](https://blog.superhuman.com/superhuman-for-outlook/) 之上，使用相同的 APIs，但通过以下方式实现更快的速度：
- 本地存储信息：Superhuman 在用户的应用程序或浏览器中存储邮件数据库，即使离线也能极快显示。
- 缓存 (Caching)：利用缓存确保内容快速显示。
- 预加载和预渲染：预先加载和渲染用户最有可能很快查看的邮件线索。
- 最小化动画：不浪费时间加载动画。
- [键盘快捷键](https://blog.superhuman.com/keyboard-vs-mouse/)：几乎所有操作都可通过键盘快捷键完成，这通常比鼠标更快。UI中会显示快捷键提示。
- 命令库 (Command library)：用户可以通过 Cmd+K (Mac) 或 Ctrl+K (Windows) 快速找到所需功能，无需在菜单中翻找。
##### Superhuman 的提速功能 (“superpowers”)
Superhuman 提供了一系列旨在提升速度和效率的功能：
- Keyboard Shortcuts: 每个操作都有极快的快捷键。
- Superhuman Command: 通过 Cmd+K (或 Ctrl+K) 快速查找功能。
- Split Inbox: 将来自团队、VIP 和其他重要发件人的邮件分开，以便专注于最重要的信息。
- Remind Me: 将邮件延后处理，保持收件箱清空。
- Snippets: 通过按键命令即时插入常用短语、段落甚至整个邮件。
- Instant Intro: 快速完成感谢、将发件人移至密送 (BCC) 并开始回复。
- Quick Links: 即时插入超链接。
- Quick Quote: 轻松回复“线索中的线索”邮件。
- See Your Day: 在收件箱内一览日程安排。
- Select All from Here: 从收件箱特定位置或未读邮件开始全选，并进行延后或标记为完成。
- Unsubscribe: 一键退订不必要的邮件列表。
- Block: 屏蔽特定发件人或域名，摆脱垃圾邮件。
##### 专注与效率
Superhuman 通过其快速和简约的UI帮助用户专注于处理邮件，从而更快地完成工作。Superhuman 的客户平均每周在邮件上节省三个小时。
### 总结
通过严格遵循并优化“100毫秒规则”，Superhuman 运用本地存储、缓存、预加载、键盘快捷键和一系列高效功能，为用户提供了极致快速的邮件处理体验。
