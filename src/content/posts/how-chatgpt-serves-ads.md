---
title: "How ChatGPT serves ads"
date: 2026-04-30T08:02:48Z
category: reading
description: "OpenAI 的广告系统已经有可观测的端到端归因闭环：ChatGPT 后端在对话 SSE 流里插入结构化广告单元，点击后通过商户侧 OAIQ SDK、Fernet token、30 天第一方 cookie，把聊天上下文、广告点击、站外商品浏览串起来。"
source: "https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/"
---

## TL;DR
OpenAI 的广告系统已经有可观测的端到端归因闭环：ChatGPT 后端在对话 SSE 流里插入结构化广告单元，点击后通过商户侧 OAIQ SDK、Fernet token、30 天第一方 cookie，把聊天上下文、广告点击、站外商品浏览串起来。

## 核心机制
- 广告以 `single_advertiser_ad_unit` 类型事件出现在 `chatgpt.com/backend-api/f/conversation` 的 SSE 响应流中；普通事件输出模型文本，部分 `delta` 事件输出广告对象，位置更接近后端协议层，而非页面外层横幅。
- 广告对象包含 `ads_request_id`、`ads_spam_integrity_payload`、品牌信息、卡片文案、图片、目标 URL 和 `ad_data_token`；`advertiser_brand.id` 形如 `adacct_<32-hex>`，看起来是稳定的商户账户 ID。
- 创意素材由 OpenAI 自己的 `bzrcdn.openai.com` 承载；`target.open_externally: false` 会让链接在 ChatGPT 内置 webview 打开，使 OpenAI 能观察点击后的导航过程。
- 同一个账号在不同对话主题里收到了不同广告：北京旅行→Grubhub/GetYourGuide/航班，NBA→Gametime，春季穿搭→Aritzia，生产力/幻灯片→Canva。作者确认上下文定向存在，但没有证据判断是否使用历史对话。

## 归因链
- 每个广告带 4 个 Fernet 加密 blob：`ads_spam_integrity_payload`、点击 URL 上的 `oppref`、点击 URL 上的 `olref`、包在 base64 JSON 里的 `ad_data_token`。
- `ads_spam_integrity_payload` 不进入点击 URL，作用更像服务端校验，防止伪造广告点击。
- `oppref` 会从 URL 被商户侧 SDK 读出，写入第一方 cookie `__oppref`，TTL 为 720 小时 / 30 天；之后每次商户像素事件都会携带它。
- `olref` 与 `oppref` 一起出现在点击 URL 中，但作者观测到的 SDK 没有持久化它；它可能用于 OpenAI 服务端的曝光或出站链接日志。
- Fernet token 的前 9 字节公开：版本字节 `0x80` 加 8 字节 Unix 时间戳；因此不用解密也能恢复 token 铸造时间。作者观测到 Home Depot URL token 在 2026-04-26 11:30:08 UTC 铸造，页面请求发生在 11:31:43，点击延迟 95 秒。

## 商户侧 SDK
- 商户页面加载 `https://bzrcdn.openai.com/sdk/oaiq.min.js`，版本为 `0.1.3`。
- 初始化调用形如 `oaiq('init', { pid: '<merchant pixel ID>' })`，事件调用形如 `oaiq('measure', 'contents_viewed', {...})`。
- SDK 会读取 `?oppref=`，写入 `__oppref`，设置探测 cookie `__oaiq_domain_probe`，然后把事件 POST 到 `https://bzr.openai.com/v1/sdk/events?pid=<merchant>&st=oaiq-web&sv=0.1.3`。
- 这意味着 ChatGPT 内广告点击后的商品浏览、内容浏览等商户站内行为，可以通过商户像素回传给 OpenAI 做归因。

## 为什么重要
- 这篇文章的价值在于提供了协议层证据：广告对象、字段名、token 位置、SDK 域名、cookie 名、事件上报端点都来自实际流量观测。
- ChatGPT 广告如果规模化，商业控制点会同时落在三处：对话上下文定向、内置 webview 点击路径、商户站内归因 SDK。
- 用户和屏蔽工具可以监控两个域名：`bzrcdn.openai.com`、`bzr.openai.com`；也可以检查两个 cookie：`__oppref`、`__oaiq_domain_probe`。

## 值得质疑
- 样本来自“consented mobile-traffic research fleet”，但文章没有给出样本规模、地域分布、账号状态、实验重复次数。
- 作者没有证明 OpenAI 使用长期记忆、历史对话或跨站行为做定向；目前能确认的是单次对话主题与广告匹配。
- token 内容无法解密，四类 token 的具体语义仍有推断成分，尤其是 `olref` 与 `ad_data_token` 的服务端用途。

## 收束
真正的信号是：OpenAI 已经在把对话入口、广告投放、商户像素和点击后行为归因组装成一套可扩展的广告基础设施。
