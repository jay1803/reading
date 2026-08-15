---
title: "I finally understand Cloudflare Zero Trust tunnels"
date: 2025-11-19T08:43:10Z
category: reading
description: "Cloudflare Zero Trust 不是\"更好的 VPN\"，而是三个互相正交的概念（Tunnel / Route / Target）叠加形成的私有网络编排系统；把这三者混为一谈是理解卡壳的根本原因。"
source: "https://david.coffee/cloudflare-zero-trust-tunnels"
---

## TL;DR
Cloudflare Zero Trust 不是"更好的 VPN"，而是三个互相正交的概念（Tunnel / Route / Target）叠加形成的私有网络编排系统；把这三者混为一谈是理解卡壳的根本原因。

## 核心洞见
Cloudflare 有两个工具，经常被混淆：**Warp Client**（客户端，负责把用户接入 Zero Trust 网络、执行策略）和 **Cloudflared**（服务端守护进程，负责在目标网络里创建出口 Tunnel）。两者互相依赖，但功能不同。

Tunnel / Route / Target 三者分工：
- **Tunnel**：运行在目标网络某台机器上的 cloudflared 进程，是"流量在私有网络里的出口"；config.yml 决定进来的流量转发到哪里（hostname → localhost:80 / ssh://localhost:22 等）
- **Route**：告诉 Warp 客户端"遇到这段 IP 就往某个 Tunnel 送"（如 192.168.1.1/24 → 家里的 Tunnel）；被路由的 IP 不需要真实存在，可以是完全虚拟的地址
- **Target**：指向某个服务或网络段，是挂载 Access Policy 的锚点；没有 Target 就无法对特定资源施加粒度访问控制

## 具体机制
两种公开暴露方式，权限模型不同：
1. Argo Tunnel + DNS CNAME：把 homeassistant.mydomain.com → Tunnel，全球公开可达，无需 Warp
2. Route（私有 IP 路由）：只有 Warp 已连接的用户才能访问 192.168.1.3

Access Policy 关键细节：
- 选择器 **Gateway**（≠ Warp）：仅匹配已注册到你 Zero Trust 组织的 Warp 用户；"Warp"选择器会误匹配使用消费者 1.1.1.1 Warp+ 的陌生人
- Include = OR，Require = AND；Action 有 Allow / Deny / Bypass / Service Auth（后者用于 bot / server-to-server 场景）
- 实用组合：公开域名 + 邮箱+GitHub 登录限制；当 Warp 已连接则 Bypass 登录页

Warp 客户端注册同样走 Policy：在 Enrollment Permissions 里定义谁能加入组织；必须开启 "WARP authentication identity" 才能在 Access Policy 里使用 Gateway 选择器。

## 隐藏限制
- 所有流量（warp-to-warp 直连除外）都经过 Cloudflare 边缘节点中转，延迟高于 Tailscale 的 p2p 直连
- 本文未覆盖：warp-to-warp 直连路由、组织内专属虚拟私有 IP 分配、通过 Target + Access Policy 实现免 SSH key 登录

## 虚拟 IP 的设计感
Route 可以把根本不存在的 IP（如 10.128.1.1）映射到 Tunnel，再由 Tunnel 转发到真实地址——这是在 Cloudflare 网络层构建抽象私有拓扑，已经接近 SDN 的思路，和传统"打通两端"的 VPN 概念根本不同。
