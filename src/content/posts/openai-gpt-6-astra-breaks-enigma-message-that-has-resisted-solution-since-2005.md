---
title: "OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005"
date: 2026-10-01T08:59:57Z
category: reading
description: "GPT–6 Astra 自主破解了自 2005 年以来未解开的 Enigma 电报 MVUEH，结合密文校勘、软件开发与档案追踪，两天内完成人类研究者需数周甚至数月的工作。"
source: "https://www.cryptocellar.org/bgac/the-mvueh-break.html"
author: "sohkamyung"
---

GPT–6 Astra 在两天内自主破解了自 2005 年以来始终未被解开的 Enigma 电报 MVUEH，并把密码分析推进到密文校勘、软件开发与档案追踪相结合的研究过程。2026 年 9 月 15 日，Carter Leffer 将破解结果交给 Crypto Cellar Research 的研究者验证，对方确认密钥和明文正确。这封电报发送于 1941 年 7 月 10 日，由战术呼号为 2ny 的电台发出，SS-Totenkopf 的 Quartiermeister（Ib）电台于当天 17:30 收到，将其登记为第 172 号来电。

MVUEH 长期难以破解，与同日其他电报提供的密钥线索失效有关。2017 年 6 月 9 日，Alex Shovkoplyas 已破解相邻的第 173 号电报 SIPVX；它的转子排列与当天通用密钥相同，均为 512，但插线板连接（Stecker）和环位设置（Ringstellung）略有差异。研究者用这个新密钥仍无法解开 MVUEH。此次结果显示，MVUEH 使用了另一套完全不同的密钥，连转子排列都变成了 253。

密钥差异很大，两封电报的明文却几乎相同。MVUEH 长度为 82 个字母，SIPVX 为 94 个字母；长度差异来自 MVUEH 将 Bitte 错误加密成 Btte，以及 SIPVX 重复了一次发送者署名 Waschbusch。破解还揭示，研究者从原始电报表格抄录的 MVUEH 密文存在数处错误，Enigma 的左侧转子在第 72 个字母处发生了进位。左侧转子进位较少出现，会增加破解难度；密文抄录错误与这一机械细节共同构成了此前破解失败的可能原因。

Carter Leffer 给 GPT–6 Astra 的任务仅是尝试破解 Crypto Cellar Research 网站上尚未解开的 Enigma 电报，目标选择和具体研究路径均由模型自行完成。它分析候选电报后，选中了第 172 号 MVUEH，并很快怀疑其明文与已破解的 SIPVX 有关。经过多种方法的尝试，它最终把重复出现的地名 **ROSENOW ROSENOW** 作为 crib，即用于约束密钥搜索的猜测明文；随后自行编写 Python 和 C++ 软件，实现 Enigma 模拟器与 Enigma Bombe 搜索工具，围绕这条线索展开系统搜索，找到了正确密钥和明文。已破解电报中的重复地名，为另一套密钥下的未知电报提供了可利用的内容关联。

模型还追踪了网站之外的档案线索。研究者在 2026 年 7 月曾公告，German Bundesarchiv 保存了 SS-Totenkopf Division 后勤指挥部门 Nachschubführer 的电报集，其中不少发往 Ib，与网站已有电报相同，另一些则可能相关；新增记录以粗体及 NF 标记区分，NF 编号属于后勤部门自己的发报序列。GPT–6 Astra 的日志显示，它沿接收电报集的来源追踪到一个私人收藏，并找到了 RS 3–3/20a 和 RS 3–3/63b 两组 Bundesarchiv 档案编号。研究者确认这两个编号正确，且网站并未提供它们；他本人此前曾花数周研究这些档案。

这部分档案探索的成果有明确边界：日志记录模型已检查目录条目，但尚未定位第 172 号收报的原始图像，当前环境中的档案浏览器也未展示相关扫描件，且没有向任何人发送询问信函。研究者仍在分析运行日志，尚不清楚模型所指的私人收藏是什么，也未确认它是否访问过 Bundesarchiv 的数字化馆藏，或从其他渠道找到档案编号。已经得到验证的是密钥与明文的破解；档案访问路径和完整执行过程仍待厘清。此次突破展示了一个具体的研究能力组合：从历史材料中识别关联，用程序检验密码假设，并通过破解结果发现原始数据中的错误。
