---
title: "Building a World Map with only 500 bytes"
date: 2026-07-06T08:01:44Z
category: reading
description: "8,523 字节的 ASCII 地图经 deflate-raw 压缩后降至 445 字节。核心跳跃：选择大陆内部填满 ~~ 字符的\"填充版\"，而非只保留海岸线轮廓的\"轮廓版\"。填充版产生大量连续重复字符，deflate 对长段重复序列压缩效率极高；轮廓版虽然视觉上更稀疏，但字符间隔多、规律弱，压缩比反而更差。结论..."
source: "https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything"
---

### 压缩友好的表示法胜过视觉精简

8,523 字节的 ASCII 地图经 deflate-raw 压缩后降至 445 字节。核心跳跃：选择大陆内部填满 ~*~ 字符的"填充版"，而非只保留海岸线轮廓的"轮廓版"。填充版产生大量连续重复字符，deflate 对长段重复序列压缩效率极高；轮廓版虽然视觉上更稀疏，但字符间隔多、规律弱，压缩比反而更差。结论先行：数据的结构对压缩友好程度比视觉细节更重要。

### 技术实现

浏览器端纯 JS 解压，无需服务端：用 ~fetch()~ 加载 ~data:~ URI 内嵌的 base64 压缩数据，通过 ~DecompressionStream('deflate-raw')~ 在客户端还原为 ASCII 文本，写入 ~<pre>~ 标签。HTML 文件含 base64 数据与解压代码在内仍低于 1k；地图数据本身 445 字节。

### AI 的实际贡献与局限

Codex 先尝试 SVG 方案失败（500 字节内坐标预算不够画出可识别轮廓），随后退回 ASCII。但 Codex 未能自主推进决定性优化——去掉水面字符、裁剪左侧空白、只保留陆地 ~*~、以及"填充优于轮廓"这个关键判断，均由作者人工提示后才落地。AI 完成了方案探索和代码生成，但核心算法直觉来自人。
