---
title: "LinkedIn is scanning browser extensions"
date: 2026-05-02T08:02:51Z
category: reading
description: "LinkedIn 的扩展扫描不是普通反欺诈遥测，而是把 Chrome 扩展清单变成一组可归属到真人职业身份的隐性属性：它能推断求职意图、政治/宗教/健康/神经多样性线索、隐私与安全工具使用情况，并在员工聚合层面暴露公司的工具链和工作流。"
source: "https://404privacy.com/blog/linkedin-is-scanning-your-browser-extensions-this-is-how-they-use-the-data/"
---

## TL;DR
LinkedIn 的扩展扫描不是普通反欺诈遥测，而是把 Chrome 扩展清单变成一组可归属到真人职业身份的隐性属性：它能推断求职意图、政治/宗教/健康/神经多样性线索、隐私与安全工具使用情况，并在员工聚合层面暴露公司的工具链和工作流。

## 核心主张拆解
- LinkedIn 探测的是登录用户的浏览器，而 LinkedIn 已经知道用户姓名、雇主、职位、职业史、地点和人脉；因此扩展扫描不是匿名设备指纹，而是直接贴到职业身份上的软件画像。
- 扫描清单已从 2017 年至少 38 个扩展增长到 2026 年约 6,278 个扩展，作者判断这不是手工维护，而是长期运行的 Chrome Web Store manifest 抓取与 probe-target 生成基础设施。
- 风险不只落在个人：求职类扩展可暴露“正在悄悄找工作”，政治、宗教、残障辅助、神经多样性相关扩展可产生敏感推断；跨员工聚合后，还可能映射公司内部工具、安全产品、竞品订阅和工作流程。
- 文章最重的指控是“未告知 + 可用于执法”：作者称 LinkedIn 隐私政策没有披露扩展扫描；browsergate 记录显示 Milinda Lakkam 曾在宣誓下确认 LinkedIn 会针对安装特定扩展的用户采取行动。

## 技术机制
- LinkedIn 的脚本向 `chrome-extension://{extension_id}/{file_path}` 发起 `fetch()`；如果扩展安装且该文件在 `web_accessible_resources` 中，request 会成功，否则 Chrome 阻止并在控制台报错。
- 扫描有两种模式：`Promise.allSettled()` 并行探测全部扩展，或按可配置延迟顺序探测以降低监控可见性；还可用 `requestIdleCallback` 推迟到浏览器空闲时执行。
- 硬编码列表之外还有一个名为 Spectroscopy 的系统：遍历 DOM 文本节点和元素属性，寻找 `chrome-extension://` 痕迹，用来捕捉会修改页面的扩展。
- 检测结果进入同一遥测管线：打包成 AedEvent / SpectroscopyEvent，用 RSA 公钥加密后发往 LinkedIn 的 `li/track`，并作为 HTTP header 注入后续 API 请求。
- 扩展扫描只是 APFC / DNA 设备指纹系统的一部分；该系统还采集 canvas、WebGL、音频处理、字体、屏幕、硬件并发、设备内存、电池、本地 IP via WebRTC、时区、语言等 48 类浏览器/设备特征。

## 更大意义
- 浏览器指纹的危险在于“可拼接”：LinkedIn 一旦把指纹绑定到实名职业档案，就可能用第三方行为数据反向补全站外浏览、购买、位置和兴趣轨迹。
- 对记者、律师、研究员、人权调查者等高风险职业，隐私工具、安全扩展、研究工具被实名平台收集，会从广告隐私问题升级为操作安全问题。
- DMA 语境让这件事更敏感：Microsoft 在 2024 年被指定为 gatekeeper，LinkedIn 属于受监管产品；browsergate 主张 LinkedIn 对第三方工具用户的系统性执法与隐蔽扫描可能违反 DMA。作者还称德国 Bamberg 的 Bavarian Central Cybercrime Prosecution Office 已确认刑事调查。

## 证据薄弱处
- 技术部分有较强可验证性：扩展 probe、控制台错误、扩展 ID 列表、混淆 JS、事件上报路径都可复核。
- 法律与执法部分依赖 browsergate、GitHub 仓库、宣誓记录和即将公开的法院文件；文章给出方向，但完整证据链尚未在文内展开。
- “跨平台数据拼接”是合理风险推演，不等于文章已证明 LinkedIn 实际购买并合并了某个第三方行为数据集。

## 最后判断
这件事真正危险的地方，是浏览器扩展清单本身已经接近一份“隐性履历”：它记录你的工具、意图、脆弱点和行动偏好，而 LinkedIn 恰好掌握把这份隐性履历绑定到真实职业身份和雇主网络的上下文。
