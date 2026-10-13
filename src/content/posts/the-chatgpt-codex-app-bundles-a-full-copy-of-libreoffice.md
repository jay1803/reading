---
title: "The ChatGPT/Codex app bundles a full copy of LibreOffice"
date: 2026-10-14T01:40:00Z
category: reading
description: "Simon Willison 发现 OpenAI 的 Codex/ChatGPT 桌面应用在本地缓存中打包了完整的 LibreOffice、Python、Node.js 等工具环境，共占用 1.7GB。"
source: "https://simonwillison.net/2026/Sep/1/codex-libreoffice/"
author: "timpera"
---

OpenAI 的 Codex 桌面应用内置了一整套本地工具环境，其中包括完整的 LibreOffice，相关缓存共占用 1.7GB。Simon Willison 使用 OmniDiskSweeper 清理 ~/.cache/ 时发现，这款后来改名为 ChatGPT 桌面应用的软件，将工具环境存放在 codex-primary-runtime 文件夹中：除了 LibreOffice，还包含完整的 Python、Node.js 安装，以及 PDF 处理库 Poppler 和 git 的原生二进制文件。LibreOffice 是 2010 年从 OpenOffice.org 分支而来的开源办公套件。

这些工具还配有指导 Codex 调用它们的 **skills**。具体目录 `~/.cache/codex-runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/documents` 中的技能文件，说明了如何定位和使用相应二进制程序。这套应用随附的运行环境，把执行工具与使用说明一起交付，为 Codex 在本地处理文档提供了现成的基础。
