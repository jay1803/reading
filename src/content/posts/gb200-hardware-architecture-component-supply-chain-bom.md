---
title: "GB200 Hardware Architecture - Component Supply Chain & BOM"
date: 2024-10-23T18:05:31Z
category: reading
description: "Nvidia 已经发布了一个标准机架...但现实是有数十种不同的部署变体，需要权衡和显着增加复杂性关于一代。供应链针对最终数据中心部署者、云、服务器 OEM/ODM 和下游组件供应链进行了重新设计。"
source: "https://www.semianalysis.com/p/gb200-hardware-architecture-and-component"
---

Nvidia 已经发布了一个标准机架...但现实是有数十种不同的部署变体，需要权衡和显着增加复杂性关于一代。供应链针对最终数据中心部署者、云、服务器 OEM/ODM 和下游组件供应链进行了重新设计。

我们将对 GB200 机架的 50 多个不同子组件的单位体积、供应商市场份额和成本进行细分。
### The 4 Rack Scale Form Factors of Blackwell
GB200 机架提供 4 种不同的主要外形尺寸，每种外形尺寸均可进行定制。
- GB200 NVL72
- GB200 NVL36x2
- GB200 NVL36x2 (Ariel)
- x86 B200 NVL72/NVL36x2

第一个是GB200 NVL72 外形规格。这种外形尺寸每个机架大约需要 120kW。每个机架的功率远远超过 40kW 是 GB200 需要液体冷却的主要原因。

GB200 NVL72 机架由 18 个 1U 计算托盘和 9 个 NVSwitch 托盘组成。每个计算托盘的高度为 1U，包含 2 个 Bianca 板。每块 Bianca 板都有 1 个 Grace CPU 和 2 个 Blackwell GPU。 NVSwitch 托盘有两个 28.8Tb/s NVSwitch5 ASIC。

大多数数据中心基础设施即使采用直接芯片液体冷却也无法支持如此高的机架密度（ DLC）。

下一个外形尺寸是GB200 NVL36 * 2 ，它是两个并排互连在一起的机架。大多数 GB200 机架将使用这种外形尺寸。每个机架包含 18 个 Grace CPU 和 36 个 Blackwell GPU。在 2 个机架之间，NVL72 中的所有 72 个 GPU 之间仍然保持非阻塞的全对全。每个计算托盘的高度为 2U，包含 2 个 Bianca 板。每个NVSwitch托盘有两个28.8Tb/s NVSwitch5 ASIC芯片。每个芯片向后指向背板的速率为 14.4Tb/s，指向前板的速率为 14.4Tb/s。每个 NVswitch 托盘有 18 个 1.6T 双端口 OSFP 笼，水平连接到一对 NVL36 机架。

每个机架的功率和冷却​​密度为每个机架 66kW，NVL36 机架* 2 的总功率和冷却​​密度为 132kW。

最后一种外形是带有定制“Ariel”板而不是标准 Bianca 板的特定机架。我们相信这个变体将主要由 Meta 使用。由于 Meta 的推荐系统训练和推理工作负载，它们需要更高的 CPU 核心和更多的每 GPU 内存比率，以便存储大量嵌入表并在 CPU 上执行预处理/后处理。

内容与标准 GB200 NVL72 类似：但 Bianca 板被替换为具有 1 个 Grace CPU 和 1 个 Blackwell GPU 的 Ariel 板。由于每个 GPU 的 Grace CPU 内容加倍，因此该 SKU 甚至比 NVL36x2 更昂贵。

我们认为 Meta 的大部分分配将是普通的 NVL36x2，因为它更适合 GenAI 工作负载，而 Ariel 版本将仅适用于其最大的推荐系统工作负载。

在 2025 年第二季度，将会有B200 NVL72 和 NVL36x2 外形规格，将使用 x86 CPU，而不是 Nvidia 的内部 Grace CPU。
### Power Budget Estimates
### Compute Tray Diagrams & Cabling
### Networking
GB200系统中有4种不同的网络：
- Frontend Networking (Normal Ethernet)
- Backend Networking (InfiniBand/RoCE Ethernet)
- Accelerator Interconnect (NVLink)
- Out of Band Networking

