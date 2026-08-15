---
title: "Google is killing the open web, part 2"
date: 2025-11-19T08:43:10Z
category: reading
description: "Google 弃用 XSLT 的真正证据是 polyfill 存在却故意不内置——若 polyfill 够用，透明内置即可，无需任何人改代码；偏偏不这么做，就把改动负担转嫁给开发者，用\"安全借口\"完成功能驱逐。配合 Mozilla 删除 RSS Live Bookmarks、WHATWG 主导 Manifest..."
source: "https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/"
---

## TL;DR
Google 弃用 XSLT 的真正证据是 polyfill 存在却故意不内置——若 polyfill 够用，透明内置即可，无需任何人改代码；偏偏不这么做，就把改动负担转嫁给开发者，用"安全借口"完成功能驱逐。配合 Mozilla 删除 RSS Live Bookmarks、WHATWG 主导 Manifest V3、2013 年废除 NPAPI，构成同一份剧本：让开放 Web 的技术基础设施逐步萎缩，每次都有一个"技术原因"可以援引。

## 核心主张拆解
- **polyfill 逻辑漏洞**：polyfill 需要开发者主动改为非标准 JS 调用，而非透明替换——这个"需要你去做"本身就是目的，不是局限。Google 要的就是你觉得太麻烦而放弃。
- **Mozilla 的同构操作**：移除 RSS Live Bookmarks 时推给第三方插件，没有官方替代；而 Pocket 却强制预装直到关服。行动比声明诚实。
- **WHATWG = 监管俘获**：WHATWG 原由 Opera/Mozilla 发起，现在驱动力是 Google/Apple/Microsoft；它对 Web 的定位是企业盈利平台，而非用户可控的知识库。与当年微软借 IE 垄断 Web 的逻辑完全同构，只是规模更大。
- **2013 年是关键节点**：NPAPI 弃用公告、EME 标准化（DRM 进 HTML5）、Manifest V3 前身逻辑——三件事同年并发，无一对用户有利，全部对大型平台公司有利。
- **插件接口消失的代价**：NPAPI 允许任何人扩展浏览器支持的协议和格式；没有插件接口，新格式只能等 Google/Apple/Mozilla 点头——谁能在 Web 上生存被三家公司预先决定。EME 的顺利推进证明"技术上做不到平滑过渡"是谎言：只要对大公司有利，过渡可以做得极其平滑。

## 值得质疑
作者对 Firefox 分支的分析停留在观望，但没有估算时间窗口：WaterFox/Pale Moon 是否有足够的工程资源在 Firefox 弃用 XSLT 后及时维护分叉——这是"抵抗路径可行"这一论点的关键，文章回避了。

## 留下的那个想法
浏览器生态的核心权力转移不是"开源 vs. 闭源"，而是"谁决定用户能访问哪些格式和协议"——插件接口的消亡把这个权力永久交给了三家公司，而那个交接仪式发生得如此安静，几乎没人注意到。
