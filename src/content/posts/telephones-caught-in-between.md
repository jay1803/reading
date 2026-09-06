---
title: "telephones caught in between"
date: 2026-09-06T15:09:55Z
category: reading
description: "美国电话租赁制度从保障网络可靠性演变为持续数十年的消费者陷阱：技术标准化、反垄断诉讼、FCC 监管分类与 1984 年 AT&T 拆分层层叠加，最终让数十万份旧租约留给后来者继续收费。"
source: "https://computer.rip/2026-08-02-telephone-leasing.html"
---

美国电话从 Bell System 的系统组件变成可自由购买的消费电子产品，经历的并非一次有序的市场改革，而是技术标准化、反垄断诉讼、FCC 监管分类与 1984 年 AT&T 拆分相互叠加的结果；改革淘汰了电话租赁的合理基础，却把数十万份旧租约留给后来者继续收费，最终让一项原本保障网络可靠性的制度演变成持续数十年的消费者陷阱。

Bell System 鼎盛时被称为"史上最大的机器"，因为 AT&T 的"One Policy, One System, Universal Service"并非单纯口号：中央交换机、线路和用户家中的电话都由同一体系设计、安装和维护。计算机网络强调标准接口与可替换的终端，把复杂性推向边缘；电话网则把复杂性集中在交换局，由少数 Western Electric 机型配合特定线路运行。早期电话使用需要定期更换的大型干电池，不同交换局又有不同接线方式；20 世纪中叶占多数的 party line 更存在约六种互不兼容的选择振铃系统，一部接错或故障的电话可能影响整条线路，持续摘机甚至会占用交换设备容量。电话直到 1960 年代通常仍以螺丝端子硬接，连接器到 1974 年才标准化，因此由电话公司拥有终端、派技术员安装维修并向用户按月出租，在当时兼顾了便利、兼容性和整个网络的可靠性。

租赁也给用户提供了持续服务：交换局从脉冲拨号升级到 touch-tone 时，电话公司负责换机；用户可以加一点月费换成 1959 年推出的 Princess 或后来的 Trimline，装修时甚至能免费换颜色。但这一模式代价很高，每增加一部分机或选择高级机型都要长期加钱。Western Electric 为可靠性而制造的电话可以服役 25 年，却生产昂贵、上门维修也侵蚀同属 AT&T 的整体利润。到 1970 年代，Bell Operating Companies 开始让客户把电话带到 PhoneCenter 自行换机，模块化插头很大程度上也是为这种零售式服务而推广。一旦普通人能够从商店拿走电话并自行插上，继续按月租赁便越来越缺乏经济理由。

真正的障碍是 AT&T 利用本地电话服务这一**自然垄断**控制终端市场。美国司法部 1949 年依据 Sherman Act 起诉 AT&T，并不否认铺设和维护本地线路适合由一家企业经营，争议在于 AT&T 能否借受监管的垄断地位排斥本可竞争的设备与服务。最终 consent decree 允许 AT&T 继续作为受州公共事业委员会约束的 common carrier，却禁止它进入未受监管的行业。这一安排尤其深刻地改变了计算机史：拥有 Bell Laboratories、Western Electric 和大量电子技术积累的 AT&T 不能销售通用计算机，IBM 因而占据了本可能属于 AT&T 的位置；AT&T 虽开发出 UNIX，却因无法像当时业界那样把软件绑定硬件出售，只能采用特殊许可方式，反倒促成 UNIX 广泛传播。

与此同时，第三方连接权逐步瓦解了 Bell 对用户终端的封闭控制。1956 年 Hush-A-Phone v. United States 先允许非电气附件，FCC 的 1968 年 Carterfone 决定又允许符合条件的电气设备接入。Automatic Electric、ITT、Ericsson 等厂商和 Target 等零售商随即开始销售电话。Bell 最初要求每部第三方电话通过一台同样需要租赁和专业安装的 Protective Connecting Arrangement 接入，每部分机都要单独配置，用户也不能处理仍属 Bell 财产的室内线路，开放在实践中几乎失去意义。FCC 于 1975 年确立延续至今的规则：network interface device 或 demarcation point 以内的布线归客户所有，用户可以自行连接经过技术认证并向 FCC 注册的设备。客户此后只需向电话公司报告电话的 FCC registration number，便可使用自购终端。

