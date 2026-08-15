---
title: "Why is Meta destroying its engineering organization?"
date: 2026-06-17T08:03:38Z
category: reading
description: "Meta 本拥有 Big Tech 中最扁平、最自治的工程文化。2026 年 6 月，这套文化在数周内被系统性摧毁。直接推手是两人：Zuckerberg 授权，Alexandr Wang（148 亿美元收购 Scale AI 后空降主导 AI 战略）执行。"
source: "https://newsletter.pragmaticengineer.com/p/why-is-meta-destroying-its-engineering"
---

## Zuckerberg + Wang 合力把 Meta 工程降级为 AI 训练原料

Meta 本拥有 Big Tech 中最扁平、最自治的工程文化。2026 年 6 月，这套文化在数周内被系统性摧毁。直接推手是两人：Zuckerberg 授权，Alexandr Wang（148 亿美元收购 Scale AI 后空降主导 AI 战略）执行。

## 五条伤口叠加造成系统性破坏

1. **强制重新分配**：核心团队 30–50% 的工程师被划入 ADO（Agent Data Optimisation）组，专职数据标注和 RLHF。ADO 约 6,500 人，其中工程师 4,000–5,000，占 Meta 全公司约 25,000 工程师的 1/5 到 1/6；被调离的往往是最强的人。

2. **键盘 + 鼠标全量监控**：4 月底强制部署，无退出选项（英国因数据保护法未推）；6 月才增加"每次最多暂停 30 分钟"的有限豁免。

3. **裁员恐慌期 4 周**：4 月 20 日公告将裁 10%，5 月 20 日执行，中间全员处于待判状态。

4. **Token 计量影响绩效**：PSC 绩效考核将 AI token 用量列为指标，工程师大规模"tokenmaxxing"——30 天消耗 60.2 万亿 tokens，按 Anthropic API 定价折合约 9 亿美元。

5. **基础设施和安全团队被抽空**：Instagram Trust & Safety 约损失 50% 人员，其中包括最资深的成员。

## 后果：史上最糟安全漏洞

5 月 30 日，Instagram 出现 zero-auth 密码重置漏洞：攻击者只需目标账号 username，通过 Meta 客服 AI 将验证码发到任意受控邮箱，即可完成账号接管，无需任何原始凭据。奥巴马白宫等高知名度账号被接管。这是 Meta 史上"第一个真正的零认证密码重置出现在生产环境"。CISO Guy Rosen 次日辞职。6 月 12 日再次发生 SEV0 全量宕机。

直接因果：AI 生成 + AI 单独 review 的代码大量合并进主干；安全团队半人力运转；无人及时触发告警。CPO Chris Cox 在内部全员会上用"这公司的疯狂"描述过去几个月的局面。

## "AI 心理症"的更大背景

Mitchell Hashimoto（HashiCorp 创始人）提出 "AI psychosis" 框架：陷入此状态的创始人相信 MTTR 够快可以弥补一切质量问题，因此放弃系统韧性。这套逻辑在基础设施时代已被驳倒（MTBF vs MTTR 争论），现在以更大规模重演。Instagram 漏洞是实证：局部指标（token 使用量、代码提交量）向好，全局风险同步积累，直到公开爆炸。

## 结构性根因

Llama 4 表现不佳（2025 年 4 月）后，Zuckerberg 以 148 亿美元收购 Scale AI，接受了 Wang 的判断：训练数据比维持工程质量更重要。CTO Bosworth 事后承认 AI 重组"一塌糊涂"，但 Zuckerberg 和 Wang 仍在职，说明方向未变，只做边际调整。

Meta 本来在 2026 年底前有望超越 Google 成为全球第一大广告商——Zuckerberg 却主动押注 coding LLM 胜过稳定运营核心业务。这是文章最不显然的结论：不是管理失误，而是有意为之的优先级排序。
