---
title: "Supercookie: Browser Fingerprinting via Favicon (2021)"
date: 2025-11-19T08:43:10Z
category: reading
description: "浏览器的 favicon 缓存（F-Cache）是一个独立于普通缓存、Cookie、隐私模式之外的持久化数据库，网站可以通过\"哪些 favicon 路径被请求了、哪些没有\"构造出一个二进制指纹，精准追踪用户——清空浏览器历史、开无痕模式、用 VPN、装 AdBlocker 全部无效。"
source: "https://github.com/jonasstrehle/supercookie"
---

## TL;DR
浏览器的 favicon 缓存（F-Cache）是一个独立于普通缓存、Cookie、隐私模式之外的持久化数据库，网站可以通过"哪些 favicon 路径被请求了、哪些没有"构造出一个二进制指纹，精准追踪用户——清空浏览器历史、开无痕模式、用 VPN、装 AdBlocker 全部无效。

## 发现
Jonas Strehle 的 PoC 复现了 UIC 研究团队的论文：网站通过将用户重定向到一组子域名/路径，选择性地让某些 favicon 写入 F-Cache（返回有效图标）、某些不写入（返回无效内容），从而在浏览器端写入一个由缓存命中/缺失状态组成的二进制掩码。再次访问时，服务器观察哪些路径触发了 GET 请求，重建出同一个 ID。32 位掩码对应约 43 亿个唯一浏览器，重建耗时约 2 秒。

## 为什么重要
F-Cache 的隔离性不足是结构性问题：主流浏览器（Chrome、Safari、Edge）在隐私模式下共享同一个 favicon 数据库，且清空历史不会清空 F-Cache。Firefox 当时因自身缓存 bug（每次都重新请求 favicon）意外免疫——但研究者向 Mozilla 报告说：若 Firefox 修复该 bug 而不同步加防护，同样会沦陷。

## 破坏了什么常识
"清 Cookie + 隐私模式" 被普遍认为足以对抗会话间追踪，但 favicon 追踪证明：只要浏览器存在任何非用户可见的持久化存储，攻击面就存在。浏览器厂商的修复方案（隐私模式独立 F-Cache、随缓存清空 F-Cache）在 2021 年披露后仍经历了反复——Chrome 一度修复又回退。

## 追踪技术的军备竞赛边界
真正难防的追踪向量不在于"数据有多大"，而在于"存在感有多低"。Favicon 之所以危险，是因为它对用户完全不可见、对开发者工具默认也不突出——这才是长期潜伏的条件。
