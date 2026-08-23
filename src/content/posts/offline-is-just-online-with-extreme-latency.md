---
title: "Offline Is Just Online With Extreme Latency"
date: 2023-04-20T13:01:04Z
category: reading
author: "Jim Nielsen"
description: "文章主要介绍了 Peter Van Hardenberg 在“Local-first Software”演讲中提出的观点，即重新定义“离线”和“在线”的概念，将“离线”视为“在线”状态下具有极端延迟的一种形式。这种新的思维方式鼓励开发者构建以本地数据同步为中心的应用，而不是依赖于持续的网络连接和 API 调用。"
source: "https://blog.jim-nielsen.com/2023/offline-is-online-with-extreme-latency/"
---

## TL;DR
文章主要介绍了 Peter Van Hardenberg 在“Local-first Software”演讲中提出的观点，即重新定义“离线”和“在线”的概念，将“离线”视为“在线”状态下具有极端延迟的一种形式。这种新的思维方式鼓励开发者构建以本地数据同步为中心的应用，而不是依赖于持续的网络连接和 API 调用。

## 主题
### 🚲 Local-first Software
Peter Van Hardenberg 提倡“Local-first Software”的开发模式，将程序运行在用户设备上，并将云端用于数据持久化或可访问性，而不是完全依赖云端运行程序。这种模式类似于渐进增强的弹性设计，将云端视为可选的增强功能。Peter 将当前构建大型企业级软件和云服务比作建造航空母舰，而实际上很多时候我们需要的是更简单、更个性化的“自行车”。

### 🤝 P2P 技术的挑战
Peter 指出，目前一些用于构建 local-first、P2P 应用的开放技术（如 webRTC）并不成熟。他建议，如果已经有了服务器，就不要折腾 P2P 技术，直接使用服务器即可。

### 🌐 重新定义在线/离线
Peter 提出将“在线”和“离线”视为同一连续体的不同延迟度量。
## Wifi: < 300ms 延迟
## 3G: 1s 延迟
## Offline: 30 秒到数天的延迟（直到重新同步）
“离线”只是延迟频谱的最极端情况。这种观点促使开发者从基于 API 调用转向基于数据同步的产品设计。

### 💡 思维转变
Peter 强调，改变构建方式的思维模式可以打开构建不同事物的大门。即使你不喜欢数据同步的想法，至少也值得考虑和想象一种不同于你习惯的范式中可能存在的东西。“离线”也有不同的延迟等级：秒、分钟、小时、天、周等。

## 总结
“离线”是在线状态下具有极端延迟的一种形式，开发者应该转变思维模式，构建以本地数据同步为中心的应用。
