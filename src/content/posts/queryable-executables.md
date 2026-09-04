---
title: "Queryable Executables"
date: 2026-09-04T13:42:11Z
category: reading
description: "把可执行文件本身设计成 SQLite 数据库，会让程序、资源、运行状态和部署记录统一为一份可查询、可事务化的文件，许多原本依赖文件系统、打包格式和专用二进制工具的机制因此收敛为 SQL。SELF 格式把 ELF 的 segments、symbols 和 relocations 存成数据库表，再由 L"
source: "https://fzakaria.com/2026/08/24/actually-queryable-executables"
author: "rguiscard"
---

把可执行文件本身设计成 SQLite 数据库，会让程序、资源、运行状态和部署记录统一为一份可查询、可事务化的文件，许多原本依赖文件系统、打包格式和专用二进制工具的机制因此收敛为 SQL。SELF 格式把 ELF 的 segments、symbols 和 relocations 存成数据库表，再由 Linux 的 binfmt_misc 调用自定义解释器 self-exec：解释器读取 segments、映射内存并跳转到 entry point，于是分析程序结构可以直接使用 SELECT。更进一步，SQLite 文件天然可写，运行中的程序也能把状态存回承载自身代码的同一文件，从而把传统上散落在 /var、/tmp、/home 等目录里的应用数据一并纳入事务管理。

概念验证项目 self-httpd 展示了这种结构如何工作：名为 server 的单一文件既是 SQLite 3.x 数据库，也是可直接执行的 Web 服务器，同时包含程序代码、网站内容、路由、访问日志和按钮点击记录。它启动后可以用 4 个 worker 提供 3 条路由；访问首页会向 visits 表插入一条记录，向 /api/press 发送 POST 请求则会在 presses 表中写入时间和按钮名称。外部工具随时可以执行 `SELECT count(*) FROM presses` 或按 path 汇总 visits，检查运行状态无需日志解析器或管理接口，因为应用状态已经是结构化关系数据。线上实例 selfdb.exe.xyz 就是以这一份文件同时承担服务器、网站和数据库的角色。

程序访问自身依赖 argv[0]。当前 binfmt_misc 命中后，Linux 实际执行的是解释器，并把原文件路径交给它；self-exec 将参数向后传递，使目标程序看到的 argv[0] 正是自己的数据库文件路径。解释器在跳转到 entry point 前释放 SQLite 连接，程序随后即可调用 `sqlite3_open(argv[0], &db)` 重新打开自身，读取 segments 等内部结构表，查询旁边的业务表，并把修改永久保存下来。现阶段不能依赖 /proc/self/exe，因为它通常指向解释器；Linux VFS 已加入对透明 binfmt_misc 的支持，未来该路径有望重新指向原始可执行文件。

self-httpd 的应用层只需要 routes、visits 和 presses 三张表：routes 保存 path、MIME 类型和页面 BLOB，另外两张表记录访问和点击。构建过程仍然从普通 C 程序开始：先用 cc 编译出 ELF，再由 elf2self 把 ELF 转换成数据库中的 rows，最后执行 DDL 创建业务 schema，并用 SQLite 的 readfile() 把 index.html 写入 routes。服务器处理 GET 请求时，从自己的 routes 表 SELECT body；响应完成后，又向自己的 visits 表 INSERT 日志。页面展示的 segments、symbols 和 relocations 也没有在构建时固化成额外报告，而是服务器运行期间从自身查询出来的。

这一思路受到 Justine Tunney 的 redbean 启发，但两者把复杂性放在了不同位置。redbean 基于 Cosmopolitan 的 Actually Portable Executable，把 Web 服务器和自解压 ZIP 归入一个跨平台文件，并通过 Lua hooks 定制响应；SELF 直接让数据库承担容器职责，一条写入 handlers 表的记录就能增加处理逻辑，例如把 `/api/busiest` 映射到按访问次数排序的 SQL 查询。redbean 的核心能力是到处运行，SELF 的核心能力是可以被 SELECT，因此作者将它称为 **Actually Queryable Executable**。

当代码、内容和状态都位于 SQLite 中，修改线上站点也就成为普通 ACID 事务。对 routes 执行 UPDATE 并提交后，新页面立即生效，无需重启、reload 或重新部署；若结果有问题，ROLLBACK 可以撤销修改。SQLite 现成的生态也被程序直接继承：sqldiff 能精确显示两个版本间 routes、segments、symbols 和 relocations 各自发生了多少插入、删除与修改，使“部署改了什么”成为可审计的数据差异；创建一张 FTS5 virtual table，再把 routes 中的文本页面插入索引，服务器便能全文搜索自己的内容，完成后仍是同一个可执行文件。

单文件结构也恢复了 scp 和 ssh 部署的简洁性，同时把完整应用 closure 一直封装到 libc 层。由于新版本代码与旧版本状态分处两个 SQLite 文件，重新部署可以视为一次数据迁移：新文件 ATTACH 当前运行的 server，再用两条 `INSERT ... SELECT` 把 visits 和 presses 复制过来，随后替换文件并重启，历史数据即可延续。segments 与业务表拥有同等地位，因此同样的迁移逻辑原则上还能反向作用于程序代码本身。

SELF 目前仍是一个带有实验性质、部分由 AI 协助完成的原型，但它证明了一个更广泛的设计判断：一旦把可执行格式从静态字节布局提升为数据库，代码装载、资源封装、状态持久化、在线编辑、搜索、审计和部署迁移便可以共享 SQLite 已积累数十年的机制。**程序即数据库，数据库即程序**的真正价值，在于让原本彼此隔离的系统层次获得同一种可查询、可组合且具事务保证的语言。
