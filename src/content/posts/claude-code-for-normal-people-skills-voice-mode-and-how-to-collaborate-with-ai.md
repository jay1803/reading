---
title: "Claude Code for normal people: skills, voice mode, and how to collaborate with AI"
date: 2026-08-16T14:58:00Z
category: reading
description: "AI 采用的真正障碍不是技术，是习惯缺口。Grace Clarke 把整个咨询业务搬进每小时自动运行的 Claude pipeline，核心论点是协作替代提示工程。"
source: "https://www.lennysnewsletter.com/p/claude-code-for-normal-people-skills"
---

## AI 采用的真正障碍是习惯缺失，不是技术门槛

Grace Clarke 是 AI 培训师兼前营销顾问。她今年年初自学 Claude Code，把整个咨询业务的后台搬进了 AI pipeline，现在用这套流程给学员和企业团队上课。

这期节目的核心论点只有一个：大多数人之所以没在用 AI，不是因为不会写 prompt，而是因为从未建立"默认打开 Claude"的肌肉记忆。技术门槛几乎已经不存在，拦住人的是习惯缺口。

## "Intent engineering"，不是"prompt engineering"

Grace 提出的概念区分直接：提示工程（prompt engineering）已死，需要的是意图工程（intent engineering）——把目标和问题说清楚，让 Claude 来设计方案，而不是你自己先把 prompt 打磨成完美指令。

她的例子：想做一个密码保护的互动提案文档。不是她设计了这个功能，是她在走路时对着手机说了两三分钟"我的问题是这个"，Claude 回来说"我觉得应该是一个密码保护的交互式 artifact，你觉得呢？"然后来回谈了十分钟，花了一小时生成。她的洞见是：**Claude 应该负责把 prompt 从你这里提炼出来，不是你负责先写出完美 prompt**。

## Pipeline operator：每小时跑一次的咨询业务后台

她最重要的工具是一个每小时自动运行一次的 pipeline operator。功能：摄取所有来信、对照客户状态上下文做关联判断、自动推进客户在流程中的位置、必要时生成 HTML 提案或问卷。

提案本身是密码保护的 HTML 文件，部署在 Netlify，包含从过往对话中提取的上下文、客户进度追踪、预工作清单。客户第一次打开就已经在操作一个 AI 生成的定制化界面——同时这也是在向客户演示"我教你做到的就是这个"。

这个 pipeline 把她每周 20 小时的行政工作压缩成了自动化。

## Voice guide：不只是"听起来像我"，而是"像我一样思考"

她区分了两种声音文件：一种只管措辞和风格，一种管决策逻辑和思维方式。她的 voice guide 属于后者——记录了她的沟通哲学、她会用和绝对不用的词，以及她如何做判断。

维护方式很实际：发现 LinkedIn 上有什么让她齿冷的 AI 腔，就给 Claude 发一条语音备注"把这种风格永远从我的 voice guide 里排除"。

额外一层：她给提案配了一个"董事会"——Cat（Anthropic Applied AI 负责人）、Ben Thompson（Stratechery）、Jamie Dimon（做 CBA 分析）、一个怀疑者、一个投资人。运行提案时让这几个角色提意见。

## Claude Code 起草，Cowork 收尾，靠 markdown session 文件过渡

她的工作流分工：Claude Code 处理模糊的、技术性的起步阶段（"如果 Cowork 说做不到，Code 会说'官方 connector 不行，但我可以开个浏览器窗口试试'"）；一旦思路清晰，让 Code 写一个 markdown session file 保存到本地，然后拖进 Cowork 继续。

这个洞见不显然：Claude Code 和 Cowork 之间可以通过一个普通 markdown 文件传递整个会话上下文。两个工具不是隔离的，context 可以随文件流动。

## 自建 Gmail 替代品：留在 Gmail 里，所有学习都白费

她一个月没有主动打开过 Gmail。替代方案是在 Claude Cowork 里做的一个 artifact，通过 Google 服务账户和自定义插件接入 Gmail。

她的论点比"我讨厌 Gmail"更深一层：**如果你继续在 Gmail 里回邮件，所有的写作积累和沟通风格都被锁在那里，不会进入你的 AI 上下文，不会复利。** 把通信搬进 Claude，才能让 AI 真正从你的沟通方式里学习。

## 推动别人采用 AI 的两步法

她给学员和企业培训时的核心方法只有两个步骤：

1. 在手机设置一个提醒，提醒触发时截图当前屏幕，把整个窗口发给 Claude，问"你能帮我处理这个吗？"目的是建立"默认先问 Claude"的条件反射，而不是教会正确的 prompt 格式。
2. 和学员一起现场做一个 voice guide。不是看演示，是亲手做，让人感受到"这就是我能 invoke 的东西"的所有权感。

她发现反直觉的一点是：**给学员提前准备好的"超级 prompt"是错的**，因为这绕过了学习协作的过程，不能真正建立习惯。人需要自己经历一次"我说了问题，Claude 给了我方案"的来回，才会真正开始信任这个协作模式。
