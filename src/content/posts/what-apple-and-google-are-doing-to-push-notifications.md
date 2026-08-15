---
title: "What Apple and Google are doing to push notifications"
date: 2026-05-29T08:01:14Z
category: reading
description: "Push 通知正在经历 email 已经发生过的命运：发送者以为自己在触达用户，实际中间多了一层由 Apple/Google 控制的编辑器；这层编辑器会按用户注意力、系统体验和平台 AI 能力重排、摘要、降级甚至吞掉通知，而发送者几乎看不到这个过程。"
source: "https://www.jacquescorbytuech.com/writing/what-apple-and-google-are-doing-your-push-notifications"
---

## TL;DR
Push 通知正在经历 email 已经发生过的命运：发送者以为自己在触达用户，实际中间多了一层由 Apple/Google 控制的编辑器；这层编辑器会按用户注意力、系统体验和平台 AI 能力重排、摘要、降级甚至吞掉通知，而发送者几乎看不到这个过程。

## 核心主张拆解
Apple 和 Google 从一开始就掌握 push 的核心管道：iOS 走 APNs，Android 走 FCM/GCM 系列服务。早期平台主要解决电池与连接问题，后来逐步把控制权从发送者手里收回：Android 8 在 2017 年引入通知频道，iOS 15 在 2021 年引入 Focus、Scheduled Summary 和 interruption level，Android 13 在 2022 年把通知变成运行时权限。

这些变化把 push 从“应用发什么，系统显示什么”改造成“应用提交候选内容，系统决定它是否值得打断用户”。用户获得更多控制是合理的，但平台也获得了不透明的判断权；这个判断现在越来越多由端侧模型执行。

email 是预演。Gmail 的 Promotions tab、Apple Mail Privacy Protection、Google/Yahoo/Microsoft 的批量发件规则，都说明开放协议上的 email 已经被客户端和邮箱服务商重新中介化。push 更脆弱，因为它没有开放协议、没有可迁移订阅列表、没有 DKIM/DMARC 这类外部可验证机制，也没有类似 Google Postmaster Tools 的诊断窗口。

## 关键机制
端侧 AI 是新编辑器。Apple Intelligence 用端侧基础模型和任务 adapter 做摘要、实体抽取、优先级判断；Google 的 Gemini Nano/AICore 在 Android 系统层服务类似功能。通知进入设备后，先经过 Focus、DND、频道静音、app block 等用户规则，再进入系统排序、摘要、聚合和展示逻辑。

发送者能影响的部分很有限。iOS 的 NotificationServiceExtension 可以在显示前短暂修改内容，NotificationContentExtension 可以定制展开视图；Android 侧可以设置 channel importance 和写入 NotificationManager。它们都不能让发送者知道通知是否被摘要、放进 Promotions、被 Focus 压掉、被 Priority Notifications 降级，或被用户在锁屏上无声清除。

测量漏斗因此变暗。APNs/FCM 能确认平台接受了 payload，但不等于用户看到了。push 平台 SDK 可以记录展示、点击和 session start，但“被系统编辑后有没有真正被看见”仍不可见。open/click/conversion 只来自被平台和用户共同筛选后的子样本，天然有偏。

数据方向支持作者的策略判断：Android 13 权限变化后 opt-in 明显下滑；Batch 2025 数据显示 Android opt-in 一年内从 85% 降到 67%，跨平台平均约 61%。通知研究也长期显示 messaging/transactional 类型被用户视为高价值，promotional 类型最低价值；高频、泛化、营销味强的通知最容易消耗权限。

## 对发送者的实际含义
push 应该承担更少生命周期营销任务，专注两类工作：唤回已经离开产品的用户，以及传递真正时间敏感、交易性、用户自己触发的事件。跨售、教育、内容发现、促销活动更适合迁移到 in-app inbox、产品内卡片、登录后界面和任务流中的嵌入消息，因为这些表面不经过 APNs/FCM，也不会被 Apple Intelligence 或 Gemini Nano 摘要。

通知文案要把标题当成结构化字段写：金额、时间、对象、状态、下一步动作必须前置。`Your delivery is 15 minutes away` 这类事实能在摘要中保留；`We've got great news!` 只有语气，没有信息，模型和用户都可能把它压扁或丢弃。

权限请求要发生在用户理解价值之后，而非首次打开时冷启动弹窗。营销方还应减少广播，强化分群与个性化，清理长期无响应的 opt-in；沉默的大用户池会训练系统相信这个 app 的通知不重要。

更长远的变化是 agentic OS。Siri、Apple Intelligence、Gemini 未来会不仅摘要通知，还可能代表用户处理通知背后的动作。于是通知不再只是锁屏上的一句 copy，而是触发 App Intents、Android App Actions 或其他可执行能力的入口。发送者要把“用户可以做什么”暴露给系统，而不能把 action 藏在三层 UI 之后。

## 值得质疑
文章对“如何写给摘要模型”的建议方向合理，但直接实验证据不足；作者也承认目前没有公开测试证明哪种 push copy 在 Apple/Google 摘要器下最稳定。

部分 Android/OEM 细节仍有不确定性，尤其是 Samsung、Pixel、Android System Intelligence、Gemini Nano 之间的实际责任边界。文章把它们作为方向性判断处理，而非完全确定的实现事实。

vendor benchmark 数据应折价使用。Batch、Pushwoosh、OneSignal 等平台的数据能说明趋势，但它们不是中立研究机构，且口径常把 accepted、delivered、displayed、opened 混在不同层级。

## 最后一层判断
push 仍然有价值，但它的价值正在从“低成本广播渠道”收缩为“用户请求、交易状态、紧急回流”的高约束通道。未来十年活下来的发送者，不会是最会写营销话术的一批，而是最能让平台编辑器也承认“这条通知确实是用户要的”的一批。
