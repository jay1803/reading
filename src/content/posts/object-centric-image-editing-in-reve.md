---
title: "Object-Centric Image Editing in Reve"
date: 2026-07-02T08:03:15Z
category: reading
description: "Reve 的 layout model 把 object-centric 图像编辑从概念演示变成了可用产品。核心突破：图像不再是像素集合，而是结构化的元素树，每个元素有位置、尺寸、描述、颜色等属性——layout 之于图像，等同于 HTML 之于网页。"
source: "https://www.lukew.com/ff/entry.asp?2156"
---

## Layout 是图像的 HTML，让每个元素变得可寻址

Reve 的 layout model 把 object-centric 图像编辑从概念演示变成了可用产品。核心突破：图像不再是像素集合，而是结构化的元素树，每个元素有位置、尺寸、描述、颜色等属性——layout 之于图像，等同于 HTML 之于网页。

Photoshop 之所以是像素工具，纯属历史原因：它被设计出来的时候根本没有语义理解能力，所以只能把像素操作推到前台。现有主流图像模型也没有本质改变——text-to-image 的内部路径是 prompt → 语言模型扩展成长描述 → 扩散模型渲染像素。文字是松散的内部表示，所以控制也松散：微调一个词，整张图重新生成。

## Layout model 的机制

Reve 的模型以 layout 为输入和内部思考格式，而非 prose。输入：layout + 指令 + 图像；模型在思维中推理出目标 layout，再渲染像素。这让编辑操作可以精确作用于单个元素：换一辆车的颜色，无需重新生成整张图；在室内场景里移动椅子，阴影、反光、透视依然一致，因为模型理解的是元素之间的几何关系，而非哪些颜色落在哪些坐标上。

## 人机协作接口

layout 是可读的结构化格式，AI agent 可以像推理代码一样推理它。这意味着 layout 可以成为人与 AI 协作的共享接口——设计师操作高层元素，agent 处理约束和渲染细节，两者读写同一个结构。这是 canvas-centric 工具无法支撑的协作模式，也是作者预期会出现大量新创意工具的原因。
