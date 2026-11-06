---
title: "Debugging walkthrough: Access violation on nonsense instruction, episode 3"
date: 2026-11-06T06:58:04Z
category: reading
description: "Raymond Chen 追查多款程序随机崩溃：anti-malware 把 64-bit 跳转代码注入 32-bit 进程，指令被错误解码后触发 access violation。"
source: "https://devblogs.microsoft.com/oldnewthing/20260925-00/?p=112731/"
author: "Raymond Chen"
---

多款互不相关程序随机出现的“内存写入错误”，被 Raymond Chen 追查到同一个原因：客户使用的 anti-malware 软件把 64-bit 跳转代码注入了 32-bit 进程，导致处理器按错误的指令格式执行，并触发 access violation。跨程序出现相同故障，使调查从单个应用的 bug 转向了影响多个进程的共同因素。

其中一份 crash dump 显示，WerFault.exe 在入口函数 wmainCRTStartup 偏移 0x7 的位置执行了 `add byte ptr [eax],al`，试图写入无法访问的内存。这条指令对应的机器码是 `00 00`，意味着处理器正在把零字节当作代码执行。其他 dump 也呈现相同模式，只是进程名称不同，进一步指向了一种共同的代码破坏机制。

从函数起点反汇编，可以看到单字节 `nop`、`dec ecx`、将地址 0x02f11160 装入 edx 的指令、连续四个零字节，以及末尾的 `inc ecx` 和 `jmp edx`。这不符合正常 Windows 函数入口的特征：x86-32 代码通常使用 `mov edi,edi`，即使在 64-bit Windows 组件中，函数也不会以单字节 `nop` 或其他单字节指令开头。更关键的是，若暂时去掉那四个零字节，`dec ecx` 与 `inc ecx` 的效果便相互抵消，剩下的代码恰好像一个 *detour*：把绝对目标地址装入寄存器，再跳转过去。故障因此收敛为一次有问题的函数入口改写。

沿跳转目标继续检查，`!address 0x2f11160` 显示该地址位于一个 4 KB、已提交、具有执行与读取权限的 MEM_PRIVATE 区域。对这块内存执行字符串搜索，又找到 `C:\Program Files\Common Files\Contoso\injcore.dll`。这条路径把可疑注入代码与 Contoso 软件联系起来，但还需要解释，为什么入口处会出现四个零字节，以及那两条看似多余的 ecx 增减指令。

突破口是零字节的位置：它们紧跟在地址常量之后，恰好可以充当一个 64-bit 常量的高半部分。Chen 将原始字节写入一个用于实验的 64-bit WerFault.exe 调试会话，重新反汇编后，整段代码变成了连贯的 `nop`、`mov r10,2F11160h`、`jmp r10` 和 `int 3`。在 64-bit 指令格式中，先前被识别为 `dec ecx` 的 0x49 和被识别为 `inc ecx` 的 0x41 都参与了后续指令的编码；那四个零字节也属于地址常量。*同一串机器码在两种执行模式下产生了完全不同的含义*，从而揭示注入程序误判了目标进程的位数。

这也解释了故障为何显得随机：员工大部分时间运行 64-bit 程序，注入代码能够正常工作；偶尔启动 32-bit 程序时，同样的代码就会被错误解码，并在执行零字节形成的内存写入指令时崩溃。后续沟通确认，Contoso 是客户部署的 anti-malware 软件。团队建议临时禁用它，以验证故障来源，客户拒绝；团队又建议向供应商查询更新，客户仍以必须先完成内部验证为由抵触修改，坚持将问题归咎于 Windows，并要求 Windows 一侧提供解决办法。因此，文章给出了明确的机器码证据，但没有报告禁用验证或更新修复已经完成。

技术定位完成后，障碍转向了组织沟通：负责转述的 customer liaison 缺乏调试背景，无法在客户反驳时充分解释证据，团队考虑让工程师直接与客户交谈。这个案例显示，共同注入多个进程的软件可以制造出覆盖广泛、表面上近似操作系统故障的崩溃；要推动修复，既需要沿指令字节追溯责任来源，也需要让有权决定软件变更的人理解这条证据链。
