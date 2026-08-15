---
title: "Google 與聯發科深化 TPU v9 合作，開發升級版 Triggerfish，聚焦 AI 代理、強化學習與有效算力最大化"
date: 2026-06-23T08:02:03Z
category: reading
description: "郭明錤最新調查指出，Google 正在 Humufish（TPU v9）基礎上開發代號 Triggerfish 的升級版晶片，訂單仍由聯發科獨家承接，進一步確立聯發科在 TPU v9 世代的首選夥伴地位。"
source: "https://medium.com/@mingchikuo/google-%E8%88%87%E8%81%AF%E7%99%BC%E7%A7%91%E6%B7%B1%E5%8C%96-tpu-v9-%E5%90%88%E4%BD%9C-%E9%96%8B%E7%99%BC%E5%8D%87%E7%B4%9A%E7%89%88-triggerfish-%E8%81%9A%E7%84%A6-ai-%E4%BB%A3%E7%90%86-%E5%BC%B7%E5%8C%96%E5%AD%B8%E7%BF%92%E8%88%87%E6%9C%89%E6%95%88%E7%AE%97%E5%8A%9B%E6%9C%80%E5%A4%A7%E5%8C%96-3f68c6e6d13d?source=rss-d19afb905185------2"
---

## Triggerfish：Google 為 AI 代理與強化學習專門升級的 TPU v9

郭明錤最新調查指出，Google 正在 Humufish（TPU v9）基礎上開發代號 Triggerfish 的升級版晶片，訂單仍由聯發科獨家承接，進一步確立聯發科在 TPU v9 世代的首選夥伴地位。

## 核心架構差異

Triggerfish 相比 Humufish 的三項主要升級：
- SRAM 容量提升至 Humufish 的 2–3 倍
- 新增 simulation die（專責本地 TPU 管理與訓練/推論模式切換）
- 記憶體由 HBM4 升級至 HBM4E

SRAM 大幅擴容的直接邏輯：強化學習與 AI 代理所需的活躍工作集（active working set）更大；將這些資料留在 TPU 本地，減少跨晶片搬移，可在超低延遲 decode 階段取得顯著效率提升。

## 設計取向的信號意義

simulation die 的加入，除了 TPU 管理功能外，明確聚焦於 RL 與 AI 代理協作——這意味著 Google 已將代理工作負載視為獨立的硬體設計約束，而非只在軟體層處理。Triggerfish 被定位為「可同時緩解 CPU wall 與 memory wall」的改版：兩個瓶頸共存是當前推論工作負載的典型特徵，尤其在多步驟代理任務中。

## 商業意義

Humufish 400–500 萬顆出貨預估不變，Google 額外加訂 100–200 萬顆 Triggerfish，預計 2027 年底投產、2028 年放量；Triggerfish 單價比 Humufish 高約 30%，將成為聯發科 2028 年的新增量動力。