前端网络只是普通的以太网，用于连接到互联网、SLURM/Kubernetes、网络存储、数据加载、模型检查点。该网络通常为每个 GPU 25-50Gb/s，因此在 HGX H100 服务器上，每台服务器将为 200-400Gb/s，而在 GB200 计算机托盘节点上，每台服务器将为 200-800Gb/s，具体取决于配置。

您的后端网络用于将 GPU-GPU 通信扩展到数百到数千个机架。该网络可以是 Nvidia 的 Infiniband 或 Nvidia Spectrum-X 以太网或 Broadcom 以太网。与 Broadcom 以太网解决方案相比，Nvidia 的选项要昂贵得多。

扩展加速器互连（ Nvidia 上的 NVLink 、 AMD 上的 Infinity Fabric/UALink、 Google TPU 上的 ICI 、Amazon Trainium 2 上的 NeuronLink）是一种超高速网络，可将系统内的 GPU 连接在一起。在 Hopper 上，该网络以每个 450GB/s 的速度将 8 个 GPU 连接在一起，而在 Blackwell NVL72 上，它将以每个 900GB/s 的速度将 72 个 GPU 连接在一起。 Blackwell 有一个名为 NVL576 的变体，可以将 576 个 GPU 连接在一起，但基本上没有客户会选择它。一般来说，您的加速器互连速度比后端网络快 8-10 倍。

最后，还有带外管理网络，用于重新映像操作系统、监控节点运行状况，例如风扇速度、温度、功耗等。服务器、PDU、交换机上的基板管理控制器 (BMC) CDU 通常连接到该网络来监视和控制这些 IT 设备。
### NVLink Scale Up Interconnect
与铜缆甚至上一代光学器件相比，1.6T NVLink 收发器等尖端收发器的可靠性要差得多。
这就是 Nvidia 选择使用 5184 铜电缆的原因，这是一种更便宜、耗电更少且更可靠的选择。每个GPU具有900GB/s的单向带宽。

此外，人们还存在一种误解，认为电缆价格昂贵。大部分成本不是来自电缆本身，而是来自电缆和连接器的端接。连接器价格昂贵，因为它们需要防止不同差分对之间的串扰。串扰非常严重，因为它会模糊其他信号并导致解串器无法读取正确位的错误。 Nvidia 选择使用 Amphenanol 的 Ultrapass Paladin 背板产品作为其 NVLink 背板互连的主要初始来源。

我们将在本文中使用每个连接器和电缆的主要来源名称，但是随着时间的推移，有 3 个来源的份额有所不同，我们在[完整的GB200 组件和供应链模型](https://www.semianalysis.com/p/semianalysis-gb200-component-and)中分享了其详细信息
### GB200 NVL576
GB200 NVLink 可以同时连接 576 个 Blackwell GPU。

不幸的是，L1 NVSwitch 和 L2 NVSwitch 之间的距离大于铜缆所能达到的距离；因此，必须使用光学连接。此外，L2 NVSwitch 使用 Flyover 电缆连接到机箱正面的 OSFP 笼。 NVL576 的额外 BOM 成本是天文数字，Nvidia 需要向其供应商支付超过 560 万美元（每个 GPU 9,700 美元）。

采用 75% 的毛利率意味着客户需要为 NVL576 铜缆 + 光纤连接为每个 GPU 额外支付 38.8k 美元。虽然 Nvidia 可以削减利润，即使横向扩展 NVLink 解决方案的利润率为 0%，但这基本上是站不住脚的。
### Backend Networking
对于后端网络，客户将根据他们使用的 NIC 使用多种不同类型的交换机。
- Quantum-2 QM9700 Infiniband NDR from NVIDIA
- Quantum-X800 QM3400 Infiniband XDR
- Quantum-X800 QM3200 Infiniband NDR/XDR
- Spectrum-X SN5600
- Spectrum-X Ultra
- Broadcom Tomahawk 5
- Broadcom Tomahawk 6

尽管后端网络硬件相同，但利用轨道优化设计仍面临巨大挑战。这是由于交换机的端口与机架上的端口数量不匹配造成的。

由于没有 ConnectX-7/8 或 Bluefield-3（两者都集成了 PCIe 交换机），因此需要 Broadcom / Astera Labs 的专用 PCIe 交换机来将后端 NIC 连接到 CPU 和 GPU。

此外， Amazon Trainium 2 部署具有大量 Astera Labs 重定时器内容。
