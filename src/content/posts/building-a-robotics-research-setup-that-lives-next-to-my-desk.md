---
title: "Building a robotics research setup that lives next to my desk"
date: 2026-06-21T08:01:16Z
category: reading
description: "作者曾在 OpenAI 机器人团队工作（2017–2020），彼时同等能力的桌面操控设置需要约 20 人团队、硬件成本是现在的 10 倍以上。文章的核心命题：2026 年，一个人靠一张桌子能走多远。物理设置总成本 €4,569.80（不含计算资源），核心硬件是 UFACTORY xArm Lite 6（€3,40..."
source: "https://dfdxlabs.com/research/2026/robotics-setup/"
---

## 个人机器人研究的可行性门槛已下降一个数量级

作者曾在 OpenAI 机器人团队工作（2017–2020），彼时同等能力的桌面操控设置需要约 20 人团队、硬件成本是现在的 10 倍以上。文章的核心命题：2026 年，一个人靠一张桌子能走多远。物理设置总成本 €4,569.80（不含计算资源），核心硬件是 UFACTORY xArm Lite 6（€3,403）+ Intel RealSense D405 腕部深度相机（€302）+ Logitech C920 静态相机（€47）+ 3Dconnexion SpaceMouse 遥操器（€174）。从拆箱到首次运行约需 30 分钟。

## 几个不显然的设计决策

**刻意不校准相机外参/内参。** 桌面、相机位置、光照会随时间漂移；维护一套随环境变化的标定参数得不偿失。作者的问题本身就是：原始图像观测能走多远——跳过标定是研究变量，不是懒惰。

**不建立在 ROS 2 或 LeRobot 的抽象层之上。** 训练和基线策略仍使用 LeRobot，但控制层从头写（~3000 行 Python）。理由：控制频率、观测延迟、执行行为全都塑造学习问题本身；只有精确知道"从相机帧到电机指令之间发生了什么"，才能在策略层面真正诊断问题。"全栈理解比全栈控制更重要。"

**动作空间约束到 4 自由度（x/y/z 平移 + yaw）。** Roll/pitch 被锁定，夹爪保持平行桌面。归一化增量 [−1,1] 作为统一接口——遥操演示与策略推理使用完全相同的动作空间，从根本上消除 train/inference mismatch。

**Fail-loud 架构。** 任何 service 崩溃立即终止整个 session 并停止机器人，而非在缺失相机流的情况下继续运行。

## 软件架构

单进程 Python，内存内 pub/sub 事件总线。Service 分 ScheduledService（固定频率，追踪 missed tick）和 PollingService（设备阻塞驱动，如相机帧）两种。Event 携带三个时间戳：单调时钟、挂钟时间、可选硬件时间戳（RealSense 直接报告采集时刻）。录制使用 Rerun .rrd 格式，原生帧率存储；RGB JPEG Q90、深度 16-bit PNG 无损，录制吞吐约 1.4 GB/min。训练时通过转换脚本重采样为固定帧率的 LeRobot v3 数据集，原始录制保留以备未来用不同对齐策略重新派生。策略推理计划迁移到 DGX Spark，通过 WebSocket + msgpack 与机器人进程通信，使观测/动作接口显式化。

## 下一步研究问题

收集 50–100 条简单任务演示，训练 ACT / Diffusion Policy 基线；零样本部署 π0.5 和 SmolVLA。核心研究问题：从头训练 vs. fine-tune VLA 的效果差异、不同任务所需演示数量、Diffusion vs. normalizing-flow 策略模型、RGB vs. RGB-D 在光照/背景变化下的泛化差异，以及单策略是否能覆盖多个桌面任务。
