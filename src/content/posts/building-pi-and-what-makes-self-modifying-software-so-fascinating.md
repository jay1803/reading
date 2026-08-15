---
title: "Building Pi, and what makes self-modifying software so fascinating"
date: 2026-04-30T08:02:48Z
category: reading
description: "Mario Zechner 是 Pi 的作者：一个极简、可自我修改的 AI coding agent，也是 OpenClaw 底层 agent core 的重要基础。Armin Ronacher 是 Flask 作者、长期开源维护者，也是 Pi 的早期重度用户和贡献者；他最近访谈了 30+ 工程团队，观察 AI..."
source: "https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying"
---

## 嘉宾背景
Mario Zechner 是 Pi 的作者：一个极简、可自我修改的 AI coding agent，也是 OpenClaw 底层 agent core 的重要基础。Armin Ronacher 是 Flask 作者、长期开源维护者，也是 Pi 的早期重度用户和贡献者；他最近访谈了 30+ 工程团队，观察 AI agents 如何改变真实研发组织。两人都深度使用 AI 工具，但整场对话的立场并不亢奋：AI 很强，工程约束也没有消失。

## TL;DR
这场对话最有价值的线索是：AI 把“生成改动”的成本压到极低，但工程真正稀缺的东西仍是判断、责任、上下文、维护痛感和说“不”的能力。Pi 的自修改能力之所以有吸引力，不在于它替工程师消灭决策，而在于它让工具本身重新变成可塑材料；危险也在这里——当代码、PR、issue、demo、内部工具都可以被廉价生成时，组织如果没有新的瓶颈和摩擦，复杂度会比生产力更快膨胀。

## Pi 的核心不是功能多，而是让用户把工具改成专用工具
Mario 做 Pi 的起点是对 Claude Code 失去信任：Claude Code 早期简单、稳定、可预测，但 2025 年夏天后功能增加、隐藏 context 注入、system prompt 变化和不可见 reminder 让既有 workflow 频繁失效。他也试过 OpenCode 等开源替代品，但不喜欢工具在背后裁剪 tool result、每次 edit 后自动塞入 LSP diagnostics 这类“替用户做主”的设计。

Pi 因此反向选择了极简：自己的 LLM provider 抽象、通用 agent loop、TUI，基础工具主要是 read / write / edit / bash。它真正的扩展性来自大量 hook points：用户可以加 custom tools、改 compaction、改 TUI、改 plan mode、接入 MCP，甚至让 Pi 自己修改 Pi。这让它更像一套可被现场加工的施工工具，而不是一个包办所有场景的通用 IDE agent。

Mario 的判断是，不同任务需要不同 harness；建筑工地不会只用锤子，工程项目也不该假设一个 agent 适合所有任务。自修改软件的意义在这里：用户不再只是配置软件，而是让软件根据具体任务重塑自身。

## AI 放大了产出，也放大了自动化偏见
Armin 访谈 30+ 团队后的观察很直接：很多公司在假期后真正开始大规模使用 Cursor / Claude Code 等工具，随后代码质量普遍下降。原因不是工程师想写烂代码，而是保持 agent 输出干净需要持续努力；PR 变得更大、更频繁，review 心理负担上升，团队更容易 rubber stamp。

Mario 补了一层：agent 经常会先产出一段“刚好正确、非常干净”的代码，让人误以为它一直可靠；几分钟后另一个窗口可能生成灾难级垃圾，但人已经进入 automation bias。危险不在于 agent 永远差，而在于它间歇性表现得太好，足以让人降低审查密度。

两人反复强调“痛感”这个概念：人类工程师会被坏接口、坏抽象、维护成本折磨，于是产生重构冲动；agent 不会痛，它会继续在糟糕结构上追加代码。junior engineer 会从维护痛苦里成长，agent 不会以同样方式沉淀教训。

## 非工程师能参与创造，但集成责任不能被生成物替代
AI 让 PM、设计师、销售、市场团队都能做原型、demo、网站改动，这是积极变化：更多人能把模糊想法变成可讨论的东西。但问题出在 integration。Armin 提到销售 demo 甚至可能生成一个产品实际不存在的功能；这类输出有探索价值，却不能直接进入工程系统。

他们讨论了“prompt request”与 agent-made PR。Armin 不只是想看 prompt，而是想理解“这个东西到底想解决什么问题”；Mario 甚至认为糟糕实现也有价值，因为它展示了最天真的实现路径，能帮维护者更快看清需求边界。关键区别是：生成物可以帮助澄清意图，但不能自动获得 merge 权。

## 开源的新瓶颈是意图过滤，不是项目生命力消失
Pi 和 OpenClaw 都遇到了 agent 生成 issue / PR 的洪水。Mario 的处理方式很粗暴也有效：未知贡献者的 PR 自动关闭，机器人回复要求对方用 human voice 开一个不超过一屏的 issue；如果他认可，再把账号加入 allowlist。这个机制不是为了证明“你是不是人”，而是制造足够的 back pressure，让维护者能处理输入。

两人对开源并没有完全悲观。Mario 认为，真正长期存活的项目仍依赖人类关心、维护社区、建立生态；AI 只会制造更多两天后死亡的项目，以及更多看似有用但缺乏意图的输入。开源的核心资源仍是 human energy，问题是现在有大量 token 伪装成 human energy。

## “无摩擦 shipping”在关键系统里会变成风险
Armin 对“ship without friction”特别警惕。工程组织过去确实追求减少坏 DX，但关键系统里的很多摩擦是故意设计的：高等级服务需要多 reviewer、配置变更需要确认、迁移前要 checklist、服务成熟度要 SLO gate。这些流程不是官僚残留，而是迫使人停下来想：这件事真的值得推进吗？

Mario 的“slow the F down”来自同一逻辑：如果 agent 每天生成 10 倍代码，即使错误率只有人类一半，错误总量仍会上升。Dark factory 式并行 agents 可以产出“某种东西”，但如果人类 review 能力没有同步扩容，复杂度会以更快速度侵蚀系统。

他的自我约束方式是分层：HTML export 这类边缘功能可以不细看，只要输出看起来对；agent loop、extension loading 等核心路径必须亲自重构、亲自进入代码。保持代码质量的方式不是永远手写，而是定期回到结构层理解系统。

## MCP 与 CLI 的分歧，本质是 context 组合方式的分歧
Armin 认为 MCP 当前像“认证 + 调工具 + 把结果塞回 context”，适合某些企业和消费场景，但开发者场景里很容易 context 膨胀、组合困难。Mario 的批评更尖锐：很多 MCP server 只是把整套 OpenAPI spec 映射成海量 tools，模型无法可靠组合多个 server 的输出，只能把中间数据都拖进上下文。

CLI / code execution 的优势在于 composition：模型可以写脚本、grep 20MB 输出、pipe 数据、只把最终结果读回 context。两人都承认 MCP 在 auth、企业合规、非技术用户连接外部服务方面有价值，但更看好“让模型写代码控制工具”的路径。Armin 甚至说，OpenClaw 这类个人 agent 本质上就是藏在用户界面背后的 coding agent。

## 收束行
这集最强的边缘感不是“agent 会不会写代码”，而是：当软件开始修改自己、组织开始依赖不可替代的模型能力、代码库开始大到 agent 自己也读不完时，真正稀缺的会变成清醒的减速能力。
