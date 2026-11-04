---
title: "Generating running routes with GPT-6 Astra and ChatGPT Work"
date: 2026-11-04T02:54:23Z
category: reading
description: "ChatGPT Work 已能根据住址自动生成可下载、可交互查看的跑步路线，但执行过程不透明、上下文压缩后无法找回代码，让完成任务与事后核查之间出现了明显断层。"
source: "https://simonwillison.net/2026/Sep/12/astra-running-routes/"
---

ChatGPT Work 已能根据住址自动生成可下载、可交互查看的跑步路线，但执行过程不透明、上下文压缩后无法找回代码，让完成任务与事后核查之间出现了明显断层。

Simon Willison 给运行 GPT-6 Astra（Max）的 ChatGPT Work 提出一个具体要求：使用 OpenStreetMap 数据，规划从家门口出发、最终回到家中的 5 公里和 10 公里跑步环线。系统工作了 27 分钟，交付了内嵌的路线可视化，以及可下载的 GPX 和 GeoJSON 文件；展示的 5 公里路线名为 El Granada harbor loop，实际长度为 5.1 公里。据系统事后解释，它先通过 Nominatim 定位住址，再用 Overpass 下载附近的 OpenStreetMap 道路和步道数据，最后在本地计算环线。

这些结果满足了请求，Willison 却无法在 ChatGPT 界面里看到实际执行的代码及操作细节；他明确把这种缺乏透明度视为产品的负面特性。等他想到索取生成路线的 Python 代码时，ChatGPT 已经无法提供，原因看起来是对话经历了上下文压缩。这暴露出 **compaction** 对可追溯性的影响：如果执行记录只留在会被压缩的上下文中，系统即使做出了成品，也可能随后丢失解释和复现过程所需的信息。因此，他主张任何使用上下文压缩的 LLM 系统，都应保存压缩前的原始文本，并允许 agent 通过工具重新读取。

路线图的呈现方式仍留下了可检查的产物。ChatGPT 调用 **visualize skill**，创建了 `/workspace/el-granada-5k-share.html`，直接嵌入聊天界面。Willison 分享的 HTML 在一个 `type="application/json"` 的 script 元素中保存了绘制路线和地图所需的完整几何数据，再通过 D3 渲染；D3 7.9.0 从 jsDelivr 加载。这个实现也受运行环境约束：visualize 的内容安全策略（CSP）只允许 cdnjs.cloudflare.com、esm.sh、cdn.jsdelivr.net、unpkg.com，以及 Google 和 Bunny 的指定字体域名，其他来源会被阻止，并且静默失败。这个案例呈现了 agent 产品的两项独立要求：既要能把自然语言请求变成可用成果，也要把支撑成果的代码、数据与执行记录保留下来，供用户事后检查。
