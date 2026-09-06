---
title: "The Friendship That Made Google Huge"
date: 2026-09-06T02:26:13Z
category: reading
description: "Jeff Dean 与 Sanjay Ghemawat 长达二十年的友谊与结对编程，如何把 Google 廉价且频繁故障的计算机集群变成一台可靠的“行星级计算机”，并推动 MapReduce、TensorFlow 等基础设施诞生。"
source: "https://www.newyorker.com/magazine/2018/12/10/the-friendship-that-made-google-huge"
author: "James Somers"
---

Google 能从脆弱的搜索实验成长为全球规模的计算与人工智能公司，关键动力之一是 Jeff Dean 与 Sanjay Ghemawat 长达二十年的友谊与结对编程：Jeff 擅长迅速提出大胆方案，Sanjay 擅长把方案组织成清晰、耐久、可扩展的系统，两人共同把廉价且频繁故障的计算机集群变成一台可靠的“行星级计算机”。

这段合作最早在 2000 年 3 月的一场危机中显出价值。Google 的网页索引系统从前一年 10 月起就已停止更新，搜索结果落后五个月；与此同时，Larry Page 和 Sergey Brin 正争取为 Yahoo 提供搜索服务，并承诺交付容量扩大十倍、足以跟上前一年规模翻倍的 World Wide Web 的索引。若无法恢复，Yahoo 合同可能告吹，Google 也可能耗尽融资。包括首位员工 Craig Silverstein 在内的工程师连续排查多日，代码逻辑处处看似正确，系统却不断遗漏单词、打乱排序。

第五天，Jeff 和 Sanjay 把索引文件转换成最原始的二进制表示，发现本应为 0 的一位变成了 1，而且所有错序单词都有同类异常。根因在内存芯片：Google 的集群已经大到足以让罕见硬件故障成为日常事件，电线会磨损、硬盘会损坏、主板会过热，甚至高能宇宙射线也可能击中芯片并翻转一个 bit。NASA 和金融机构会使用能容忍单 bit 错误的昂贵硬件，创业期的 Google 却依赖廉价消费级机器。Jeff 和 Sanjay 写出绕过故障设备的代码，索引很快恢复；Silverstein 的感受是，优秀调试者会追到问题底部，而他们进入了比软件逻辑更深的硬件层。

这场事故暴露了 Google 的生存难题。Page 和 Brin 在 Stanford 写下的研究型代码缺少可靠诊断，爬虫崩溃时只显示“Whoa, horsey!”，被称为 BigFiles 的程序也被员工戏称为 BugFiles；索引一旦中途失败，就得从头运行数日。当时没有一台超级计算机足以处理整个网页索引，Google 只能把消费级主板和硬盘层层叠放：Santa Clara 的六英尺高机架里共有一千五百台设备，真正能工作的只有一千二百台。公司的前途因此取决于一个工程问题：如何让数量庞大、性能不一且随时损坏的机器表现为统一、连续、可靠的系统。

Jeff 和 Sanjay 随后主导了 Google 基础设施的重建。他们每周工作九十小时，使单块硬盘失效不再拖垮全局，为爬虫加入可以从中途恢复的 checkpoint，并借助新的编码和压缩方法把系统容量实际翻倍。他们利用硬盘外圈线速度高于内圈的物理特性，把高频数据放在外圈，同时把此前闲置的内圈用于保存常见查询的预处理结果；2001 年，他们又用四天证明索引可以放进速度远高于硬盘的随机存取内存，从而重塑了搜索速度与成本之间的经济关系。Google 想以即时答案吸引用户，计算能力却价格昂贵，Jeff 和 Sanjay 用软件持续压低每次查询所需的硬件成本。

两人解决大规模问题的方法建立在对微小细节的掌握上。Jeff 熟记 L1 cache 访问约需半纳秒、从内存顺序读取一 megabyte 约需二百五十 microseconds 等延迟数据；Sanjay 则能把复杂系统整理成结构严谨、便于他人理解和扩展的代码。随着他们多次重写核心软件，Google 的容量提高了数个数量级，数据中心里的技术员可以按照软件指令沿固定路线更换硬盘、电源和内存条。机器部件持续死亡，整体服务仍然运转，这种把故障视为常态并在系统层消化的能力成为 Google 规模化的基础。

