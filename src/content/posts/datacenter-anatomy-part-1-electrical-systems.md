---
title: "Datacenter Anatomy Part 1: Electrical Systems"
date: 2024-10-22T15:31:33Z
category: reading
description: "人工智能引发的电力需求激增，宏观和微观影响巨大，供给紧张。"
source: "https://www.semianalysis.com/p/datacenter-anatomy-part-1-electrical"
---

人工智能引发的电力需求激增，宏观和微观影响巨大，供给紧张。
在过去的几年里，该行业一直在逐步采用关键系统，以实现更高的功率密度，这对于随意的人工智能应用至关重要。这一推动力主要由规模较小的厂商主导，他们提供了自己的新设计来适应人工智能，而没有得到英伟达的认可，而英伟达在采用液体冷却方面与谷歌相比进展缓慢。

这一切都随着即将到来的布莱克韦尔坡道而改变。 Nvidia 的 GB200 系列需要直接芯片液体冷却，并具有高达 130kW 的机架功率密度，与 H100 相比，推理性能提高约 9 倍，训练性能提高约 3 倍。任何不愿意或无法提供更高密度液体冷却的数据中心都将错过为其客户带来的巨大性能 TCO 改进，并将在生成式 AI 军备竞赛中落后。

这些设计转变已经造成了相当大的影响。例如，Meta 拆除了整个在建建筑，因为这是他们使用多年的低功率密度的旧数据中心设计。

我们将深入探讨人工智能数据中心的电气系统，并探讨千兆瓦级集群将如何影响传统供应链。
We’ll discuss key equipment suppliers such as Vertiv, Schneider Electric, and Eaton and the impact of AI on their business.
### Datacenter Basics
数据中心是一种专用设施，旨在以高效、安全的方式向 IT 设备供电，并在 IT 硬件的生命周期内提供尽可能最低的总拥有成本。 IT设备通常放置在装有服务器、网络交换机和存储设备的机架中。运行这些设备可能需要大量电力并产生大量热量。

由数据中心问题引起的任何中断都可能导致重大收入损失并损害运营商的声誉。确保高正常运行时间可以确保更多收入，这很大程度上取决于内部拥有可靠的电气和冷却系统。

