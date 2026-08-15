---
title: "#496 – FFmpeg: The Incredible Technology Behind Video on the Internet"
date: 2026-05-07T08:02:46Z
category: reading
description: "Jean-Baptiste Kempf 是 VLC 核心开发者、VideoLAN president，也是把 VLC 从学生项目维持成全球级公共软件的人。Kieran Kunhya 是长期 FFmpeg contributor、codec engineer、Open Broadcast Systems 创始人之一..."
source: "https://lexfridman.com/ffmpeg/?utm_source=rss&utm_medium=rss&utm_campaign=ffmpeg"
---

## 嘉宾背景
Jean-Baptiste Kempf 是 VLC 核心开发者、VideoLAN president，也是把 VLC 从学生项目维持成全球级公共软件的人。Kieran Kunhya 是长期 FFmpeg contributor、codec engineer、Open Broadcast Systems 创始人之一，也是 FFmpeg X 账号背后那种“用 meme 捍卫底层工程尊严”的声音。

## TL;DR
FFmpeg/VLC 的真正主题不是“视频播放器很强”，而是现代互联网的视频文明被极少数低调、偏执、以代码质量为信仰的工程师托住：他们写 C 和手写汇编，逆向工程旧格式，拒绝广告和后门，处理公司、专利、安全研究和用户边缘案例留下的复杂性。它们像公共基础设施，却没有公共基础设施级别的稳定资助；价值来自极深的工程文化，而不是商业叙事。

## FFmpeg/VLC 是现代视频的隐形地基
FFmpeg 覆盖 codec、muxer/demuxer、filter、CLI 与底层库，YouTube、Netflix、Chrome、Firefox、Discord、VLC 和大量线上/线下视频 workflow 都依赖它；Lex 提到估计 90%+ 的视频处理流程涉及 FFmpeg。VLC 则是把这些能力交到普通用户手里的应用层：从 URL/文件拿到 byte stream，demux 出音频、视频、字幕，再用 codec 解码，最后交给 CPU/GPU 渲染。

Kieran 把 VLC 与 FFmpeg 的关系比成 Android 与 Linux：VLC 不只是“套 FFmpeg 外壳”，它提供播放器、奇怪文件兼容、跨平台发行、用户触达和一整套 VideoLAN 生态；FFmpeg 也集成 x264、libopus 等第三方库。两者更像 binary star system：互相放大，而不是谁吞并谁。

## 这套系统的难度在于“真实世界永远不干净”
容器和 codec 的区别只是入门：MP4/MOV/MKV 是容器，H.264/AV1/ProRes 是编码格式，但真实文件经常扩展名撒谎、实现不标准、边缘设备写出怪变体。FFmpeg/VLC 的价值在于吃下这些脏现实：VHS capture card、DVD-Audio、GoToMeeting 私有 codec、RealMedia/Windows Media 老格式、中文 CCTV MPEG-4 变体，甚至物理 VLC cone 触发播放。

逆向工程的核心不是“猜格式”，而是靠样本、bit exactness、反汇编和大量 edge cases 推回 codec 行为。每多支持一种 codec，整个系统的价值都会上升，因为 FFmpeg 变成多媒体世界的 Rosetta Stone。

## 手写汇编不是怀旧，是规模经济
对 FFmpeg/VLC 这种软件，C 经常还不够快。对 AV1、H.264、实时广播、10-bit 视频转换、低延迟链路来说，手写汇编能带来数量级差异；对话里提到 FFmpeg 有约 10 万行汇编，dav1d 里汇编占比极高，某些路径可比 C 快 60 倍以上。

这也解释了他们对 Rust 的谨慎：memory safety 有价值，尤其适合 parsing、networking 和边界检查，但如果性能路径最终仍要 inline/handwritten assembly，安全模型会被汇编层重新打开。更现实的方向不是“全改 Rust”，而是为汇编建立 compile-time/checkasm 类工具，理解 register、cache、calling convention、SIMD 与不同 ARM/x86 代际差异。

