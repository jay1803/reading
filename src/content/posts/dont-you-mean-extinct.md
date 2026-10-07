---
title: "Don't you mean extinct?"
date: 2026-10-07T02:01:39Z
category: reading
description: "LLMs 正在削弱逐行写代码的稀缺性，但程序员仍能通过掌握新工具、保留解决问题与判断代码质量的能力，在技术更替中继续创造价值。"
source: "https://fabiensanglard.net/extinct/index.html"
---

LLMs 正在削弱逐行写代码的稀缺性，但程序员仍能通过掌握新工具、保留解决问题与判断代码质量的能力，在技术更替中继续创造价值。Fabien Sanglard 用 Phil Tippett 的经历说明这种转型：1993 年拍摄 Jurassic Park 时，Steven Spielberg 原本请这位定格动画大师用 go-motion 技术制作全身恐龙，对 CGI 能否呈现真实恐龙十分怀疑。直到 Dennis Muren 与 Industrial Light & Magic（ILM）的数字艺术家展示了一段概念验证：一只纹理完整、照片般逼真的 T. rex 在日光下追逐 Gallimimus 群。Spielberg 当即决定采用 CGI，已经选好三十人团队、准备投入制作的 Tippett 说自己感觉"灭绝了"，此前积累的整套技艺似乎突然失去了用途。

今天程序员对被淘汰的焦虑，与这种冲击相通。Sanglard 把 LLMs 放进历次技术转型的脉络：1990 年代的互联网、2000 年代初的 Computer Graphics、2010 年代初的 Mobile First，都要求从业者重新学习。适应当前变化需要同时理解模型原理与学习用模型开发；他推荐 Andrej Karpathy 合计约 25 小时的视频，以及 Sebastian Raschka 的 Build a Large Language Model (From Scratch)。他判断，拒绝使用 LLM agents 的开发者会因产出能力落后而失去竞争力。John Carmack 的观点进一步明确了应当保留的能力：**解决问题才是核心技能**，传统编程要求的纪律与精确性仍有迁移价值，但亲手写代码的门槛正在下降；过度依恋某种实现方式，也会像热爱 assembly language 而拒绝转向 C 一样阻碍适应。

产出速度提高并不自动带来可维护的软件。Sanglard 认为，完全放任 LLM 的"full-vibe-code"可以让自己生成过去千倍的代码，却留下难以理解的混乱；原型或小型个人项目可以接受这种代价，其他项目仍然高度依赖代码质量。模型即使声称理解整个项目，也会提出严重错误的方案、产生幻觉，因此开发者必须能读懂代码、理解架构。他主动降低生成速度，反复修改 PR，直到达到自己手写时的质量，并把每次发现的问题补充到 `~/.gemini/GEMINI.md` 或 `~/.claude/CLAUDE.md`，让 agent 逐渐遵循自己的标准。

这些标准落在具体的工程选择上：用常量或适当的 enum 消除 magic numbers 与 magic strings；通过 early return、continue 减少嵌套，避免 Arrow Anti-Pattern；函数参数用 enum 表达含义，避免含混的 boolean；遵守分层，不跨层打洞；逻辑块之间留空行，并用简短注释解释做什么、为什么做。不过，同时驱动多个项目或独立功能的 agents，也会增加 **context switching** 的负担。Sanglard 已亲身感到精神疲劳加重，其他开发者也报告了 mental burnout；并行产出的收益需要与维持多个任务上下文的认知成本一起衡量。

代码编写成本下降，也应提高 code review 的要求。Sanglard 认为，糟糕的 commit message 已经很难找到借口：Chris Beams 的七条规则涵盖标题长度、imperative mood、标题与正文分隔等要求，花一分钟让 LLM 总结并加入 agent 指令即可落实。同样，开发者应投入更多精力设计清晰、简洁的方案；混乱的 PR 应重写，过大的 PR 应拆成便于审查的小块，因为这些工作过去的繁琐程度已经降低。他自己会先让 LLM 批评代码、寻找错误，再交给人工 reviewer，避免把明显问题转嫁给对方。

测试与依赖管理也可以采取更严格的标准。大型重构越来越常见，而编写测试的成本下降，使要求每个 PR 配备 unit tests 或 CI tests 更有理由；测试能够捕捉人工与 LLM 审查共同漏掉的破坏。对于简单功能，拒绝引入依赖也更容易实行，Sanglard 当天就让 LLM 编写了 Levenshtein distance 函数，避免为此给项目增加一个 dependency。这些变化把生成代码节省的时间转向审查、验证与控制长期维护成本。

更高的个人生产力还扩大了小团队和个人项目的可行范围。Sanglard 认为，软件开发可能重新接近 1990 年代四人团队就能制作专业软件的模式。他已重启过去因过于耗时或复杂而搁置的项目，上个月完成了 Silpheed 视频格式的 reverse engineering，并继续推进 Dreamcast 上的 Ikaruga 与 SNES 上的 Zelda: A Link to the Past。LLMs 同时也是学习自身技术生态的工具：他借助模型理解 llama-cpp、OpenCode、ollama、vLLM 的代码与架构，关注 Tenstorrent、Etched、MatX、d-Matrix、Cerebras Systems 等硬件方案，还用模型弥补数学符号理解上的困难、辅助阅读研究论文，但会复核模型给出的解释。

是否继续投入学习，最终仍取决于个人的信念与动力；有人选择离开原有领域并取得成功，继续适应并非唯一的人生选择。Tippett 的后续经历则展示了留下来转型的可能性：当时 41 岁的他被 Spielberg 留任为 Dinosaur Supervisor。ILM 的计算机动画师擅长编程与数字技术，却缺少传统表演动画经验，不知道怎样让恐龙动作体现重量、节奏与生物意图。Tippett 与 ILM 共同开发 Dinosaur Input Device（DID），一种带传感器、关节高度可动的实体骨架；他的团队沿用定格动画的操作经验摆动骨架，再由计算机把动作转换到数字空间。

1994 年，Tippett 与 Dennis Muren、Stan Winston、Michael Lantieri 共同获得 Jurassic Park 的 Academy Award for Best Visual Effects；Tippett Studio 此后继续参与 StarShip Troopers、Dragonheart 等七十多个片名的制作。他赖以工作的媒介发生了变化，对生物运动的理解却成了新制作流程需要补上的关键能力。技术更替会压低旧操作方式的价值，也会让能够跨越工具变化的专业判断获得新的用途。
