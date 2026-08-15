---
title: "Meta's ships facial recognition on smart glasses"
date: 2026-06-06T08:04:42Z
category: reading
description: "APK 逆向证实：Stella v273 内置完整的面部识别栈，检测→对齐→2048维嵌入→余弦向量索引→通知管道全部装配并可端到端运行，唯一与普通用户之间的屏障是服务端的 enrollment 数据尚未推送。"
source: "https://www.buchodi.com/meta-glasses-facial-recognition/"
---

## TL;DR
APK 逆向证实：Stella v273 内置完整的面部识别栈，检测→对齐→2048维嵌入→余弦向量索引→通知管道全部装配并可端到端运行，唯一与普通用户之间的屏障是服务端的 enrollment 数据尚未推送。

## 三个模型、一个向量数据库、一条完整管道
设备本地运行三个 ExecuTorch 模型：SCRFD（人脸检测，3.4 MB）、KPSAligner（关键点对齐，117 KB）、SFace（2048 维生物特征嵌入，96 MB，比公开参考实现大一倍）。人脸数据库使用 sqlite-vec 扩展做余弦相似度搜索，向量维度与 SFace 输出精确匹配，说明这三个组件是作为一套系统设计的，而非拼凑的死代码。数据库位于 RLDrive 的 person_profiles 命名空间下——RLDrive 是 Meta 现有的跨设备同步框架，架构上即为服务端写入而设计。

## NameTagsPending：设备在主动积累生物特征档案
研究者端到端测试发现两条分支：已知人脸触发推送通知「Recognized [姓名]」；未知人脸则将裁剪后的面部图像（.jpg）与 2048 维指纹（.emb）成对写入 NameTagsPending/ 目录，持久化到磁盘且重启后保留。这一结构的字面含义是「等待打标签的人脸」——一旦 Meta 通过 RLDrive 推送 enrollment 数据，此前积累的所有未知人脸均可被回溯识别。

## Meta 声称的「未上线」与实证的距离
研究者明确：未观察到 Meta 向 person_profiles 推送身份数据，通知深链目标页面在 v273 中缺失，「Connections」UI 卡片在未注册账户上隐藏。这些确实表明功能未对普通用户开放。但一套经过端对端验证、内部一致（模型维度＝向量索引维度＝embedding 形状）的系统，距离「意外残留的研究碎片」相去甚远。Meta 能否以及何时将其推向生产，完全取决于 Meta 自己。
