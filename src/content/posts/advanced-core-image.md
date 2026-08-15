---
title: "Advanced Core Image"
date: 2025-05-12T13:49:20Z
category: reading
description: "Core Image kernel 不是\"把滤镜叠在图上\"——Warp kernel 是反向查表：对每个目标像素，你告诉 GPU 去哪个源坐标取样；只有被实际渲染的像素才会触发计算，CPU 层面几乎零开销。一个 linker flag（~-framework CoreImage~）+ 一个 ~.metallib~..."
source: "https://blog.jacobstechtavern.com/p/advanced-core-image"
---

## TL;DR
Core Image kernel 不是"把滤镜叠在图上"——Warp kernel 是反向查表：对每个目标像素，你告诉 GPU 去哪个源坐标取样；只有被实际渲染的像素才会触发计算，CPU 层面几乎零开销。一个 linker flag（~-framework CoreImage~）+ 一个 ~.metallib~ 捆绑文件，就能把自定义 Metal shader 接入任何 ~CIFilter~ 管线。

## 三类 Kernel 的分工

**Color kernel**（~CIColorKernel~）：对每个像素独立计算，输入是当前像素颜色，输出是新颜色；不感知位置（可选），适合色彩变换（胶片颗粒、灰度反转、RGB 通道置换）。

**Warp kernel**（~CIWarpKernel~）：输入是目标像素坐标，输出是源像素坐标（~float2~）；通过 ~sin~/~tan~ 驱动坐标偏移实现扭曲。用 ~tan~ 比 ~sin~ 物理上更准确——模拟凸透镜折射时 ~tan(π/2 × 归一化距离)~ 才是斯涅尔定律的正确映射。

**Texture kernel**（~CIKernel~ 基类 + ~CISampler~）：对目标像素可任意采样其他坐标的颜色，是三类中唯一能感知邻域的——3D 眼镜效果靠的是把 R/B 通道偏移到不同坐标后重组为最终像素。

接入配置：Build Settings → Metal Linker — Build Options → 加 ~-framework CoreImage~；~.metal~ 文件统一编译进 ~default.metallib~，运行时用 ~Bundle.main.url~ 加载。

## 隐藏限制
- ~CIImage~ 技术上是无限 extent，不指定 ~extent~ 会白白处理不可见区域——~apply(extent:)~ 必须明确传入。
- Shader 的 key-value coding 接入（~@objc dynamic~ + ~setValue(_:forKey:)~）是运行时魔法，漏掉就导致参数不生效且没有编译器警告。
- Shader 调试困难：~[[stitchable]]~ 属性标注容易忽漏，编译错误定位不总是精确。
- 文章代码全部 ~try!~，生产环境需要改成有错误处理的路径。
- *证据薄弱处*：未给出 Core Image 管线 CPU fallback 时的性能差距数据。

## 留下的那个想法
Warp kernel 反向查表思路是图形学里的"逆变换"原则——正向变换会在目标像素中制造空洞，所以 GPU 永远跑反向映射。同样的原则出现在光线追踪、纹理映射里。Core Image 的人没发明它，但把它包进了最易用的 iOS API 里。
