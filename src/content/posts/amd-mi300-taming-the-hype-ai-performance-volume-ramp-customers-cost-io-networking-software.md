---
title: "AMD MI300 – Taming The Hype – AI Performance, Volume Ramp, Customers, Cost, IO, Networking, Software"
date: 2023-06-13T10:58:32Z
category: reading
description: "AMD MI Series 算是 Nvidia Grace Hopper 的主要竞争对手，两者的基本架构类似，都是将 CPU 和 GPU 整合进同一块芯片来提升性能。"
source: "https://www.semianalysis.com/p/amd-mi300-taming-the-hype-ai-performance"
---

AMD MI Series 算是 Nvidia Grace Hopper 的主要竞争对手，两者的基本架构类似，都是将 CPU 和 GPU 整合进同一块芯片来提升性能。
## Summarized by BingChat
这篇文章是关于AMD的MI300芯片，它是一个采用先进封装技术的异构计算平台，包含了CPU和GPU的不同组合。文章介绍了MI300的设计、架构、性能、成本、发布时间、软件和客户等方面的信息，重点分析了它在人工智能领域的竞争力和挑战。文章认为MI300是一个令人惊叹的工程奇迹，但是要在市场上成功还需要解决很多问题。
### 可以详细介绍下 AMD的MI300芯片 吗？
当然可以。AMD的MI300芯片是一个数据中心APU（应用处理单元），它集成了24个Zen 4 CPU核心和一个CDNA 3 GPU核心，以及128GB的HBM3内存，共有1460亿个晶体管²。它是AMD生产的最大的芯片，也是世界上最先进的异构计算平台之一。它的主要特点有：

- 采用了3D堆叠技术，将9个5nm的计算芯片（CPU和GPU）堆叠在4个6nm的基础芯片（负责I/O和内存控制）之上，实现了高密度、高带宽、低延迟的连接²。
- 支持CPU和GPU之间的统一内存访问（UMA），可以在同一块HBM3内存上同时进行计算，无需复制数据，节省了功耗、提高了性能、简化了编程²。
- 拥有强大的人工智能计算能力，支持INT8、BF16、FP16、FP32等多种精度，以及新的矩阵乘法指令¹。
- 配备了无限缓存（Infinity Cache），可以有效降低对外部内存的访问频率，进一步减少功耗和延迟¹。
- 兼容AMD的Infinity Fabric架构，可以与其他MI300芯片或EPYC处理器进行高速互连，构建大规模的集群系统¹。

MI300芯片将首先应用于美国国家核安全局（NNSA）的超级计算机El Capitan，该计算机预计在2023年底投入使用，将成为世界上最快的超级计算机，峰值性能达到2艾浮点（ExaFLOPS）¹⁵。MI300芯片也将面向其他数据中心和云计算市场，与英特尔、英伟达等竞争对手展开激烈的竞争。

如果你想了解更多关于MI300芯片的信息，你可以参考以下链接：

