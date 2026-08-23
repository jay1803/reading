---
title: "Elon Dreams and Bitter Lessons"
date: 2024-10-22T15:39:50Z
category: reading
author: "Ben Thompson"
description: "To review the levels of automation:"
source: "https://stratechery.com/2024/elon-dreams-and-bitter-lessons/"
---

To review the levels of automation:
- Level 0: Limited features that provide warnings and momentary assistance (i.e. automatic emergency braking)
- Level 1: Steering or brake/acceleration automation (i.e. cruise control or lane centering)
- Level 2: Steering and brake/acceleration control, which must be constantly supervised (i.e. hands-on-wheel)
- Level 3: Self-driving that only operates under pre-defined conditions, and in which the driver must take control immediately when requested
- Level 4: Self-driving that only operates under pre-defined conditions, under which the driver is not expected to take control
- Level 5: Self-driving under all conditions, with no expectation of driver control

但话又说回来，较高的成本结构本身就限制了可扩展性； Waymos 非常棒，但他们需要以更便宜的价格来改变世界。

Rich Sutton wrote one of the most important and provocative articles about AI in 2019; it’s called [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html):
> The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin. The ultimate reason for this is Moore’s law, or rather its generalization of continued exponentially falling cost per unit of computation. Most AI research has been conducted as if the computation available to the agent were constant (in which case leveraging human knowledge would be one of the only ways to improve performance) but, over a slightly longer time than a typical research project, massively more computation inevitably becomes available. Seeking an improvement that makes a difference in the shorter term, researchers seek to leverage their human knowledge of the domain, but the only thing that matters in the long run is the leveraging of computation. These two need not run counter to each other, but in practice they tend to. Time spent on one is time not spent on the other. There are psychological commitments to investment in one approach or the other. And the human-knowledge approach tends to complicate methods in ways that make them less suited to taking advantage of general methods leveraging computation. There were many examples of AI researchers’ belated learning of this bitter lesson, and it is instructive to review some of the most prominent.

Waymo 没有试图明确制定一系列车辆要遵循的规则（例如“留在车道上”和“不要撞到其他车辆”），而是像LLM一样训练模型。该模型通过尝试预测真实道路上人类驾驶车辆的轨迹来学习驾驶规则。

Sinavski 指出的一个大问题是 Wayve 尚未找到一种“真正擅长空间推理”的视觉语言模型。如果您是《理解人工智能》的长期读者，您可能还记得当我要求领先的LLMs通过模拟时钟判断时间或解决迷宫时。 ChatGPT、Claude 和 Gemini 都失败了，因为今天的基础模型不善于进行几何思考。

多年来，马斯克在自动驾驶方面对现有特斯拉车主的承诺过多，但兑现却不足，因此，目前的汽车是否能获得完全无人监督的自动驾驶，目前还没有定论。
