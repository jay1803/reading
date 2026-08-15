---
title: "No right to relicense this project"
date: 2026-03-06T08:53:42Z
category: reading
description: "chardet 原作者 Mark Pilgrim 现身：v7.0.0 的\"完整重写\"声明不构成合法换证依据——接触过原始 LGPL 代码即不满足清洁室条件，再授权无效。"
source: "https://github.com/chardet/chardet/issues/327"
---

## TL;DR
chardet 原作者 Mark Pilgrim 现身：v7.0.0 的"完整重写"声明不构成合法换证依据——接触过原始 LGPL 代码即不满足清洁室条件，再授权无效。

## 关键时刻
chardet 7.0.0 在声称"完整重写"后将许可证从 LGPL 切换；Pilgrim 以原作者身份在 GitHub issue 直接反对，要求回退到原始 LGPL。

## 背后逻辑
LGPL 传染性条款：衍生作品必须继承同一许可证。合法绕过的唯一路径是"清洁室实现"（完全隔离、零接触原始代码）。维护者对原始代码有充分接触记录，引入代码生成器也不改变这一法律事实。

## 更大意义
若"声称重写就能换证"的逻辑被接受，Copyleft 的核心保护机制将形同虚设——任何 LGPL/GPL 项目都可通过"重写"声明脱离 copyleft 约束。Pilgrim 此次公开反对，本身是在测试开源许可证的实际可执行性。

**证据薄弱处**：Pilgrim 的断言建立在"维护者有充分原始代码接触"上，但未提供具体代码对比或独立性分析——若维护者能证明新代码在实质上独立，争议可能更复杂。
