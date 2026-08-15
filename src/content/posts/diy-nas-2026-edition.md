---
title: "DIY NAS: 2026 Edition"
date: 2025-11-30T20:20:18Z
category: reading
description: "自组 NAS 的真实门槛从来不是选主板或机箱，而是\"配件价格已经在反映宏观经济的烂透了\"——作者差点因此不出 2026 年度版。在涨价浪潮下，这套方案的核心命题是：用 Topton N22（N355, 8核, 15W, 8×SATA, 10GbE）+ JONSBO N4 + TrueNAS CE，以 ~$400..."
source: "https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html"
---

## TL;DR
自组 NAS 的真实门槛从来不是选主板或机箱，而是"配件价格已经在反映宏观经济的烂透了"——作者差点因此不出 2026 年度版。在涨价浪潮下，这套方案的核心命题是：用 Topton N22（N355, 8核, 15W, 8×SATA, 10GbE）+ JONSBO N4 + TrueNAS CE，以 ~$400 可压缩成本实现超出网速上限的存储性能。

## 核心洞见
- **主板是唯一真正升级的选择**：Topton N22 比上一代 N18 多出 2 个 SATA 口（共 8 口，+33% 容量上限）和 PCIe x1 扩展槽；N355 CPU 8 核 / 15W TDP 对纯 NAS 功能是过剩，但给 VM / 容器自托管留了大量余量。
- **机箱性价比陷阱**：JONSBO N4 比同类便宜 $20-40 的原因是四个 3.5" 托架没有 SATA 背板，接线极度反人类——作者建议"先装这四个盘再做任何事"，否则重装一次。
- **功耗实测**：空闲 ~67W 均值，满载传输峰值 237W；108 小时全流程总耗电 7.17 kWh。
- **网络是瓶颈，不是存储**：SMB 基准下，flash pool（NVMe mirror）顺序读写超过 SATA SSD 速度，并几乎跑满 10GbE 接口；HDD pool（RAID-Z2）顺序读 ~544 MB/s，随机读 IOPS 受限于机械盘本身。
- **Burn-in 是必须步骤，不是可选项**：新硬件故障率峰值在开始使用时，Memtest86+（3+ passes）+ fio + Spearfoot 磁盘脚本是最低保障。

## 具体机制
完整 BOM 关键决策链：
1. **主板/CPU**：Topton N22（AliExpress）→ N355 CPU（8核 / 3.9GHz boost / Intel Quick Sync）
2. **机箱**：JONSBO N4（6×3.5" + 2×2.5"，Micro-ATX 容积但装 Mini-ITX 主板显宽松）
3. **散热**：Noctua NF-A12x25 PWM 替换自带风扇，接主板 SYS_FAN 头以便 BIOS 调速
4. **电源**：SilverStone SX500-G（SFX, 500W, 80+ Gold）
5. **启动盘**：2×128GB Silicon Power A55 SATA SSD（<$30/块）
6. **VM/App 盘**：2×Silicon Power 1TB M.2 NVMe（PCIe 3.0 x1，速度受限于单 lane）
7. **数据盘**：作者用退役 8TB HDD × 8 跑 RAID-Z2；建议新购时多家供应商分批买
8. **系统**：TrueNAS CE 25.10.0.1（Goldeye，Early Adopter 通道）

节省 $400 的 EconoNAS 路径：降低 CPU 规格、换小容量 RAM、用更便宜机箱。

## 隐藏限制
- M.2 NVMe 槽仅 PCIe 3.0 ×1，不是 ×4；选"好价格而非高性能" NVMe 是正确策略，但别误以为这是全速 NVMe。
- JONSBO N4 四个无背板盘位需要手工走线，热插拔不可行，且线缆管理会顶住风扇——用扎带能解决，但增加维护复杂度。
- 价格窗口不稳定：DDR5、HDD、AliExpress 主板均处于涨价通道，文章发布时刻已是"趁现在囤"的心态。

## 备注
作者将这台机器挂 eBay 无底价拍卖处置；对想"用成品替代 DIY"的人，他也暗示即将出独立文章评估现成 NAS 的 TrueNAS 兼容机。
