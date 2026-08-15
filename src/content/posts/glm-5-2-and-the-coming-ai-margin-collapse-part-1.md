---
title: "GLM 5.2 and the coming AI margin collapse (part 1)"
date: 2026-07-07T08:02:31Z
category: reading
description: "市场对 DeepSeek R1 的解读是错误的：训练是一次性固定支出，推理才是随需求线性扩展的边际成本。Anthropic/OpenAI 以 $25/MTok 销售推理，作者估算 GPU rack rate 对应毛利率约 90%；OpenAI 泄露财报显示整体收入毛利约 60%（含支持、支付等非推理成本）。前沿实..."
source: "https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
---

### 真正的 DeepSeek 时刻是推理毛利崩溃，而非训练成本下降

市场对 DeepSeek R1 的解读是错误的：训练是一次性固定支出，推理才是随需求线性扩展的边际成本。Anthropic/OpenAI 以 $25/MTok 销售推理，作者估算 GPU rack rate 对应毛利率约 90%；OpenAI 泄露财报显示整体收入毛利约 60%（含支持、支付等非推理成本）。前沿实验室的商业模式是用高推理毛利摊销研发，开放权重模型正在威胁这一结构。

### GLM 5.2 的实际水准与弱点

作者将 GLM 5.2 定性为首个真正达到 Opus / GPT-5.5 水准的开放权重模型。在 Claude Code 中使用时几乎察觉不到差异。

当前弱点：
- 思考时间偏长（更多 thinking tokens），交互场景响应慢，同时推高 token 用量
- 无视觉支持，无法处理图片 PDF、截图、设计稿
- 网络搜索能力弱：Z.ai 的官方搜索 MCP 质量差，Fireworks 无搜索集成；作者用 ddgr CLI 临时绕过，但这是系统性短板

### 切换成本接近于零

Z.ai 和 Fireworks 均提供 OpenAI 兼容和 Anthropic 兼容 endpoint，切换只需改 base URL 和 API key，Claude Code 与 Codex 开箱可用。这与企业级软件迁移截然不同——没有年级别的规划，切换摩擦甚至低于追踪前沿实验室频繁变动的政策与条款。

### 成本优势

当前 GLM 5.2 定价约 $4.40/MTok，约为 Opus 零售价的 18%、GPT-5.5 的 15%。考虑到 GLM 更高的 token 消耗，实际综合成本仍有 50% 以上优势。Wafer 基准测试显示 AMD 硬件运行 GLM 5.2 推理成本比 Nvidia Blackwell 低 2.75 倍，后续价格预计继续下降。

### 数据隐私障碍及绕过路径

Z.ai 官方 API 在企业场景基本不可行（条款薄弱、深度关联大陆）。但开放权重意味着可选其他合规提供商，或完全自托管——反而使更敏感的数据进入 Opus 级别 agentic 工作流成为可能。

### 注

第二部分将分析推理毛利崩溃对整个行业格局的影响（赢家与输家）。作者援引贝佐斯名言："你的利润就是我的机会。"披露：Fireworks 为本文提供了免费 credit。
