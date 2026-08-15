---
title: "“I haven’t written a single line of front-end code in 3 months”: How Notion’s design team uses Claude Code to prototype"
date: 2026-03-03T23:53:57Z
category: reading
description: "Brian Lovin，Notion AI 的 product designer，长期热衷代码原型，也是个人项目 brianlovin.com 的作者。主持人 Claire Velo 是产品负责人，节目为 How I AI。"
source: "https://www.lennysnewsletter.com/p/i-havent-written-a-single-line-of"
---

## 嘉宾背景
Brian Lovin，Notion AI 的 product designer，长期热衷代码原型，也是个人项目 brianlovin.com 的作者。主持人 Claire Velo 是产品负责人，节目为 How I AI。

## TL;DR
设计师只要把"AI 叫你干的事情教会 AI 自己干"作为第一原则，就能让 Claude Code 无限期自治运行——这一原则与 Notion 内部的 prototype playground 一起，正把设计团队从 Figma 静态稿推向可连接真实模型的浏览器级代码原型。

## Prototype Playground：一个 repo，所有人的原型在同一个地方
Notion 设计团队共用一个 Next.js 项目（Vercel 部署），每位设计师有自己的命名空间目录，原型即目录。优势双重：可见性（直接看到队友在做什么）、复用性（直接从别人原型里 yoink 代码，通常就是让 Claude 搬运）。之前各自建仓库的结果是：重复造 Notion 风格组件，还找不到彼此的东西。

## Plan Mode + 真的读计划，才是用 Claude Code 的正确姿势
Brian 固定工作流：先进 plan mode，用语音工具 Monologue 口述需求，然后真的读计划——这步需要一点编程背景，但即使没有，有结构化计划也好过直接生成代码。Repo 里放了全局 CLAUDE.md（工具链、目录结构说明）和 per-machine 的 CLAUDE.local.md（不提交 git，存个人用户名、"不要碰别人的文件"等指令），给 Claude 提供充分上下文。

## "AI 叫你做的事，教它自己做"——让 agent 持续运行的核心原则
每当 Claude 要求人类检查某件事（看浏览器、确认 CI），Brian 的反应不是去做，而是把这个动作教给 Claude：用 Playwright MCP 或 Chrome DevTools MCP 让它自己开浏览器、点按钮、对比截图。Podcast player 那个 demo 里，Claude 自己跑 eslint、自己用 Chrome 打开页面、自己验证 confetti 触发——Brian 全程没动鼠标。

## Slash Commands + Skills：把流程编码成可复用指令
项目里几条核心 slash command：
- /create-prototype：自动建目录和元数据文件，附代码样本给 Claude 参考，避免生成空文件。
- /figma：先验证 Figma MCP 是否安装（没装输出安装教程），再提取设计、生成代码，最后进验证循环——Claude 自己用 Chrome DevTools MCP 比对实现与 Figma 截图，循环到两次迭代无变化为止。从粘贴 Figma 链接到"80% 完成"约 27 秒。
- /deploy：检查 GitHub CLI 登录 → 自动建分支 → commit → 开 PR → 在浏览器打开 PR → 每 60 秒轮询 CI，失败则自动修复再推送，直到全绿。
Claude Skills 是 Claude 自动识别触发时机的能力：find-icon skill 附带 TypeScript 脚本，让 Claude 主动搜索 5000 个图标文件并匹配同义词，解决它反复猜错 Notion 自定义图标名称的问题。

## 为什么 AI 产品必须用代码原型
Brian 最初在 Figma 里画"用户发消息 → AI 完美回复"的黄金路径，工程师实现后全不对：AI 卡住、追问澄清、产生错误状态。Figma 能画聊天气泡，但无法设计"模型思考 2 分钟时用户看到什么"，也无法测试"连接 Notion MCP 后 AI 还不会建数据库"这类边界。结论：越是 AI 功能，越必须在真实模型上原型——不为像素完美，而是为了了解模型在哪里断、在哪里好。

## 留下的那个想法
Brian 说自己仍有 60-70% 的时间在 Figma。真正推动他转向代码原型的不是"AI 很强"，而是"模型行为不可预测"——静态稿永远无法捕捉一个会说错话、会超时、会反问的 AI。Prototype playground 本质上是认识工具，不只是提速工具。
