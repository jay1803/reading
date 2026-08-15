---
title: "State of AI Report 2023"
date: 2023-10-17T19:37:40Z
category: reading
description: "官方总结的关键要点："
source: "https://mp.weixin.qq.com/s/MpU2ZLKBcVvzQlSqwtx-QQ"
---

## Summary
官方总结的关键要点：
- GPT-4 is the master of all it surveys (for now). GPT 是现在 AI 界大佬，无论是从传统基准测试还是人类的考试中都超越其他的 LLM。
- Efforts are growing to try to clone or surpass proprietary performance. 在一些专有领域上越来越下功夫，比如用更小的模型、更好的数据、更长的上下文来寻求更好的 AI 表现。
- LLMs and diffusion models continue to drive real-world breakthroughs. LLM 和 diffusion 模型还是引领世界，在多个领域
- Compute is the new oil. 算力是新的石油。算力将会是未来 AI 角逐中的必争资源。
- GenAI saves the VC world, as amid a slump in tech valuations. GenAI 拯救了风投圈，确实现在的 AI 公司最受 VC 追捧。
- The safety debate has exploded into the mainstream 关于安全性的讨论已经被逐渐摆上台面，成为主流
- sChallenges mount in evaluating state of the art models 评估模型是否先进变得越来越难。

我自己看到觉得有意思的：
- AI 发展的迅猛趋势，最长能延续到什么时候（这个有关投资和回报周期），根据 EpochAI 的预测：
  - 到 2030 年至 2050 年，我们将耗尽低质量语言数据的库存
  - 到 2026 年之前，我们将耗尽高质量语言数据
  - 到 2030 年至 2060 年，我们将耗尽视觉数据
- AI 目前最受关心的局限 - context length 有没有改善的可能。
  - 当输入长度过长时，模型的性能会下降
  - 专有模型比通用模型更不容易出现问题
  - 可能需要在架构方面创新
- 关于 Prompt Engineering，我们众所周知 prompt 对 AI 的表现影响很大，有两种改善你 prompt 的方法：
  - Chain of Thought prompting (CoT)，通过让 AI 自证它的每一步推理来提升表现
  - Tree of Thought (ToT)，通过多次举例或采样来提升表现
- AI Agent，让 AI 去使用我们的软件。（比如 ChatGPT 插件等等）
- 在图片、视频生成、还有抠图领域都有了不小的进展。尤其是图像生成上，不用像之前一样得重新写 prompt 然后再重新生成了，可以用比如 InstructPix2Pix 让你可以微调，Imagen Editor 则是将图像“分层”，让你可以对某个区域进行编辑
- 音乐生成方面，Google 出了 MusicLM，Meta 出了 MusicGen。
- 美国在 AI 研究方面的影响力最大，过去三年 70% 的被引用最多的 AI 论文都来自美国。
- 算力：2023 年 NVIDIA 的市值进入万亿俱乐部，比 10 年前增长了 130 倍。
- 美国对芯片出口的管制越来越严格，导致很多芯片公司在其他国家（尤其是中国）的营收下滑，但它们也出品了刚好能绕过限制的芯片销往这些国家。
- 沙特阿拉伯国王阿卜杜拉国王科技大学（KAUST）已经购买了超过 3,000 枚 H100 GPU，用于构建名为 Shaheen III 的超级计算机.....所以算力是新石油，沙特就开始屯新石油了是吗....（该大学以研究 LLM 为主，其研究人员主要是中国国籍，因为他们所在的大学受到限制，无法进入美国....）
- StackOverflow 网站的流量被 ChatGPT 打掉一半
- ChatGPT 在帮助写作方面，可以帮作者减少 40% 的时间，提升 18% 的输出质量
- Midjourney 和 Discord 双赢，Midjourney 的用户数从去年同期的 200 万增长到了 1480 万。而每个月有超过 3000 万人在 Discord 上使用 Midjourney
- ChatGPT 的用户留存率和活跃度都不如传统 app。这个我之前写过。
- 美国版权局开始研究 AI 对版权法的影响，并发布了新的版权指南。OpenAI 和 Meta 都会被一些传统内容公司起诉，版权这块所有人都还不知道怎么弄
- 2023 上半年投资于 AI 领域的资金与 2022 年上半年持平...说明没有更多的热钱涌入啊，可能进入了一个暂时的平缓期。大厂无疑还是这场 AI 革命中的关键推动者，无论是从技术革新还是人才流动方面。
- 2023 年美国 AI 公司吸引了全球私募资金的 70%。2022 年是 55%。美国目前有 315 个 AI 独角兽，中国有 70 个，英国有 27 个，以色列 14 个，德国 12 个，剩下的都是 10 个以下。
- 企业软件、Fintech、医疗是 AI 获投最多的领域
- 2023，VC 投资的 24% 流向了 AI 公司。不过只有少数几家占了最多的钱，OpenAI 一家遥遥领先。与其他创业公司比，AI 领域的种子轮融资规模增长了 33%，A 轮融资规模增长了 130%。
## State of AI：2023 年度人工智能报告之 Research 篇
## State of AI: 2023 年度人工智能报告之 Politics 与 Safety
## State of AI: 2023 年度人工智能报告之 Industry 篇