Google 后来建立了从 Level 1 到 Level 10 的工程师等级体系，Level 6 已属于能决定项目成败的前百分之十，Level 9 是备受尊敬的 Distinguished Engineer，Level 10 的 Google Fellow 通常已是某个领域的世界级专家；Jeff 和 Sanjay 成为公司最早且仅有的两位 Level 11 Senior Fellow。然而，他们的生产力很难拆分成个人贡献。两人常共用一台电脑，Sanjay 操作键盘，Jeff 坐在旁边校正方向；他们能接完彼此的话，也常把家庭生活交织在一起。未婚的 Sanjay 会与 Jeff、妻子 Heidi 和两个女儿共同度假，女儿们称他 Uncle Sanjay，两家在 2004 年 Google I.P.O. 后买下相距四英里的住宅，并长期保持周五聚餐。

这种关系体现了创造性搭档的特殊力量。社会学家 Michael P. Farrell 研究 Impressionists、Freud 及其同时代人后发现，新思想最脆弱也最关键的部分，常产生于两人之间的持续回应；Monet 与 Renoir 共同发展 Impressionism，Picasso 与 Georges Braque 在六年合作中催生 Cubism，John Lennon 与 Paul McCartney 则靠一人写出开头、另一人突破卡点推进歌曲。遗传学家 François Jacob 也指出，两颗头脑能让想法更快碰撞、嫁接，并更早剪除幻觉；过去三十五年里，约一半 Nobel Prize in Physiology or Medicine 授予科学搭档。个人会陷入思维惯性，两个人却很少同时困在同一条死路上。

软件业通常把 pair programming 理解为两名“副驾驶”互相检查，Jeff 和 Sanjay 的合作却形成了具有互补功能的共同认知系统。Jeff 是加速器：他喜欢野心勃勃的新想法，能迅速做出展示其潜力的 prototype，一旦看清解法轮廓便转向下一个问题。Sanjay 是刹车和结构工程师：他关注 corner cases、接口、可读性与长期维护，让系统经得起规模和时间的压力。Barbara Liskov 认为优秀代码像优秀写作，每个词都承担作用，结构还要照顾未来读者；Sanjay 的代码正具备这种“社会性”，信息密度高却容易理解，而且别人添加功能时经常发现所需的接口早已预留。Silverstein 将这种感受比作 Salieri 面对 Mozart：他看得懂伟大之处，却不知道这种预见力如何产生。

两人的表现也重新激活了“10x programmer”争论。1966 年的研究发现，最佳程序员的效率可超过最差者十倍，但大型软件成果通常依赖集体协作，把成功归于孤立天才会扭曲现实。Jeff 和 Sanjay 却说明，超常生产力可能来自一个无法按个人切分的组合：他们的论文往往有十余名共同作者，管理者仍会围绕这对搭档组建团队，因为两人能够提出架构、写出核心实现，并让其他工程师在其上工作。Google 的最高杠杆因此集中在**创造性二人组**与大规模组织之间的连接处。

这种杠杆在 2003 年的 MapReduce 中达到高峰。第三次重写爬虫和索引器时，Jeff 和 Sanjay 意识到，他们每次都在重复解决同一个问题：如何把任务分配给数量庞大、地理分散且单机不可靠的计算机，并在机器故障后继续执行。他们用四个月将通用解法提炼成 MapReduce，使普通工程师也能像操作一台计算机那样使用整个数据中心。程序员只需定义“map”阶段，例如让各台机器统计网页上的单词，以及“reduce”阶段，例如汇总各机结果；数据切分、工作调度、网络分发和硬件容错都由系统隐藏。2004 年，Google 用 MapReduce 重写爬虫与索引后，工程师又把它用于处理视频、绘制 Google Maps 图块，并利用夜间流量低谷运行批量任务，让闲置机器持续加工白天积累的数据。

