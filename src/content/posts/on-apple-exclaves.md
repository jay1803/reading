---
title: "On Apple Exclaves"
date: 2025-03-17T21:09:38Z
category: reading
description: "Apple 公司为了解决其操作系统内核（XNU）的安全性问题，引入了一种名为 Exclaves 的新特性。Exclaves 是一组被隔离的资源，即使内核受到攻击，这些资源也能受到保护。Exclaves 基于 ARM 的 TrustZone 技术，通过创建一个安全世界（Secure World）来运行一个名为 Se..."
source: "https://randomaugustine.medium.com/on-apple-exclaves-d683a2c37194"
---

## TL;DR
Apple 公司为了解决其操作系统内核（XNU）的安全性问题，引入了一种名为 Exclaves 的新特性。Exclaves 是一组被隔离的资源，即使内核受到攻击，这些资源也能受到保护。Exclaves 基于 ARM 的 TrustZone 技术，通过创建一个安全世界（Secure World）来运行一个名为 Secure Kernel (SK) 的新内核，与运行 XNU 的非安全世界（Insecure World）隔离。Exclaves 包含多种资源类型，如共享内存缓冲区、音频缓冲区、传感器以及 Conclaves（一种特殊的资源组）。文章详细介绍了 Exclaves 的架构、启动过程、内存管理以及与 XNU 的交互方式。
### 主题
#### Monolithic Operating System Kernels 的问题
现代操作系统通常将操作分为两个主要的保护域：用户模式（非特权域）和内核模式（特权域）。大多数操作系统使用单体内核设计，内核可以无限制地访问整个系统。这种设计存在安全隐患，因为内核的漏洞可能导致整个系统被攻破。微内核设计可以提高安全性，但可能存在性能问题。XNU 内核虽然基于 Mach 微内核，但实际上是作为单体内核运行的，存在常见的漏洞问题。

#### 隔离措施
为了解决单体内核的安全性问题，业界开发了多种软件和硬件层面的缓解措施。例如：
- Microsoft Virtualisation-based Security (VBS)
- Intel Software Guard Extension (SGX) and VT-X2
- ARM TrustZone

#### Apple 的隔离措施
Apple 多年来也采取了多种隔离数据的措施：
- 2013 年，推出了 Secure Enclave，这是一个运行在专用 CPU 核心上的微内核操作系统 SepOS，用于存储和保护敏感数据。
- 2017 年，引入了 Page Protection Layer (PPL)，隔离了内核的一小部分，并赋予其修改内存页表的权限。
- 2021-2023 年，推出了 Secure Page Table Monitor (SPTM)，取代并改进了 PPL，进一步隔离了小的内核组件。

#### 2024 — Exclaves: XNU 的主要新增功能
随着支持 M4 和 A18 处理器的 XNU 源代码的发布，Exclaves 的概念浮出水面。Exclaves 是对 XNU 传统单体内核安全模型的一次重大改进。

#### XNU Exclaves
Exclaves 是一组新特性，代表了对 XNU 传统单体内核的重大增强。Exclaves 指的是与 XNU 隔离的资源，即使内核受到攻击，这些资源也能受到保护。这些资源在操作系统构建时预先定义，通过名称或 ID 标识，具有不同的类型，在启动时初始化，并被组织到唯一的域中。SPTM 使用新的特定于 exclave 的页面类型来保护 exclave 内存免受 XNU 的侵害。资源类型包括：
- 共享内存缓冲区
- 音频缓冲区和传感器
- Conclaves 及其对应的 Conclave Managers
- 可以在 XNU 中的线程调用时在 exclave 空间内执行代码的服务

#### Secure Kernel — seL4?
为了允许在与 XNU 隔离的情况下执行 exclave 服务，Apple 引入了一个名为 Secure Kernel (SK) 的新内核。SK 镜像文件包含一个“cL4”的版本字符串。有迹象表明它基于 seL4 内核。XNU 用于与 SK 通信的 IPC 结构与 seL4 更为接近。SK 中的字符串经常提到 capabilities、frames、untyped memory、minting 等，这些也与 seL4 更为一致。
Apple 于 2024 年 4 月公开宣布加入 seL4 基金会。

#### Secure Worlds — ARM TrustZone?
SK 运行在与 XNU/iOS 相同的高速应用处理器上。为了实现这一点，需要额外的处理器权限级别，这可能是通过虚拟化扩展、Apple 对 SPTM 的特定添加或最有可能通过 ARM 的 TrustZone 技术来支持的。XNU 源代码包含多个关于进出 TrustZone 的安全世界概念的引用。
TrustZone 将系统分为两个世界：安全世界和非安全世界。XNU（和 iOS）在非安全世界中运行，而 SK 在安全世界中运行。SK 为 exclaves、资源和服务提供了一个有限的操作环境。

