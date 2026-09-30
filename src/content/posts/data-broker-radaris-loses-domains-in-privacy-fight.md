---
title: "Data Broker Radaris Loses Domains in Privacy Fight"
date: 2026-09-30T21:57:05Z
category: reading
description: "新泽西州法院依据 Daniel's Law 判决数据经纪商 Radaris 移交 radaris.com 等 14 个域名，案件牵出其长期通过虚构股东、离岸实体逃避监管的运作方式。"
source: "https://krebsonsecurity.com/2026/09/data-broker-radaris-loses-domains-in-privacy-fight/"
author: "BrianKrebs"
---

Radaris 长期无视个人信息删除请求，最终在新泽西州的诉讼中失去了 radaris.com 等 14 个域名；但域名移交能否维持，以及针对数据经纪商的隐私保护法能否经受宪法审查，仍未有定论。2024 年 2 月，Atlas Data Privacy Corp 起诉 Radaris 违反 **Daniel's Law**：这部法律允许州执法人员、政府工作人员、法官及其家属要求商业数据经纪商彻底删除个人信息，对无视请求的公司可按每项违规处以 1,000 美元罚款。Radaris 一方多次拖到最后时刻才应诉，并争辩 Atlas 没有起诉网站的真正所有者。Atlas 于 2025 年 6 月重新起诉，将更多同系人物搜索网站列为被告；今年 8 月 26 日，法官认定被告已有多次出庭抗辩的机会却未利用，随后下令移交域名。radaris.com 目前显示 Atlas 的法院移交通知，不再出售美国居民的详细个人档案。

这场诉讼之所以旷日持久，关键在于网站运营者、域名所有者和法律实体的身份不断变动。Radaris 联合创办人、住在马萨诸塞州的俄裔兄弟 Igor 和 Dmitry Lubarsky 曾通过律师声称，公司真正的所有者是住在乌克兰的乌克兰人；律师 Val Gurvits 后来承认，Radaris 使用过虚构 CEO "Gary Norden"的名字，而公司多年来还在向潜在投资者募资的新闻稿中引用过这位假 CEO。Atlas 首席执行官 Matt Adkisson 称，被告又不断把隐私政策中的管理实体改为位于 Marshall Islands、British Virgin Islands 或 Seychelles 的公司；Atlas 曾派调查员到 Marshall Islands，发现 Radaris 声称负责管理网站的新实体当时甚至尚未成立。辩方一面主张运营域名的实体才应被起诉，一面主张实际持有域名的实体不应承担责任。

类似策略曾奏效。Radaris 在 2017 年的一宗集体诉讼中因未应诉而面临 750 万美元缺席判决；原告无法收款后，法院一度命令 Verisign 移交 radaris.com。Gurvits 上诉称，诉讼没有列入当时持有域名的塞浦路斯公司 Bitseller Expert Limited，移交域名会侵犯其正当程序权利。法官因此叫停移交，允许原告重新起诉，但原告没有继续推进。Atlas 的律师 Raj Parikh 认为，以往原告往往被这类程序争议和跨国追偿难题耗尽资源；Atlas 这次决定持续追诉，是因为网站持续暴露新泽西州执法人员和其他公职人员的信息。Radaris 现任律师 Victor Worms 则称，针对"Radaris.com"这一非法人的缺席判决无效，已申请撤销，并拟就域名移交提出上诉。

Atlas 称，诉讼取得的逾 10,000 封邮件和文件把这些名义上分立的公司连到了一起：Radaris America、Bitseller、Veripages 等实体由同一小批人使用相同邮箱管理，共用银行账户或支付卡及一处虚拟办公室；来自银行、支付处理商、托管商、注册商和公司内部系统的记录，指向一个由波士顿地区小团队经营、涵盖 radaris.com 和至少 25 个其他人物搜索网站的业务。按 Atlas 对邮件的解读，Radaris.com 每月收入约 42,000 美元，Veripages.com 通过与旗下拥有 PeopleLooker、PeopleSmart、NumberGuru 等品牌的 Lifetime Value Company 合作，每月收入约 45,000 美元；网站群与个人信息删除服务 Onerep 的合作，每月还可带来高达 25,000 美元。Onerep 创办人此前被揭露经营过数十个人物搜索网站，并仍在运营 Nuwber，使"删除信息"服务与信息曝光业务形成利益纠缠。

域名移交并未结束更大的法律争执。Radaris 相关公司仍可能因 Daniel's Law 的每项违规面临 1,000 美元罚款；与此同时，Atlas 起诉的约 150 家其他数据经纪商中，至少 70 宗案件已被移至联邦法院，业界主张该法范围过广、侵犯第一修正案权利。联邦第三巡回上诉法院尚未裁决，案件也被普遍预计可能上诉至最高法院。至少 14 个其他州已通过仿照新泽西州的法律，但西弗吉尼亚州版本在 2025 年 8 月被一所联邦地区法院裁定表面违宪。

隐私专家 Justin Sherman 指出，即使 Daniel's Law 获得支持，它保护的仍只是特定人群；州隐私法通常把选民登记、房产文件、婚姻与法院记录等"公共"或"政府"记录排除在外，人物搜索业务仍可依靠这些资料运转。他还以年龄验证为例：至少 25 个州要求成人内容网站核验访问者年龄，联邦法律却没有限制扫描驾照的公司如何使用、分享或保存所得资料；IDScan.net 近期的数据泄露涉及超过 1.53 亿美国人的驾照信息。Radaris 案显示，夺回域名可以暂时切断一项具体的个人信息销售业务，但要让普通人也获得持续保护，仍取决于覆盖数据收集、流转和保存的全面隐私法律。
