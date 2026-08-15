---
title: "'Popa' Botnet Linked to Publicly-Traded Israeli Firm"
date: 2026-06-19T08:02:21Z
category: reading
description: "研究人员已确认 Popa 流量直接进入 NetNut 的代理池，而非仅仅\"与之关联\"。Synthient 的分析显示，Popa SDK 发出的出站流量明确标识为 NetNut 客户端流量——\"无疑问\"。NetNut 的母公司 Alarum Technologies 在纳斯达克上市（ALAR），将自身定位为 AI..."
source: "https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/"
---

### Popa 僵尸网络是 NetNut 代理基础设施的直接来源，而非"关联"

研究人员已确认 Popa 流量直接进入 NetNut 的代理池，而非仅仅"与之关联"。Synthient 的分析显示，Popa SDK 发出的出站流量明确标识为 NetNut 客户端流量——"无疑问"。NetNut 的母公司 Alarum Technologies 在纳斯达克上市（ALAR），将自身定位为 AI 训练数据抓取基础设施的商业代理服务商。

### 溯源链条

Popa 是 Vo1d 僵尸网络的插件组件，Vo1d 专门感染非官方 Android TV 盒子。2025 年 7 月 Badbox 2.0 被联合打压后，Popa 立即注册了一批新控制域名——其中包括 ninjatech[.]io。该域名归属 Moishi Kramer，其 LinkedIn 显示他是 NetNut 的研发副总裁，并在 NetNut 被 Alarum 收购前"从零搭建"了该公司架构。Kramer 否认掌控该基础设施，称 Popa SDK 在五年前已售给第三方。但 Nokia Deepfield 独立追踪到 359 个已知中继节点中的 26 个，仅这 26 个节点在 24 小时内处理了 75 万个唯一 IP 来源。

### 规模与危险性的核心不在大，而在散

Lumen/Black Lotus Labs 估计 Popa 每日活跃 IP 在 150 万至 250 万之间，远小于此前的 IPIDEA（高峰时近 1000 万）。但其危险性来源于散布：NetNut 被大量代理服务商转售，因此 Popa 的 IP 出现在生态系统中的无数服务里，一旦封堵需要跨服务协同。

### "同意"机制是虚构的

Alarum 声称强调"适当的通知与同意机制"。Synthient 分析的 20 余个真实 Popa 发布者，没有一个向用户请求同意。最新版本虽加入了请求同意的能力，但几乎没有实际使用。Spur 发现 NetNut 的 KYC 声明是营销话术：任何人用一个匿名邮件加 5 美元加密货币即可通过转售商购买访问权限。

### AI 抓取经济是整个生态的驱动力

Popa、Vo1d、IPIDEA 等僵尸代理网络并非因传统网络犯罪而存在，其主要客户是 AI 训练数据抓取。代理商明确将自身产品定位为"AI 抓取基础设施"。Spur 扫描显示：LG webOS 应用商店 42% 的应用、三星 Tizen 超过 25% 的应用内嵌代理 SDK。用户在电视上用遥控器滚动隐私条款、点击同意按钮，实质上是在把家庭 IP 永久出借给 AI 公司的抓取任务。

### 影响范围超出电视

Infoblox 发现其客户群中 65% 在查询一个或多个住宅代理相关域名，每月相关查询超 5000 亿次。90% 以上的制药和食品饮料客户、60% 以上的政府和银行客户已有查询记录。代理节点出现在企业内网后，如果被滥用于攻击第三方，事故溯源会指向该企业的 IP——法律暴露和声誉损失由受害企业承担。
