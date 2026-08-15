---
title: "Transcript for FFmpeg: The Incredible Technology Behind Video on the Internet | Lex Fridman Podcast #496"
date: 2026-05-07T08:02:46Z
category: reading
description: "Jean-Baptiste Kempf 是 VideoLAN/VLC 的核心人物与主席，也是 FFmpeg、x264、dav1d 等开源多媒体生态的重要组织者；Kieran Kunhya 是长期 codec 工程师、FFmpeg 贡献者，也是 FFmpeg 在 X/Twitter 上高强度发声的人之一。两人的共同..."
source: "https://lexfridman.com/ffmpeg-transcript/?utm_source=rss&utm_medium=rss&utm_campaign=ffmpeg-transcript"
---

## 嘉宾背景
Jean-Baptiste Kempf 是 VideoLAN/VLC 的核心人物与主席，也是 FFmpeg、x264、dav1d 等开源多媒体生态的重要组织者；Kieran Kunhya 是长期 codec 工程师、FFmpeg 贡献者，也是 FFmpeg 在 X/Twitter 上高强度发声的人之一。两人的共同位置不是“播放器作者”，而是维护互联网视频底层基础设施的人：VLC 面向用户播放一切，FFmpeg 面向几乎所有视频工作流处理一切，二者和 x264、dav1d、libVLC 等项目互相嵌套，像一个“binary star system”。

## TL;DR
这场对话最核心的线不是“FFmpeg/VLC 很强”，而是：现代视频世界建立在一小群志愿者维护的极端复杂、极端底层、极端高影响力的软件上；它们之所以能长期存在，靠的不是抽象口号，而是对质量、开放、低层优化、反商业污染、反政府后门、反大公司白嫖的硬边界。

## 视频的魔法本质是把不可管理的复杂度压成“按下播放”
从 URL/文件到屏幕像素，中间要经过字节流读取、container/demux、音视频帧切分、GPU 能力探测、软件解码、去熵编码、反量化、运动补偿、YUV/RGB 处理、音视频同步等一整条链。用户看到的是“VLC 能打开任何文件”，实际背后是对混乱现实格式的长期吸收：`.mp4` 只说明容器，不保证 codec；现实文件常常命名错误、封装错误、标准实现错误，但 VLC/FFmpeg 的使命就是尽量不把复杂性交还给用户。

## 开源在这里不是免费，而是基础设施伦理
Kempf 用“蛋糕和配方”解释开源：不只给成品，也给源代码、修改权、再分发权。VLC 曾多次拒绝带广告、工具栏、捆绑软件的巨额商业化机会，因为那会背叛用户信任和贡献者共同体。这个选择在 2000 年代尤其不容易：当时下载软件顺手装 spyware/toolbar 是常态，VLC 的“不作恶”反而成为品牌的一部分。这里的伦理很朴素：钱可以再赚，但一旦污染分发渠道，项目的灵魂和用户安全就回不来了。

## 质量门槛来自代码，不来自身份
FFmpeg/VLC 的社区标准接近硬核 meritocracy：不在乎你来自大公司、大学、国家，甚至“也许你是条狗”，只看代码质量。青少年可以写进世界级 assembly，维护者也会被最强程序员严厉 review。粗粝交流并不总是友善，但核心原则是批评结果而不是攻击人；同时也要看到，大量贡献者不是英语母语、不是全职维护者，而是在下班后维护支撑全球视频系统的代码。

## 大公司依赖开源，却常把志愿者当供应商
Google 用 AI 找 FFmpeg 安全问题并公开宣传、Microsoft Teams 在志愿者 bug tracker 里标“高优先级”、XZ 事件暴露单点维护者被持续施压的风险；这些案例共同说明：万亿美元公司经常把免费开源当作默认基础设施，却没有匹配的资金、补丁、联系人和维护合同。FFmpeg/VLC 在 X 上“spicy”的公开施压虽然吵，但有效：它让 Android/Windows Store 等平台终于回应，也让更多人意识到这些项目的重要性。

## 手写 assembly 不是怀旧，而是视频规模下的经济学
Kieran 解释 SIMD assembly：一条指令同时处理多个像素，能带来 10x、50x、甚至 62x 的函数级提升。dav1d 为 AV1 写了约 30,000 行 C 和 240,000 行手写 assembly，因为 AV1 复杂到很多人认为必须靠硬件解码；但在硬件普及前，优秀软件解码器决定了标准能否真正落地。这里的非直觉点是：在数十亿设备、Netflix/YouTube 级流量、移动电池和带宽成本面前，底层优化不是审美洁癖，而是全球资源账本。

## “重写一切”通常低估了旧代码里的隐性知识
Rust 被认可为适合新项目、解析器、网络边界和内存安全的强工具，但 Kempf 反对把复杂成熟系统简单“重写成 Rust”。原因是读代码比写代码难一个数量级；旧代码里沉积了业务逻辑、硬件坑、格式怪癖、历史兼容和测试经验。更关键的是，x264/dav1d 这类项目的性能核心在 assembly：如果仍然要内联 assembly，单纯把 C 改成 Rust 并不能自动得到安全性。真正值得做的是类似“secure assembly”的编译期检查和 checkasm 式验证。

## Codec 进化是感知、算力、专利和分发成本的博弈
H.264/x264 成功不只是数学压缩率，而是 hobbyist 社区把“人眼觉得好看”放到 PSNR 等传统指标之上，发展出 psychovisual rate distortion。AV1/AV2、H.265/H.266 每代大致带来约 30% 压缩收益，但代价是更高编码复杂度和更复杂专利格局。HEVC 的多专利池和不确定授权成本让 YouTube/Netflix/Meta/Google 等推动 royalty-free 的 Alliance for Open Media；当授权可能变成每年上亿美元，自己做开放 codec 就成了理性选择。

## VLC/FFmpeg 的安全边界是“播放文件”，不是审查内容
Vault 7 暴露 CIA 曾利用修改版 VLC 做攻击，Kempf 也说情报机构曾要求 VLC 加后门，答案是明确拒绝：如果必须妥协软件，就宁可关闭项目。VLC 不按视频内容审查能否播放，它只关心文件能否被解析。压力来自政府、军事使用、恶意下载站、假 VLC、GPU driver/第三方库攻击面、sandboxing 难题；但其底线是：播放器不能变成审查器或后门分发器。

## 未来的多媒体会扩展到机器人、点云、脑机接口，但旧问题不会消失
Kyber 把 VLC/广播/低延迟经验用于机器人、无人机和远程控制，目标是极低 glass-to-glass latency，并解决多摄像头、多传感器、clock drift、训练数据时序一致性。更远处，多媒体可能包括 point cloud、RGB-D、haptics、smell、brain-computer interface；Kieran 开玩笑说未来会有 `FFmpeg -i input format human brain`。但无论媒介怎么变，标准化、开放实现、压缩、同步、兼容、专利与长期保存仍是同一组问题。

## 收束行
这期真正留下的边缘感是：文明最常用的技术并不总由最显眼、最富有的组织维护；很多时候，是几个对“文件应该能打开、代码应该够好、用户不该被背叛”异常固执的人，在替世界守住底层。
