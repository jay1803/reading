---
title: "You should be using SwiftLog"
date: 2025-05-12T13:44:36Z
category: reading
author: "Jacob Bartlett"
description: "这篇文章的核心观点很务实：如果你在写 Swift 应用，还在到处 print() 调试和排障，那你大概率早该切到 SwiftLog 了。 作者想强调的，不只是“有个更优雅的 logging API”，而是 SwiftLog 能把你项目里的各种日志出口统一起来：开发时打到 LLDB / OSLog，线上时写到本地文..."
source: "https://blog.jacobstechtavern.com/p/swiftlog"
---

## TL;DR
这篇文章的核心观点很务实：**如果你在写 Swift 应用，还在到处 `print()` 调试和排障，那你大概率早该切到 SwiftLog 了。** 作者想强调的，不只是“有个更优雅的 logging API”，而是 SwiftLog 能把你项目里的各种日志出口统一起来：开发时打到 LLDB / OSLog，线上时写到本地文件，严重问题再送到 Crashlytics 或别的远端系统。它本质上提供的是一个统一 logging interface，让你不用再把监控和排障逻辑散落在各处。

## 关键洞察
文章最值得记住的地方，是它把 SwiftLog 定义得很清楚：**SwiftLog 不是一个具体日志后端，而是一个 API package。** 它自己不负责真正“打印”或“上传”日志，而是定义一套统一协议，让你把不同 backend 挂到同一套 LoggingSystem 上。这个点很重要，因为很多人一听 logging framework 就会以为是“换一种 console 输出方式”；但 SwiftLog 真正的价值在于抽象层：你只需要在业务代码里调用同一个 `Logger`，至于日志最后流向哪里，是开发控制台、本地文件还是 Crashlytics，由 handler 决定。

作者对这种设计的推崇，其实来自一个很现实的开发问题：logging 的需求会随环境变化。开发期你可能什么都想看，trace/debug 全开；线上你更在乎 warning / error / critical；某些用户问题你希望拿到一份本地 file trace；而真正严重的问题，你又希望能自动进入远端监控系统。没有统一接口时，这些逻辑就很容易散在各处，最后既难维护，也难切策略。

文章把几个关键概念拆得挺清楚：
- `LoggingSystem.bootstrap`：应用启动时一次性配置整个日志系统
- `MultiplexLogHandler`：把一条日志同时广播给多个 backend
- `Logger`：你日常在业务代码里真正要用的对象
- `LogHandler`：各个后端的具体实现，比如 OSLog、文件、Crashlytics

其中最值得记的是 `MultiplexLogHandler` 这个思路。它意味着你不必在代码里写一堆 if/else 去决定“这条日志现在该发给谁”，而是通过 handler 和 log level 统一控制。比如：
- 所有日志都可以走 OSLog
- `.info` 以上写入本地文件
- `.warning` / `.error` / `.critical` 再送 Crashlytics

这样一来，业务代码里只保留“我要记录什么”，而不需要操心“我要怎么记录、记录到哪”。这是一个很典型的工程抽象收益。

文章里还顺手给了几个具体实现示例，我觉得最实用的是它们共同说明了一个原则：**每个 handler 都可以有自己的 logLevel 和职责边界。** 你完全没必要把所有日志都送到每个系统。比如 debug spam 没必要上报 Crashlytics，但 critical issue 当然值得。也就是说，SwiftLog 不只是统一入口，也方便你做日志分层和成本控制。

作者最后那句 “you are, in fact, using print wrong” 其实挺有代表性：不是说 `print()` 一无是处，而是它在稍微严肃一点的项目里，很快就会暴露出局限——没有统一格式、没有 severity、没有目标后端抽象、也不好做生产环境监控。SwiftLog 给的不是一种花哨替代品，而是一个更像真正 production logging system 的起点。

## 对你（行动层面）的启发
如果你写 Swift / iOS / server-side Swift，这篇最直接的 takeaway 是：**尽早把日志从 `print()` 升级成统一 logging interface。** 哪怕你暂时还没决定最终接哪个远端监控，也可以先用 SwiftLog 的 no-op / basic handler 把接口铺好。这样后面要接 OSLog、文件导出、Crashlytics 时，就不用满项目替换。

一个很实用的落地顺序可以是：
- 先引入 `swift-log`
- 在 app launch 时统一 `bootstrap`
- 业务代码里只使用 `Logger`
- 先接一个开发期 handler（OSLog）
- 再逐步补本地 file / Crashlytics / 其他远端 handler
- 按 handler 区分 log level，避免所有东西都一锅端

我自己的感觉是，这篇文章值钱的地方，在于它没有把 logging 讲成一个 observability 大工程，而是把它降到了一个很可执行的层面：你其实不需要先成为监控专家，只要先停止滥用 `print()`，把日志入口统一起来，就已经比很多项目先进一大步了。

## 一句话总结
SwiftLog 的真正价值，不是替代 `print()` 这么简单，而是给 Swift 项目提供一个统一、可扩展、适合生产环境的日志抽象层。
