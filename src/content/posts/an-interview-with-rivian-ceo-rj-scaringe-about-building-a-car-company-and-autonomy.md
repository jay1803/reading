---
title: "An Interview with Rivian CEO RJ Scaringe About Building a Car Company and Autonomy"
date: 2026-02-14T20:35:18Z
category: reading
author: "Ben Thompson"
description: "RJ Scaringe，Rivian 创始人兼 CEO。10 岁立志造车，MIT 机械工程 PhD（研究方向：ICE 效率优化，与 Rivian 无关），博士毕业次日正式创立 Rivian（2009 年）。本期由 Ben Thompson（Stratechery 创始人）主持，采访契机是 Rivian 发布 Au..."
source: "https://stratechery.com/2025/an-interview-with-rivian-ceo-rj-scaringe-about-building-a-car-company-and-autonomy/"
---

## 嘉宾背景
RJ Scaringe，Rivian 创始人兼 CEO。10 岁立志造车，MIT 机械工程 PhD（研究方向：ICE 效率优化，与 Rivian 无关），博士毕业次日正式创立 Rivian（2009 年）。本期由 Ben Thompson（Stratechery 创始人）主持，采访契机是 Rivian 发布 Autonomy & AI Day。

## TL;DR
Rivian 正在从汽车公司向自动驾驶平台公司转型——芯片、传感器、软件全栈自研，目标是把平台卖给其他车企，自己的车只是"狗粮"和数据飞轮。这条路径直接师法 Amazon AWS 的逻辑，而亚马逊恰好是 Rivian 的最大股东。

## PhD 是融资工具，不是学术追求
Scaringe 读 MIT 博士的动机是"最快获得信用"：26 岁拿到顶校 PhD 比工作 30 年更快让 VC 相信他。博士课题（均质压缩点火引擎）与 Rivian 毫无关系，但通过 MIT 校友网络获得了第一笔大额融资——策略完全奏效。他用房子再融资的 10 万美元启动了公司。

## 没有钱反而是运气
前几年融不到资，导致 Rivian 无法过早锁定错误方向。正是在"穷"的阶段，他从最初的运动跑车（太接近 Tesla）转到"探险"叙事，最终定义了 R1T/R1S 的产品逻辑——越野、储物、强悍耐用。他说如果当时有钱，可能早早造了错误的车。

## 同时发三款车是最大的战略失误
R1T、R1S 和亚马逊配送货车同期上市，叠加 COVID，让 Rivian 在最脆弱的时候面对三套供应链从零起步。供应商毫无顾忌地要求双倍价格，Rivian 没有谈判筹码只能接受。他明确说：如果重来，先发 SUV，间隔 12 个月发皮卡，再间隔 12 个月发货车。R2 已经严格执行这个逻辑，只做一个配置的 launch edition，R3 明确推迟。

## Gen 1 自动驾驶是完全的包袱
Gen 1（2021 年）基于 Mobileye 前置摄像头 + 规则引擎，与现在的端到端神经网络路线没有任何共享代码或硬件。Scaringe 明说：2020 年以前的所有自动驾驶技术积累基本都是 throwaway。Rivian 从 2021 年起从零重建 Gen 2（含 NVIDIA 芯片、新雷达、数据飞轮），Gen 2 车辆 2024 年中才上路采集数据，飞轮刚开始转。

## 每台量产车都是地面真值传感器
与 Tesla 视觉 only 不同，Rivian Gen 3（R2 及以后）每台量产车都搭载 LiDAR（900 英尺）和雷达。核心逻辑：LiDAR/雷达快速提供地面真值，加速训练摄像头，等摄像头足够强之后再降低传感器成本。Tesla 只有少数 ground truth 专车，Rivian 是全量产车队充当 ground truth。

## 自动驾驶平台是比汽车更大的生意
大众合作（$5.8B）只覆盖区域控制器 + 软件栈，自动驾驶平台完全自有。Scaringe 认为西方能做完整端到端自动驾驶平台的公司不超过 5 家，Rivian 要成为其中之一并向其他车企出售。他的判断：自动驾驶对汽车的重要性，很快会像电力对房子一样基础——不做这个优先级，市场份额就会流失。自研芯片（Gen 3：1600 sparse TOPS，专为视觉机器人优化）是打开平台售卖的关键。

## 留下的那个想法
Scaringe 说"自动驾驶和电动化其实是完全不相关的两件事，它们同时发生只是历史巧合"——但 Rivian 偏偏在两条线上都选择了最激进的垂直整合。如果它成功，证明的是：一个靠 10 万美元房贷起步、穷到迭代出品牌定位的小公司，有可能把最重的基础设施生意（汽车平台 + 自动驾驶平台）都做成——前提是有足够长的时间轴和不惧怕亏损的合作伙伴。
