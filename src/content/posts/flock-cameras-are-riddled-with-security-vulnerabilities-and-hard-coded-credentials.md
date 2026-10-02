---
title: "Flock cameras are riddled with security vulnerabilities and hard-coded credentials"
date: 2026-10-02T03:51:39Z
category: reading
description: "一台在用的 Flock 车牌识别摄像头固件暴露长期缺失的安全更新、硬编码的凭据分发密钥，以及明文保存的后端认证凭据，风险延伸到 Flock 的生产基础设施。"
source: "https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/"
author: "Micah Lee"
---

一台在用的 Flock 车牌自动识别摄像头，其固件暴露出长期缺失的安全更新、硬编码的凭据分发密钥，以及明文保存的后端认证凭据；这些问题把路边监控设备的安全风险延伸到了 Flock 的生产基础设施。2026 年 9 月 16 日，DDoSecrets 发布了黑客集体 stegan0gram 从现场取得的摄像头中提取的文件系统镜像，404 Media 与 Wired 随后联合报道。Micah Lee 下载并分析这些镜像，发现设备的软件、持久化存储和日志共同提供了一条可追溯的证据链。

这台摄像头的固件构建于 2025 年 6 月 5 日，运行的却是 2017 年发布、2021 年结束 Google 支持的 Android 8.1，安全补丁级别仍停留在 2018 年 6 月 5 日。系统分区中的 build.prop 直接记录了这些版本信息。启动分区里的内核则是 2017 年发布的 Linux 3.18.71；3.18 系列维护到 2019 年 5 月，最终版本为 3.18.140，设备连这一早已停止维护的分支后续更新都没有跟上。*固件构建时间较新，并不意味着底层系统获得了相应的安全修复。*

这些版本信息指向具体的潜在提权路径。2021 年 5 月修复的 CVE-2021-1905 是 Qualcomm Adreno GPU 驱动的 use-after-free 漏洞，设备上运行的非特权应用也可能借此破坏内核内存并取得完整控制权；2018 年 12 月修复的 CVE-2018-9568，又称 WrongZone，涉及内核处理 IPv6 socket 时的类型混淆，可让本地程序提升到 root，且已有公开利用代码。Lee 没有实物设备，未验证这两项漏洞能否实际利用；已确认的是，摄像头包含相关组件，声明的补丁级别早于这两项修复。Flock 对联合调查的回应是，公司设有公开的漏洞披露流程，但未通过该流程收到报告，现有信息不足以评估指控，并要求研究者提交技术细节。

更直接的发现来自设备的认证机制。固件包含 20 个 Flock 应用，其中 19 个共享 com.flocksafety.android.common.lib，库中的 CameraSettings 类硬编码了一个 API key，因此同一密钥出现在这 19 个应用里。负责凭据配置的 flock-sambuca 会把这个密钥和摄像头的 MAC 地址提交给 hpnotiq.flocksafety.com 的凭据接口，获取用于认证的资料。Lee 据此提出，持有该共享密钥的人可能仅凭其他摄像头的 MAC 地址就能取得相应凭据，但他没有向服务器发起请求验证这一推断。

镜像中还存在这台摄像头的 Auth0 client ID 与 client secret，明文保存在 /persist 分区的 flock/auth0/auth0_cred 文件中；该分区没有加密，而且设计上会在恢复出厂设置后保留。Auth0 是 Okta 旗下的身份管理服务，摄像头使用这组凭据向 device-login.flocksafety.com 的 OAuth 接口申请短期 bearer token，再以设备身份访问 Flock 后端。由此形成的风险链条是：共享的硬编码密钥用于取得设备凭据，设备凭据又用于生成后端访问令牌。Lee 未测试泄露凭据是否仍然有效，并明确指出，未经授权使用它们连接 Flock 服务器属于违法行为。

设备日志进一步揭示了存储保护的局限，也让镜像能够对应到一台具体的路边摄像头。18 GB 的 media 分区包含一个加密容器，但解密密钥就存放在同一分区，取得镜像的人因此也取得了解锁材料。容器里的 crashpack 日志记录了 2,264 次对 hpnotiq 的调用，以及 155 次摄像头 GPS 位置；这些坐标集中在约 100 米范围内，Lee 将偏差解释为固定接收器的 GPS 漂移。最常出现的坐标是 43.10151313、-88.05270186，指向 Milwaukee 西北侧的 Wauwatosa。结合 Google Maps 和 Street View，他把设备定位到 Webster Park 附近 N Mayfair Rd 西侧、靠近公园停车场的一根灯杆上，并对应出序列号 23091220026 和 MAC 地址 F4:6A:DD:57:46:FB。

Lee 希望这些发现促使市议会取消与 Flock 及其他 ALPR 供应商的合同，停止以公众隐私为代价增加警方监控能力。这份分析直接检验的是一台摄像头的镜像，尚未证明所有 Flock 设备具有相同漏洞，也未证明泄露凭据仍能访问生产服务器；但它已经揭示了一个完整的安全责任问题：收集公众行踪的设备，在自身的软件维护、密钥管理和日志保护上同时留下缺口，使现场硬件的失守可能进一步牵动后端身份体系。
