---
title: "An Interview with Google Cloud Platform CEO Thomas Kurian About Building an Enterprise Culture"
date: 2025-05-06T16:12:01Z
category: reading
author: "Ben Thompson"
description: "Thomas Kurian，Google Cloud CEO，2018 年加入 Google 领导云业务；此前在 Oracle 工作 22 年，担任产品开发总裁。采访者 Ben Thompson 是 Stratechery 主理人，本次是两人第三次对话，背景是 Google Cloud Next 2025 大会前夕。"
source: "https://stratechery.com/2025/an-interview-with-google-cloud-platform-ceo-thomas-kurian-about-building-an-enterprise-culture/"
---

## 嘉宾背景
Thomas Kurian，Google Cloud CEO，2018 年加入 Google 领导云业务；此前在 Oracle 工作 22 年，担任产品开发总裁。采访者 Ben Thompson 是 Stratechery 主理人，本次是两人第三次对话，背景是 Google Cloud Next 2025 大会前夕。

## TL;DR
Google Cloud 真正的护城河不是模型，而是将 Google 内部工程文化从"自建一切"改造成"接受企业异构现实"的组织变革——这比任何单项技术都更难复制，Wiz 的收购正是这种变革已经完成的证明。

## 基础设施不是背景，是差异化本身
Kurian 的核心主张：推理成本直接进入产品 COGS，延迟 / 可靠性 / 可扩展性都需与基础设施协同优化（co-optimize）。他举的案例——金融服务客户做实时欺诈检测，推理速度决定了可以扫描多大的数据面，进而影响准确率——说明基础设施能力和模型能力之间是乘法关系，而不是加法关系。此次发布的 TPU Ironwood v7 / 13 种 GPU 规格 / Cloud WAN，覆盖从训练到分布式推理的全栈，且 Google 将模型与基础设施联合调优，这是其他云提供商难以单独复制的集成优势。

## 多云承诺是走向统一控制点的桥梁
Kurian 2019 年提出多云时，90% 的企业还在用单一云（且不是 Google）；今天 85% 以上企业用至少两个云，BigQuery 已成最大数据云（比第二大大 4 倍，90% 用户从 AWS/Azure 迁数据过来）。600+ 连接器（Salesforce、ServiceNow、Microsoft Office、Workday 等）让 AI agent 能访问企业现有系统数据，同时维持原有权限模型。Agent2Agent（A2A）开放协议 + 开源 ADK（60+ 合作伙伴）让 Google agents 能与第三方 agents 直接互操作。落点是 Agentspace：统一的企业 AI 入口，而不是要求企业把数据都搬到 Google。

## 内部文化变革比技术发布更难——但已经完成
Kurian 坦承这花了"几年时间"。关键路径：每次向企业需求妥协（BigQuery 联邦查询、AlloyDB 多云部署）都被证明带来了更多客户，工程师信任因此逐步建立。Wiz 收购是这种信任的产物——Google 内部已能接受"某些场景买比建更好"。Wiz 补全了三层自建安全栈：威胁情报（Mandiant）→ 企业系统分析与修复（Security Operations）→ 云配置与供应链审计（Wiz）。三层打通后，Google 提供从攻击面发现到修复验证的全链路安全，且支持多云 / 本地混合环境。

## 供给，不是需求，是增长瓶颈
Google Cloud 上季增速 35%，Kurian 明确承认是 GPU 容量不足拖累增长，而非需求疲软。飞轮已在转动：Gemini 模型 ready 到客户可用仅需 6 小时；Gemini Code Assist 免费版 3 天从零涨到 10 万用户，C 端曝光直接转化为 B 端模型改进反馈。

## 留下的那个想法
Google Cloud 是 Google 唯一不会"自我蚕食"的 AI 分发渠道——消费端承压于监管和广告模式争议，而企业云恰好是 Google 可以无顾虑地把所有 AI 能力全押的地方。这个结构性优势，或许比任何单项技术领先都更持久。
