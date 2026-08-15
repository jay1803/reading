---
title: "The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy"
date: 2026-06-08T08:01:29Z
category: reading
description: "智能电视是住宅代理网络的终极节点：Bright Data 的 SDK 以\"偶尔使用\"为由获取用户同意，实际配置的月流量上限却高达 200 GB；数据通道专门绑定物理网卡以绕过 VPN，整套协议安全性低于典型 C2 框架。"
source: "https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/"
---

## TL;DR
智能电视是住宅代理网络的终极节点：Bright Data 的 SDK 以"偶尔使用"为由获取用户同意，实际配置的月流量上限却高达 200 GB；数据通道专门绑定物理网卡以绕过 VPN，整套协议安全性低于典型 C2 框架。

## 核心洞见
Bright Data 是目前最大的合法住宅代理网络（自称 150M+ IP），向 AI 公司等客户出售住宅 IP 出口，用于绕过 Cloudflare/DataDome 对数据中心 IP 的封锁。SDK 以"免费使用 app、偶尔贡献资源"的同意模式嵌入合作方 app，包括多款 Roku/CTV 平台应用（PlayWorks 覆盖数亿家庭）。智能电视比手机更优越：全天候联网、不断电、无人看管、无 MDM/EDR，是完美的代理节点。

## 具体机制
SDK 启动时无认证地拉取服务端配置（含带宽上限、空闲阈值、合作方列表），随后向 AWS 上的 WebSocket 服务器建立持久连接（TLS 证书 CN 仍用 2018 年更名前的旧品牌 Luminati）。服务器下发 =cmd_tun= 指令后，SDK 以用户住宅 IP 代理执行目标网站的 HTTP 抓取，全程传输明文 JSON，无消息签名、无客户端证书、无设备验证。"空闲"判定包含 =ignore_screen_on: true= 和 =ignore_on_call: true=，即用户正在看屏幕或打电话时仍可被用作代理节点。服务端配置还内置跨平台身份绑定，将同一品牌的 iOS/Windows/macOS 安装映射为同一实体。

## 隐藏限制（两层检测逃逸）
控制面用 =CFHTTPMessage= 而非 =URLSession= 构建 HTTP 请求，规避 URLSession 级插桩工具；数据面用 =NWConnection= 绑定物理网卡（=use_netifs: true=），直接跳过 VPN 的 tun0 接口。两种绕过均调用 Apple 公开 API，但组合效果是：任何单一检测技术（URLSession hook 或 VPN 流量审计）都只能看到 SDK 行为的一半。

## 防御
最简单的方法：在路由器 DNS 屏蔽 =proxyjs.brdtnet.com=、=proxyjs.luminatinet.com=、=clientsdk.bright-sdk.com= 等域名，不影响 Bright Data 客户侧合规流量。企业可通过 TLS SNI 过滤 =*.brdtnet.com=。移动设备管理可检测 app 二进制中 =BrdWebSocketFacade= 和 =BrdNetwork.DNSResolver= 符号来禁止相关 app 上设备。

法律"同意"文本掩盖的是技术层面的主动逃逸设计——SDK 不是被动地利用用户资源，而是专门工程化地绕开可见性工具。
