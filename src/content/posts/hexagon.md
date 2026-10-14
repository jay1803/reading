---
title: "Hexagon"
date: 2026-10-14T08:09:31Z
category: reading
description: "Ben Antieau 宣布 Hexagon：一个为 LLM 辅助乃至完全生成的数学/TCS 研究成果而建的新仓库，允许人类理解之前就先公开收集，由 Hexagon Mathematics Foundation 运营。"
source: "https://terrytao.wordpress.com/2026/10/06/hexagon/"
author: "Terence Tao"
---

Hexagon 要为 LLM 辅助乃至完全生成的数学成果建立一个可引用、长期保存、由学术共同体维护的入口，让这些成果在获得人类理解和学界认可之前就能被公开收集。Ben Antieau 宣布，这个面向数学科学与 theoretical computer science（TCS）的新仓库始于 2026 年 8 月初的一次集体筹建：LLM 正在快速产出研究结果，而散落在 GitHub 仓库及 X、Bluesky、Mathstodon、LinkedIn 上的记录缺乏稳定的归宿。Hexagon 希望降低 arXiv 对作者身份与共同体关注度的门槛，同时保留研究成果所需的可引用性与持久存储。

Antieau 自己的经历体现了这种需求。他与一个由 FRG grant 联结的研究小组合作时，点击按钮便发现了一个新结果：特征零情形下，四维代数簇的 Hodge numbers 具有 derived invariance。按过去的标准，这项成果足以投向优秀但非顶尖的期刊；这一次，他却不愿以自己的名字署名，只在博客中记录了结果。这种发布方式难以支撑数学成果的长期汇集，如今该成果已收入 Hexagon，编号为 hexagon:2609.00104。他希望，与 LLM 合作时自然涌现的结果，包括研究过程中的附带发现，都能被识别并提交到这里，逐渐形成共同体惯例。

这一设想把**成果出现**与**成果获得理解和认可**分成不同阶段。Hexagon 明确允许提交完全由 LLM 生成的研究，即使提交者声明自己没有人类层面的理解，也可以让成果进入公共视野。Antieau 设想，这些数学想法先在 Hexagon 显露，随后经共同体理解、接受和整理，再形成适合提交 arXiv、正式发表及进入公认知识体系的版本。大型语言模型实验室、大规模合作团队和其他组织也被邀请提交；其产生的数学与 TCS 成果，应当默认向相关学术共同体开放，并存放在共同体维护的平台上。

Hexagon 的定位来自对现有基础设施边界的确认。筹建者在 8 月通过私人 Zulip 频道讨论政策并搭建网站，也与 arXiv 管理层及其他相关人士交流。arXiv 表明将专注于维持现有项目，不会提供他们所寻求的这类成果入口，Antieau 支持这一选择；其他 AI 时代的仓库则尚未获得足够使用，或未具备筹建者希望采用的完整政策。技术搭建本身已相对容易：整个系统在 OpenAI Codex 的帮助下创建，部署于普遍可用的商业云服务器。更耗时的工作是决定具体功能，以及精确撰写网站上的政策与说明。

为支撑平台运营，团队在 Delaware 注册了非营利组织 Hexagon Mathematics Foundation，并计划申请美国税法 section 501(c)(3) 下的免税资格。Antieau 担任首任 Executive Director，董事会由 Mohammed Abouzaid、François Charles、Bryna Kra、David Savitt 和 Lauren Williams 组成；顾问委员会包括 Kevin Buzzard、Akhil Mathew、Johannes Schmitt、Steinn Sigurðsson、Nikhil Srivastava、Ravi Vakil 和 Rachel Ward。截至发布时，全部资金由参与者承担，团队仍在探索其他资金来源和可持续运营路径；除购买云基础设施服务外，平台与营利公司或其他组织没有关系。

开放收集的门槛与提交责任也被具体区分。Hexagon 接受对数学与 TCS 共同体有意义的小型、渐进式改进，不要求成果经过形式化验证，但会链接 mathlib、Palomar、prove2.me 和 TauCeti 等形式化项目。**Contributors** 是对成果创作负责的人类或组织，**Submitters** 则是拥有经 ORCID 验证账户的人类；部分账户可以获准代表其他个人或组织提交。提交频率起步为每天一项，后续能否提高，由 Hexagon 根据此前提交通过 moderation 的情况决定。平台同时提供类似 arXiv 的读取 API，以及用户可从账户页面获取 token 的提交 API；目前仍处于 beta，继续增加功能并测试扩展能力。

Hexagon 的名字取自 Jorge Luis Borges 的《The Library of Babel》中六边形的图书馆大厅，回应了数学成果迅速增殖时寻找知识归宿的问题。它所尝试建立的是一条新的知识流转路径：先为尚未被充分理解的机器生成成果留下稳定、可追踪的记录，再让人类理解、共同体认可和正式发表逐步接续。
