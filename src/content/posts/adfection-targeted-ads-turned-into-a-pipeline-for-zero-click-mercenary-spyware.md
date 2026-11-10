---
title: "AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware"
date: 2026-11-10T12:08:48Z
category: reading
description: "定向广告已经成为商业间谍软件的零点击感染通道：Citizen Lab 首次以公开技术证据确认，攻击者能够借助正常广告投放系统，在广告被加载时向选定设备植入 spyware，无需用户点击"
source: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
author: "jcomp"
---

定向广告已经成为商业间谍软件的零点击感染通道：Citizen Lab 首次以公开技术证据确认，攻击者能够借助正常广告投放系统，在广告被加载时向选定设备植入 spyware，无需用户点击。研究将这种攻击称为 **AdFection**，并确认 Al Jazeera 在 2024—2025 年遭到此类攻击，至少 45 台设备被列为目标，其中有设备感染了 Candiru、现更名为 Integrity Labs 的间谍软件。连接广告市场与攻击者的是以色列公司 Discover-Tech，其平台 Controlium 把用户识别、设备侦察和恶意代码投递整合成了可供多个监控厂商使用的服务。

这条攻击链依赖在线广告系统两项相互配合的能力。首先，**Real-Time Bidding（RTB）** 每天进行数千亿次实时竞价，网站与 App 为出售广告位，会向广告交易所和买方平台传递设备标识、IP 地址、位置、访问页面或所用 App 等信息；广告买方据此能够定位单个移动广告 ID、cookie ID 或 IP 地址。其次，广告可以携带 HTML 与 JavaScript，在浏览器或 App 内运行，并继续加载第三方代码。攻击者由此既能找到某个人，也能通过赢得其设备上的广告位，把代码送到这个人面前。广告数据原本已被用于 ADINT，即通过广告标识、位置和网络变化追踪人的活动；AdFection 又把这种侦察能力接入了设备入侵。

Discover-Tech 的关键设计是把真正的攻击决策推迟到广告展示之后。它投放的广告嵌入指向 **NOAS／getAd server** 的脚本，广告一经渲染，就把用户的广告标识等信息提交给 Discover-Tech，并执行服务器返回的 JavaScript。服务器根据 IP 地址与标识判断访问者是否符合目标条件：普通访问或扫描器可能只收到零字节响应，选定设备则收到后续代码；一些任务只返回一次，之后保持空响应，直到重新下达任务。即使没有进入感染流程，广告仍可回传浏览器数据，包括部分页面 cookie 与公开 IPv6 地址。这种按访问者动态分发的方式，也让广告平台难以在事前审核中看到恶意载荷。

Al Jazeera 提供的网络日志展示了实际感染的时间顺序：设备先接触 Discover-Tech 广告基础设施，随后连接 Candiru 的 validator server，接受初步检查，再进入后续画像与感染流程，最终连接 Candiru 的 Command and Control（C&C）服务器。研究者为验证服务器和 C&C 服务器分别建立了网络响应指纹；在 2022 年 8 月至 2026 年 7 月的历史扫描数据中，验证服务器指纹匹配到 305 个域名、319 个 IP，其中包含其他安全机构此前归因于 Candiru 的域名。Al Jazeera 还从受感染设备提取出 Windows DLL，其硬编码 C&C 地址与该指纹吻合。

恶意样本本身进一步巩固了归因。它与 Citizen Lab 在 2021 年获取的 Candiru 样本都使用 COM hijacking 实现持久化，都以 48 字节循环 XOR 密钥混淆字符串，并保留一种特殊的“虚假空终止符”处理方式；两者还按同样顺序访问 Google 与 Microsoft 网站检查网络连通性。基础设施、连接时序和这些实现细节共同支撑了研究者对 Candiru 的高置信度判断。不过，报告没有公开本轮攻击所用的完整漏洞利用链，也没有把所有广告接触都判定为感染。

Controlium 将这套能力产品化。客户可以按 Android 或 iOS 广告标识、MyDSP 或 Beeswax 浏览器标识，以及 IP 地址指定目标，也能批量上传受众，选择投放国家、网站或 App，并查看最近 30 分钟内的广告展示和竞价请求。管理者可以限制客户的投放频率、目标组合、每日或每月任务量，并为不同客户配置白标界面与访问权限。平台接入 Discover-Tech 自有 MyDSP，以及 Beeswax、Eskimi；MyDSP 又可使用 Google、Yandex 等广告渠道。界面还提供 Script、Monitor、Pixel、De-anon 等任务类型，但研究者没有确认其中每项功能的确切含义。

