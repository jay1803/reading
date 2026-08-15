---
title: "TPU Deep Dive"
date: 2025-06-24T10:15:49Z
category: reading
description: "TPU以“硬软协同 + 规整数据流”为核心：在芯片侧用大规模systolic array配合深流水、加大片上存储（CMEM/VMEM/SMEM）并缩小HBM；在软件侧以XLA的Ahead-of-Time编译与图并行（如GSPMD）统一切分与通信调度，从单芯片到多Pod实现极强扩展性；由此获得高吞吐与能效，但对稀疏..."
source: "https://henryhmko.github.io/posts/tpu/tpu.html"
---

## TL;DR
TPU以“硬软协同 + 规整数据流”为核心：在芯片侧用大规模systolic array配合深流水、加大片上存储（CMEM/VMEM/SMEM）并缩小HBM；在软件侧以XLA的Ahead-of-Time编译与图并行（如GSPMD）统一切分与通信调度，从单芯片到多Pod实现极强扩展性；由此获得高吞吐与能效，但对稀疏/不规则计算（如MoE）并不天然友好。

### 主题
#### 设计哲学与定位
TPU的两大支柱是“systolic array + 深度流水线”和“AoT编译（XLA）”。前者依赖高度规整的数据流（矩阵乘、卷积），后者在编译期做算子融合、切分与通信编排，从而在体系结构上减少控制与访存开销、把性能压到上限。

#### 单芯片结构（以TPUv4为例）
单芯片包含两个TensorCore（推理型TPU常为一个），共享CMEM（约128MiB）与HBM（约32GiB）。每个TensorCore由：
- MXU：128×128的systolic array，承担主矩阵乘。
- VPU：逐元素运算与归约。
- VMEM：约32MiB的向量缓冲，从HBM搬入后才能计算。
- SMEM：约10MiB的标量存储与控制/寻址。
相较GPU：TPU片上存储更大、HBM更小；GPU（如H100）则是小L1/L2（约256KB/50MB）、大HBM（约80GB）、海量小核。

#### 吞吐与规模
- 单芯片：TPU v5p约500 TFLOPs/s。
- 单Pod：v5p满配8960芯片约4.45 ExaFLOPs/s。
- 新一代：TPUv7“Ironwood”单Pod（9216芯片）最高约42.5 ExaFLOPs/s。

#### Systolic array：优势与局限
优势在于数据一旦灌入阵列，控制逻辑与中间访存极简，适合规整算子（matmul/conv）并易于与DMA/流水线重叠。局限在于对同尺寸稀疏矩阵不提速，PE仍按周期工作；若行业更偏好非规整稀疏（如MoE），需额外机制应对。

#### 硬软协同与XLA编译
通过硬件（大阵列+大片上存储）与XLA（AoT）协同，减少对层级缓存的依赖；XLA在编译期决定分片策略、流水顺序与collective（如all-reduce）分解，并能跨切片/跨Pod统一调度通信（如多Pod“multislice”训练）。

#### 内存与数据流
计算遵循“HBM → VMEM → 阵列”的上料路径；片上CMEM/VMEM/SMEM容量相对更大以承载更粗粒度的tile与更少的回写；通过流水线重叠搬运与计算，提升有效利用率。

#### 互联拓扑与切片
- Rack层：64芯片组成4×4×4的3D torus。
- Pod与Slice：TPUv4的“Superpod”约4096芯片（64个Rack），TPUv7约9216芯片；通过OCS（光交换）把多个Rack连接为Pod，并可灵活切出非连续的“slices”。
- 拓扑可变：为all-to-all密集的工作负载可从规则torus切换为“twisted torus”，缩短跨面通信路径。
- 多Pod（Multislice）：跨Pod训练由XLA把跨slice与slice内的通信collective一起分解与调度。

#### 物理形态速写
一行可见两块tray（每tray含多颗TPU），典型每行约8颗芯片；单芯片封装中心为ASIC，四周为HBM堆叠（TPUv4含2个TensorCore因而有4个HBM堆）。TPUv4i（推理）平面图显示CMEM面积占比明显。

#### 实践含义
- 算子选择：规整密集算子（matmul/conv）收益最大；不规则稀疏需权衡或改写。
- 并行策略：利用GSPMD在图级做数据/模型/专家维度的切分，结合XLA让通信靠近硬件拓扑。
- 切片与拓扑：为all-to-all重的训练优先选择更“扭转”的拓扑切片；常规场景选择规则torus性价比更高。

### 总结
TPU以大阵列+大片上存储配合XLA的编译期并行/通信编排实现高吞吐与强扩展；强项在规整密集计算，弱项在非规整稀疏场景。
