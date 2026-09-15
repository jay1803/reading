---
title: "The case of the progress callback that never got called when progress happened"
date: 2026-09-15T04:43:21Z
category: reading
description: "进度回调始终没有触发，根因是 AggregateSource::DownloadAsync 只等待并返回内部下载操作的最终结果，从未把内部进度转发给调用者。"
source: "https://devblogs.microsoft.com/oldnewthing/20260903-00/?p=112672"
author: "Raymond Chen"
---

进度回调始终没有触发，根因在于 **AggregateSource::DownloadAsync** 创建了一个新的外层 **IAsyncOperationWithProgress<bool, double>**，却只等待并返回内部下载操作的最终结果，完全没有把内部操作产生的进度转发给调用者。

C# 调用端的写法本身很标准：先调用 `DownloadAsync` 获得异步操作，再订阅 `Progress` 事件，随后 `await` 操作完成。即使下载持续很久，回调仍然毫无动静，因此问题不在下载速度过快。排查这类跨 C# 与 C++/WinRT 边界的问题，可以先观察 COM-callable wrapper 是否被创建并注册为进度回调，再在 wrapper 上设置断点：如果断点触发而 C# 委托没有执行，故障位于语言投影层；如果断点从未触发，故障就在 C++ 侧。

检查 C++/WinRT 实现后可以看到，`AggregateSource::DownloadAsync` 解析由 provider、冒号和 item ID 组成的复合 ID，查找对应 provider，然后执行 `co_return co_await provider.DownloadAsync(providerItemId)`。这段代码确实等待了 provider 的下载结果，却从未调用 `co_await winrt::get_progress_token()`，更没有通过该 token 报告任何进度。外层协程和 provider 返回的内部异步操作是两个不同的 `IAsyncOperationWithProgress`；C# 订阅的是外层操作，而进度产生在内部操作上，因此内部进度不会因 `co_await` 自动穿透到外层。

最简单的修复方式是取消这层异步中间包装，让 `AggregateSource::DownloadAsync` 直接返回 `provider.DownloadAsync(providerItemId)`。这样调用者订阅的就是实际执行下载的异步操作，provider 产生的进度可以直接到达 C# 回调。对于 ID 格式无效或找不到 provider 的分支，可以返回一个已经完成且结果为 `false` 的 `completed_async(false)`；如果不使用 `completed_async`，也可以通过一个立即返回 `false` 的微型协程生成同等的已完成操作。

因此，`co_await` 只传递完成状态和最终结果，不会自动转发 `IAsyncOperationWithProgress` 的进度通道；包装带进度的异步操作时，要么直接返回底层操作，要么显式订阅底层进度并通过外层 progress token 重新报告。