研究者通过登录页公开提供的前端代码重建了 Controlium 界面，并从无需认证的接口导出了 128 天登录日志，识别出 120 个不同用户名。他们还发现平台错误使用 Auth0：后端收到的“令牌”是用前端公开密钥加密的用户元数据，真正经过数字签名的 JWT 反而被弃用。报告判断这种设计可能允许伪造授权，但没有尝试绕过访问控制。公开代码、登录来源与基础设施交叉关系，使研究者得以追踪 Discover-Tech 与其他监控公司的联系，而无需进入受保护的客户业务数据。

Discover-Tech 与 Candiru 的合作还体现在一种防止攻击链被研究者截获的交接机制上。部分感染链接携带加密参数，可用 Discover-Tech 公开解码工具中的密钥还原为目标 IP；较新版本又包含时间戳、User-Agent 和广告 ID。研究者判断，攻击服务器可据此检查访问设备是否就是收到广告的原始目标，阻止别人将感染链接转移到分析环境。一条公开留存在 VirusTotal 的链接解密后指向 Saudi Ministry of Foreign Affairs 的 IP，构成该机构可能被针对的线索，不能单凭这一条链接确认其设备感染。

这套基础设施也被用于大规模侦察。研究者估计，2025 年有数十万至数百万用户经 Discover-Tech 广告被导向与 Candiru 有关联的服务器。2026 年 1—6 月间一个公开统计接口所覆盖的约五个月数据，又记录了 3,637,213 个符合 Infinite FIFO 代码投递条件的用户，但该功能可能同时被其他客户使用，因此不能将全部用户归入 Candiru，更不能将其全部视作感染者。Controlium 登录记录、服务器指纹和域名关联还指向 spyware 厂商 Bindecy，以及提供广告情报服务的 Intelos；这些证据说明 Discover-Tech 服务于多个监控参与方，各方合作的完整范围仍未查明。

另一名被命名为 **DARK CARTOGRAPHER** 的攻击者，则利用广告把移动广告 ID 与真实电话号码关联起来。其代码既尝试通过 WebRTC 暴露 VPN 或代理背后的 IP，也利用移动运营商“零点击登录”和 HTTP header enrichment 中的安全问题，取得用户的 MSISDN 电话号码。例如，运营商可能为特定明文 HTTP 请求追加包含号码的请求头，而目标网站匹配、白名单或第三方认证服务中的缺陷会导致号码泄露。研究者归纳出五类问题，涉及超过 30 个国家的运营商，并判断相关活动至少始于 2019 年。其基础设施同时关联商业广告技术厂商与一家美国政府承包商；具体技术和归因仍待漏洞披露完成后另行发表。

Discover-Tech 的覆盖规模由两个公开暴露的 Apache Druid 数据库揭示。2026 年 3—6 月，MyDSP 提交约 37.7 亿次竞价，赢得约 4.42 亿次，胜出率为 11.7%；76.7% 的竞价面向移动 App，23.3% 面向网页。按数据库成本单位为美元微单位的假设，该期间支出约 109,091 美元。竞价主要经 Yandex、Google Ad Manager 和 Vungle 进行，分别占 67.4%、24.74% 与 7.24%。这些记录不含其通过 Beeswax、Eskimi 进行的投放，也没有记录广告 ID、cookie ID 或 GPS 坐标，因此只能呈现业务的一部分。

在这些记录中，至少约 7.19 亿次竞价涉及名称显示可能含 NOAS 脚本的广告，占全部竞价约 19%。携带攻击者脚本的广告实际出现在 75,373 个 Android／iOS App 和 120,768 个网站上，竞价目标 IP 的地理定位覆盖 161 个国家。传播入口包括 MX Player、Viber、Truecaller、Duolingo、Yahoo Mail、VPN、经期记录和约会 App，也包括 Weather.com、Yahoo 及多个国家的新闻网站。广告内容常推广 Discover-Tech 关联的 Akedo、MyIPInfo、RemindMeWhere，或使用 AliExpress 商品促销图片。研究没有证据表明 Amazon、AliExpress 或 Ugreen 购买了这些广告；数据库大部分收入和利润字段为零，转化字段始终为零，也削弱了其作为普通广告生意的解释，但不能排除记录不完整。