¹: [AMD Instinct MI300 Details Emerge, Debuts in 2 Exaflop El Capitan Supercomputer | Tom's Hardware](https://www.tomshardware.com/news/new-amd-instinct-mi300-details-emerge-debuts-in-2-exaflop-el-capitan-supercomputer)

²: [AMD Instinct MI300 Data Center APU Pictured Up Close: 13 Chiplets, 146 Billion Transistors | Tom's Hardware](https://www.tomshardware.com/news/amd-instinct-mi300-data-center-apu-pictured-up-close-15-chiplets-146-billion-transistors)

³: [AMD: Instinct MI300 APU with Zen 4 and CDNA 3 Up and Running in the Lab](https://www.tomshardware.com/news/amd-instinct-mi300-apu-with-zen-4-and-cdna-3-up-and-running-in-the-lab)

⁴: [AMD Radeon Instinct MI300 Specs | TechPowerUp GPU Database](https://www.techpowerup.com/gpu-specs/radeon-instinct-mi300.c4019)

⁵: [AMD’s extraordinary next-gen CPU is so fast, it’ll be used in the most powerful supercomputer ever - TechRadar](https://www.techradar.com/news/amds-extraordinary-next-gen-cpu-is-so-fast-itll-be-used-in-the-most-powerful-supercomputer-ever)

Source: Conversation with Bing, 6/13/2023(1) AMD Instinct MI300 Data Center APU Pictured Up Close: 13 Chiplets, 146 .... https://www.tomshardware.com/news/amd-instinct-mi300-data-center-apu-pictured-up-close-15-chiplets-146-billion-transistors Accessed 6/13/2023.
(2) AMD Instinct MI300 Details Emerge, Debuts in 2 Exaflop El Capitan .... https://www.tomshardware.com/news/new-amd-instinct-mi300-details-emerge-debuts-in-2-exaflop-el-capitan-supercomputer Accessed 6/13/2023.
(3) AMD’s extraordinary next-gen CPU is so fast, it’ll be ... - TechRadar. https://www.techradar.com/news/amds-extraordinary-next-gen-cpu-is-so-fast-itll-be-used-in-the-most-powerful-supercomputer-ever Accessed 6/13/2023.
(4) AMD: Instinct MI300 APU with Zen 4 and CDNA 3 Up and Running in the Lab. https://www.tomshardware.com/news/amd-instinct-mi300-apu-with-zen-4-and-cdna-3-up-and-running-in-the-lab Accessed 6/13/2023.
(5) AMD Radeon Instinct MI300 Specs | TechPowerUp GPU Database. https://www.techpowerup.com/gpu-specs/radeon-instinct-mi300.c4019 Accessed 6/13/2023.
### 对比 nvidia grace hopper 两者有什么不同？
NVIDIA 的 Grace Hopper 和 AMD 的MI300都是新一代的数据中心处理器，它们都将CPU和GPU集成在同一个封装中，并使用HBM内存提供高带宽。它们都针对高性能计算和人工智能应用，与英特尔的Ponte Vecchio等产品展开竞争。它们之间有一些不同之处，我根据网上的信息，为你做了一个简单的对比表格：

| 特征 | NVIDIA Grace Hopper | AMD MI300 |
| --- | --- | --- |
| 发布时间 | 2023年上半年¹ | 2023年下半年² |
| 制程 | 5nm¹ | 5nm/6nm² |
| 芯片数 | 4个CPU芯片+1个GPU芯片¹ | 9个计算芯片（CPU+GPU）+4个基础芯片² |
| 晶体管数 | 1000亿¹ | 1460亿² |
| CPU架构 | ARM Neoverse V1¹ | Zen 4² |
| CPU核心数 | 256¹ | 24² |
| GPU架构 | Ampere Next¹ | CDNA 3² |
| GPU核心数 | 未知 | 未知 |
| 内存类型 | HBM+DDR5¹ | HBM3² |
| 内存容量 | 4TB/s¹ | 128GB² |
| 内存带宽 | 未知 | 1.2TB/s² |
| 缓存容量 | 未知 | 192MB（无限缓存）² |
| 峰值性能 | 未知 | 比MI250x快8倍（AI）² |
| 功耗 | 未知 | 约900瓦特³ |

从表格中可以看出，NVIDIA的Grace Hopper拥有更多的CPU核心和更大的内存容量，而AMD的MI300拥有更多的晶体管和更高的内存带宽。Grace Hopper使用了ARM的CPU架构，而MI300使用了AMD自己的Zen 4架构。Grace Hopper和MI300都采用了3D堆叠技术，但MI300更加复杂，将所有的计算芯片堆叠在基础芯片之上，实现了统一内存访问（UMA），可以让CPU和GPU同时在同一块HBM内存上进行计算，无需复制数据，节省了功耗、提高了性能、简化了编程²⁴。

如果你想了解更多关于NVIDIA的Grace Hopper和AMD的MI300的信息，你可以参考以下链接：

¹: [NVIDIA Grace: The Future of AI Is Arm](https://www.nvidia.com/en-us/data-center/grace-cpu/)

²: [AMD’s MI300 Targets HPC and AI](https://www.techinsights.com/blog/amds-mi300-targets-hpc-and-ai)

³: [Will AMD’s MI300 Beat NVIDIA In AI?](https://www.forbes.com/sites/karlfreund/2023/01/09/will-amds-mi300-beat-nvidia-in-ai/)

⁴: [MI300 vs Nvidia’s Grace: A Comparison of New Data Center Processors](https://www.linkedin.com/pulse/mi300-vs-nvidias-grace-comparison-new-data-center-processors-rios)

Source: Conversation with Bing, 6/13/2023(1) Will AMD’s MI300 Beat NVIDIA In AI? - Forbes. https://www.forbes.com/sites/karlfreund/2023/01/09/will-amds-mi300-beat-nvidia-in-ai/ Accessed 6/13/2023.
(2) MI300 vs Nvidia’s Grace: A Comparison of New Data Center ... - LinkedIn. https://www.linkedin.com/pulse/mi300-vs-nvidias-grace-comparison-new-data-center-processors-rios Accessed 6/13/2023.
(3) AMD’s MI300 Targets HPC and AI | TechInsights. https://www.techinsights.com/blog/amds-mi300-targets-hpc-and-ai Accessed 6/13/2023.
(4) Will AMD's MI300 Beat NVIDIA in AI? - Business News. https://biz.crast.net/will-amds-mi300-beat-nvidia-in-ai/ Accessed 6/13/2023.
