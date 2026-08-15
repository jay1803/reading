---
title: "Energizing AI: Power Delivery Competition Heats Up Vicor, MPS, Delta, ADI, Renesas, Infineon"
date: 2024-10-23T17:36:44Z
category: reading
description: "人工智能加速器变得越来越耗电。 Nvidia H100 的热设计功率 (TDP) 为 700 瓦 (W)，而世界上最常安装的数据中心 CPU（Intel Skylake/Cascade Lake）的热设计功率 (TDP) 还不到 200 瓦。"
source: "https://www.semianalysis.com/p/energizing-ai-power-delivery-competition"
---

人工智能加速器变得越来越耗电。 Nvidia H100 的热设计功率 (TDP) 为 700 瓦 (W)，而世界上最常安装的数据中心 CPU（Intel Skylake/Cascade Lake）的热设计功率 (TDP) 还不到 200 瓦。

因此，我们现在看到机架级到芯片级的电力传输网络正在重新架构，以解决人工智能训练和推理等耗电计算工作负载中的问题。
先进的电力传输架构的主要目的是提高效率。

电力输送公司 Vicor 一直是历史上从这一趋势中受益最多的公司之一。在过去的十年中，Vicor 从一家商品电源组件供应商进入了先进的数据中心电源应用领域，并在来自 Nvidia、Google、AMD、Cerebras、Tesla 和 Intel 的各种超大规模数据中心机架级电源解决方案和 AI 加速器中获得了设计胜利。

Vicor 的命运最近发生了迅速变化。正如我们一年多前独家发现和披露的那样，Monolithic Power Systems 能够在 Nvidia 的 H100 GPU 中取代 Vicor 。此外，Vicor 的第二大客户的关系也很混乱。此外，超大规模数据中心机架电源解决方案也发生了许多变化，包括多个新竞争对手 (MPS, Delta, Renesas, Infineon, ADI).
### Power Delivery for Chips, Primer
电力通过交流电 (AC) 产生并在电网中传输，电压高达数十万。计算和存储芯片需要的是稳定且清洁的电源，即电压低得多且采用直流 (DC) 形式的电源。过高的电压会过载并损坏芯片的精密电路。电压太低，芯片电路将无法正常切换。变压器、电源单元 (PSU) 以及最后的稳压器模块 (VRM) 负责向芯片提供正确类型的电源。随着电力需求的增加，高效电力传输也变得更具挑战性。

### What makes up a Voltage Regulator Module (VRM)?
VRM 是一组重要的部件，它从系统 PSU 获取输入电压，然后将其转换为正确的电压以为 SoC 供电。通常，我们会在容纳芯片的 PCB 上看到 VRM，但在极少数情况下，这些组件可能位于封装本身上，甚至集成在硅片上。现代 VRM 有 3 个主要部分：电容器、电感器和功率级。电容器存储电能，然后以恒定速率释放该能量，从而平滑传输到处理器的功率。电感器用于抵抗电流变化并防止大量电流尖峰损坏处理器。
### Higher Power, Lower Efficiency
如果您要将芯片的 12 伏输入电压降低到 0.8 伏（降低 15 倍），这意味着电流需要从 12 伏时的 60 安培增加到 0.8 伏时的 875 安培（增加 15 倍） ）。与耗电较少的CPU相比，GPU的电流要高得多。正如我们从 P = R*I 2方程中得知的那样，较高的电流意味着较高的电阻损耗（损耗是电阻乘以电流的平方）。

当我们将电压降低至 0.8V 时，电阻会急剧恶化：电流增加 15 倍，导致电阻损耗呈指数级增加 225 倍。这说明效率损失如何成为最近几代数据中心芯片的一个大问题。随着工艺尺寸的缩小，电压持续下降，先进的封装使封装变得更大、更耗电，这种情况只会变得更糟。
### The Rise Of 48 Volt
为了解决这个问题，正在使用更高的输入电压。长期以来，12V 直流 (DC) 电源一直是电子产品 PSU 提供的标准电压。 12V 电压在其工作效果足够好时被引入，因为瓦数足够低，因此由此产生的效率损失并不重要。随着行业开始要求更高瓦数和更低电压的 SoC，导致效率受到双重打击。这些效率损失超过了相对便宜且普遍存在的 12V 组件所带来的好处。

从 12V 变为 48V 意味着所需电流减少 4 倍，因此损耗将降低 16 (4 ^2 ) 倍。这就是许多公司转向 48V 供电网络的原因。但如果你还是要降到 1V，那还有什么意义呢？

2016 年左右，Google 是第一家在其数据中心采用 48V 电源的超大规模企业，并推动 OpenCompute 联盟对 48V 进行标准化。
### Vicor’s Rise
Vicor 是为计算用例提供 48V VRM 的主要参与者。

Vicor 的第一个主流商用芯片设计是 2018 年 Nvidia 的 V100 SXM3 更新版。它采用了使用 Vicor 组件的 48V VRM。然后是 A100，整个系列都使用 Vicor VRM 部件。

从那时起，当 Vicor 被设计在 H100 中并被 SemiAnalysis 首先爆料的 Monolithic Power Systems (MPS)取代时，这种叙述就被违反了。这份独家报告发布后，Vicor 的股价在发布后的第二天早上就下跌了 20% 以上，并且由于 Nvidia 对 Vicor 收入的巨大贡献，在接下来的一年里又下跌了 30%。直到今天，Vicor 仍然没有在Nvidia 的 H100 中实现批量出货，而 Nvidia H100 的出货量正在大幅增加。
