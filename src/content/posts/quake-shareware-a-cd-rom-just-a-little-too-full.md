---
title: "Quake Shareware, a CD-ROM just a little too full"
date: 2026-11-18T15:55:09Z
category: reading
description: "id Software 在 1996 年把完整游戏目录的加密版本塞进 Quake Shareware 光盘，试图让玩家通过电话付费即时解锁，却把生成解锁码所需的全部材料也一并交给了玩家；光盘上市仅 39 天，整套保护就被破解，原本用于直销的分发渠道成了免费获取全部游戏的入口。"
source: "https://fabiensanglard.net/quake_shareware_cd/index.html"
---

id Software 在 1996 年把完整游戏目录的加密版本塞进 Quake Shareware 光盘，试图让玩家通过电话付费即时解锁，却把生成解锁码所需的全部材料也一并交给了玩家；光盘上市仅 39 天，整套保护就被破解，原本用于直销的分发渠道成了免费获取全部游戏的入口。

这个商业实验源于 CD-ROM 容量与游戏体积之间的悬殊。1990 年代中期，一张 CD 可容纳约 640 MiB，达到当时 PC 硬盘容量的三倍，游戏开发商却往往制作不出足够多的素材填满它。《7th Guest》和《Phantasmagoria》用 Full Motion Video 消耗容量，另一些游戏加入高品质音乐。John Carmack 在 1994 年甚至开玩笑说，如果 DOOM 出 CD 版，可以随盘附送一小时的制作纪录片。到 1996 年 6 月，历经三年开发的 Quake 完成，其 Shareware 版本只占 22 MiB，id Software 于是决定利用余下空间放入加密的完整游戏，包括 Quake、多个 DOOM 版本、HEXEN 和 HERETIC，让玩家打电话、刷信用卡后立即解锁，减少销售中间环节。

这张光盘于 1996 年 7 月 3 日公布，8 月 30 日上市，玩家可以在 CompUSA、Computer City 等连锁商店以 9.95 美元购买。包装上的电话通向解锁服务，另有标识零售渠道的 SOURCE CODE；后者不参与解锁码生成，可能用于分销商认领交易佣金。因此，这套试图缩短销售链的设计，仍保留了实体零售与电话订单处理的环节。《Masters of Doom》记载，破解之外，分销和订单履约也逐渐失控，id Software 想叫停零售 Shareware 时，仓库里已经积压了近 15 万张光盘。

从玩家看到的界面看，解锁流程具备几层防护。程序为所选游戏生成一个 CODE NUMBER，即 **CHALLENGE**，玩家向电话客服报出这个号码，付款后获得 UNLOCK CODE NUMBER，即 **SERIAL**。两种号码都带校验机制，以降低电话口述出错的风险；CHALLENGE 每次启动都会变化，界面运行期间还会每五分钟轮换，防止旧 SERIAL 被重复使用。程序因此提醒玩家备份已解锁的游戏，因为同一 SERIAL 无法保证以后再次安装。

底层保护由 TestDrive Corp. 提供。它将游戏安装程序的前 32 KiB 替换成禁用提示，把处理后的可执行文件改名为 .MJ3，再把原始头部加密存为 .ST3，并生成恢复所需的 seed。光盘上同时保存了各游戏的 MJ3 文件，以及 PAGEMKR 档案中的 ST3 文件。如果恢复文件所需的秘密只能在付款后从外部取得，那么把这些受保护的数据提前分发出去，本身并不构成漏洞。

致命问题出在 **SERIAL 并未带回任何客户端原先不掌握的秘密**。光盘自带的 FLOW.EXE 能直接根据 CHALLENGE 生成正确 SERIAL，它对玩家输入的验证，只是与本地计算结果进行比较。电话解锁码承担的是付款凭证的作用，而全部验证逻辑都在玩家手里。GNOMON 因而可以制作 QCRACK.EXE，根据 CHALLENGE 自动生成 SERIAL，解锁光盘上的每一款游戏；该工具于 1996 年 10 月 8 日发布。

本地生成过程虽然曲折，却没有改变这个安全边界。2016 年，rmolina 逆向还原了计算链：11 位 CHALLENGE 被拆成四位 GAME-ID，以及决定 OFFSET、DEPTH 的七位数字；GAME-ID 在加密数据库 SKU.17 中查出游戏 CODENAME，再据此从 FLOWLIB.LIB 提取对应的 512 字节 DOC 文件。DOC、CODENAME 和固定字符串“Testdrive Corp.”共同变换一张硬编码表，得到该游戏专属的 254 个 16 位数值；程序随后依据 OFFSET、DEPTH 反向遍历并执行 XOR 运算，生成中间值 MEM，最终计算出以 B 开头的 SERIAL。这些查表与变换增加了逆向分析的工作量，但所需数据和算法始终完整地留在光盘上。

其他缺陷进一步暴露出产品缺乏打磨。Final DOOM 的 GAME-ID 为 12，SKU.17 却把它的 CODENAME 写成了首字母大写的“Final”，正确值应为“final”，导致程序取错 DOC，付费用户无法通过正常电话流程解锁，盗版用户反倒能获得更顺畅的体验。所谓加密数据库也有明文副本 SKU.TXT 留在 FLOWDIR 档案中，PRODUCT、EXE 等文件同样同时保留了明文与加密版本；光盘还混入 DM.TMP 临时文件、FLOWWORK.BAK 编辑备份及未使用的 ENCRYPT.EXE。存放关键 DOC 文件的库格式既未加密也未混淆，进一步降低了提取难度。Sanglard 将这些迹象归于时间压力下的仓促交付：容量充裕让 id Software 得以提前分发整套商品，但这套商业模式能否成立，最终取决于解锁系统是否真正把授权秘密留在玩家触及不到的地方。