广告还进入 NATO、United Nations、European Parliament、European Commission，以及多个国家的国防、外交、警务、网络安全和关键基础设施网络。北欧的记录涉及瑞典军方、电网运营商、Saab，挪威议会与警务机构，丹麦铁路、能源和数字基础设施企业；其他记录覆盖澳大利亚核研究机构，以及 Intel、Nvidia、ARM、Raytheon 等企业网络。**广告展示、被选为攻击目标和成功感染必须分开判断**：这些记录至少说明设备接触了 Discover-Tech 的画像基础设施，不能证明对应组织均遭 spyware 入侵。IP 地理定位也会受到 VPN、服务器和卫星网络影响，但敏感网络能够被正常广告交易触达，本身已构成需要调查的暴露面。

即使用户没有看到 Discover-Tech 广告，其浏览活动也可能进入该公司的身份关联系统。研究发现，Discover-Tech 通过 myweb3id、tracookiepixel 等域名与 Yandex、Beeswax 交换标识，并取得 Microsoft 广告平台 Xandr 的用户标识。这些请求会在大量网站访问中后台发生，向 Discover-Tech 传递用户 ID、IP、浏览器和操作系统信息。其追踪代码还能识别 GDPR 适用地区，并处理 IAB Europe 的 Transparency and Consent Framework（TCF）同意信号。跨厂商 ID syncing 由此为浏览器用户建立可关联身份，为后续个人级追踪和广告投递提供条件。

Discover-Tech 与监控行业的联系，在公开公司资料中已存在多年。公司于 2020 年成立后不久，Circles 联合创始人、Intelos 股东 Eric Banoun 进入董事会，直到 2025 年离任；股东还曾包括与管理 Intellexa 公司网络的 Sara Hamou 有关联的 Chaia Services。Discover-Tech 与 Intelos 的网站也曾多年共用同一个 Wix 发布账户，另有 Tekma、Akedo 等站点存在关联。其 MyDSP 广告技术则源于 Matomy，经过 Market Group／Glispa 后，于 2020 年转入 Discover-Tech 控制。对 Adtimizer、Volasim 等关联企业，报告明确区分了人员、域名或产品关联与知情参与攻击：两家公司均否认参与 spyware 活动，研究也没有得出其知情协助感染的结论。

尽管这些关系可以从公开资料查到，Discover-Tech 仍在 2020—2026 年间列于 Google 的多个认证或获准广告供应商名单，以及 IAB Europe 的 TCF Global Vendor List。这些资格使其能够稳定进入广告供应链、运行第三方代码、接收欧洲用户数据，并被纳入用户每天看到的同意弹窗。研究因此质疑以供应商自我声明为基础的行业认证：它为公司提供了可信外观，却没有阻止广告基础设施被用于监控。Eskimi 的回应也证实了审核难点：这些广告根据设备、IP 和位置返回不同代码，并采用极窄的 IP 目标列表，第三方扫描器因而看不到同一载荷。Eskimi 称其投放规模仅数百美元，最后一次活动已于 2026 年 8 月 6 日停止。

调查披露后，Google 于 2026 年 10 月初终止 Discover-Tech 的广告交易权限，并部署 Safe Browsing 防护；IAB Europe 于 10 月 8 日将其除名；Beeswax 移除了其账户，Vungle／Liftoff 暂停其访问，Eskimi 永久封锁相关账户与域名。这些处置切断了已识别公司的部分渠道，但报告将风险归结到更深层的广告架构：个人级识别、大规模共享竞价数据、层层嵌套的第三方代码，以及尽量减少人工介入的自动交易，共同形成了一条从海量侦察到精确入侵的供应链。

这种结合尤其威胁记者和消息源。广告情报能够暴露记者的行动、会面与报道方向，设备感染又能进入私人通信；对于在冲突地区工作的记者、协助者和消息源，后果包括人身危险。Citizen Lab 因此主张在行业证明能够可靠阻断此类攻击之前，组织应同时在网关和终端拦截广告与追踪，禁用或限制工作设备的广告标识，并检查广告展示前后的异常网络连接；高风险个人仍需专业取证与安全协助。监管层面则应调查 Discover-Tech 和 Candiru、执行现行隐私与安全法律，要求供应商 KYC、持续尽调和独立审计，并推动将个人数据移出 RTB 竞价。AdFection 暴露出的核心问题是：当一套商业系统同时允许购买“某个人的注意力”和在其设备上执行第三方代码时，广告投放权限就可能被转换成监控与入侵权限。
