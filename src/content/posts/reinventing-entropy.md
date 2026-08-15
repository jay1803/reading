---
title: "Reinventing Entropy"
date: 2026-06-08T08:01:29Z
category: reading
description: "cross-entropy 作为 LLM 训练损失只是一行代码，但\"为何它是有原则的损失函数\"这个问题的答案，要求重新推导 Shannon 信息论全貌——\"压缩即智能\"是把这条线索从一个视频拉成三部曲的引力核心。"
source: "https://3blue1brown.substack.com/p/reinventing-entropy"
---

## TL;DR
cross-entropy 作为 LLM 训练损失只是一行代码，但"为何它是有原则的损失函数"这个问题的答案，要求重新推导 Shannon 信息论全貌——"压缩即智能"是把这条线索从一个视频拉成三部曲的引力核心。

## 背景与起源
Grant 最初只计划做一个关于 cross-entropy 的视频，解释它为何用于语言模型预训练。两个月后演变成信息论基础的三部曲，原因在于：cross-entropy 的起源是压缩理论，而不是统计学习。沿着压缩这条线追下去，就无法回避"compression is intelligence"这个命题。

## 核心洞见
cross-entropy 的机制层面极简——预训练损失就是一行代码——但理解它**为何**是正确的损失函数，等价于理解 Shannon 如何从第一性原理推导出熵的公式。两者本质上是同一条数学线索在不同时代的两个断面。

## 第一部分的论点结构
本集以"让观众重新发现 Shannon 无噪信道编码定理"为结构目标：从信息量和熵的公式**从何而来**出发，而非从定义直接灌输。这是 Grant 信息论系列的入场角度。

## 收束
"压缩即智能"在这里不是修辞——它是 Shannon 1948年编码定理与现代 LLM 交叉熵损失函数之间的同一条数学结构的两端。
