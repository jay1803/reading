---
title: "The tech of 'Terminator 2' – an oral history (2017)"
date: 2026-07-12T08:02:55Z
category: reading
description: "1991 年《终结者 2》上映时，ILM 的 CG 部门只有 12 到 15 人。T-1000 的每一个视觉效果背后，都是一个专门写出来的工具。Body Sock、Make Sticky、MORF、Chan Math、poly-alloy shader——这些名字今天听起来像教科书词条，当时却是工程师在 80 小..."
source: "https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/"
---

## T2 的每个 CG 工具都是为这部电影从零发明的

1991 年《终结者 2》上映时，ILM 的 CG 部门只有 12 到 15 人。T-1000 的每一个视觉效果背后，都是一个专门写出来的工具。Body Sock、Make Sticky、MORF、Chan Math、poly-alloy shader——这些名字今天听起来像教科书词条，当时却是工程师在 80 小时工作周里临时发明的一次性解决方案。现在任何 3D 软件都内置的骨骼蒙皮、UV 锁定贴图、形态插值，在 1990 年都不存在。

## T-1000 的五个阶段

Spaz Williams 将角色分解为 RP1–RP5 五个版本：无定形液态团（RP1）→ 平滑人形（RP2，内部叫"Oscar"）→ 柔性金属警察（RP3）→ 锐利金属警察（RP4）→ 真人 Robert Patrick（RP5）。五个版本共享完全相同的控制顶点数量，只是用平滑算法压扁或还原。没有动作捕捉——Williams 把 Robert Patrick 身上画上四英寸方格，用两台 VistaVision 摄影机从正面和侧面同时拍摄，再手动逐帧 rotoscope。Patrick 跑步时磨破了脚，而 Williams 发现他的足球伤腿有轻微跛行，还要在骨架动画里修正这一点——因为 T-1000 应该走路像机器。

## 核心工具

- *Body Sock*（Enderton、Natkin、Hu、Frederick）：B-spline patch 动画时关节处会裂开，Body Sock 在每帧自动缝合所有接缝。膝盖、胯部、三面或五面汇聚的角点各有不同的混合数学。今天这功能内置在每个软件的蒙皮权重里。
- *Poly-alloy shader*（Alex Seiden）：没有光线追踪，用动画化的反射平面和 RenderMan hit-test 模拟液态金属反射。Dennis Muren 要求加入漫反射"铅灰"分量，否则 T-1000 没有质感。Stefen Fangmeier 在火焰穿行镜头里把火焰素材贴到场景卡片上逐帧驱动反射。
- *Make Sticky*（Tom Williams）：把贴图坐标"钉"在变形几何体上，防止 UV 滑动——头部穿越牢笼镜头的核心。原名 Make Me Sticky，因不雅被改名。
- *MORF*（Doug Smythe）：最初为 Willow（1988）写的 2D 变形工具，后移植到 SGI 用于 T2。John Berton 在"Turnaround"镜头里用它实现衬衫拉链式的风格化变形，暗示 T-1000 有些炫耀个性。
- *Chan Math*（Natkin）：把 Alias 的 pivot point 动画坍缩归零的脚本语言，用于 Splash Head 镜头的缝合，否则所有 pivot 在动画过程中会飞遍整个场景。
- *Ray casting tool*（Enderton）："Head through floor"镜头——从参考平面射线打到面部+地板的混合表面，在交点处生成新控制顶点，形成皮肤状覆盖层。Liza Keith 因调不好而不去看 dailies 的那天，镜头突然成功，现场自发鼓掌。

## 被忽视的技术代价

死亡序列的熔化效果用随机分形位移。Natkin 住在旅馆里缩短通勤，每天拿新 random seed 给 Dennis Muren 看。Muren 在低分辨率（640 像素）版本定稿时说"就这个，发货"，拒绝再渲染高分辨率版——这帧在正式上映的胶片里确实偏模糊。Natkin 还有数周时间不明白为何颜色每天被"纠正"回去，后来才发现是光学部门的手工调色师在每一帧上"修正"他的色彩，双方完全没有沟通。

## 规模与遗留

T2 共 50 个 CG 镜头，6 个月，团队从 12 人扩张至 40 人（CG 部门），ILM 整体随后扩张到 300 人。1990 年 1GB 存储约 9000 美元；购置"百万美元计算机"对当时的 Enderton 来说是"大到荒唐"的数字。ILM 选 Alias 而非行业主流 Wavefront 本是争议决定；T2 的成功直接为 Alias 正名，成为此后行业标配软件的起点。
