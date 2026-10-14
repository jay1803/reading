---
title: "Inside Nvidia GPU: 谈谈Blackwell的不足并预测一下Rubin的微架构"
date: 2026-10-14T14:31:31Z
category: reading
description: "Nvidia的核心壁垒在于用近十年的软硬件协同演进把矩阵计算、异步供数、内存同步和任务调度的复杂细节封装起来；文章分析Blackwell暴露的SFU、CPU和跨Die访存瓶颈，并预测Rubin架构的演进方向。"
source: "https://mp.weixin.qq.com/s/iNXR3fSIIrov870D5z6vIA"
---

Nvidia 的核心壁垒在于用近十年的软硬件协同演进，把矩阵计算、异步供数、内存同步和任务调度中的复杂细节逐步封装起来；Blackwell 暴露的 SFU、CPU 和跨 Die 访存瓶颈，也说明下一代 GPU 的关键取决于整个系统能否跟上 Tensor Core 的扩张。

从 Volta 引入 Tensor Core 开始，Nvidia 就在逐步改变传统 SIMT 架构。计算单元从 FMA、向量化 DP4A 走向更大规模的矩阵乘法，同时增加低精度格式，以提高计算访存比、控制芯片面积。Volta 的 Tensor Core 支持 FP16，Turing 增加 INT8、INT4，Ampere 增加 BF16 与 FP64，Hopper 引入 FP8 并取消 INT4，Blackwell 进一步支持 MXFP8/6/4 和 NVFP4。到了 Blackwell Ultra，也就是 B300，部分 FP64 和 INT8 算力被削减，显示面积分配已经需要在不同工作负载之间作出明确取舍。

这一演进更深刻的变化发生在**供数路径与结果存储**上。Volta 和 Ampere 的矩阵操作数、累加结果依赖 CUDA Core 的寄存器；Ampere 用 cp.async 绕过 L1 和寄存器中转，缓解搬运压力。Hopper 引入 TMA，让操作数直接进入 SMEM，并通过 CGA 和 DSMEM 支持更大范围的协作，但累加结果仍留在寄存器中，方便 Epilogue 处理，也继续带来寄存器占用和等待同步的负担。Blackwell 则引入 TMEM：矩阵 A 可来自 TMEM 或 SMEM，矩阵 B 来自 SMEM，结果写入 TMEM，Tensor Core 因而与 CUDA Core 的寄存器体系大幅解耦，形成更独立的异步计算路径。

异步化也经历了逐层推进。Volta 为线程提供独立 PC，并以 Cooperative Groups 提供协作抽象，但 Tensor Core 仍要求 Warp 同步执行；Ampere 的 cp.async 将异步执行扩展到供数路径；Hopper 的 MBarrier 则让异步流水线和 Warp Specialization 成为主要编程方式。General Proxy 与 Async Proxy 区分普通 LD/ST 和异步操作的内存访问路径，再通过相应屏障满足同步与内存序要求。Hopper 的 WGMMA 仍大量占用寄存器，并需要等待同步，Nvidia 在推出时就明确其 SM_90a 指令不保证后续架构兼容。Blackwell 的 Tensor Core 操作复用 MBarrier，TMA 和 tcgen05.mma 可以由单线程发起，但 TMEM 分配及部分搬运仍要求 Warp 级协作；ClusterLaunchControl 又增加了动态调度能力。

硬件逐步解耦的同时，软件必须接住增加的复杂度。CuTe Layout 用代数表达 Tile、Partition 和边界计算，并隐藏 Hopper、Blackwell 上复杂的 Swizzle，使布局与数据划分更容易组合；代价是学习曲线陡峭。它的重要性还会随多 Die 和未来 3D-DRAM 架构增长，因为数据布局需要更直接地适配物理存储结构。不过，Blackwell 的 tcgen05 指令仍混合同步与异步操作，发起粒度横跨线程、Warp 和双 SM，程序员必须同时考虑屏障、内存生命周期与协作范围。Pipeline 抽象和 TMEM 的 alloc/dealloc 降低了出错概率，却没有消除底层规则。

