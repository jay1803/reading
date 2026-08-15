---
title: "How I learned Vulkan and wrote a small game engine with it (2024)"
date: 2025-11-30T20:19:43Z
category: reading
description: "Vulkan 没有想象中可怕——一个自学图形程序员 3 个月从零写出 19k LoC 的游戏引擎，而且他的结论是：一旦掌握几个关键技巧，Vulkan 比 OpenGL 需要更少的抽象层，因为它本身已经无状态、明确。"
source: "https://edw.is/learning-vulkan/"
---

## TL;DR

Vulkan 没有想象中可怕——一个自学图形程序员 3 个月从零写出 19k LoC 的游戏引擎，而且他的结论是：一旦掌握几个关键技巧，Vulkan 比 OpenGL 需要**更少**的抽象层，因为它本身已经无状态、明确。

## 核心洞见

"繁琐"是可以几乎消除的，靠三个具体决策：

- **PVP + BDA**（Programmable Vertex Pulling + Buffer Device Address）：顶点格式不再需要 VAO 或 VkVertexInputAttributeDescription，顶点地址直接塞进 push constant，shader 里用 gl_VertexIndex 读取。
- **Bindless descriptor**：全部纹理进一个全局 descriptor set，其余数据全走 push constant。整个引擎里只有一个 descriptor set，消灭了 vkCmdBindDescriptorSets 的绝大部分调用。
- **VK_KHR_dynamic_rendering**：扔掉 render pass 和 subpass，draw 函数只关心"画什么"，不关心"画到哪"，调用方负责 begin/end rendering。

结果是：一个 pipeline class 只有 init / draw / cleanup 三个函数，PostFXPipeline.cpp 约 60 行。

## 具体机制

- **工具链**：vk-bootstrap（初始化样板）+ VMA（内存分配）+ volk（扩展函数自动加载）+ glslc + CMake DEPFILE（shader 增量编译）。
- **GfxDevice**：单一对象封装 context、swapchain、bindless descriptor set，作为参数传递，取代到处传 VkDevice / VkQueue 的写法。
- **计算着色器 skinning**：骨骼动画在 compute pass 输出蒙皮后的顶点缓冲，后续所有渲染阶段（阴影、主渲染）对静态和蒙皮网格完全一致处理。
- **精灵批处理**：N 个精灵一次 `vkCmdDraw(cmd, 6, N, 0, 0)`，顶点坐标在 vertex shader 里用 `1 << (gl_VertexIndex % 6)` 位运算生成，无顶点缓冲。10000 精灵 315 微秒。
- **NBuffer 模式**：N 个 CPU staging buffer + 1 个 GPU buffer 处理每帧动态数据（如 joint matrices），避免 CPU/GPU 数据竞争。
- **手动同步**：在各 pass 之间插 vkCmdPipelineBarrier2，目前用 "fat memory barrier" 覆盖，靠 vkconfig sync validation layer 兜底。

## 隐藏限制

- **引擎适用范围窄**：19k LoC 只够关卡式小游戏；作者明确说不做通用引擎是工期控制在 3 个月的核心原因。
- **同步是技术债**：fat barrier 够用但低效；作者承认需要 render graph，目前没有。
- **sRGB + Dear ImGui 陷阱**：官方 Vulkan backend 的 sRGB 处理有根本性缺陷，需要自写 backend + DiligentEngine 方案才能彻底修复，不是小修小补能解决的。

## 收束

文章末尾的 Future Work 列表最后一条是"Finishing the game? (hopefully…)"——他花 3 个月造了引擎，游戏本体却还未完成。这不是作者的特例，是所有自造引擎项目的结构性宿命：引擎建设本身会消耗掉制作游戏的意愿。Vulkan 的技术门槛已经不是最大的风险。
