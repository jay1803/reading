---
title: "The Coming Wave: Post-Quantum Cryptography and the Future of Cybersecurity"
date: 2025-10-10T00:35:07Z
category: reading
description: "\"Harvest now, decrypt later\" 攻击让量子威胁已经是当下问题——对手今天收集的加密数据，将在量子计算机成熟后被解密，迟迟不迁移到后量子密码（PQC）等于把现在的数据变成未来的数据泄露。"
source: "https://blog.publiccomps.com/the-coming-wave-post-quantum-cryptography-and-the-future-of-cybersecurity/"
---

## TL;DR
"Harvest now, decrypt later" 攻击让量子威胁已经是当下问题——对手今天收集的加密数据，将在量子计算机成熟后被解密，迟迟不迁移到后量子密码（PQC）等于把现在的数据变成未来的数据泄露。

## 核心主张拆解
RSA/ECC 的安全性依赖"经典计算机无法高效分解大整数/求离散对数"；量子计算机用 Shor 算法可在多项式时间内攻破两者——这是存在性破坏，不是渐进式退化。

NIST 2022 年 7 月已完成标准化：CRYSTALS-Kyber（密钥交换）与 CRYSTALS-Dilithium（数字签名）是两个主力算法，基于格密码学（lattice-based），目前没有已知有效的量子攻击路径。

PQC 胜过量子密钥分发（QKD）的核心原因：PQC 是纯软件实现，可作为现有系统的直接替换；QKD 需要专用量子硬件，且只能保护点对点信道，无法在互联网基础设施上规模化部署。

迁移代价实质性地高：PQC 算法的密钥尺寸和签名比经典算法大一至数倍，对带宽、内存和计算资源都有额外压力；Fortinet 等硬件厂商面临固件与硬件双重升级负担，而 CrowdStrike 等云原生架构可快速推送更新。

**值得质疑**：文章对 Palo Alto Networks、CrowdStrike"内部已在准备"的判断完全是推测，没有任何公开路线图支撑。文章以投资分析视角写成（Public Comps），市场机会的乐观预判与技术评估混杂，且未提及 CRYSTALS-Kyber 在 2022 年曾遭遇侧信道攻击（虽未动摇标准本身的安全性）。

## 边缘判断
量子威胁真正的倒计时不是"量子计算机何时建成"，而是"你的加密数据已经被对手收集了多久"。
