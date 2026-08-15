---
title: "The Claude Code research playbook behind my State of Marketing Reports"
date: 2026-05-07T08:02:46Z
category: reading
description: "这篇最有价值的结论不是“Claude Code 可以帮你做调研”，而是：一旦调研规模超过几个问题，Claude Code 必须被当作一套可审计的数据生产系统来用。核心不是让 agent 更聪明，而是把研究对象、URL、字段定义、方法、未知值、抽查记录和输出模板都外部化到 spreadsheet、skill、art..."
source: "https://newsletter.mkt1.co/p/state-of-marketing-report-part-3-how-to-research-in-claude-code"
---

## TL;DR
这篇最有价值的结论不是“Claude Code 可以帮你做调研”，而是：一旦调研规模超过几个问题，Claude Code 必须被当作一套可审计的数据生产系统来用。核心不是让 agent 更聪明，而是把研究对象、URL、字段定义、方法、未知值、抽查记录和输出模板都外部化到 spreadsheet、skill、artifact 和文件系统里；否则 Claude 会用看似完整的答案掩盖方法漂移、抓取失败和幻觉数据。

## 核心洞见
Claude Code 的调研起点应该是“先研究自己公司”。这不是自恋式练习，而是低成本校准：你最知道哪些信息应该存在，因此最容易发现 LLM 抓不到什么、误读了什么、是否被 JavaScript 渲染挡住、schema/robots.txt 是否让爬虫看不懂。作者在 100 家 B2B 公司报告中发现，很多基础信息抓不到并不是 Claude 不会找，而是公司网站本身对 LLM 不可读。

文章把 AEO 具体化成几个可操作检查：主页内容是否在 HTML 中，而不是只靠 JavaScript；是否有 schema；robots.txt 是否明确表达 LLM crawler 规则。报告中的关键数字是：只有 2% 的 startup 使用 FAQ schema，40% 主页完全没有 schema，97% 允许 LLM crawler，但只有 12% 在 robots.txt 里显式写了 LLM bot 规则。Attio 的做法被作者认为聪明：挡 CCBot 这类训练爬虫，但允许 GPTBot 和 ClaudeBot 这类实时引用爬虫。

做多公司调研时，spreadsheet 必须成为 source of truth。第一列是公司，后续每个数据点、每个关键 URL 都应该是单独列；不要让 Claude 每次根据公司名临时猜 URL。研究顺序也应按“一个字段横向跑所有公司”，而不是“一个公司纵向填完所有字段”。这样才能先在少数样本上验证方法，再扩展到全量，并让后续字段复用前面已经确认的 URL 和上下文。

## 具体机制
作者反复强调要把“有效方法”沉淀成 skill。skill 里不只是 prompt，而是字段定义、抓取路径、失败处理、是否需要人工确认、输出模板、对应 spreadsheet 位置。比如竞争调研 skill 应该先问公司列表来源，再创建 tracker，再锁定 pricing、positioning、customer logos、recent launches 等字段，并要求每个需要抓取的页面都先变成一列 URL。

Claude Code 的 memory 在作者看来不可靠。它会自动记东西，但不一定在正确时间引用；session 压缩后也容易丢关键上下文。因此重要信息要显式保存到 CLAUDE.md、skill、spreadsheet 或本地文件。这个判断很实用：可靠性来自用户可见、可检查、可复跑的文件，而不是模型声称“我记得”。

大规模报告的关键是分阶段：先确定公司列表，再设计字段，再每个字段用 3-5 家公司试方法，确认后扩展到全量；跑完后要抽查随机样本和所有 outlier。作者的经验是，outlier 经常不是洞察，而是 scrape error。她也承认很多时间不是花在自动化生成，而是花在最后一公里的数据验证上。

Claude Artifacts 应该用于调研中期的快速可视化，而不是一开始就进 Figma。HTML chart/table artifact 可以快速尝试不同切法，比较 by category、by funding、by company size、mean vs median 等视角；等数据锁定后再推到 Figma、Gamma 或其他设计工具做最终资产。否则数据一改，图表和洞察都要反复重做。

## 隐藏限制
这篇文章最有用的部分是它没有神化 agent。Claude 会自信地给出低效方法，比如作者一开始用 Clay MCP 消耗 250 credits 抓 follower counts，后来发现 curl 直接抓 HTML 更快。Claude 也会填入看似合理的圆整数字、把 unknown 当作 no、找出已离任 1-3 年的高管，或者在 JavaScript-heavy 页面上抓不到正文却不充分暴露失败。

因此字段设计要允许第三状态：yes / no / unknown。凡是无法确认的格子应留空或标记 unknown，而不是为了表格完整性补一个假值。对难抓字段也要有放弃机制：如果 LinkedIn posts、JS 渲染内容或某些页面需要过高 workaround，可能应该从自动化范围里移除，而不是让最难字段拖垮整个调研系统。

文章里推广 MKT1 MCP Server 的部分带有明显产品营销目的，但它提出的分发判断值得单独看：Claude/LLM 不只是内容生产工具，也可能变成内容分发引擎。MCP 可以把报告、模板、job board、数据集和研究 skill 暴露给用户，让内容从“被阅读的页面”变成“可被调用的资源”。Profound 的 “Open in ChatGPT / Claude” 按钮和 AllTrails MCP 都是这个方向的早期形态。

## 一句话总结
Claude Code 调研的胜负手不是 prompt 写得多漂亮，而是能否把 agent 的每一步变成可验证、可复用、可回滚的数据流程；真正的护城河在 workflow、skill、spreadsheet 和分发接口，而不是一次性生成的答案。这篇可以看成调研版的 Software Factory。
