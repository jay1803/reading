---
title: "Understanding ChatGPT Work"
date: 2026-10-29T14:10:00Z
category: reading
description: "ChatGPT Work 把 ChatGPT 扩展成能联网执行代码、操作浏览器、跨会话存文件并部署应用的任务执行环境，但 OpenAI 的产品说明掩盖了真正决定用途的能力差异。"
source: "https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/"
---

ChatGPT Work 的核心价值，是把 ChatGPT 扩展成能够联网执行代码、操作浏览器、跨会话保存文件并部署应用的任务执行环境，但 OpenAI 的产品命名与文档掩盖了这些真正决定用途的能力差异。Simon Willison 在 2026 年 7 月 9 日产品发布后持续试用，到 8 月底梳理出的首要区别，是同名的 ChatGPT Work 实际包含两种产品：网页和手机应用里的 **Work Cloud**，以及由原 Codex 桌面应用改名而来的 **Work Local**。后者可以直接访问本机文件、运行程序，更像面向非开发者重新包装的 Codex；本文讨论的则是云端版本。两者都要求每月至少 20 美元的订阅，免费用户和每月 8 美元的 Go 用户无法使用。

OpenAI 建议用 Chat 获取答案、解释和短稿，用 Work 完成简报、演示文稿、分析、定期更新或可交付文件，但这套区分无法解释用户早已通过 Chat 完成同类工作的事实。真正有用的判断依据是各自开放了什么功能。Work 可以明确选择 GPT-5.6 Sol、Luna、Terra，并搭配 Light、Medium、High、Extra High、Max、Ultra 六档推理强度，也提供 GPT-5.5 的前四档，选择看起来与 OpenAI API 一致。Chat 则显示 5.6 Instant、Medium、High、Extra High 和 Pro，不说明对应哪个模型家族；每月 20 美元订阅最高到 High，Extra High 和 Pro 要求每月至少 100 美元，且 Pro 在 Work 中没有对应选项。根据 Codex 使用经验，Willison 认为 Ultra 更积极地委派子代理，并推测 Work 消耗 Codex 配额，Chat 使用独立配额；这些仍是他的观察与判断，不能当作官方确认的机制。

Work Cloud 最重要的突破，是代码执行环境可以访问互联网。普通 Chat 的容器代理会阻止访问网站、API 和安装额外软件包；它在 2026 年 1 月曾开放包安装，但 Willison 此次测试发现该能力似乎已经失效。Claude 自 2025 年 9 月推出类似容器以来，允许从 PyPI、NPM 安装包及克隆 GitHub 仓库，但域名白名单很短。Work 支持配置允许访问的域名，默认状态看起来则不限制域名，因此可以把克隆仓库、安装依赖、运行代码与访问外部服务连成完整流程，显著扩大 Code Interpreter 模式的实际用途。

这种联网能力还延伸到了完整的 Chrome 浏览器：Work 能加载网站、填写表单、截图，并对页面 DOM 执行 JavaScript。Willison 要求它提取自己网站的标题，系统便通过 Playwright 查询 h1 至 h6，返回标题级别、整理过空白的文本和元素 ID，相当于把他的 shot-scraper JavaScript 工具搬进了手机可调用的环境。遇到需要登录的网站，浏览器可以请求用户接管，直接输入密码和双重验证代码，无须让凭据经过模型。

文件持久化进一步改变了任务之间的关系。普通 Chat 每次会话都获得独立的新文件系统，其他会话无法访问；Work 每个会话虽有自己的临时工作目录，例如 /workspace/scratch/e00a0a017944，但这些目录会跨会话保留，Willison 当时已积累了 171 个。他观察到，正在运行的 Work 会话似乎共同挂载 /workspace，一个会话的文件修改会立即被另一个看到；进程空间却没有共享，一个会话启动的 localhost 服务无法从另一个会话访问。因此，跨任务复用文件成为可能，但共享文件并不意味着共享运行中的服务。

Work 还可以通过 **ChatGPT Sites** 构建并部署完整网站，底层使用 Cloudflare Workers，支持 HTML、JavaScript、服务端逻辑，以及基于 D1 和 R2 的有状态功能。Willison 的示例任务是查找 London 所有带有"pelican in her piety"图像的地点，把调查结果整理成 JSON，再生成一个介绍这些地点的网站；这种图像属于中世纪基督教意象。生成的网站默认仅创建者可见，也可以公开，团队套餐还支持分享给指定成员。Work 同时支持让多个子代理并行处理复杂项目，普通 Chat 没有这项能力。

定时执行则能把这些工具组合成持续运行的工作流。用户可以要求每天早上 8 点搜索 Waymo 是否宣布在 Half Moon Bay 上线，任务执行后自行判断是否出现值得通知的新信息。Willison 最初把它列为 Work 的独有功能，随后更正：Chat 也支持定时提示词。Work 的额外价值来自定时任务与其他能力的结合，例如每小时自动更新一个 ChatGPT Site，把一次性交付延伸成持续维护。

这些能力也同时满足了 Willison 所说的 **lethal trifecta**：访问私人数据、接触不可信内容，以及向外发送信息。当代理能够读取私密文件、浏览可能包含恶意指令的网页，又能联网传输数据时，prompt injection 就可能把完成任务的权限转化成窃取信息的通道。浏览器登录时避免让凭据经过模型，只解决了其中一个环节，不能回答整个代理环境如何防止此类攻击。Willison 希望 OpenAI 更明确说明防护措施，并猜测 Work 可能沿用了 Codex 的 auto-review 机制，但文中没有确认其实际保护效果。

Work 的能力边界之所以难以辨认，最终涉及两项信息缺口：OpenAI 主要用"适合做什么"介绍产品，缺少对实际工具与权限的明确说明；同时又隐藏了 system prompt 和工具描述，迫使用户靠实验反推模型选择、网络访问、持久化和执行机制。对于能够接触数据并采取行动的产品，工具、权限、状态如何保存以及防护如何生效，本身就构成了产品定义，也应当成为用户判断用途与风险的基础。
