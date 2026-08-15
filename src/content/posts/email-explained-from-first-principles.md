---
title: "Email explained from first principles"
date: 2023-05-05T17:38:32Z
category: reading
description: "本文从第一性原理出发，详细解释了电子邮件 (Email) 的各个方面，包括其概念、架构、协议、格式、存在的问题以及针对这些问题的修复方案。文章涵盖了从用户角度的邮箱、地址、收件人等概念，到技术层面的 SMTP、IMAP、POP3 等协议，再到邮件格式、安全问题（如垃圾邮件、隐私泄露、钓鱼攻击）以及相应的解决方案（..."
source: "https://explained-from-first-principles.com/email/"
---

## TL;DR

本文从第一性原理出发，详细解释了电子邮件 (Email) 的各个方面，包括其概念、架构、协议、格式、存在的问题以及针对这些问题的修复方案。文章涵盖了从用户角度的邮箱、地址、收件人等概念，到技术层面的 SMTP、IMAP、POP3 等协议，再到邮件格式、安全问题（如垃圾邮件、隐私泄露、钓鱼攻击）以及相应的解决方案（如 SPF、DKIM、DMARC、TLS、S/MIME 和 PGP）。

## 主题

### 📧 概念 (Concepts)

电子邮件是一种通过互联网异步发送消息的服务。与传统邮件相比，电子邮件具有数字数据、即时全球交付和由邮箱提供商提供邮箱的特点。电子邮件地址由用户名、@ 符号和域名组成。邮件可以发送给主要收件人 (To)、次要收件人 (Cc) 和隐藏收件人 (Bcc)。邮件包含发件人 (From)、回复地址 (Reply-To)、主题 (Subject) 和正文 (Body) 等字段。

### 🏛️ 架构 (Architecture)

电子邮件遵循客户端-服务器模型。简化架构包括：发件人的邮件客户端、发件人的外发邮件服务器、收件人的传入邮件服务器和收件人的邮件客户端。使用的协议包括：用于消息提交和中继的 SMTP，用于消息存储的 IMAP，以及用于消息检索的 IMAP 或 POP3。官方架构则更复杂，包括邮件用户代理 (MUA)、邮件提交代理 (MSA)、邮件传输代理 (MTA)、邮件投递代理 (MDA) 和消息存储 (MS)。

### 👤 实体 (Entities)

简化架构中的三个实体分别是：

- **邮件客户端 (Mail Client)**：用于撰写、发送、接收和阅读电子邮件的程序，可以是本地程序（如 Outlook、Thunderbird）或 Web 应用程序（如 Gmail、Yahoo Mail）。
- **外发邮件服务器 (Outgoing Mail Server)**：接受来自邮件客户端的消息并将其排队以进行投递，同时确定每个收件人的传入邮件服务器并将消息投递给他们。
- **传入邮件服务器 (Incoming Mail Server)**：等待来自其他用户的外发邮件服务器的连接，并在收到消息后记录消息及其他信息。它还负责评估邮件是否为垃圾邮件，并将其投递到收件人的收件箱、垃圾邮件文件夹或直接丢弃。

### 🤝 协议 (Protocols)

电子邮件实体之间使用两种协议：

- **传递协议 (Delivery Protocols)**：用于传递消息，主要是 SMTP。
- **访问协议 (Access Protocols)**：用于访问用户的邮箱，主要是 POP3 和 IMAP。

历史上，这些协议直接在 TCP 上运行，这意味着通信既不加密也不进行身份验证。为了解决这个问题，引入了两种 TLS 使用方式：

- **Implicit TLS**：为每个服务引入一个新端口，通信直接从 TLS 握手开始。
- **Explicit TLS (STARTTLS)**：允许客户端在服务器指示支持 TLS 后，使用命令将不安全连接升级为安全连接。

### ✉️ 格式 (Format)

电子邮件的格式在 RFC 5322 中指定。邮件由多个标题字段和一个可选的正文组成，正文跟在一个空行之后。标题字段的格式为 `Name: Value`。邮件使用 MIME (RFC 2045) 进行编码，以支持非 ASCII 字符和长行。常见的 MIME 编码方式包括 Quoted-Printable 和 Base64。邮件可以包含多个部分 (multipart messages)，常见的类型有 multipart/mixed（用于附件）和 multipart/alternative（用于提供不同格式的相同内容）。

### ⚠️ 问题 (Issues)

电子邮件存在诸多问题：

- **垃圾邮件 (Spam)**：大量发送的未经请求的邮件。
- **隐私泄露 (Privacy)**：邮件客户端和服务器可能会泄露发件人的 IP 地址、设备名称、时区、邮件客户端等信息。HTML 邮件中的远程内容和链接跟踪也可能泄露收件人的信息。
- **安全问题 (Security)**：包括伪造发件人 (Spoofing)、钓鱼攻击 (Phishing)、缺乏机密性和完整性、不可靠的传递等。
- **复杂性 (Complexity)**：电子邮件系统经过 40 年的修补，变得非常复杂。
- **缺乏创新 (Innovation)**：过去二十年来，电子邮件领域几乎没有创新。

### ✅ 修复 (Fixes)

针对上述安全问题，提出了一些修复方案：

- **域身份验证 (Domain Authentication)**：
    - **SPF (Sender Policy Framework)**：在 DNS 记录中列出外发邮件服务器的 IP 地址，以验证 MAIL FROM 地址。
    - **DKIM (DomainKeys Identified Mail)**：让外发邮件服务器对邮件进行签名，并在 DNS 记录中发布公钥。
    - **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**：发布策略，告诉收件人如何处理未通过 SPF 和 DKIM 的邮件，并提供报告机制。
- **传输安全 (Transport Security)**：
    - **DANE (DNS-Based Authentication of Named Entities)**：使用 DNSSEC 来验证服务器的公钥，并防止降级攻击。
    - **MTA-STS (Mail Transfer Agent Strict Transport Security)**：使用 HTTPS 和 PKIX 证书来验证传入邮件服务器。
    - **TLSRPT (SMTP TLS Reporting)**：让接收域报告传输安全失败。
- **端到端安全 (End-to-end Security)**：
    - **S/MIME (Secure/Multipurpose Internet Mail Extensions)**：使用 X.509 证书和中心化认证机构。
    - **PGP (Pretty Good Privacy)**：使用 OpenPGP 格式和信任网络。

## 总结

电子邮件是一个复杂但至关重要的通信系统，它具有悠久的历史、广泛的应用和一系列安全问题。通过实施域身份验证、传输安全和端到端安全等措施，可以提高电子邮件的安全性、可靠性和隐私性。
