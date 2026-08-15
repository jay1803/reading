---
title: "Will Eatherton: How Cisco Plans to Compete in the AI Datacenter"
date: 2025-10-30T14:52:02Z
category: reading
description: "这篇访谈最重要的结论是：Cisco 在 AI 数据中心里的打法，不是正面复制 NVIDIA/Broadcom 的芯片故事，而是试图用“系统级整合 + 可管理性 + 多样化选择”切入。 换句话说，Cisco 想卖的不是一颗更强的芯片，而是一套对大企业、主权云和部分 hyperscaler 来说更容易部署、管理和扩展..."
source: "https://www.fabricatedknowledge.com/p/will-eatherton-how-cisco-plans-to"
---

## TL;DR
这篇访谈最重要的结论是：**Cisco 在 AI 数据中心里的打法，不是正面复制 NVIDIA/Broadcom 的芯片故事，而是试图用“系统级整合 + 可管理性 + 多样化选择”切入。** 换句话说，Cisco 想卖的不是一颗更强的芯片，而是一套对大企业、主权云和部分 hyperscaler 来说更容易部署、管理和扩展的网络系统。

## 关键洞察
这场对谈里最值得注意的，是 Cisco 对自己历史位置的重新定义。Will Eatherton 很坦白地承认，Cisco 在早期云时代错过了节奏，传统企业和电信时代的优势并没有自动延续到 hyperscale 与 AI 基建时代。所以过去几年它的核心任务其实不是“继续当老大”，而是重新获得上桌资格。这也是为什么 Cisco 同时押了几个方向：Silicon One、自研网络 OS、多 OS 兼容（包括 SONiC）、Acacia optics、NVIDIA 合作、以及面向 AI cluster 的管理层产品。

如果把这套策略抽象一下，会发现 Cisco 的真正筹码不在单点性能，而在异构整合能力。今天 AI 网络的难点早就不只是 box 和 box 之间能不能连起来，而是当你有成百上千 GPU、不同层级交换机、前后端网络、存储网络、跨数据中心互联和海量光模块时，谁来提供“一个可被理解、可被运维、可被 debug 的整体系统”。这也是 Eatherton 反复强调 manageability 的原因：对 hyperscaler 来说，也许自己能搞；但对 sovereign cloud 和高端 enterprise 而言，这个管理复杂度本身就是一个巨大门槛。

我觉得文章里最有价值的判断之一，是 Cisco 与 NVIDIA 的关系。表面看，这像是 Cisco 在向 NVIDIA 生态妥协；更深一层看，它其实是在用“可兼容 + 可替代”的方式争取存在感。通过在 NVIDIA 生态内提供互通能力，Cisco 试图让客户不必在 Broadcom、Cisco、NVIDIA 三套完全不同架构之间做单选题，而是能保留供应链与架构上的灵活性。这种“choice as strategy”非常 Cisco，也很符合今天 AI 基建里的现实需求。

另一个值得你记住的点，是网络正在从芯片竞争慢慢变成系统竞争。尤其一旦进入 CPO（co-packaged optics）时代，网络设备会更像高集成度系统而不是可随意拆换的模块。这对 Cisco 反而是机会，因为系统设计、服务ability、跨层软件集成，本来就是它比纯硅片厂更擅长的地方。

## 对你（行动层面）的启发
如果把这篇放进你的研究框架，很适合转成一个产业判断问题：**在 AI 数据中心里，未来最值钱的是“最快的器件”，还是“让复杂系统可被运维的能力”？** 这个问题会直接影响你怎么看 Cisco、Broadcom、NVIDIA 甚至 HPE/Arista 这类公司。

对投资上也很有启发：不是所有赢家都会长得像 NVIDIA。很多二线甚至看似“掉队”的老牌厂商，未必能在 compute 上赢，但可能会在 manageability、光学系统、DCI/WAN、cluster-level control 这些相对不性感但黏性很高的环节重新建立地位。Cisco 更像是这一类。

## 一句话总结
Cisco 在 AI 数据中心的机会，不是再当一次唯一标准，而是把自己变成“复杂 AI 网络世界里最会把异构系统拧成一个整体的人”。
