---
title: "Markdown is holding you back"
date: 2025-11-30T20:19:43Z
category: reading
description: "作者的核心判断是：Markdown 很适合写短文档和 README，但不适合充当严肃技术文档体系的“源格式”。问题不在于它难用，而在于它几乎不给内容结构提供可验证、可复用、可迁移的语义信息；一旦文档要被搜索、被 AI/IDE 消费、被多渠道发布、被跨系统复用，Markdown 就会从低门槛工具变成结构债务。作者主..."
source: "https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/"
---

## TL;DR
作者的核心判断是：Markdown 很适合写短文档和 README，但不适合充当严肃技术文档体系的“源格式”。问题不在于它难用，而在于它几乎不给内容结构提供可验证、可复用、可迁移的语义信息；一旦文档要被搜索、被 AI/IDE 消费、被多渠道发布、被跨系统复用，Markdown 就会从低门槛工具变成结构债务。作者主张按文档复杂度升级源格式：中等复杂度用 reStructuredText 或 AsciiDoc，大规模可复用出版体系用 DocBook 或 DITA，再向下导出 Markdown。

## 关键洞察
作者先把问题从“写起来顺不顺手”转成“内容最终要被谁消费”。技术文档早已不只是给人眼看的页面：搜索引擎要索引，LLM 和 agent 要解析，IDE 集成也要调用。真正被这些系统消费的，是最终发布出来的结构化 HTML；而 Markdown 只能表达很小一部分语义，机器看到的往往只是标题、列表、段落，分不清某一段究竟是步骤、注释、概念定义还是普通说明。

这就是作者把 Markdown 类比成“隐式类型”的原因。它让人写得很快，却没有 schema、没有约束、也没有一致性保证。一个文件里的二级标题可能表示概念，另一个文件里却表示操作步骤，机器无从判断。再加上 CommonMark、GFM、MyST、MultiMarkdown 等方言并存，所谓“写 Markdown”本身就不稳定：脚注、换行、代码块等特性在不同系统里可能表现不同。结果是 Markdown 更像最低公分母交换格式，而不是可靠的源数据模型。

MDX 在作者这里是一个很关键的证据。人们明明选择了 Markdown，却又不断往里塞 React 组件、定制标签和插件，例如用 <Command> 统一命令展示。这说明需求从来都不只是“排版”，而是“表达语义”。问题在于，这种语义层是私有的、脆弱的、不可移植的：离开原有发布系统就会失效，迁移到别的平台时还得重新实现一遍。也就是说，团队表面上在坚持 Markdown，实际上已经在偷偷重建一套更复杂但更差的标记系统。

作者接着解释为什么“语义标记”有实际价值。第一是转换与复用。若源文档明确标出 step、note、xref、command 之类的结构，就能稳定地转换成 HTML、PDF、ePub，甚至再降级导出成 Markdown；如果源头只有普通列表和段落，后续转换只能靠猜，信息在一开始就丢了。第二是机器消费。对 LLM、agent、索引系统而言，明确标记的 step 就是 step，普通 bullet 则可能是步骤、提示、枚举项中的任何一种；这类歧义会直接降低机器可用性。

后半篇不是空谈原则，而是给出一条按复杂度递增的格式谱系。reStructuredText 仍是纯文本，但已经有 directive、admonition、cross-reference 等结构能力，适合需要更多语义但又不想离开文本写作体验的团队。AsciiDoc 在此基础上更强调属性、条件内容、include、原生 front matter、UI 元素和键盘快捷键等技术写作能力，能更好支撑参数化内容和多格式输出。DocBook 则进入 XML 层级，用丰富标签把 command、note、xref、product term、index term 等都显式建模，适合工业级转换和验证。DITA 再往前一步，把内容组织成 task、step 等主题化单元，并内建复用、特化、过滤与多版本发布能力，因此特别适合企业级、多渠道、标准化内容体系。

作者也承认 XML 冗长、工具链没 Markdown 普及、迁移成本高、团队可能排斥学习曲线，所以并没有把 Markdown 全盘否定。真正的分界线是文档系统的复杂度：短命文档、快速 README 用 Markdown 完全合理；需要一定结构的网站更适合 reStructuredText 或 AsciiDoc；需要复用、联发、严格治理的大型文档库才值得上 DocBook 或 DITA。最终原则很清楚：源格式应尽量富语义，再按需要向下导出；如果反过来把 Markdown 当 source of truth，后面缺失的上下文几乎补不回来。

## 一句话总结
Markdown 适合当输出层和轻量协作层，但一旦文档需要被机器理解、跨渠道复用和长期治理，就该把它降级为导出格式，而不是继续拿它充当源模型。
