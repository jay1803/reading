---
title: "How to use the Qwen 3.5 LLMs to OCR documents"
date: 2026-03-27T08:01:53Z
category: reading
description: "用 OpenRouter + Qwen3.5-9B 做批量 OCR，速度和成本都已经优于 OpenAI / Google 等前沿 API——不是\"差不多便宜\"，是实质性更快更便宜：1000页约12美分、约60秒。"
source: "https://martinalderson.com/posts/how-to-use-qwen-3-5-to-ocr-documents/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

## TL;DR
用 OpenRouter + Qwen3.5-9B 做批量 OCR，速度和成本都已经优于 OpenAI / Google 等前沿 API——不是"差不多便宜"，是实质性更快更便宜：1000页约12美分、约60秒。

## 核心洞见
- Qwen 3.5 系列全系多模态，最小到 0.8B/2B——此前最小的开源视觉模型约 4-5B，这个变化让本地部署门槛大幅下降。
- OCR 最优规格是 9B：更小的模型（尤其 <4B）在复杂文档上容易偏离任务，变成摘要而非逐字转录；9B 是质量与速度的实际甜点。
- OpenRouter 允许 128 路并发请求，而 OpenAI 在未大额消费的情况下几个并发就触发限速——这是吞吐量差距的根本原因。

## 具体机制
流程分两步：① 用 PyMuPDF（fitz）将 PDF 每页导出为 JPG（100dpi）；② 将图片 base64 编码后以标准 chat completions 格式发给模型，prompt 要求"原样返回所有文字，表格/列表用 Markdown 格式，不加评论"。
- 本地方案：LM Studio + 9B 模型，Radeon 9070XT 约 3s/页；LM Studio 对 prefill/decode 批处理未优化，作者认为速度仍有较大提升空间。
- 云端方案：OpenRouter 两家供应商，用 ThreadPoolExecutor 128 线程并发，1000页约12美分、60秒完成。

## 隐藏限制
- 128路并发以上的速率上限作者未测试，实际天花板未知。
- 100dpi 是作者经验值，作者明确说"your mileage may vary"——对低质量扫描件可能需要调整分辨率。
- 本地方案的实际瓶颈是推理框架效率，而非模型本身，LM Studio 在高吞吐场景并非最优选择。

## 收束行
最有意思的场景是历史文献数字化：传统 OCR 对破损扫描件几乎无效，人工转录极其昂贵——现在一台笔记本跑本地模型可以免费完成，OpenRouter 几美分就能处理整个档案馆。这个成本曲线变化的意义远超商业 OCR 本身。
