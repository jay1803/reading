---
title: "AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint"
date: 2026-10-24T15:32:51Z
category: reading
description: "AliExpress 首页悄悄运行静音 WebAudio 指纹采集链，足以占住蓝牙音频通道，阻止 multipoint 耳机切回手机，静音标签页也无法解决。"
source: "https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html"
---

AliExpress 首页会悄悄运行用于浏览器指纹采集的静音 WebAudio 处理链，而这些听不见的音频活动，在作者的设备上足以占住电脑的蓝牙音频通道，阻止支持 multipoint 的耳机切回手机，连静音标签页、Firefox 或 Windows 都无法解决。

作者的耳机同时连接 PC 和手机，平时由 PC 优先播放音频，PC 空闲时便能正常播放手机音乐。但在 Firefox 或 Chrome 中打开 AliExpress 首页，等待几秒后，手机音乐就会中断；关闭 AliExpress 标签页，播放立即恢复。页面没有可见的视频或音乐，排查也没有发现任何 <audio>、<video> 元素、HTMLMediaElement.play() 调用或有效的媒体播放状态，navigator.mediaSession.playbackState 始终为 none。这使调查从常规媒体播放转向了底层的 Web Audio API。

通过在页面加载前监测 AudioContext 的创建及 AudioNode.connect() 调用，作者发现首页会创建两个进入 running 状态、并连接到 AudioContext.destination 的音频上下文。调用栈分别指向 Alibaba 资源域名下的 collina.js 和 fireyejs.js，路径位于 AWSC/uab/1.140.0/ 与 AWSC/fireyejs/1.231.67/，看起来属于浏览器安全与反滥用组件。这两个脚本经过高度混淆；作者借助 AI 分析仍可辨识的名称与操作，重建出它们的音频处理流程。

两个脚本的处理链都大致由锯齿波振荡器、AnalyserNode、ScriptProcessorNode、增益设为零的 GainNode，以及系统音频输出端组成。振荡器生成已知波形，分析器读取经过浏览器音频实现处理后的频率数据；不同浏览器版本、操作系统、音频库和硬件产生的细微差异，可以成为设备指纹的一部分。**零增益只让最终输出听不见，连接系统输出端仍会让浏览器持续处理音频图。**作者据此判断，这种活动在其 Firefox／Windows 环境下维持了 PC 蓝牙音频路径的活跃状态，妨碍耳机切回手机；标签页静音也没有终止这些处理链。

音频测量只是这套采集机制的一部分。脚本还涉及 canvas 渲染与 toDataURL()、WebGL 渲染器信息与扩展及着色器精度、屏幕和视口尺寸、device pixel ratio、硬件并发数与设备内存、浏览器插件、音视频格式支持、WebRTC 行为、性能计时，以及鼠标、触摸、焦点、滚动、设备运动和方向事件，同时检测常见的浏览器自动化特征。代码还包含结果序列化、加密，以及通过 fetch() 或 sendBeacon() 向 Alibaba 遥测服务发送数据的逻辑。单独的音频特征未必能唯一识别设备，与图形、硬件、计时和交互数据组合后，识别价值便明显提高。

这种采集有明确的商业与安全动机：AliExpress 需要应对账号接管、批量假账号、抓取、自动购买、支付欺诈、评价操纵，以及优惠券和新客促销滥用，也有利用用户行为数据进行营销的需求。Cookie 容易被清除、复制或替换，多种独立测量组成的指纹更难被一致伪装，交互行为也能帮助区分真人与自动化客户端，从而减少部分 CAPTCHA 验证。不过，浏览器端代码只能证明这些指纹式测量被采集并传输，无法证明服务端最终将其用作持久设备标识，还是反欺诈与机器人检测评分的输入，更无法确认保存期限或是否与其他 Alibaba 产品关联。

作者用 Firefox 上 Raymond Hill 开发的官方 uBlock Origin，定向拦截 assets.aliexpress-media.com 域名下 AWSC/uab/*/collina.js 与 AWSC/fireyejs/*/fireyejs.js 两类脚本，并将规则限制在 aliexpress.com 的脚本请求范围内。对照测试显示，拦截后首页仍能渲染，监测期间没有再出现 AudioContext 创建或输出端连接，手机音乐也不再被打断。应用规则后需要关闭已有 AliExpress 标签页再重新打开，因为阻止后续脚本加载不会销毁已经创建的音频上下文。

这项处理的验证范围仍限于首页和普通商品浏览。两个脚本可能参与反欺诈，拦截后可能增加 CAPTCHA，或影响登录与结账；作者建议遇到合法登录或付款受阻时临时禁用规则，也承认脚本路径和实现变化可能让规则失效。其选择拦截的核心理由是：普通购物首页在用户尚未执行敏感操作时，就无提示地启动了广泛的设备与行为采集，并产生可感知的硬件副作用。这个案例揭示了静音与停止占用音频资源之间的区别：一段没有声音、没有播放标志的网页代码，依然能够影响浏览器之外的耳机切换行为。
