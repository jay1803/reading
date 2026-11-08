---
title: "The Pelican comparison grid for Astra is pretty interesting"
date: 2026-11-08T12:37:18Z
category: reading
description: "GPT-6 Astra 的 low 档只花 9.55 美分，画出的骑车鹈鹕 SVG 就超过 GPT-5.6 Sol 所有推理档位；token 单价更高，但用量少得多，实际成本差距缩小。"
source: "https://simonwillison.net/2026/Sep/4/astra-pelicans/"
---

GPT-6 Astra 在“生成骑自行车的鹈鹕 SVG”这项测试中，同时提高了图像质量和单次支出的回报：最低推理档 low 花费 9.55 美分，效果已经超过 GPT-5.6 Sol 的所有推理档位。Simon Willison 获得 Astra 访问权限后，分别测试了 low、medium、high、xhigh 和 max 五档推理强度，并将结果与 GPT-5.6 Sol、Terra、Luna 放进同一张比较网格；Astra 不支持关闭推理的 none 档。

视觉上的提升贯穿 Astra 的各档输出。Willison 认为 Sol 最好的版本是 xhigh，甚至优于 max，但画面仍明显像一组抽象形状；Astra 从 low 到 xhigh 的每张图都超过了这个水平，max 档尤其出色。不过，整体形象更逼真并不代表空间关系已经可靠：低于 max 的 Astra 仍不能稳定地把鹈鹕两条腿分别画在自行车车架两侧。

这种质量优势也改变了价格比较。Astra 每百万 input tokens 收费 10 美元、每百万 output tokens 收费 50 美元，Sol 对应为 5 美元和 30 美元；尽管 Astra 的 token 单价更高，它在各推理档位消耗的 tokens 显著更少，因此实际单次费用的差距被缩小。在这项测试中，同样花约 10 美分，其他模型的结果都明显逊于 Astra low，说明单看 token 标价会漏掉完成任务所需用量与最终质量的差异。

比较网格还暴露出一个模型关系上的线索：相同任务中，Astra 和 Luna 的输入计数都是 16 tokens，Sol 和 Terra 则都是 26 tokens。Willison 据此提出疑问：Astra 与 Luna 的关联是否比 OpenAI 已披露的更深？这组计数尚不足以证明模型之间的亲缘关系，却让一次绘图测试同时呈现了能力、实际成本和输入编码差异。
