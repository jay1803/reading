---
title: "A 12TB Steam \"teraleak\" spills more than a decade of lost PC gaming history"
date: 2026-10-17T00:30:00Z
category: reading
description: "一份超过 12TB 的 Steam 旧服务器内容档案，让 2003 至 2013 年间大量被认为已经失落的 PC 游戏版本重新公开，也暴露了游戏发行平台集中保存开发历史所带来的安全与版权风险。"
source: "https://arstechnica.com/gaming/2026/08/a-12tb-steam-teraleak-spills-more-than-a-decade-of-lost-pc-gaming-history/"
author: "WithinReason"
---

一份超过 12TB 的 Steam 旧服务器内容档案，让 2003 至 2013 年间大量被认为已经失落的 PC 游戏版本重新公开，也暴露了游戏发行平台集中保存开发历史所带来的安全与版权风险。这次被称为 **Steam2 Teraleak** 的泄露正通过 BitTorrent 传播，包含数千个 depot，号称尽可能完整地收录旧 Steam2 服务器上的内容：除正式发行版本外，还有 Valve 与第三方发行商上传过的预发行版、原型和测试版；一旦广泛镜像，Valve 将很难彻底清除它们。

档案的时间边界来自 Steam 分发架构的更替。2013 年，Valve 从使用专有文件分发格式的 Steam2 转向 SteamPipe，以标准 HTTP 文件树分发内容，减少更新过程中依赖 Valve 审批的瓶颈，并让补丁下载只传输文件差异。迁移之后，一些早期游戏版本无法再从 Valve 获取，保存者一度认为它们只残留在老旧电脑的本地下载中。这次公开的档案表明，至少部分被认为失落的版本仍保存于尚未公开的收藏之中。

这些文件如何流出，仍有一个关键环节未明。长期追踪 Valve 的数据挖掘者 Gabe Follower 表示，他已验证档案内容全部来自一个公开可访问的 API 端点；西班牙语 Valve 分析者 Scolcer 也称，下载来源对所有人开放，不需要密码。不过，这些说法没有厘清文件究竟是近期下载的，还是在 2013 年架构迁移前就已被私人保存。Valve Cut Content Discord 的管理员 The One Epicplayer 与 CrazyBubba 提出的解释是，多人可能把早年下载、长期囤积的 depot 汇总成了这份档案。随附 readme 鼓励广泛分享和镜像；一名自称原始上传者的用户还提供了 22TB 服务器上传日志的截图作为佐证，并表示公开这些文件耗费了大量精力。公开接口缺乏保护与私人收藏多年后集中释出，都可能参与了这条传播链，但具体过程尚未确认。

目前最引人注目的发现来自多个可玩的 Portal 2 预发行版本。玩家找到了被删除的 GLaDOS 台词，以及 Aperture CEO Cave Johnson 的意识被困在方块中的片段；其中一句临时配音是"My life is torture, please kill me"，此前人们只在游戏附带的文本文件里见过这段台词。早期版本还出现了正圆形传送门、黏附凝胶、慢动作枪，以及一种曾在 Valve 官方纪录片的未发行 Half-Life 2: Episode Three 画面中出现的武器模型。这些可运行版本让保存者得以研究最终被删去的机制及其实际表现。

这些发现也有明确边界：档案中没有可玩的 Half-Life 3，挖掘者只报告发现了疑似关联 Episode Three 的"ep3"数据文件。其他 Valve 内容包括带有未公开删减素材的 Left 4 Dead 2 与 CS: GO 早期测试版，以及 F-Stop 的模型和图像；F-Stop 是一个以相机为核心机制、最初计划作为 Portal 续作、后来被取消的项目。档案能够补全哪些开发史，取决于文件里实际存在的版本，项目代号或零散素材本身不能证明完整游戏已经出土。

泄露的范围远超 Valve 自家作品。数据挖掘者已识别出 Spore、Dragon Age: Origins、Batman: Arkham Asylum、Sonic the Hedgehog 4 和 Spec Ops: The Line 等游戏的测试版或原型。它们同样受服务器存档范围限制：从未离开开发者本地电脑或办公室网络的版本不在其中，但临近发行时上传到 Steam 的测试构建仍可能保留后来删除的内容。因此，这份档案覆盖的是曾进入 Steam 分发系统的开发痕迹，无法等同于这些游戏的完整开发档案。

保存价值也伴随着法律与安全代价。即使内容止于 2013 年，第三方发行商仍面临未公开开发成果外流，以及完整旧版游戏被用于盗版的问题。长期追踪 Valve 的 Tyler McVicker 特别警告，大量第三方内容让处理这份档案的法律风险远高于只涉及 Valve 测试版的情况，并以自己过去因 beta 内容惹上麻烦的经历劝人谨慎。六年前 Nintendo 的"gigaleak"曾揭示大量未知开发史，这次泄露可能对更广泛的 PC 游戏历史产生类似影响：同一个集中式发行平台，既能保存跨越多家公司、多代版本的历史，也能成为让整批历史同时失去控制的单点故障。