## 开源共同体的伦理是代码质量、信任和长期维护
JB 反复强调：社区关心的是 code quality，不关心你来自大公司、工厂、哪个国家，甚至“你是不是一条狗”。这不是冷酷，而是维护者必须对未来负责：临时 contributor 可能换工作、换生活、消失；留下来的 10-15 个 core maintainers 要长期维护你的 patch。

VLC 拒绝数千万美元广告/toolbar/spyware offer 是同一套伦理的商业版本。JB 不是反钱，而是认为 sneaky ads、偷数据、污染用户信任不对；最后一次 offer “obscene”，对方甚至用“拿钱再做开源”诱惑他，但他仍拒绝。VLC 的品牌资产不是流量，而是用户相信它不会背刺自己。

## 大公司依赖开源，却常把它误认为 vendor
Google AI security report 事件的核心不是“不能报漏洞”，而是大型公司用 AI 批量生成公开安全报告，让志愿者处理，同时 funding 很有限，还先向媒体宣传 AI 能力。Kieran 的批评是：FFmpeg 处理 untrusted data，有漏洞正常；问题是公司把公共 bug tracker 当 vendor Jira，把志愿者当有 SLA 的供应商。

FFmpeg X 账号的 meme 与“rap battle”风格，本质是把不可见劳动变得可见：teenager 能写 assembly、找到并修 bug，而一些安全研究流程却倾向制造 CVE drama。争吵表面粗糙，但带来了更高 awareness，也迫使外界承认 FFmpeg 不是 Kubernetes 式企业项目，而是少数人维护的全球基础设施。

## VLC 的安全边界来自“不妥协”
CIA Vault 7 里出现过 fake VLC；JB 也提到中国黑客面向印度用户的假 VLC、德国长期存在的 fake installer，以及疑似政府机构试图推 fake binary 到服务器。官方 VLC 的原则很硬：如果必须 compromise software，他们宁愿 shut it down。

这种边界体现在发布流程：offline build boxes、从 compiler 开始编译、double signing、组件 sandbox。VLC 不审查用户播放什么，因为它是离线工具，不回传内容，不是平台。专利上，VideoLAN 留在法国也有现实意义：法国/欧洲对软件专利更不友好，否则按 JB 的计算，VLC 若为所有专利付费，每用户可能要付 200+ 欧元。

## x264、AV1/AV2 与视频压缩的经济账
x264 是 H.264 时代的标杆编码器，至今仍是新 encoder（AV1/AV2/VVC/HEVC）比较的参照。它强在 psychovisual quality：不只是数学误差最小，而是让人眼觉得好看。动漫字幕、Blu-ray、HD 视频普及都推动了这套文化。

每代 codec 大致带来 25%-50% 压缩效率提升；AV1 相比 H.264 可节省约 40%-60% bandwidth，但编码成本更高。YouTube 的策略体现了经济账：大多数视频仍用 H.264，热门视频才值得重编码 AV1，因为“encode once, serve millions”。AV2 目标是在 AV1 上再降约 30% bandwidth，并尽量保持 royalty-free；这也是对 MPEG/H.265/H.266 专利矿区的制度性反击。

## 长期意义：FFmpeg 是数字文明的保存层
最打动人的部分是 archiving community：他们把 FFmpeg/FFV1 当成未来 1000 年还能播放多媒体的 Rosetta Stone。对档案馆来说，问题不是今天能不能播，而是未来还能不能验证、迁移、恢复；lossless、error recovery、开放源码和可复现 workflow，比短期压缩率更重要。

所以 FFmpeg 大概率会活 100 年，VLC 可能不一定以今天形态存在。未来 multimedia 可能扩展到 hologram、VR、BCI、haptics、teleoperation、robot video feedback；但只要世界需要把连续现实压成可传输、可播放、可保存的数据，就需要这类底层系统。

## 收束
这期最边缘但最重要的想法是：现代软件文明最可靠的一部分，往往不是最大公司的产品线，而是少数人因为“这东西有用、我喜欢、我不想它变坏”而长期守住的公共工具。