根据预期停机时间和冗余来评估数据中心的一个有用框架是 [Uptime Institute 的“Tier”分类](https://uptimeinstitute.com/tiers)，或 ANSI/TIA-942 标准（基于 Uptime 的 Tiers），具有下图中的以下四个评级级别。

“3 级”数据中心（及同等标准）是全球最常见的大型设施，并且始终需要 IT 设备的备用电源冗余。当谈论冗余时，我们使用“N”、“N+1”或“2N”等术语。例如，如果一个数据中心需要 10 台变压器，N+1 意味着总共购买 11 台，其中 10 台可用，1 台冗余，而 2N 则需要购买 20 台变压器。

3 级设施必须“同时可维护”，通常要求变压器和发电机等组件实现 N+1 冗余，配电组件（不间断电源 (UPS) 和配电单元 (PDU)）实现 2N 冗余。评级为 4 的数据中心不太常见，并且必须具有“容错性”——通常用于关键任务或政府数据中心设施。

顺便说一句，CSP 经常谈论“三个九”(99.9%) 或“五个九”(99.999%) 预期可用性 – 这是他们与客户之间的服务级别协议的一部分，涵盖服务的正常运行时间，其范围不仅仅限于服务的正常运行时间。单个数据中心的预期可用性。涵盖多个数据中心（“可用区”），并包括服务器和网络等组件的正常运行时间。
### From Retail Datacenters to Hyperscale Campuses
数据中心的空间成本远远低于为客户服务器供电的电气和冷却设备的成本。

平均而言，云计算工作负载的电源利用率通常为 50-60%，AI 训练的电源利用率通常为 80% 以上。企业往往甚至低于50%。

我们将设施分为三大类：
- Retail Datacenters : small facilities with a lower power capacity – at most a few Megawatts, but typically located within cities. They generally have many small tenants who only lease a few racks (i.e. a few kW). The value proposition lies in offering a strong network ecosystem by bringing together many different customers within the same facility. By offering easy interconnection to other customers and networks with low latency, operators of retail datacenters can lower customers’ networking costs. Thus, the business model of a retail datacenter operator is more akin to a traditional real estate play with its “location, location, location” value proposition.
- Wholesale Datacenters: larger facilities in the range of 10-30MW. Customers in these facilities tend to lease larger areas, i.e. a whole row or multiple rows, and with the option to further expand. In contrast to retail datacenters, the value proposition is about deploying larger capacities and having scalability over time. Many wholesale datacenters are built out in phases to attain their ultimate capacity, which means they can expand as customers’ demanded leading capacity grows. Below is an example owned by Digital Reality.
- Hyperscale Datacenters: These facilities are commonly self-built by hyperscalers for their own exclusive use, typically with individual buildings of 40-100MW each, and part of larger campuses with multiple interconnected buildings. Such campuses are rated in the 100s of MW, such as the below Google site with close to 300MW of power. Big Tech firm can also engage a colocation provider to construct a “build-to-suit” datacenter that will be built to the specifications of the hyperscaler, then leased out to the hyperscaler. Build to suit lease sizes north of 100MW are increasingly common.

  我们还可以根据运营商对数据中心进行细分：托管或自建。

  托管只是从第三方数据中心运营商以功率为单位（美元/千瓦/月）租用数据中心容量。典型的小规模租赁为 100-500kW 的关键 IT 电源，而批发规模的租赁通常为 1-5 MW。超大规模客户的租赁规模通常超过 5 MW，有时在租赁整个园区时会达到 100 MW！

  另一方面，自建数据中心是由公司私人为他们自己建造的。历史上，这是由金融、支付、医疗保健、政府、能源等敏感数据行业的大公司承担的——例如摩根大通或威瑞森。这些数据中心的设计非常异构，但每个设施的电力容量通常介于零售和批发数据中心之间。

  过去 10 年数据中心市场最具影响力的趋势是自建超大规模数据中心的兴起，这在很大程度上是由运行日益强大的推荐模型和内容交付等的云计算和社交媒体平台的兴起推动的。

  Hyperscalers also have requirements for smaller scale deployments closer to the end customers, for purposes such as network edge, content delivery networks (CDN) where colocation would is more appropriate.

  我们之前数据中心深入研究中的表格还应帮助您将这些容量数字与 AI 部署联系起来：20,840 个 Nvidia H100 集群需要一个具有约 25.9MW 关键 IT 电源容量的数据中心。随着人们现在正在构建 100,000 个 H100 集群和千兆瓦集群，这一数字仍将大幅上升。

### The Electrical System of a Datacenter
为了最大限度地减少配电损耗，我们希望保持电压尽可能高，直到物理上接近终端设备 - 电压越高意味着电流越低，功率损耗与电流的平方成正比。

但高压可能很危险，并且需要更多的绝缘，这不适合靠近建筑物 - 因此中压（例如 11kV 或 25kV 或 33kV）是向建筑物输送电力的首选解决方案。当进入数据大厅时，我们需要再次降低电压至低压（美国为 415V 三相）。

从外到内，权力遵循以下路径：

- 该公用事业公司提供高压 (>100kV) 或中压电力。在前一种情况下，需要配备电力变压器的现场变电站将其降压至中压 (MV)。
- 然后，中压电源将使用中压开关设备安全地分配到物理上靠近数据大厅的另一个变压器中，将电压降低至低电压 (415V)。
- 与变压器配对的是柴油发电机，也可输出 415V 交流电。如果电力公司停电，自动转换开关 (ATS) 将自动将电源切换至发电机。

从这里开始，有两条电源路径：一条通向 IT 设备，另一条通向冷却设备：
- IT设备路径首先经过UPS系统，该系统连接到一组电池：通常有5-10分钟的电池存储时间，有足够的时间让发电机打开（一分钟内）并避免临时断电。
- 然后，“UPS 电源”通常通过配电单元 (PDU) 直接提供给 IT 设备。
- 最后一步是通过电源单元 (PSU) 和稳压器模块 (VRM) 向芯片供电，我们在此介绍了这一点。
### High Voltage Transformers
现代超大规模数据中心当然比上图更复杂。此类园区通常设有现场高压变电站，例如下面所示的 Microsoft 站点，或上面的 Google 综合体。

鉴于在密集地点需要 >100MW，这些设施通常会放置在高压 (HV) 输电线路（138kV 或 230kV 或 345kV）附近。
在某些地区，监管机构根据电力线路的电压水平施加最大功耗。因此，超大规模企业将需要现场变电站将电压从高压降压至中压。如果没有配备高压变压器的现有变电站，数据中心运营商要么自行建造，要么资助公用事业公司建造变电站。

这些变压器的额定值以MVA为单位：MVA大致相当于MW
典型高压变压器的额定容量在 50 MVA 到 100 MVA 之间
在这种 N+1 配置中，所有三个变压器将共享负载，但以其额定容量的 2/3 运行
值得注意的是，高压变压器通常是定制的，因为每条传输线都有其自己的特性，因此往往具有较长的交货时间（>12mo）。为了缓解瓶颈，数据中心运营商可以在规划过程中预先订购它们。

尽管变压器是我们电力传输系统的核心部分，但它是非常简单的设备：它们将交流 (AC) 电源的电压和电流从一个级别更改为另一个级别。

The two major components of a transformer are copper for the coils, and steel for the “transformer core” whose role is to facilitate the transfer of energy. When dissecting the shortage of transformers, the issue is generally the latter: a specific type of steel is required, called GOES (Grain Oriented Electrical Steel), for which the number of manufacturers is limited.
变压器的两个主要部件是用于线圈的铜和用于“变压器芯”的钢，其作用是促进能量传输。在剖析变压器短缺问题时，问题通常是后者：需要一种特殊类型的钢材，称为GOES（晶粒取向电工钢），而这种钢材的制造商数量有限。

### Data Halls and Pods
A building is generally broken down into multiple Data Halls
a Data Hall is simply a room in which we place servers.

Inside a Data Hall are located multiple “Pods”, and each Pod runs off its own dedicated set of Electrical Equipment: generators (orange rectangle), transformers (green rectangle), UPS and switchgear.

Data Halls are typically broken into Pods for two reasons.
- 模块化：设施可以逐步快速扩展以适应更高的负载。
- 标准化：Pod 的尺寸旨在匹配最标准化（即便宜且容易获得）的电气设备。在 Microsoft 的示例中，我们看到多个 3MW 发电机和 3MVA 变压器 - 这些尺寸广泛应用于许多行业，并且比更大、小批量、定制的变压器更容易采购。最常见的吊舱尺寸为 1600kW、2MW 和 2.5MW，但理论上任何吊舱尺寸都是可能的。
### Generators, Medium Voltage Transformers and Power Distribution
在高压变压器的帮助下从高压（即 115kV 或 230kV 等）降压到中压(33kV、22kV 或 11kV 等)
服务器和网络交换机等典型 IT 设备无法在 11kV 下运行，因此在数据大厅内通电之前，我们需要另一套中压 (MV) 变压器，通常为 2.5 MVA 或 3 MVA，以从 MV (11kV) 降压/25kV/33kV) 至 LV（美国常见电压 415V）。