MapReduce 的影响很快越过 Google。Jeff 和 Sanjay 为帮助天文学家、遗传学家等需要处理海量数据的科学家，在 2004 年公开论文《MapReduce: Simplified Data Processing on Large Clusters》。正在扩展 Nutch 搜索引擎的 Mike Cafarella 与 Doug Cutting 随即从头实现开放版本，最终以 Cutting 儿子的玩具象命名为 Hadoop。Hadoop 后来被 Fortune 50 中的一半公司采用，Facebook 曾拥有全球最大的 Hadoop cluster，用它处理点击、Like 和广告浏览等用户 metadata；LinkedIn 与 Netflix 也依赖它。美国 National Security Agency 的测试中，Hadoop 把一项分析任务加速了一万八千倍，继而成为被批评者称为“collect it all”的情报收集方式的基础。Jeff 和 Sanjay 由此把早已存在的 distributed computing 概念转化为普通程序员可掌握的工作模型，也为“Big Data”产业提供了通用语法。

同一套规模逻辑把 Google 推向人工智能。2001 年，Noam Shazeer 发现外购拼写检查器会把“TurboTax”纠正成“turbot ax”，于是利用整个 Web 的文本统计规律构造词典，使系统理解“pritany spears”和“brinsley spears”都指向“Britney Spears”。他又与 Jeff 和 Georges Harik 运用类似方法匹配广告与网页，广告收入随之回流到计算基础设施，形成**规模产生智能、智能产生财富、财富继续扩大规模**的循环。BigTable、MapReduce 及其后继系统让 Google 得以转录语音信箱、自动补全查询、回答问题并在一百多种语言之间翻译；算法本身未必复杂，海量数据和可驾驭的算力使简单方法获得异常强大的效果。

2011 年，Jeff 开始每周抽出一天加入 Andrew Ng 领导的秘密 neural-network 项目 Google Brain。神经网络在 Jeff 读本科时还无法解决现实问题，Ng 却发现，大量数据已经使它们的能力发生变化；Google 的规模可能把这种潜力推到新的层级。公司内部许多人认为 Jeff 浪费了基础设施方面的天赋，连 Sanjay 起初也不理解他的选择，但接下来七年，Google Brain 在机器翻译、语音识别和图像识别上超越原有技术，并逐渐替代搜索排序与广告定向等核心算法。Jeff 的真正优势恰好在于系统工程：人工智能开始依赖规模，而他能提供规模。

Jeff 随后领导 TensorFlow 的开发，试图创造“人工智能时代的 MapReduce”，让工程师可以把 neural network 分布到整片计算机集群上，把机器群组织成一个巨大头脑。TensorFlow 于 2015 年开放后迅速成为 A.I. 的通用语言；Sundar Pichai 宣布 Google 转型为“A.I. first”公司，并让 Jeff 负责三千人的人工智能组织。Jeff 此后每周四天管理 Google Brain，同时参与专为神经网络设计的 Tensor Processing Unit 和用神经网络设计神经网络的 AutoML，只剩一天能与 Sanjay 一起写代码。

两人的角色由此分化。Jeff 向外扩张产品和研究边界，Sanjay 则坚持做不管理任何人的 individual contributor，继续加固底层结构，并参加决定全公司技术方向的 Area Tech Leads 小组。如果把 Google 比作一栋房子，Jeff 在修建新的侧翼，Sanjay 在检查横梁、螺栓与承重。两人的每周编程中仍能看到原有节奏：Jeff 会推动立即重构，Sanjay 会阻止过早深入局部；二十年里他们几乎没提高过嗓门。由于代码会在全球数据中心运行多达十亿次，他们争论的 kilobits 与 microseconds 最终可能让整个 Google Search 快百分之十。

工程成就往往会在成功后隐形：人们记得十八世纪的探险家，却很少记得制造可靠航海钟、使经度测量成为可能的 John Harrison。Google 手机今天能够听懂问题并即时作答，是因为从设备到全球数据中心的一整套程序已经无缝连接，用户看不到 Jeff 和 Sanjay 写下的基础设施，也看不到成千上万台设备持续故障。两人晚年共同启动的项目，是训练一个可以完成数千乃至数百万种任务的“giant”机器学习模型；Jeff 提出方向，Sanjay 与他先写 prototype，再让团队围绕代码成长。在软件世界里，他们证明了最有效的领导可以从共同写下的代码开始，而最强大的规模优势可能起源于两个人愿意长期坐在同一块屏幕前，把彼此尚未完成的思想继续下去。