零售市场迅速压低价格，也暴露出账单对租赁成本的掩盖。客户可能买来一部 ITT 电话插上使用，却继续为旧 Bell 电话付租金，直到主动取消并退回旧机；州监管机构因此要求租赁费单独列项。以 1983 年 New York Telephone 为例，一部 500-style 转盘电话月租 3.03 美元，在 PhoneCenter 买断为 45 美元，使用约两年就已更划算；Radio Shack 的亚洲进口电话只卖 15 美元。Western Electric 仍可凭质量和耐用性竞争，但电话已经脱离网络本体，成为承受价格竞争的普通商品。

计算机的发展同时迫使 FCC 重画通信监管边界。1966 年启动的 Computer inquiry 试图把受监管的"communications"和自由竞争的"data processing"分开，并规定同一集团若进入两边，必须通过具有会计和政策防火墙的独立实体经营。然而电子邮件、协议转换和网络中的数据改写几乎都落入灰区，使 Computer I 的技术分类难以执行。1976 年启动的 Computer II 改从用户所购买的功能判断：单纯传输属于 **basic service**，以数据处理、存储或检索为目的的业务属于 **enhanced service**；电话网被归入前者，计算机网络通常落入后者，跨界企业仍须严格分离。FCC 随后把 terminal equipment 也视为低门槛的竞争市场，裁定受监管的电话公司只能通过独立子公司出租电话。

AT&T 因此在 1982 年成立 American Bell，其 Advanced Information Systems 准备与 IBM 竞争计算机市场，Consumer Products 则制造、销售并出租电话。原 Bell PhoneCenters 全部改挂 American Bell 招牌，AT&T 还在每家 Sears 设置专柜，并把 Western Electric 电话批发给零售商，与 ITT、Automatic Electric 和亚洲品牌并排销售。FCC 允许 Bell Operating Companies 处理已有库存，却禁止补充新的 customer premises equipment，并要求各州逐步把电话租赁移出受监管资费；电话公司只能告诉新客户，有库存就"提供"一部，颜色无法保证，库存可能在 1983 年耗尽。消费者对此并不抗拒，因为零售电话早已流行，租赁量从 1970 年代末便持续下降。

棘手的是数以百万计仍在付费的 **embedded phones**。这些电话名义上属于 AT&T，由本地公司安装维护，租金最终交给母公司。强制收回会让 AT&T 一次性注销巨额资产，强制买断又需要监管者为不同年龄和状态的电话定价并确定保修责任，FCC 只好暂时维持原租约。AT&T 抱怨自己既要用独立资本建立 American Bell，又要继续维修旧租赁机，还不能把旧租金用于资助新公司；其提出用买断收入支持 Consumer Products，也因估价问题陷入僵局。

1974 年司法部另行发起的 United States v. AT&T 最终打乱了 Computer II 的安排。Computer II 关注 AT&T 会不会利用本地网络压制信息服务，1982 年 Modified Final Judgment 则主要回应 Sprint、MCI 等长途竞争者的崛起：微波与光纤已大幅降低长途网络门槛，而本地 outside plant 仍属自然垄断。判决要求 AT&T 在两年内剥离本地 Bell Operating Companies；1984 年 1 月 1 日起，AT&T 退出本地服务，保留竞争性长途业务、Western Electric 与 Bell Laboratories。法院还把 Bell 名称和商标留给拆出的本地公司，迫使刚成立的 American Bell 改名为 AT&T Technologies，下设 AT&T Information Systems 和 AT&T Consumer Products，一千多家 PhoneCenter 再次更换招牌。

