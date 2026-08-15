---
title: "Would you like a drainer served at the very top of DuckDuckGo?"
date: 2026-06-17T08:03:38Z
category: reading
description: "作者在 DuckDuckGo 搜索 Tronscan 时点了排名第一的结果——仿冒钓鱼站。次日换设备再搜，第一名已替换为另一个仿冒站，前一个被封后过夜完成切换。继续测试：Solscan、Phantom、Etherscan 搜索结果前三名均存在钓鱼站。这是系统性攻击面。"
source: "https://timsh.org/drainer-at-the-top-of-duckduckgo/"
---

## SEO 钓鱼是 Web3 最可复制的攻击面，而非偶发漏洞

作者在 DuckDuckGo 搜索 Tronscan 时点了排名第一的结果——仿冒钓鱼站。次日换设备再搜，第一名已替换为另一个仿冒站，前一个被封后过夜完成切换。继续测试：Solscan、Phantom、Etherscan 搜索结果前三名均存在钓鱼站。这是系统性攻击面。

## 网关-目的地分离架构：对爬虫不可见，对用户透明

所有钓鱼站共享同一基础设施模式：一个外观无害的网关域（tronscan.gr.com、etherscan.github.io 等）做 client-side form 自动提交跳转（100ms 延迟），destination 钓鱼站接到 ~?verified=1~ 后才触发 drainer。

关键细节：
- 简单爬虫 / 纯 HTTP 请求看到的网关页完全无害，只有真实浏览器触发跳转
- 被封后只换 destination，gateway 保留 SEO 排名，次日即完成替换
- GitHub Pages / Cloudflare Workers 被用作 gateway：高信任域名助推排名，平台侧行为无异于正常页面
- 网关 PHP 注释为俄语

## Drainer 实现细节

Tronscan 仿冒站（web3-loader.js，混淆，作者用 Python 轮换解码 + LLM 美化）流程：
- WalletConnect popup 劫持所有页面点击，伪装为 AMLBot 合规工具诱导连接
- 连接后服务端扫描余额，为每种 TRC-20 代币生成 ~increaseApproval(attacker_addr, uint256_max)~ 签名请求
- TRX 原生币不可 approve：通过攻击者控制合约的 ~ClaimRewards()~ 空壳函数转走（余额 - 15 TRX 保留 gas）
- 签名成功后前端通知 ~api.tr0nscan.com~，后端主动发起转移
- 合约未验证，反编译可见大量空壳函数（全为名称伪装）
- 部署者钱包在合约上线数日后已收入至少 $15k

## AML/KYT 工具对此几乎无效

作者用两个 KYT 工具检测硬编码攻击者地址：收 token approve 的 EOA 显示零风险，部署 relay 合约的地址最高评级仅因"高风险交易所资金进出量大"触发。合约字节码反编译异常明显，但工具未捕获。实际后果：攻击者可直接通过 Binance 等合规 CEX 出金，不会被拦截。闭源黑箱算法使 KYT 工具的实际防御价值存疑。

## 为什么 DuckDuckGo/Bing 比 Google 更容易操控

流量少 → top 3 SEO 竞争门槛低；Bing 审核力度推测弱于 Google；Web3 社区持续向 DuckDuckGo 迁移（2026 年 5 月安装量增长 30%）。攻击者投入相同 SEO 资源，在 DuckDuckGo 获得的 ROI 更高，且几乎无人关注 Bing/DDG 端的 SEO 异常。
