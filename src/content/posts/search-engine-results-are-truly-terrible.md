---
title: "Search engine results are truly terrible"
date: 2026-05-16T08:04:15Z
category: reading
description: "现代搜索的核心失败在默认入口：广告、AI 概览、SEO/AI 垃圾与浅层内容把正确答案挤到用户很少继续翻的位置；即使高质量结果真实存在，只看前 3–5 条时，命中好答案几乎接近抛硬币。"
source: "https://maurycyz.com/misc/search/"
---

## TL;DR
现代搜索的核心失败在默认入口：广告、AI 概览、SEO/AI 垃圾与浅层内容把正确答案挤到用户很少继续翻的位置；即使高质量结果真实存在，只看前 3–5 条时，命中好答案几乎接近抛硬币。

## 核心主张拆解
### 测试对象
作者用 5 个查询测试 Google、Bing、Kagi、DuckDuckGo、Marginalia 与 ChatGPT：广告拦截器推荐、钼的最低 K-alpha 发射能量、光电二极管电路、飞机机翼原理、直流有刷电机为何高速更高效。

### 总体结果
没有任何工具稳定给出好结果。主流搜索经常把正确页面排在垃圾、广告、AI 摘要或内容农场后面；ChatGPT 能答对简单事实和常识推荐，但在需要机制解释时容易复述同一批垃圾页面的错误。

### 评分分布
- Google：Bad / Ok / Crap / Ok / Crap
- Bing：Bad / Ok / Crap / Ok / Crap
- Kagi：Crap / Ok / Bad / Ok / Crap
- DuckDuckGo：Ok / Ok / Bad / Ok / Crap
- Marginalia：Crap / Crap / Crap / Crap / Ok
- ChatGPT：Good / Good / Bad / Crap / Crap

## 关键证据
### 广告拦截器
合理答案应优先推荐 uBlock Origin 或 DNS 级方案，因为浏览器扩展拥有高权限，付费且难取消的“可接受广告”扩展风险更高。Google、Bing、Kagi 都把 AdBlock/AdBlock Plus 或类似付费扩展排得过高；DuckDuckGo 至少在前三给出 uBlock；Kagi 前五没有 uBlock。

### 钼 K-alpha 能量
正确答案是 Kα2 的 17,374 eV，而不是 Kα1 的 17,479 eV。多个搜索 AI 摘要把“最低能量”误判成 Kα1；Kagi 的 AI 摘要甚至给出 0.709 eV 这种差四个数量级的结果。传统结果里 LBL、Horiba、HyperPhysics 等表格能提供正确值，但 AI 摘要会把好来源读错。

### 光电二极管电路
合理答案应指向跨阻放大器，并补充反馈电容、带宽、自举、对数转换等实际设计问题。Google/Bing/DDG/Kagi 多数结果是广告页、坏电路、泛泛视频或论坛片段；Hamamatsu 的应用笔记是可用资料，却只出现在 Kagi/DDG 的第 5 条附近。ChatGPT 说出“跨阻放大器”，但画出的示意图不可用。

### 机翼升力
作者接受的简单正确模型是“机翼把空气向下推，因此飞机获得向上升力”。搜索结果仍大量出现 equal-transit 或半截 Bernoulli 解释；这些解释要么违反动量直觉，要么无法解释倒飞、平板翼和纸飞机。Google、Bing、Kagi、DuckDuckGo 都能在前几条找到部分好结果，但 AI 摘要和浅层页面仍会误导。

### 有刷电机高速效率
核心机制是机械功率等于扭矩乘转速，而线圈电阻损耗主要随电流变化，不随转速直接下降；低速时每转损耗更高，所以电机通常应接近空载转速运行并用齿轮降速。主流搜索几乎全是“有刷 vs 无刷”的 AI 垃圾内容，答非所问；Marginalia 反而找到 Rochester 机器人课程这种旧但有用的手写资源。

## 对工具的判断
- Google / Bing / DuckDuckGo：索引覆盖仍强，但默认界面已被广告、AI 摘要、信息框和 SEO 内容污染；普通用户很难稳定抵达好材料。
- Kagi：付费搜索并不自动等于高质量排序；它减少了一些噪音，但 AI 摘要同样会严重幻觉。
- Marginalia：不适合简单事实检索，覆盖面太窄；但在“电机效率”这种被新内容污染的问题上，它能挖出旧网页和维护过的教学资料。
- ChatGPT：能在广告拦截器和钼能量上表现最好；一旦问题需要物理/电子机制推理，它会把垃圾来源重新包装成更自信的错答案。

## 值得质疑
样本只有 5 个查询，评分也带有作者标准；测试更像“普通用户不带技巧地搜索”而非专家检索。会用站内搜索、关键词约束、排除词、旧论坛或专业资料库的人，结果会更好。但这恰好强化了作者的问题：默认搜索体验对普通人已经不可靠。

## 最后一层
高质量网页仍在，只是发现层越来越偏向新鲜、可变现、可 SEO 化的内容；真正的损失不是知识消失，而是入口把人系统性导向低质量答案。