这两轮改革形成了制度上的错位：Computer II 先要求 AT&T 把不受监管的业务隔离，MFJ 两年后又把促成隔离的本地受监管业务直接剥离。1984 年起，租赁用户分别收到本地电话公司和 American Bell／AT&T Consumer Products 的两张账单；维修或收回一部旧电话还要由雇用技术员的本地公司与持有租约的 AT&T 结算费用，并接受 FCC 审查。剥离后的 BOCs 理论上可以成立独立子公司恢复租赁，但廉价零售电话和 AT&T 留存的旧租约让这项业务毫无吸引力，多数公司没有重返市场。各州陆续允许 AT&T 向旧客户提出买断，许多人接受，但到约 1985 年项目结束时仍有大量客户没有回应，此后继续按季度向 AT&T Consumer Products 交租。FCC 到 1986 年也承认严格分离削弱了 AT&T 的竞争能力，逐步撤销相关限制，AT&T 随即重新吸收子公司，但其 3B UNIX 小型机和 PC 业务始终未能建立有意义的市场地位。

这些遗留租约随后随着企业拆分不断迁移。1996 年 AT&T Technologies 独立为 Lucent Technologies 时，约有一百万部电话仍在租赁，Lucent 获准继续用 AT&T Consumer Products 名义收费。PhoneCenters 已于 1995 年关闭，Lucent Consumer Products 后来转向批发；2000 年 Lucent 拆售制造业务，企业网络部分成为 Avaya，消费电话业务大多交给 VTech 并以 Advanced American Telephones 运营，唯独仍有数十万份的租赁合同被卖给 North Street Consumer Phone Services LLC。该公司似乎专为交易而成立，办公地点和与 Lucent 的"managed by"关系都缺乏透明记录。约 2008 年，合同又转到 QLT Consumer Lease Services，QLT 只是取"quality"的近似发音，并无实际缩写含义。

到这一步，曾有技术依据的租赁已具有明显的剥削性。大多数租约在 1982 年后便停止营销，今天仍付款的人往往已经连续支付约 45 年。两张账单本想减少混淆，改为季度收费后却让客户更容易把标有 AT&T 和模糊"equipment fee"的租赁账单误认为长途电话费。FCC 和 FTC 在 1996 年警告公众检查遗忘租约，媒体发现不少老年客户为同一部电话支付 20 年、累计超过 1,000 美元，有些人早已丢弃或换掉设备却仍在付款。2002 年合并为全国集体诉讼的案件指控 AT&T 及历任继承者靠惯性账单从弱势消费者手中收取数千万美元；各方未承认责任，但设立最高 3 亿美元赔偿基金，最终因申请人数过少仅支付不足 1,000 万美元。消费者组织指出，没意识到自己仍在交租的人，本来也最不可能注意到需要主动申领的和解通知。由于历次拆分附带复杂的责任分配，AT&T 和 Lucent 承担大部分赔偿，短暂隶属 AT&T Technologies、从未经营电话租赁的 NCR 也因历史合同被摊上数百万美元责任。

这项业务至今仍未消失。QLT 在 2012 年声称拥有超过 30 万客户，LinkedIn 显示公司只有 11 至 50 名员工，其中数人从 AT&T 拆分时代一直任职。它在 2019 年表示，约四分之三受访租赁客户家中另有至少一部自购电话，并把租赁机解释为高可靠性的备用设备；这一数据同时说明大量客户长期付费，却很少真正需要租来的电话。QLT 仍以药房折扣、优惠券和换机服务包装租约，继续发行随账单寄送的 Lease News & Views，并以每月 5.95 美元出租一部 touch-tone 的 Western Electric 500 风格电话——实物更接近 Cortelco 2500——同一部电话买断只需 45 美元。电话租赁的漫长余生由此揭示出监管改革最隐蔽的失败：市场竞争成功解放了新消费者，却没有终结旧合同的收费权，原有垄断关系便以资产的形式穿越拆分、并购和品牌更替，依靠用户的疏忽继续获利。