下图有助于说明典型的高压和中压配电：电力如何从高压降压到中压，然后通过中压开关设备进行分配，中压开关设备通常放置在设施外部或内部，并进行配置，以便每个数据大厅可由两个不同的电源供电，不留任何单点故障。

Inside these enclosures you will find the following devices:
- 断路器：一种电气安全装置，设计用于在电流过高时中断电流并防止火灾。
- 计量元件和继电器。
- 电流互感器和电压互感器：它们与断路器和计量设备协同工作。
- 用于打开或关闭电源的开关。
- 中压电缆。

一台 3 MW 发电机的马力超过 4,000 马力，类似于机车发动机，在超大规模数据中心中通常会找到 20 个或更多这样的装置！这些装置通常使用柴油，天然气是主要替代品。数据中心通常可以在满负荷的情况下容纳 24 至 48 小时的燃料，而柴油卓越的运输和存储便利性使其通常成为首选。柴油也更节能，但污染更多：由于监管限制，柴油发电机往往更昂贵，因为需要特定的设备来减少环境污染。

自动转换开关 (ATS) 的直接下游是不间断电源 (UPS) 系统，以确保电源永不中断。
因为其响应时间通常低于 10 毫秒，并使用以下组件：
- 逆变器：一般基于IGBT功率半导体，将电池的直流电转换为交流电，用于数据中心。
- 整流器：将交流电转换为直流电，并允许 UPS 为电池组充电 - 必须充满电才能确保电力流动。
- 电池组，铅酸或锂。铅酸电池正在被锂电池取代，尽管后者确实需要遵守严格的防火规范。
- 静态旁路开关：如果UPS出现故障，负载将自动切换到主电源。如果 UPS 需要停止服务进行维护，也可以手动切换贷款。

