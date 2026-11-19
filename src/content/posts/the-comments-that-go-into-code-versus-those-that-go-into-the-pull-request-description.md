---
title: "The comments that go into code versus those that go into the pull request description"
date: 2026-11-19T20:28:15Z
category: reading
description: "PR 描述解释一项改动为什么值得被接受，代码注释保存未来理解和使用代码仍然需要的信息，两者的分界在于信息的有效期与读者所处的上下文。"
source: "https://devblogs.microsoft.com/oldnewthing/20260812-00/?p=112607"
---

PR 描述解释一项改动为什么值得被接受，代码注释保存未来理解和使用代码仍然需要的信息，两者的分界在于信息的有效期与读者所处的上下文。

PR 标题应当明确指出修复的问题或新增的功能，并在大型代码库中标明涉及的组件。例如，“Add support for polarity reversal”应具体到“Add support for widget polarity reversal”；“Fix crash when polarity changes”则可以写成“Fix widget crash when polarity changes twice in a short time”。这些限定能帮助排查 regression 的人筛选近期改动：如果发生 crash 的 doodad 使用 widget，新增 polarity reversal 支持就值得调查，因为 doodad 可能无法处理反向极性的 widget；修复 widget 极性变化时 crash 的改动，嫌疑相对较低。如果 doodad 根本不用 widget，两项改动都可以跳过。省略组件名称，则会迫使同样具有 polarity 概念的 gadget 团队打开 PR，读完才发现与自己无关。

标题帮助定位改动，PR 描述则承担接受改动所需的论证：问题从何而来、实现如何解决问题、做过哪些验证、考虑过哪些替代设计，以及为何因风险过高等原因放弃它们。修复前后的截图、unit tests 和 checkin template 要求的手续也属于这里。越接近发布，审批要求通常越严格；在产品周期后期，还可能需要证明 release management team 已认定该 bug 达到允许修复的 **bug bar**。这些内容共同回答的是特定时间点上的审查问题：为什么现在需要改，以及为什么这份实现可以获批。

代码注释应保存更持久的使用约束与知识，例如函数的正确调用方式、调用前提，以及所接受的 JSON schema 的文档链接。相应地，“我检查了这个函数的所有调用，只有这里传错了 flag”应放进 PR 描述：它回答了 reviewer 对其他调用点是否也有同类错误的疑问，但检查范围只覆盖提交时的代码。后续新增的调用仍可能传错 flag，把这句话留在代码里，就会让一次历史检查看起来像持续成立的保证。

功能的需求背景也需要区分当前动机和历史事实。“Doodad component 将使用 polarity reversal”解释了为什么今天要实现这个功能，适合放在 PR 描述中。若留作代码注释，将来时会让后来的读者以为 Doodad 仍未开始使用它；Doodad 日后停止依赖该功能，也未必会有人更新另一个组件里的注释。更危险的是，这句话会暗示只要 Doodad 不再需要，就能删除功能，忽略其他组件可能已经成为使用者。若希望保留功能的起源，可以在代码里写成“polarity reversal 最初是为 Doodad component 添加的”：这一表述记录历史，不承诺当前依赖关系，也不构成删除依据。

持久性之外，代码注释还必须在脱离 PR 描述后独立成立。用新函数替代旧函数时，在新函数上写“等所有客户端迁移到新函数后，保留此函数”，会让没读过原 PR 的人困惑：迁移完成后究竟需要做什么？可执行的信息应写在旧函数上：“等所有客户端迁移到新函数后，删除此函数。”PR 保存当时做出决策的理由，代码注释则应让未来的维护者无需记住那次审查，也能正确理解约束并采取行动。
