---
title: "Banned book library in a wi-fi smart light bulb"
date: 2026-06-17T08:03:38Z
category: reading
description: "ESP32 智能灯泡本质上是个 4MB 闪存的 SoC，刷自定义固件后可变成无需互联网的 WiFi 图书馆死点，任何连上其 AP 的人都能访问禁书。4MB 存储上限每台只能放 5-6 本书，但作者认为这恰恰让每个死点成为创建者价值观的\"策展作品\"。"
source: "https://www.richardosgood.com/posts/banned-book-library/"
---

## TL;DR

ESP32 智能灯泡本质上是个 4MB 闪存的 SoC，刷自定义固件后可变成无需互联网的 WiFi 图书馆死点，任何连上其 AP 的人都能访问禁书。4MB 存储上限每台只能放 5-6 本书，但作者认为这恰恰让每个死点成为创建者价值观的"策展作品"。

## 核心洞见

- Tasmota 预装灯泡已有 OTA 路径，无需拆焊即可刷入完全自定义固件。
- ESP-IDF 的 =SPI_FLASH_DANGEROUS_WRITE_ALLOWED= 选项允许运行时覆写分区表（0x8000），将 SPIFFS 从 320K 扩至 2MB；若操作失败则只能串口恢复。
- 原 Tasmota safeboot 依赖 NVS 里的 WiFi 凭证，而固件会主动擦除 NVS（防止留下 SSID/密码明文），因此必须自制 safeboot——最小化 IDF 固件，在独立 AP 下提供 OTA 刷写入口。

## 具体机制

- 捕获门户：DNS 服务器把所有查询指向 ESP32 自身 IP，同时处理 Windows/Android/iOS/Firefox 各自的探测请求，用户一连上 AP 就自动弹出图书馆页面。
- 灯光伪装：管理页面通过 PWM（AnalogWrite）控制 CW/WW/RGB 各通道强度，配色存入 NVS 重启后保持，方便在公共场所降低被发现概率。
- OTA 更新由 ElegantOTA 库处理，Restore 功能可重启进入自制 safeboot，支持刷回 Tasmota 或其他固件。

## 隐藏限制

- 外扩存储死路：六根 LED 控制引脚全部是输出，无法复用为 SPI；焊 microSD 需完全拆出主板（不可逆），3D 打印夹具方案因可靠性差也宣告失败。
- Restore 不完整：safeboot 分区本身无法自我更新，刷回 Tasmota 后其 OTA 升级体验被破坏。
- Arduino IDE 屏蔽危险闪存写入，必须改用 ESP-IDF + "Arduino as a Component" 才能绕过，构建环境复杂度大幅提升。

整个项目的真正约束不是技术而是存储：正是这 2MB 上限迫使每个死点创建者认真思考"哪几本书值得留下"，让硬件限制变成了人文表达的空间。