B200 最直接的失衡是**矩阵算力增长快于 SFU 能力**。TMEM、构成 DSMEM 的互联网络，以及 L2 取消 Partition 后的结构变化占用了面积，单 Die 的 SM 数降到 80 个，而 CUDA Core 配套的 SFU 性能没有同步增强，导致 GEMM 加速后，Attention 中的 Softmax 成为瓶颈。作者认为，不能把解决这一问题寄托在 Linear Attention 普遍替代现有 Attention 上：Qwen-Next 的 GDN、Kimi Linear 的 KDA 采用线性路线，MiniMax M2 却放弃了这一路线；DeepSeek 的 NSA 和 V3.2 的 DSA 则走向 Sparse Attention，MoR 等方向还可能增加 Attention block 的计算需求。

作者选择 Sparse Attention 的依据是，计算能力容易扩展，内存访问更难扩展，而 Linear Attention 没有充分解决后者。他进一步引用 SDPA 与单边熵最优输运的联系：Softmax 生成的注意力权重对应这一问题的精确解，因此判断 Softmax 会继续占据重要位置，SFU 应与 Tensor Core 保持匹配。这是作者对算法路线及未来负载的判断；文中的数学联系本身并未证明所有注意力机制都必须保留 Softmax。作者认为 B300 已修正 SFU 配比，代价是削减部分高精度算力，也因此不看好 B200、GB200 的投资价值。

GB200 的另一组瓶颈来自 Grace CPU。随着 GPU kernel 缩短到微秒级，系统进入 **Killer Microsecond** 区间：纳秒级等待可以同步处理，毫秒级任务能够摊薄上下文切换成本，微秒级任务却容易被启动和调度开销吞噬。CUDA Graph 和 persistent kernel 能缓解问题，但并不适用于全部 workload。Grace 使用 Neoverse V2 Core，却只配置 1MB L2，低于同样采用 V2 的 AWS Graviton 4 的 2MB；作者将部分客户遇到的 L1 ICache miss 问题与这一裁剪联系起来。Grace 选择 LPDDR5x 平衡带宽与容量，并通过 NVLink C2C 扩展 GPU 访存能力，但 Mesh NoC 上访问 L3 需要多跳，缓存缺失后的延迟仍然突出。

ScaleOut 流量进一步放大了这一问题。GB200 配套的 CX7 没有内置 PCIe Switch，RDMA 流量需要穿越 Grace NoC，再经 NVLink C2C 到达 Blackwell，与 CPU 的缓存、内存访问争用片上网络。作者引用 Chips and Cheese 的测试说明 Grace 的访问延迟高于 x86 和 Graviton 4，并将较小 L2、邻近负载干扰和 NoC 噪声视为原因；Nvidia 的 DeepSeek-V3 GB200 NVL72 训练优化报告也提到了 CPU overhead。AWS 额外加入 PCIe Switch 以绕开这一流量路径，Meta 则将 Grace 与 Blackwell 配比调整为 1:1，GB300 也缓解了部分问题。作者认为，基于 Grace 的 BlueField4 存在类似风险，而核心数增长后 NoC 的复杂度具有普遍性：他参与的 Cisco QFP 从 40 Core、160 线程扩展到 56 Core、224 线程时表现良好，到 224 Core、896 线程的第三代就遇到大量问题。

Blackwell 的 Dual Die 结构还增加了跨 Die 访存延迟，使 CTA 所在位置与数据位置的匹配变得重要。按文中的软件状态，CUDA 13.0 尚不支持 CTA 内存亲和性调度。作者提出，可以尝试通过 CuTe Layout 错开 memory bank，并预期未来会出现 CTA affinity API。随着 Rubin Ultra 走向四 Die，布局与调度必须更充分地利用片内拓扑，否则逻辑上统一的设备仍会因访问路径不同付出性能代价。

