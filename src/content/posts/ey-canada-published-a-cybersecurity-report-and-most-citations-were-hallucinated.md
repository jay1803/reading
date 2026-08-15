---
title: "EY Canada published a cybersecurity report and most citations were hallucinated"
date: 2026-05-31T08:00:59Z
category: reading
description: "GPTZero 的调查把“vibe citing”从学术论文问题推进到咨询业信任问题：EY Canada 一份 2025 年网络安全报告疑似混入伪造引用、错配来源、互相冲突的数据，并因 Big Four 品牌背书进入新闻和 AI 检索语料，后续研究者很难一眼识别污染源。"
source: "https://gptzero.me/investigations/ey"
---

## TL;DR
GPTZero 的调查把“vibe citing”从学术论文问题推进到咨询业信任问题：EY Canada 一份 2025 年网络安全报告疑似混入伪造引用、错配来源、互相冲突的数据，并因 Big Four 品牌背书进入新闻和 AI 检索语料，后续研究者很难一眼识别污染源。

## 关键发现
- 被调查对象是 EY Canada 的 44 页报告《Points of Attack: Uncovering Cyber Threats and Fraud in Loyalty Systems》，主题是忠诚度积分系统中的网络威胁与欺诈。
- GPTZero 称报告的资源表集中在第 41-43 页，很多 URL 已失效或疑似虚构，超过一半标题无法对应到真实来源。
- 报告一处称全球 loyalty points 市场规模为 2000 亿美元，且 30-50% 积分未被使用；另一处又把 2000 亿美元说成全球未兑换积分价值，两组表述无法同时成立。
- 一条“McKinsey & Company: Loyalty Economics Report (2022)”引用被指向一个并不存在的报告；GPTZero 追溯后认为它可能从 Financial IT 的低质量金融科技博客中被原样洗入 EY 报告。
- “72% loyalty programs reported theft or fraud”一项数据在报告不同页面被归因给 Paystone 和 Forter，但两者都不是原始来源，原始来源可能是 2017 年 Ipsos 调查。
- “fraud attacks increased 89% since 2019”又被另一页改写成 2018 到 2019 单年增长；Forter 的 2019 Fraud Attack Index 部分支持后者，但不支持前者这种宽泛表述。

## 为什么重要
这类错误的杀伤力来自权威传递链。低质量博客可以制造伪来源，Big Four 报告可以把它包装成咨询业材料，新闻报道再引用咨询报告，AI deep research 和搜索摘要继续把它当作可信网页信号吸收。

GPTZero 提到该 EY 报告已被 Canberra Times 一篇关于 Qantas loyalty points phishing 的文章引用，并被澳大利亚 60 多家报纸转载。即使原报告传播不广，引用链也能让错误信息跨地区扩散。

## 值得质疑
这篇调查本身来自 GPTZero，并在结尾推广自家的 Hallucination Check 产品，所以它既是调查文本，也是产品案例。文章说结果经过人工核验，但没有在正文中公开完整核验表；因此更适合作为“强烈风险信号”，不应单独当作最终审计结论。

## 更大意义
AI 生成文本最危险的部分未必是措辞像机器，而是把不可验证的引用变成可被后续系统复用的“网络事实”。一旦错误进入高权重机构网页，人工读者、新闻编辑和 AI 代理都会更倾向于继承它，而不是重新追溯源头。