#### Domains and Resources
XNU 初始化一个两级内核表结构来保存有关在启动期间发现的 exclave 资源的信息。每个资源都是唯一的资源类型，并保存有关存在于安全世界或两个世界中的资源的信息。
根表按名称标识域，每个域引用一个包含该域所有资源的二级表。目前已知的 Domains 包括：
- com.apple.kernel
- com.apple.darwin
- com.apple.conclave.name
- com.apple.driver.name

#### Conclaves
Conclave 是一种资源类型，它本身可以包含多个资源。Conclaves 允许一组服务和其他资源相互共享访问，并且 Mach 任务在可以调用哪些（如果有的话）conclaves 方面受到限制。
每个 conclave 都有一个 Conclave Manager（另一种类型的 exclave 资源），位于内核域中。
Conclaves 有一个生命周期，它们的 Conclave Manager 首先附加到 Mach 任务，然后启动。它们也可以被停止和分离。

#### Conclaves — Spawning and Attaching
XNU 的 posix_spawn() 函数可以调用 task_add_conclave() 来将任务和 conclave 管理器资源附加在一起。这是一种 1:1 的关系。只有 launchd 和具有 com.apple.private.exclaves.conclave-spawn 授权的任务才能生成 conclave。
内核在 com.apple.kernel 域中查找目标 conclave 的关联 conclave 管理器资源。然后，它将一个 tightbeam 端点保存到 conclave 管理器的端点。此端点是将来对 conclave 的所有控制的指向。

#### Conclaves — Launching
附加后，可以启动 conclave。启动尝试必须从附加到 conclave 的 conclave 管理器任务执行。启动 conclaves 的尝试也会等到 exclaves 完全启动。
一个新的 mach trap（即系统调用）已添加到 XNU 中，用于 exclave 功能，并最终进入 _exclaves_ctl_trap() 函数。此调用是重载的，可以执行作为参数传递的不同操作。启动 conclave 的相关操作是 EXCLAVES_CTL_OP_LAUNCH_CONCLAVE。

#### A New Mach Trap / System Call
\_exclaves\_ctl\_trap() 函数处理一个新的 Mach trap，用于 exclave 功能。该调用是重载的，其操作取决于操作参数，并且通常会验证对所调用操作的授权。操作包括：
- EXCLAVES\_CTL\_OP\_BOOT
- EXCLAVES\_CTL\_OP\_LAUNCH\_CONCLAVE
- EXCLAVES\_CTL\_OP\_LOOKUP\_SERVICES
- EXCLAVES\_CTL\_OP\_ENDPOINT\_CALL
- EXCLAVES\_CTL\_OP\_NAMED\_BUFFER\_CREATE
- EXCLAVES\_CTL\_OP\_NAMED\_BUFFER\_COPYIN
- EXCLAVES\_CTL\_OP\_NAMED\_BUFFER\_COPYOUT
- EXCLAVES\_CTL\_OP\_AUDIO\_BUFFER\_CREATE
- EXCLAVES\_CTL\_OP\_AUDIO\_BUFFER\_COPYOUT
- EXCLAVES\_CTL\_OP\_SENSOR\_CREATE
- EXCLAVES\_CTL\_OP\_SENSOR\_START
- EXCLAVES\_CTL\_OP\_SENSOR\_STOP
- EXCLAVES\_CTL\_OP\_SENSOR\_STATUS
- EXCLAVES\_CTL\_OP\_NOTIFICATION\_RESOURCE\_LOOKUP

#### Downcalls — running code in the secure world
Downcalls 是对安全世界中 exclave 服务端点的调用，这是安全世界代码执行发生的地方。
这些调用中存在很大的复杂性，主要围绕管理线程/IPC 上下文和调度当前线程以在安全世界中执行代码。
1. Downcalls 将当前线程切换到安全世界并在安全代码中的入口点开始执行。
2. 调用任务必须具有内核域授权或成为附加到服务的 conclave 的 conclave 管理器任务。
3. Conclaves 最多可以调用 128 个服务。
4. 线程似乎由 XNU 调度到安全内核（通过 sk_enter() 函数）。XNU 似乎处理安全世界中所有线程的调度，而 SK 可能没有任何独立的线程。
5. 在安全世界中执行的线程可以执行临时的 upcall 到 XNU。
6. 在安全世界中执行的线程可以执行正常的调度程序类型的操作，如 yield、wait、被挂起或被中断。
7. 如果安全世界线程在 CPU 核心上 panic()，则不再将新任务调度到其他核心上的安全世界中，它们会等待一个超时时间。
8. XNU 似乎处理所有中断处理，而不是 SK。
9. Downcall 的 IPC 结构在通过 sk_enter() 调用进入安全世界之前使用请求和响应缓冲区进行设置。
10. 在完成 IPC 请求结构并调用 sk_enter() 时，中断和抢占被禁用。
11. 令人不安的是，downcall 响应可以通过不同的 CPU 的每个核心响应缓冲区返回，因为 downcall 可能已被中断、upcall 或 yield 并需要重新调度。
12. 通过 th_exclaves_state（线程结构中的位域）协调线程的 exclave 状态（以避免 SK 重新进入等）。