UPS 可能是导致效率低下的一个重要原因，通常会造成 3-5% 的损耗，并且当负载较低时，损耗会进一步加剧。现代设备可以通过在待机模式（下文中称为“VFD”）下运行并绕过 AC-DC-AC 转换将效率提高至 >99%，但这会增加传输时间几毫秒 (ms)，并带来短路风险电源中断。

现代系统是模块化的：它们不再是一个固定大小的大型单元，而是被分解成更小的“核心”，这些“核心”可以堆叠在一起并作为一个整体工作。在 Vertiv 的最新产品中，核心功率为 200kVA 或 400kVA - 相比之下，特斯拉 Model 3 逆变器可输出 200kW 的交流电源。

额定 3 级数据中心的 UPS 系统上的 2N 冗余（即“2N 配电”）是典型的。 PDU 等下游组件也将是 2N，从而实现“同时可维护”设施。

现在，我们的数据大厅内有 UPS 电源，在向 CPU、GPU 和其他 IT 组件供电之前，还需要一些其他设备。
机架通常彼此相邻放置并形成一排。在下图中，每个房间有六排，每排 26 个机架，但这当然可以有很大差异。

电力通过架空母线槽（一根实心导电金属条，通常是铜）或使用柔性电力电缆进行分配。
使用母线槽时，除了远程电源面板 (RPP) 之外，还使用配电单元 (PDU) 来管理、监控电源并将其分配给使用母线槽的各个行和机架。

使用柔性电源线时，会使用机架外部的配电单元 (PDU)，该单元还管理配电并包含各个机架的断路器。然后将这些柔性电源线直接布线到每个机架中。

为了实现冗余，母线槽成对使用，由独立的 UPS 系统供电，每个机架通常有两个母线分接单元 - 一个用于 A 侧，一个用于 B 侧，代表 2N 配电中的两个独立配电侧冗余方案。
### OCP Racks and BBUs
在追求效率的过程中，超大规模企业通常会偏离典型的部署。一个很好的例子是 Meta 十年前推出的开放计算项目 (OCP) 机架。

在 OCP 架构中，中央电源架负责将整个机架的交流电转换为直流电，而不是使用垂直机架内 PDU 向每台服务器提供交流电

电源架还可以集成电池备份单元 (BBU)，其中锂离子电池可支持几分钟的负载，充当“机架内 UPS”，从而无需任何中央 UPS。通过绕过中央UPS，电池的直流电源可以直接为IT设备供电，从而提高了效率。

这还有一个好处，即可以将数据中心所需的总电池容量减少一半，因为不再需要同时使用 A 侧和 B 侧 UPS，而仅使用单个机架内电池作为备份。这种方法的缺点是，将锂电池放置在机架内需要先进的灭火解决方案才能满足消防规范，而在中央 UPS 系统中，所有电池都可以隔离在防火室中。

### Pushing The Limits Of Traditional Datacenters
工智能的电力需求增长极快，明年每个设施 50MW+ 都不够。

在大型集群中，无论是纵向扩展网络还是横向扩展网络，我们都希望使用尽可能多的铜缆。使用铜电缆进行通信可以避免使用光纤收发器，因为光纤收发器成本高昂、耗电并会引入延迟。但当以非常高的速度传输时，铜缆的传输范围通常最多只有几米，因此，GPU 必须尽可能靠近，以便通过铜缆进行通信。

NVL72 版本是由72个GPU组成的机架，总功率超过130kW。所有 GPU 均通过超快速扩展网络 NVLink 互连，与 H100 相比，最大语言模型的推理性能吞吐量提高了 9 倍。
### Why Meta had to scrap a datacenter
Meta 拆除了整个在建建筑，因为它是他们使用多年的低功率密度的旧数据中心设计。相反，他们将其替换为全新的 AI-Ready 设计。

Meta“H”拥有多达 36 个发电机组，而 Google 有 34 个。但 Google 使用更大的发电机，并且其每座建筑物都比“H”小 >2x。在比较功率密度时，按每平方英尺千瓦计算，Google 的密度比 Meta 高 >3x。此外，考虑到其规模和复杂的结构，“H”型建筑的建造时间很长——从开始到完工大约需要两年时间，而谷歌的建筑则需要 6-7 个月。
### How to build a next-generation Blackwell Datacenter – winners and losers
[paid content]
