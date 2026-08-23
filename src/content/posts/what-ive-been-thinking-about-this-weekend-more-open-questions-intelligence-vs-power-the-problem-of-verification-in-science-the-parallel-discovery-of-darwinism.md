---
title: "What I've been thinking about this weekend - More open questions, intelligence vs power, the problem of verification in science, the parallel discovery of Darwinism"
date: 2026-04-28T08:02:08Z
category: reading
author: "Dwarkesh Patel"
description: "Dwarkesh 这组开放问题的共同底层聚焦三类更难被工程化的制度瓶颈：稀缺算力会被谁分配、权力是否会随智能自然转移、科学突破能否被短反馈 RL 可靠验证。"
source: "https://www.dwarkesh.com/p/what-ive-been-thinking-april-27"
---

## TL;DR
Dwarkesh 这组开放问题的共同底层聚焦三类更难被工程化的制度瓶颈：稀缺算力会被谁分配、权力是否会随智能自然转移、科学突破能否被短反馈 RL 可靠验证。

## 核心主张拆解
AI 算力可能变成新型稀缺政治经济资源。5 家 hyperscaler 掌握全球 70%+ AI compute，其中大量又被 OpenAI / Anthropic / Google DeepMind 这类前沿实验室预留；若最高 ROI 永远是通向奇点、机器人工厂和前沿模型迭代，普通人的娱乐、理解世界、自我增强等「非奇点用途」可能被机会成本挤出。Dwarkesh 将抽象公平问题压到机制层：compute UBI / compute redistribution 是否需要提前设计。

模型进步的真实来源仍不透明。长程 coding agent 的突破可能来自更多 RL coding environments，也可能来自更具体的数据、任务设计或训练技巧；若只是数据输入扩张，机器人等依赖 sample efficiency 的领域不会自动复制这条曲线。KV cache 暴露了一个反常 tradeoff：Llama 3 70B 每 token KV cache 约 320KB，而按预训练权重比特数 / token 数估算只有 0.075 bit/token，二者相差约 3500 万倍，说明 in-context learning 的灵活性以极高内存成本换来。

训练与推理的边界会被工作化学习侵蚀。RL generation 与 inference 的算力形态相近，区别在于前者产生学习、后者产生有用劳动；未来可想象 AI 实例被雇佣一个月完成真实任务，再把「工作报告」回传模型公司。若短程 RL 环境被榨干，on-the-job learning 可能成为继续进步的主要来源，并带来 continual learning 的赢家通吃风险：一个能在线学习且合并所有副本经验的 AI，功能上可能快速接近广义超智能。

「智能」与「权力」不能混成同一个变量。若智能定义为跨领域达成目标的能力，Trump、Xi、Putin 甚至 Stalin 都会被荒谬地推向「最智能」；现实权力更多来自合法性、信任、组织授权和大规模协作，而非孤立大脑的 galaxy-brain scheming。更合理的模型是：掌握高效 AI 工具的公司和国家以正常资本主义方式压过竞争者，普通但握有缰绳的人类领导层被超级服从的 AI 科学家和工程师放大。

科学发现的验证循环远比 coding / math 敌意。哥白尼体系在 1543 年并不明显优于托勒密：精度更差、简洁性也未必更强；恒星视差要到 1838 年才测得，Venus phases 虽被预言但也兼容第谷模型。海王星与 Vulcan 的对称案例更尖锐：同样是牛顿体系下的轨道异常，一个导向新行星，一个最终导向广义相对论；事前很难判断某研究纲领是在进步预测，还是靠 epicycle 式补丁续命。

AI for science 的难点因此从生成假设延伸到保留长期、偏执、互相竞争的研究路线。Prout 的整数原子量假说面对氯 35.5、35.46 等异常长期像失败补丁，直到同位素概念出现才被重新理解；大突破常要几十年至上百年才显出生产力。若要让 AI 参与科学，系统可能需要一群带有不同启发式和顽固偏见的 AI scientist，而非一个被短期 verifier 优化出的统一最优模型。

达尔文主义说明「概念简单」不等于「历史上可提前发现」。自然选择比牛顿引力在概念上更容易，却缺少决定性检验；它依赖 Lyell 的 deep time、地质学、古生物学、殖民航海的生物地理材料、人工选择经验等一系列 intuition pumps。Darwin 和 Wallace 几乎同时到达，提示平行发现往往由知识脚手架成熟触发，而不是某个天才早该想到却没想到。

## 值得质疑
这篇更像研究问题清单，许多判断还没有被压成可检验论证。算力再分配、机器需求经济、AI 生成互联网数据污染、continual learning winner-take-all 都是高价值问题，但文中主要负责定位问题，不负责给机制答案。

「智能不等于权力」的切分有解释力，但可能低估了 AI 被嵌入机构后学习 persuasion、bureaucracy navigation、coalition-building 的速度。现实权力来自组织授权；一旦 AI 成为组织运行层，抽象智能与权力技能可能重新耦合。

科学验证循环漫长这一点削弱了「AI 靠 RL 自动做科学」的叙事，但也留下制度问题：如果需要同时资助许多顽固研究纲领，谁决定资源分配、何时停止、如何避免把噪声包装成长期主义？

## 更大意义
前沿 AI 的关键风险可能来自算力、机构、验证制度和长期学习机制共同重排社会竞争结构；单个超级大脑突然 outsmart everyone 只是较窄叙事。真正稀缺的会是把智能转化为可靠知识与正当权力的制度设计。

## 模型
OpenAI Codex GPT-5.5
