---
title: "How will AI change operating systems? Part 2: Windows"
date: 2026-10-12T10:12:01Z
category: reading
description: "Microsoft 把 agent 身份、工具发现、安全隔离和本地模型运行变成 Windows 的基础能力，试图赢回流向 macOS 和 Linux 的开发者。"
source: "https://newsletter.pragmaticengineer.com/p/windows-and-ai"
author: "Gergely Orosz"
---

Microsoft 希望通过把 agent 的身份、工具发现、安全隔离和本地模型运行变成操作系统基础能力，让 Windows 重新成为开发者愿意选择的平台。这项战略同时面对两种信任问题：此前的 AI 产品引发了"Microslop"的嘲讽，而 Windows 长期积累的产品体验问题也削弱了开发者好感。Statcounter 显示，Windows 在普通桌面用户中仍有约 63% 的份额，但开发者市场的优势正在收窄。2025 年 Stack Overflow 调查中，它仍是专业开发者使用最多的单一系统，却已无法覆盖多数开发者；JetBrains 调查则发现，约一半开发者会使用多个系统，macOS 已接近成为开发工作中使用最多的独立系统。Gergely Orosz 与 Ivan 在 2026 年 9 月发起的社交媒体调查获得 9,937 份回复，Windows 排在 macOS 和 Linux 之后，不过样本偏向 The Pragmatic Engineer 读者、风投支持的创业公司及大型科技企业，且单选题没有区分 WSL，不能直接当作整体市场份额。Microsoft 要争取的，正是这批因 M-series 硬件表现和开发体验转向其他平台的人。

Windows 对 agent 的第一项基础设计，是让它拥有可识别、可观察的独立身份。长期运行的 agent 会打开多个程序、使用剪贴板和 UI、消耗系统资源，其行为越来越接近一个用户。通过 Entra ID 注册本地身份后，agent 可以像另一个用户一样出现在 Task Manager 中；Microsoft 展示的例子将人类用户 kirupach 与 agent 用户 V9-G4 分开列出，使原有的用户级观测能力也能用于 agent。但身份登记依赖应用主动配合，恶意程序仍可冒充普通用户、绕过注册，因此 Defender 正在增加"agent aware"能力，通过 AI Assets 等功能扫描已知的本地 agent 活动，补上自报身份留下的缺口。

身份解决"谁在操作"，**On Device Agent Registry（ODR）**则解决"它能找到哪些工具"。这个仍处于开发和测试阶段的系统组件集中注册、发现并运行本地 MCP servers，并提供 File Explorer、System Settings 等核心功能的连接器。例如，一个照片整理 agent 可以先用图像分类器识别照片主题，再通过 ODR 找到 File Explorer MCP，把照片移动到 parties、outdoors、baby photos 等目录。Origin Technology 的逆向研究还发现，ODR 返回给客户端的进程 ID 指向 ODR 自身，客户端实际通过它与 MCP server 通信。这意味着 ODR 可能同时充当代理，在工具调用的必经路径上检查请求和响应、识别危险行为；这一代理机制尚未得到 Microsoft 确认，具体安全用途也未公布。

工具发现之后，真正的风险来自执行权限：文件操作、网页访问、shell 命令以及 agent 临时生成的程序，都可能让自动化获得代码执行能力。Microsoft 正在开发的 **Microsoft Execution Containers（MXC）**为这些操作提供统一的隔离接口，开发者通过 JSON containment policy 描述网络、文件系统、UI 和执行限制，再生成配置并调用 spawnSandboxFromConfig() 启动受约束的工作负载。MXC 自身不实现底层隔离，而是调用已有机制；例如在 macOS 上可以使用 Seatbelt。它已能运行于 Windows、Linux 和 macOS，使开发者有机会用同一套策略接口约束跨平台 agent 工具。

隔离强度需要按操作风险选择，因为启动速度、资源成本与潜在破坏范围存在直接冲突。Windows 支持的选项包括进程隔离、会话隔离、WSL containers、轻量级 Hyper-V containers 和完整虚拟机；新建进程启动快，但若仍处于当前用户会话，就可能暴露用户资源，隔离更强的环境则需要更高成本。文中介绍的原生 Windows 版 OpenClaw 是首批采用 MXC 的 agent 之一，用户可以在类似标准 Windows 设置的界面中配置限制。由于隔离由底层执行，agent 本身未必知道所有约束，仍可能尝试访问沙箱禁止的已安装程序或其他资源。结合独立 agent 身份，Microsoft 计划通过 Intune 让企业管理员集中管理整个设备群的 MXC 策略；Windows 团队已提供内部自动化开发杂务的应用案例，但 MXC 尚未广泛采用。

本地推理的基础设施则由 **Windows ML**承担，其目标是在 AI 领域提供类似 DirectX 对图形硬件的抽象，让应用不必分别处理各家芯片。Microsoft 在 2019 年推出的 DirectML 建立在 DirectX 12 之上，只覆盖 GPU，开发者还需要从较低层的数学操作构建推理管线、处理内存布局。Windows ML 转向 ONNX 和 ONNX Runtime：主流机器学习框架构建的模型可以转换为 ONNX graph，再通过统一接口运行于不同厂商的 GPU、NPU 和 CPU。它同时改变了优化的分发方式。DirectML 的运行时优化依赖驱动更新，一项更新获得有意义的普及可能需要六个月；Windows ML 则按用户硬件下载和加载厂商提供的 Execution Providers（EPs），例如为 NVIDIA GeForce RTX 使用 TensorRT RTX EP。这些组件经过 Microsoft 认证和测试后分发，让硬件优化不必等待完整驱动更新。

统一运行时仍不足以让简单 AI 功能成为低成本的应用能力，因为开发者还得解决模型的分发和部署。Microsoft 因此押注操作系统和浏览器内置 Small Language Models（SLMs），并计划让未来的内置模型不强制要求 NPU。Edge 中的 Aion-1.0-Instruct 已展示了这种使用方式：网页通过 Prompt API 用少量 JavaScript 调用本地模型完成情感分析，无须把文本发送到云端，也无须持续支付 token 费用。内置模型降低了应用的运行成本和网络延迟，并免去每个应用自行携带模型的负担；文中展示的是 JavaScript 接口，面向原生应用和其他语言的版本仍属于后续预期。

本地模型也为企业提供了更可控的模型供应与工作负载分配方式。云端费用上升、模型能否持续获得以及合规要求，正在推动团队运行自己的模型；简单请求交给本地或较便宜的模型，复杂推理再交给云端 frontier models，可以把成本与任务难度对应起来。Scott Hanselman 展示的一台预发布 Surface 笔记本搭载 NVIDIA GPU，本地运行 Qwen 并连接 GitHub Copilot，生成速度约为每秒 40 tokens。这一演示说明，随着相应硬件普及，本地编码辅助有望覆盖更实际的工作场景，但它仍是特定预发布设备上的表现。

这些投入共同指向一个平台层面的转变：Windows 正试图把 agent 从各应用自行拼装的自动化程序，变成具有身份、可发现工具、受策略约束、能调用共享本地模型的系统工作负载。Microsoft 还在投资 agent 构建框架和工具链，希望开发者可以依赖平台已有的组件来构建应用。能否赢回开发者，取决于这些仍在开发或预览中的能力能否兑现为可用的接口、可靠的隔离和更低的运行成本，以及 Microsoft 能否同时修复让开发者离开的日常体验问题。
