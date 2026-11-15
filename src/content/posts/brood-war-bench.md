---
title: "Brood War Bench"
date: 2026-11-15T01:16:41Z
category: reading
description: "Brood War Bench 暴露了当前 AI agent 玩《StarCraft: Brood War》的核心短板：它们能发现奏效的骚扰战术，也会尝试攀升科技树，却仍难以把持续生产、兵力集结和战场控制组织成稳定的行动循环，连初学者的简单进攻都招架不住。"
source: "https://bw.swerdlow.dev/report"
author: "benswerd"
---

Brood War Bench 暴露了当前 AI agent 玩《StarCraft: Brood War》的核心短板：它们能发现奏效的骚扰战术，也会尝试攀升科技树，却仍难以把持续生产、兵力集结和战场控制组织成稳定的行动循环，连初学者的简单进攻都招架不住。

Codex 最常奏效的办法是早期骚扰。使用 Protoss 时，它经常派一只 Probe 穿过地图攻击敌方工人或建筑；对手会花几十秒思考如何应付这只 Probe，期间几乎停下其他行动。这种打法利用了对手决策停滞的弱点，但 Codex 自己的长期运营同样薄弱：科技升级拖延，每次只派一两个基础单位冲进已有防御的基地，败局中还会把工人投入最后抵抗。

这种零散进攻也暴露出多 agent 协作的问题。Codex 经常分别创建负责经济、部队生产和军队控制的 subagent，但它们交流很少；负责控兵的 agent 会把刚生产出的单位立即送去进攻，并不知道其他 agent 正计划积累一支更大的军队。结果是典型的新手失误：兵力逐个送掉，无法等到形成规模后按预定时机出击。作者亲自指导 Codex 时，它在安排进攻时点、协调 subagent 上明显改善。不过，Codex 的持续行动能力确实存在：G009 中，Codex 5.6 Terra / medium 在军队和主基地被摧毁后，让最后一座 Command Center 起飞并向地图另一端撤离，又存活了六分钟。这证明了它会设法延续对局，却没有解决如何积累优势并赢下比赛的问题。

Grok 4.6 的障碍更基础：大量推理没有转化为持续操作。G043 的 xhigh 配置在一场长达 43 分钟的比赛里产生了 11,138 个 reasoning tokens，却只发出六批指令，从未造出战斗单位。另两场也没有形成有效进攻：G003 的 xhigh 配置造出三名 Marines，却始终未抵达敌方基地；G002 的 medium 配置造出两名 Zealots，也未穿过地图。这些表现指向*观察与行动循环的失效*，仅靠评价其战术选择无法解释它为何长时间几乎什么都不做。

Claude Fable 则更持续地尝试发展经济、推进科技，没有停留在最初可生产的兵种上。G007 中，它完成 Lair、Spire 并造出 Mutalisks，最终获胜；G027 中，它建造了 Robotics Facility、Citadel of Adun、Observatory 和 Templar Archives，也赢下比赛。但科技发展并不自动形成作战能力：G036 中，Fable 虽然建成 Factory 和 Academy，仍被 Opus 5 攻破。即使 Astra 和 Fable，也无法可靠地组织复杂兵种组合、防住简单进攻或执行具体战术；作者判断，一个会用 photon rush 的初学者就能赢下这些对局中的任何一场。

这些失败让 Brood War Bench 仍有充足的评测空间：模型已经展现出局部战术发现、科技发展和败局求生的能力，但距离稳定获胜，还缺少将这些能力连接起来的实时协调机制。这个基准真正检验的是，agent 能否在对手不断行动的环境里，把规划持续兑现为彼此配合、时机正确的操作。
