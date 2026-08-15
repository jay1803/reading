---
title: "LotusNotes"
date: 2026-03-24T08:01:26Z
category: reading
description: "Lotus Notes 不是从 email 文化进化出来的，而是 PLATO（1970 年代军事资助的大学教学计算机）的精神续作——其\"公开优先\"社区逻辑、数据库复制架构、\"万物皆笔记\"设计，全部直接来自 PLATO 的 =notes= 功能，而非当时任何一个主流商业软件的传承。"
source: "https://computer.rip/2026-03-14-lotusnotes.html"
---

## TL;DR
Lotus Notes 不是从 email 文化进化出来的，而是 PLATO（1970 年代军事资助的大学教学计算机）的精神续作——其"公开优先"社区逻辑、数据库复制架构、"万物皆笔记"设计，全部直接来自 PLATO 的 =notes= 功能，而非当时任何一个主流商业软件的传承。

## 关键时刻
PLATO 1950 年代末诞生于伊利诺伊大学，源自军方对技术教学的资助。1972 年，两名高中生用暑假时间写出 =notes= 模块：最初是系统公告板，迅速成为全平台最受欢迎的应用，比早期电子游戏还流行。关键细节：公开留言功能比私信功能早一年出现，"先公开后私信"的次序塑造了 PLATO 整体的"公开优先"文化，Brian Dear 认为这直接预示了后来的 BBS 和社交网络。

Ray Ozzie 本科期间深度参与 PLATO，1984 年离开 Lotus 创立 Iris Associates，专门受 Lotus 资助把 PLATO 的 =notes= 移植到 Windows PC 网络。五年后，这个产品以 Lotus Notes 的名字发布。

## 背后逻辑
Notes 架构直接继承 PLATO 的终端-大型机模型：数据以"笔记数据库"存储，通过服务器间复制同步，而非单一中央服务器——这在各地办公室靠昂贵专线连接的年代极合理（断网时本地仍运作，联网再同步）。"万物皆笔记"让 Notes 同时是 email、日历、工作流平台、RAD 开发环境，用户可在其上构建完整企业应用。IBM 1995 年以 35 亿美元收购 Lotus，认为其瘦客户端/厚后端架构契合 IBM 的主机传统。

IBM 随后将 Notes 全面 Java 化，2008 年客户端完全替换为基于 Eclipse 的实现。同年推出的 XPages 试图提供 Web 界面，但与桌面端逻辑割裂——企业被迫同时维护两套 UI，"不如直接用 Sharepoint"的结论越来越容易得出。

## 更大意义
Notes 的衰落数据清晰：1995 年 64% 市场份额，1997 年 47%，2008 年 10%。三重夹击：Exchange 的 Windows 垂直整合、对 SMTP 开放标准的更快适配，以及 Notes 的身份危机——Forbes 1998 年写道，Notes 先后被定位为协作工具、应用开发平台、email 替代品，"你可以用它做任何事"在竞争激烈的时代变成了负面标签。2018 年 IBM 将 Notes 打包卖给印度 IT 公司 HCL，今天叫 HCL Notes，靠存量客户维持。

**证据薄弱处**：作者认为 PLATO "比 ARPANET/NSFNET 更重要地塑造了现代互联网"，论据是"氛围上的"（in a vibes way）而非技术传承——有趣但难以证伪。

## 遗留的一个念头
Notes 死于太通用、太难解释自己是什么——而它正是因为"什么都能做"才在 1980-90 年代如此强大。这个悖论在今天的 Notion、Obsidian、Emacs org-mode 身上还在重演；作者顺手把 Lotus Agenda（Notes 的先驱 PIM 产品）和 org-mode 相提并论，并非调侃，而是同一条遗传线还在延续。
