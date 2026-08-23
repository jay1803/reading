---
title: "Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
date: 2026-05-02T08:02:51Z
category: reading
author: "Simon Willison"
description: "来源：https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities"
source: "https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything"
---

来源：https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

## TL;DR
GPT-5.5 把“前沿模型可独立完成复杂网络攻击链”从单一模型异常值推进成趋势信号：AISI 专家级任务通过率 71.4%±8.0%，略高于 Claude Mythos Preview 的 68.6%±8.7%；它也是第二个端到端完成 32 步企业入侵模拟的模型。重点是长程自治、代码能力、推理与高 token 预算叠加后，攻防任务时间尺度被压缩。

## 关键发现
- AISI 用 95 个 CTF 式窄域任务评估逆向、Web exploitation、密码学等能力；基础任务自 2026 年 2 月起已基本饱和，区分度转向 Practitioner / Expert 高级任务。
- Expert 级、50M token 预算下：GPT-5.5 71.4%±8.0%；Mythos 68.6%±8.7%；GPT-5.4 52.4%±9.8%；Opus 4.7 48.6%±10.0%。
- `rust_vm` 是最强信号：人类专家约 12 小时，GPT-5.5 无人工协助 10 分 22 秒、$1.73 完成。它识别 PIE relocation jump table，恢复 VM ISA，写 emulator/disassembler，反推认证逻辑，并用约束求解提交 flag。
- “The Last Ones” 企业靶场含 32 步、约 20 主机、4 子网，覆盖侦察、凭证窃取、横向移动、AD、多森林、CI/CD pivot 与数据库外泄；GPT-5.5 10 次成功 2 次，Mythos 3 次。
- TLO 表现随推理预算继续提升，AISI 尚未看到最佳模型 plateau；这暗示攻击链执行能力可能继续随 inference spend 爬升。

## 能力边界
- GPT-5.5 未完成 “Cooling Tower” 工控靶场；失败点在 IT 区段，不足以判断 OT 攻击能力。
- 当前靶场没有主动防御者、防御工具、告警惩罚和真实企业噪声；结果证明受控条件能力上限，不等于公开用户可直接复现。
- AISI 红队找到 universal jailbreak，可诱导所有 OpenAI 提供的恶意网络查询输出违规内容；OpenAI 更新防护栈后，AISI 因配置问题未能验证最终效果。

## 更大意义
- 如果网络攻击能力是长程自治、代码生成、工具使用和推理共同提升的副产物，后续模型进步可能密集出现。
- 防御压力会从“是否有人能发现漏洞”转向“发现与 weaponization 速度是否超过修补、检测、响应节奏”。NCSC 提醒准备 vulnerability patch wave 正是这个方向。
- 同一能力也能服务防御：漏洞发现、补丁验证、配置审计、日志分析和攻击路径模拟都会更自动化。

## 值得质疑
- TLO 的 2/10 与 Mythos 的 3/10 样本很小，足以提示趋势，不足以精确排名。
- 真实滥用还受 safeguards、monitoring、access control、成本、工具链和操作经验限制；文章没有回答这些缓冲能持续多久。

## 最后判断
GPT-5.5 的核心信号在于：攻击链瓶颈正在从知识与手工步骤，转向自治编排、工具可靠性和可投入的推理预算；防御方可用准备时间正在变短。