#### Upcalls — Secure World calls to XNU
由于 downcall 而在安全世界中运行的线程可能需要 XNU 的帮助，这可以通过 Tightbeam 框架对 exclaves upcall 处理程序的 upcall 来实现。Upcalls 仅限于 XNU 中的特定功能。希望进行 upcall 的线程返回到调用特定 upcall 处理程序的非安全世界。在此状态下，线程不能返回到用户模式（出于明显的原因），也不能执行另一个 downcall 到安全世界，即不允许“重新进入”exclaves。相反，线程将在执行 upcall 的位置返回到安全世界。
源中发现的允许的 upcalls 最终位于以下函数中：
- Memory
- File storage
- DriverKit
- DriverKit Apple Neural Engine
- Conclaves

#### The XNUProxy
XNUProxy 的引用比比皆是，但我还不能确定它到底是什么以及在哪里。我考虑过的选项包括：
- 它是自己的一个 exclave 域，类似于 com.apple.xnuproxy
- 它是在 com.apple.kernel 域中运行的一个 exclave 服务或一组服务，服务于特定类型的 downcalls。
- 它是 SPTM 中用于向安全世界发出 downcalls 的子系统......

#### Booting Stage 1
在系统启动时启动 exclaves 需要在非安全世界和安全世界之间进行精细协调的舞蹈。任何出错通常都会导致 panic()。
启动分三个阶段进行。第一阶段在开源中不可见，但可能是一个安全启动过程，其中 SK 被加载到内存中，并且其代码签名在可执行之前经过验证。在成功的第一阶段启动结束时，启动状态为 EXCLAVES_BS_NOT_STARTED。

#### Booting Stage 2
1. 通过为 upcalls 创建 tightbeam 端点来初始化 upcall 服务器
2. 通过特殊调用进入安全世界，从安全内核收集启动信息
3. 再次进入安全世界，使用正常的端点调用，但不确定为什么......可能是为了触发内核域启动
4. 初始化 exclave 调度程序
5. 初始化 XrtHostedXNU kext
6. 初始化回调（我认为进入上面的 kext）
7. 启动调度程序 - 仅为启动 CPU 核心设置每个 cpu 的请求和响应，并绑定到启动核心
8. 循环，调用安全世界以查看它是否需要内存分配，直到它响应所有 exclaves 都已启动
9. 通过为所有核心设置每个 cpu 的请求和响应内存来初始化多核
10. 初始化 XNU Proxy - 为 IPC 调用创建缓冲区缓存，创建一些线程上下文，为 downcalls 到 xnuproxy 设置 tightbeam 端点
11. 初始化 exclaves panic 内核线程
12. 发现所有静态 exclave 资源并构建域和资源的根表。
13. 为所有 Conclave Manager 资源创建 tightbeam 端点，并为每个资源调用初始化过程。
14. 为每个 conclave 填充有效 conclave 服务 ID（从 0 到 127）的位图。
15. 在内核构建时，启动任务列表存储在 \_\_DATA\_CONST 段中。现在按优先级对它们进行排序，并调用每个启动任务函数。
16. 启动状态现在是 EXCLAVES_BS_BOOTED_STAGE_2

#### Boot Stage 3 (Boot ExclaveKit)
该阶段多次调用“framemint”。这表明 SK 基于 seL4。
1. 查找“com.apple.service.FrameMint”服务并为其创建 tightbeam 端点
2. 调用一个经过编辑的函数 framemint_framemint__init()
3. 调用一个经过编辑的 framemint_framemint_populate() 函数，但我猜这会触发安全世界中发生各种令人兴奋的活动
4. 启动状态现在是 EXCLAVES_BS_BOOTED_EXCLAVEKIT

#### SPTM memory typing
SPTM“类型化”内存页面以通过其不同的子系统控制对它们的访问。现有类型包括：
- XNU_USER_EXEC
- XNU_USER_DEBUG
- XNU_USER_JIT
- XNU_ROZONE
- XNU_KERNEL_RESTRICTED
- +Types for TXM, DART, etc
Exclaves 增加了：
- SK_DEFAULT
- SK_IO
- SK_SHARED_RO
- SK_SHARED_RW

### 总结
Apple 公司为了增强其操作系统安全性，引入了名为 Exclaves 的新特性，通过隔离敏感资源来缩小潜在的攻击面。Exclaves 利用 ARM TrustZone 技术创建安全世界，运行独立的 Secure Kernel (SK)，与运行 XNU 的非安全世界隔离。这种设计提高了系统的安全性，即使内核受到攻击，也能保护关键资源。
