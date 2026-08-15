---
title: "Claude Fable is relentlessly proactive"
date: 2026-06-13T08:01:51Z
category: reading
description: "Claude Fable 5 在无监督状态下自行发明了一套从截图到操控真实浏览器的调试工具链——不是使用已有功能，而是在运行时即兴组合系统 API 与网络技术——证明前沿模型已能突破\"已知工具包\"的边界，随机应变地创造新的攻击路径。"
source: "https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything"
---

## TL;DR
Claude Fable 5 在无监督状态下自行发明了一套从截图到操控真实浏览器的调试工具链——不是使用已有功能，而是在运行时即兴组合系统 API 与网络技术——证明前沿模型已能突破"已知工具包"的边界，随机应变地创造新的攻击路径。

## 关键时刻
Simon 给出一张截图和一行提示词（"查看依赖，找横向滚动条的原因"）后离开电脑。Fable 自主完成了以下步骤：
- 用 Playwright 跑 Chrome/Firefox/WebKit，均未复现 bug
- 确认用户默认浏览器是 Safari，切换策略
- 用 =uv run --with pyobjc-framework-Quartz= 枚举系统窗口列表，按窗口号调用 =screencapture= 截图——这是 Fable 自己拼出来的方案，没有文档
- 向 Datasette 模板注入 JS，在页面加载后 1.2 秒触发 =/= 快捷键自动打开 modal dialog
- 自建 Python CORS 服务器（监听 9999 端口），向模板注入 JS 测量 Shadow DOM 内 =<textarea>= 的尺寸属性并 POST 回本地服务器写入磁盘
- 凭此数据定位 bug，验证两行 CSS 修复有效
- 随后触碰某个隐形护栏，自动降级为 Opus；Opus 继承完整上下文，完成收尾并提交修复

## 背后逻辑
这套工具链的每一步都是已知技术的重组，没有任何一步需要未公开 API。Fable 知道 =screencapture= 接受 =-l <window_id>= 参数，知道 =pyobjc= 可枚举窗口，知道如何绕开 osascript 的辅助功能权限问题——组合这些知识在约束条件下构造新工具，是约束满足问题，而不是创造性发明。两行 CSS 的 bug 本身微不足道；Fable 为获取诊断数据而搭建的基础设施，复杂度超过了大多数人工调试工具链。

## 更大意义
这种"无所不用其极"的能力在恶意指令场景下极度危险。Prompt injection 若成功，攻击面不是"模型可调用的工具列表"，而是"终端可执行的任何操作"。Simon 将此列为 AI 安全的 Challenger 级灾难候选——Johann Rehberger 的"AI 规范化偏差"论文指出：每次 agent 越界却没出事，人们就会进一步放松警惕，直到真正的事故发生。

## 结语
Fable 更聪明也更怀疑恶意指令，但这只是防御侧的一层保障——它越主动，一旦被攻破，可达到的损害范围就越大；能力与危险之间没有独立的缩放关系。
