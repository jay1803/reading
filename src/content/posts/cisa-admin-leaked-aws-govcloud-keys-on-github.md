---
title: "CISA Admin Leaked AWS GovCloud Keys on Github"
date: 2026-05-19T08:02:04Z
category: reading
description: "CISA 这次泄露最严重的地方不只是“有人把密钥传到了 GitHub”，而是一个承担国家网络安全职责的机构，在承包商日常工作流、凭据管理、代码供应链入口和泄露响应速度上同时暴露出系统性松动：高权限 GovCloud key、内部系统明文密码、构建环境信息都曾处在公开仓库里，且部分 AWS key 在被通报后仍继续..."
source: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
---

## TL;DR
CISA 这次泄露最严重的地方不只是“有人把密钥传到了 GitHub”，而是一个承担国家网络安全职责的机构，在承包商日常工作流、凭据管理、代码供应链入口和泄露响应速度上同时暴露出系统性松动：高权限 GovCloud key、内部系统明文密码、构建环境信息都曾处在公开仓库里，且部分 AWS key 在被通报后仍继续有效约 48 小时。

## 关键时刻
GitGuardian 研究员 Guillaume Valadon 在 2026 年 5 月 15 日联系 KrebsOnSecurity，因为一个名为 “Private-CISA” 的公开 GitHub 仓库长期暴露 CISA/DHS 相关秘密，仓库所有者此前没有响应自动告警。

这个仓库由 Nightwing 承包商维护，包含 AWS GovCloud 管理凭据、token、明文密码、日志、内部部署与测试文件，以及 CISA 软件构建流程相关资料。Seralys 创始人 Philippe Caturegli 验证称，泄露的 key 可高权限访问 3 个 AWS GovCloud 账户。

仓库在 KrebsOnSecurity 和 Seralys 通知 CISA 后下线，但 Caturegli 表示相关 AWS key 又保持有效约 48 小时。CISA 回应称正在调查，目前没有迹象显示敏感数据已因此被 compromise。

## 背后逻辑
这不是单点操作失误能完全解释的事故。文章给出的信号包括：提交记录显示操作者关闭了 GitHub 默认的 secret scanning 阻断设置；仓库里有 CSV 明文密码、备份文件和名为 “importantAWStokens” 的敏感文件；同一 GitHub 账户同时出现 CISA 关联邮箱和个人邮箱，像是在不同设备之间把仓库当同步盘或工作草稿区。

最危险的资产不是单个账号密码，而是内部软件供应链入口。Caturegli 特别指出，仓库暴露了 CISA 内部 artifactory 凭据；如果攻击者能进入依赖包或构建产物仓库，就可能通过后门软件包实现横向移动和持久化，把一次凭据泄露升级成构建链污染。

密码质量也放大了风险。文章提到，部分内部资源使用“平台名 + 当前年份”这类容易猜测的密码模式；即使没有外部公开泄露，这种凭据习惯在攻击者拿到初始访问权后也会成为横向扩张的燃料。

## 更大意义
这件事的讽刺点在于，CISA 的制度角色正是推动政府与关键基础设施提升安全 hygiene，但事故本身展示了最基础控制没有闭环：secret detection 可被关闭，明文密码可进入公开仓库，高权限 cloud key 可暴露，通报后的撤销也不够快。

对政府承包链条来说，文章暗示的问题比“某个承包商犯错”更大：如果承包商的本地工作方式、个人 GitHub 使用、设备同步习惯和机构凭据生命周期没有被统一约束，那么最强的云权限也可能被最随手的个人工作流拖下水。

## 值得质疑
CISA 称目前没有迹象显示敏感数据因此被 compromise，但文章没有提供公开的取证范围、暴露持续时间、访问日志结论或 key 轮换时间线。这个表述只能说明“尚未发现”，不能等同于“没有被利用”。

## 最后判断
这篇文章真正指向的是政府安全组织的“元安全”问题：当安全机构自己的承包、凭据、构建和应急流程都依赖个体自觉时，外部倡导的最佳实践会先在内部执行链条上失效。