对 Vera CPU 的判断来自开发板观察与架构推测，不能视为最终规格。作者看到八通道内存，预计带宽相较 Grace 翻倍；CPU Core 增至 88 个，PCIe 升级到 Gen6，并估计提供 80 条 Lane。他猜测 Core 采用 Neoverse V3，该架构最多支持 3MB L2，但 Nvidia 是否配置更大缓存仍不确定，因为 Jetson Thor 的 V3-AE 仍只有 1MB。Vera 的 PCIe 和 Memory Controller 被放到不同 Die，类似 Graviton 3/4；这种结构调整也无法自动消除 CPU overhead，因为 L1 读取约需 3 个 cycle，穿越 Mesh NoC 访问 L3 则可能超过 120 个 cycle。

对 Rubin GPU，作者预计 Tensor Core 在 M 维度扩大一倍，推测矩阵规模达到 256 × N × 256 bits，TMEM 随之扩容，并从 Blackwell 的双 CTA、双 SM 协作扩展到四 CTA、四 SM MMA，以进一步复用数据。他设想 CGA cluster shape 扩展到 4，并沿用 preference cluster shape 调度来提高整个 GPC 的利用率；在面积约束下，独立 I/O Die 也成为其分析中的重要方向。这些预测的共同目标，是让供数、结果存储和协作范围随矩阵计算规模一起增长。

更具结构性的设想是在每个 SM 内加入一个小型**标量核**，配备约 2KB—4KB Private SMEM。TMA、MMA 描述符准备、指令发起和 cluster 调度通常只需要单线程，却仍占用 CUDA Core、寄存器和指令缓存；Host CPU 经 NVLink C2C 传递控制信息也需要数百个 cycle。将这些工作转移到贴近 L1/SMEM 的标量核，再把 MBarrier 放入 Private SMEM，可以释放寄存器资源，并将程序拆成 TC Function、TMA Function 和负责 Epilogue 的 CUDA SIMT kernel，减少复杂 Warp Specialization 的负担。调度与算法进一步分离，也更接近 Helion、TVM、TileLang 的组织思路，有利于编译器生成和优化。

这一标量核还可承接 IBGDA、GIDS 相关的部分控制及文件系统逻辑，降低通信任务占用 SM 的成本，并与 Warp Scheduler 交互。在四 Die 的 Rubin Ultra 上，Green CTX、CTA affinity 和 MPMD 可以组合出更贴合物理拓扑的并行策略，Google Pathways 已提供了 MPMD 框架的先例。这样的构成接近 Ascend 的 Scalar AI CPU、SIMD Vector Core 和 Tensor Core 分工，也引出作者对技术落地节奏的判断：先进架构需要软件与用户共同迁移，Nvidia 从 Volta 开始用近十年逐步牵引生态，降低了每一步采用新机制的门槛。

作者以自己 2018 年在 Cisco 开发边缘 AI、神经网络动态控制相关产品，以及 eRDMA 与 Google Falcon 可靠传输路线的比较，说明技术提前完成并不保证市场同步接受。芯片架构师必须预测未来三到五年的 workload，同时深入理解算法、算子、互联、编译与系统；作者将 Nvidia 的全栈能力视为这种预测能力的基础，并以自己在网络芯片、RDMA、ScaleUP、CUDA 算子和算法领域的经历说明，跨层经验需要长期积累，对下一代互联产品的领先判断则属于他的自我评估。

对国产芯片的具体建议，是把资源投入那些容易让真实用户遭遇性能雪崩的细节：CGA 内 SM 如何互联，MBarrier 和 Async Proxy 如何简化异步内存访问，CuTe Layout 如何表达复杂布局，为什么 Pipeline 在 consumer.release 中封装 tcgen05.commit，以及 TMEM 为什么采用按列 alloc/dealloc。这些机制涉及同步正确性、资源生命周期、编程负担与性能之间的连续取舍，单看功能表难以理解。最终决定一套架构竞争力的，是它能否把真实 workload 所需的计算、供数与控制配平，并将这种配平转化为用户能够稳定获得的性能。
