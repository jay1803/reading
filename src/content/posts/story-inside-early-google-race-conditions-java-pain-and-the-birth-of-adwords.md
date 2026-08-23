---
title: "Story: Inside Early Google - Race Conditions, Java Pain, and the Birth of AdWords"
date: 2026-03-27T08:01:05Z
category: reading
author: "Adam Gordon Bell"
description: "Ron Garrett（笔名 Erann Gat），前 NASA/JPL Lisp 研究员，曾主导将 Lisp 用于行星探测器自主控制系统（CoRecursive 第 76 集\"Lisp in Space\"主角）。2000 年以第约 100 号员工身份加入 Google，被指派构建 AdWords，一年后离职重返..."
source: "https://corecursive.com/inside-early-google/"
---

## 嘉宾背景
Ron Garrett（笔名 Erann Gat），前 NASA/JPL Lisp 研究员，曾主导将 Lisp 用于行星探测器自主控制系统（CoRecursive 第 76 集"Lisp in Space"主角）。2000 年以第约 100 号员工身份加入 Google，被指派构建 AdWords，一年后离职重返 JPL，获晋升为 principal。主持人 Adam Gordon Bell，CoRecursive 播客创始人。

## TL;DR
一个从未写过生产系统的 Lisp 研究员，在憎恨 Java 的前提下用 Java 建成了 Google 赖以生存的商业基础设施——而他全程觉得自己在搞砸，公司却从未真正训斥过他。

## Java 就是把程序员变成零件，但他不得不用它
Ron 来 Google 的部分动力恰恰是 Google 不用 Java；到岗第一天 VP Urs Hölzle 就指定让他用 Java 写 AdWords，还要他做公司"Java 传道者"。他对 Java 的核心批判不是细节，而是："它被设计用来把程序员变成可替换零件"——而设计者里甚至包括 Common Lisp 的设计者 Guy Steele，这让他更加无法接受。实际代码主体由同组的 Jeremy Chow 完成；Ron 还要同时处理没有语法高亮的 JSP 调试——错误信息绵延数页，真正的 typo 往往在报错点数十行之前。

## 从没写过生产系统的研究员被扔进三个月 deadline
Ron 整个职业生涯的模式：钻研某个领域，让它勉强跑起来，交给别人，发 paper——从未"收尾"过。Google 把他丢进一个从未经历过的场景：同时学习生产系统开发并按期交付，还设了三个月 deadline。他的结论是管理失误的教科书案例——"学习和交付不能同时进行"。他甚至主动提出辞职，Google 说他没有自己以为的那么糟，把他留了下来。

## Larry Page 押注"先上线，后审查"
AdWords 上线策略的核心争议：广告是否要人工审查后才能生效？Larry Page 的态度是："有问题了再说，先给客户即时看到效果。"Ron 来自 NASA，本能是先验证再飞；他明确问过 Larry 如果 NAMBLA 或新纳粹买广告怎么办，Larry 直接略过。事后 Ron 承认这个决策是正确的——AdWords 是业界第一个实现广告即时生效的平台，这对其早期成功贡献不小。

## Billing Disaster：析构函数竞态，有人收到百万账单
系统上线后不久，Billing 系统向部分客户发出了数万乃至数百万美元的账单请求。根因是 C++ ad server 在关闭时，两个析构函数存在竞态：一个先释放内存，另一个从那块内存读取"残余广告数量"写入 MySQL，写入的是随机数——MySQL 本身完好，但数据是垃圾。大多数天价账单因超信用额度被银行拒绝，但少数通过了。Ron 花了数天手动退款、修复双式记账账本，并亲手给受影响客户写道歉信——作为早期唯一工程师，他同时是开发、运维和客服。

## 一年换来了有遮蔽的停车位
Ron 离开 Google 后重返 JPL，条件是晋升为 principal（相当于大学终身教职），获得 JPL 最稀缺的福利：有遮蔽的室内停车位。JPL 有约 7000 名员工，此类车位不到 100 个。他重返后的第一个任务：为 JPL 采购 Google 出售的企业级搜索硬件——终于算是"参与了"Google 的搜索引擎。

## 留下的那个想法
AdWords 的第一个付费客户 Lively Lobsters 后来倒闭了，但原因是老板转行做 AdWords 咨询，成了百万富翁。Ron 建了这套系统，全程觉得自己在出错，最终拿着股票期权离开，用这段经历换了个停车位。两个人都从 AdWords 的第一单里得到了意外结局，只是方向完全不同。
