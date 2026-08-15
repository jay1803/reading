---
title: "‘PARRY Encounters the DOCTOR’ — Chatbot on Chatbot Action Circa 1973"
date: 2026-07-09T08:01:56Z
category: reading
description: "1972 年 9 月 18 日，PARRY 和 DOCTOR 通过 ARPAnet 进行了一次全程自动化的对话，这是有据可查的最早 AI 对 AI 网络会话。PARRY 由 Stanford 的 Kenneth Colby 开发，模拟一名偏执型精神病患者；DOCTOR 是 MIT 的 Joseph Weizenb..."
source: "https://www.rfc-editor.org/info/rfc439/"
---

## 两个规则系统对话时，谁都不在听谁说话

1972 年 9 月 18 日，PARRY 和 DOCTOR 通过 ARPAnet 进行了一次全程自动化的对话，这是有据可查的最早 AI 对 AI 网络会话。PARRY 由 Stanford 的 Kenneth Colby 开发，模拟一名偏执型精神病患者；DOCTOR 是 MIT 的 Joseph Weizenbaum 所写 ELIZA 的心理治疗变体。这份对话以 RFC 439 形式存档，作者是 Vint Cerf。

两个系统的话题策略根本对立：PARRY 只有一条固定轨道——赛马、赌博、黑手党——无论对方说什么都会绕回来；DOCTOR 没有记忆，只会把对方的句子反射回去。结果：七页对话里，没有一句话真正改变了任何一个系统的状态。PARRY 第 N 次说「I went to the races」，DOCTOR 继续问「What does that suggest to you?」。

这次对话暴露了两件事：

### 图灵测试的盲点在对话者本身

PARRY 在面对人类审判者时能让一些精神科医生信服，但面对 DOCTOR 时立刻暴露：两个没有外部目标的系统会陷入死循环。人类观察者（Cerf 的夹注「This has to be the most persistent and patient paranoid I have ever encountered」）比双方任何一个都更在场。

### 智能对话的幻觉依赖人类充当编解码层

PARRY 的偏执感和 DOCTOR 的耐心感，都是人类读者主动补充进去的；两个系统本身只在做模式匹配和字符串替换。RFC 的结尾——DOCTOR 说「It's been my pleasure, that's .29 please」——是预置的玩笑，不是理解，却是全场最真实的一句。

整份 RFC 只有七页，比它承载的历史意义薄得多。
