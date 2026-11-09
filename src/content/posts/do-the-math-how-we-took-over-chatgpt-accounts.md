---
title: "Do the math: How we took over ChatGPT accounts"
date: 2026-11-09T11:08:29Z
category: reading
description: "这次漏洞的核心结论是：一个普通的 ChatGPT 公共分享链接，曾能把攻击者控制的 JavaScript 注入访问者已登录的 chatgpt.com 会话，从而读取其从未分享过的私人对话，并以受害者身份调用前端可用的认证 API。受害者无需安装 App、加入 Project、粘贴"
source: "https://www.parameter.ai/labs/we-found-a-gap-at-openai"
author: "armcat"
---

这次漏洞的核心结论是：一个普通的 ChatGPT 公共分享链接，曾能把攻击者控制的 JavaScript 注入访问者已登录的 chatgpt.com 会话，从而读取其从未分享过的私人对话，并以受害者身份调用前端可用的认证 API。受害者无需安装 App、加入 Project、粘贴代码或打开开发者工具；在最成熟的利用版本中，仅打开恶意 `/share/<id>` 链接就会触发完整攻击链。OpenAI 于 2026 年 10 月 26 日完成修复，将漏洞定为 P1，并支付了 5,000 美元赏金。

攻击链由两个各自看似安全的功能拼接而成：交互式图表在 ChatGPT 主页面加载 MathLive，HTML Preview 则在隔离域名的 frame 中运行攻击代码。Preview 的沙箱本身有效，其代码无法访问 `parent.document`，但跨域 frame 仍可通过浏览器的 `postMessage` 向顶层页面发送消息。MathLive 为虚拟数学键盘安装了消息监听器，却在处理 `mathlive#virtual-keyboard-message` 时没有同时验证 `event.origin` 和 `event.source`，其 origin policy 实际为 `none`，因此来自任意网站、任意窗口的发送者都能提交改变键盘状态的指令。

Preview 先发送 `update-setting` 消息，用攻击者提供的内容替换虚拟键盘 layout，再发送 `show` 消息要求 MathLive 显示键盘。这个 layout 的 `layers[].markup` 可以包含原始 HTML；MathLive 将各层拼接成字符串后，通过 `innerHTML` 写入真实的 ChatGPT 页面。名为 `createHTML` 的辅助函数虽然看起来与安全处理有关，实际只是 identity-style Trusted Types 包装器，它把字符串标为可信，却没有净化其中的攻击内容。由此，受限 Preview 获得了一条把任意 HTML 写进主页面的跨沙箱通道。

直接通过 `innerHTML` 插入 `<script>` 不会执行，因此研究者改用没有 `sandbox` 属性的 `iframe srcdoc`。`srcdoc` 会触发一次新的 HTML 文档解析，而这个 iframe 由 ChatGPT 主文档创建，因而继承 `https://chatgpt.com` 的 origin；其中执行的代码可以访问父页面及其认证上下文。此时 ChatGPT 的 Content Security Policy 仍阻止内联脚本，但允许加载 YouTube 脚本，这为最后一步 CSP 绕过留下了空间。

YouTube 的 oEmbed 接口支持 JSONP 风格的 `callback` 参数。接口虽然会判定恶意 callback 名称无效，却先把 callback 原样写进 JavaScript 响应，再附上错误对象。研究者构造类似 `globalThis.__marker=31337;void` 的 callback，使响应先执行任意语句，再由 `void(...)` 吞掉随后追加的错误对象。由于 `www.youtube.com` 已在 ChatGPT 的 CSP 允许列表中，浏览器会把这个 HTTP 200、`text/javascript` 响应当作脚本，在新建的同源 iframe 内执行。至此，原本被隔离在 Preview 域名中的输入，经过 MathLive 的未认证消息通道、HTML 注入、无沙箱 `srcdoc` 和 YouTube JSONP，最终变成以 chatgpt.com 身份运行的任意 JavaScript。

研究者最初使用自己控制的 ChatGPT App 发送消息，但这种复现要求受害者连接或调用 App，现实攻击价值有限。随后尝试通过原生 HTML 附件传递 payload，附件可以在 Preview 中发送恶意消息，但导出公共分享时，附件会保留，负责加载 MathLive 监听器的早期图表却会消失。最终可行的载体是把两部分都放进同一段普通公开对话：一个真实图表负责在主页面初始化 MathLive，后续由 assistant 生成的 HTML Preview 负责发送两条消息。这样生成的 `/share/<id>` 可以通过邮件、聊天、工单或社交媒体传播，并在其他账号和 workspace 中复现。

最稳定的早期版本要求受害者点击一次 ChatGPT 自带的 Preview 按钮；研究者随后把 HTML block 标记为可自动预览，使它在分享页打开后自行运行。他们在独立账号中连续复现三次，包括 hard refresh 后的情况，alert 约在 4.5 秒后出现。由于图表和 Preview 独立加载，恶意消息偶尔会早于 MathLive 监听器就绪，最终 payload 会在有限时间内重复发送两条消息，并在主页面设置 guard，保证读取私人对话和对外请求只执行一次。

能够在页面上显示一个由浏览器认定来自 chatgpt.com 的 alert，或直接修改主页面并插入 banner，只证明了同源代码执行；真正的影响来自它继承了受害者的认证环境。payload 从父页面的 `#client-bootstrap` 解析 session access token 和 account ID，在两者都存在时还会确认 token 内的账号与 session 一致，然后携带 `Authorization: Bearer <victim token>` 和 `ChatGPT-Account-ID: <victim account>` 请求 ChatGPT 后端。它先通过 `/backend-api/conversations?...&limit=20&order=updated&offset=0` 枚举最近对话，再通过 `/backend-api/conversations/<conversation-id>?num_turns=2` 读取指定私人会话；只有 detail 请求返回 403、404 或 405 时，才回退到旧版 `/backend-api/conversation/<id>?include_full_conversation=true` 路径。

这些操作直接调用受认证 API，并非抓取屏幕上已经显示的文字。研究者成功读取了一段与恶意分享完全无关、从未向攻击者公开的私人对话，再用普通图片请求把其中一个经过控制的小片段发送到自己的服务器。验证过程中只外传少量值是为了限制披露范围；注入代码已经拿到了完整的认证响应，也能读取其中内容。完成请求前，代码还主动清除了对 token、account、bootstrap、session 和请求 headers 的引用。由于它运行在正常前端的安全边界内，影响也不局限于论文中演示的两个 conversation endpoints：凡是 ChatGPT 网页端允许当前账号读取的数据或执行的动作，理论上都可能被同一脚本调用，实际效果接近接管受害者的 ChatGPT 账号。

完整 payload 的编码过程也说明这条链并非概念性的 alert。研究者先把读取函数经 `toString()` 转成源码，将双引号改成单引号并压缩空白，再用 `URLSearchParams` 编入 YouTube callback；随后在 `<script src>` 中进行 HTML 转义，并把整个 script 元素再次转义后写进 iframe 的 `srcdoc` 属性。最终 callback 长 5,533 个字符，YouTube URL 长 7,309 个字符，script 元素长 7,337 个字符，完整 iframe markup 长 7,390 个字符。Google 会改写 callback 中的尖括号，因此 payload 还特意使用传统 function 语法，避开依赖箭头函数或相关字符组合的写法。

根本缺陷集中在三个连续的信任失误：MathLive 接受了未经发送者身份验证的状态修改消息，跨窗口 setting 允许携带原始 HTML，受影响的 HTML 又能创建继承 chatgpt.com origin 的无沙箱文档。YouTube JSONP 只是把 HTML 注入升级为 JavaScript 执行的最后一条 CSP 绕过路径；单独封禁该 endpoint，只会切断当时使用的脚本载体，仍会留下不受信任 Preview 向主页面注入 HTML 的高危能力。Trusted Types 同样无法补救 identity policy，因为它只能限制谁有权向 HTML sink 赋值，不能自动使攻击者控制的字符串变得安全。

研究者在 10 月 13 日确认 MathLive 消息到 HTML 的生产环境路径，14 日通过正常 UI 将固定 alert 升级为任意 JavaScript，16 日完成跨账号、跨 workspace 的公共分享复现，17 日验证自动 Preview 和 hard refresh 后触发，18 日向 OpenAI bug bounty 提交报告，19 日补充私人聊天数据外泄证明。OpenAI 于 21 日完成复现，并将最初的 P2 提升为 P1；22 日表示一个 web frontend 已修复、另一个仍在更新，23 日先通过 CSP 改动阻断部分链路，26 日确认两个前端版本都已拒绝报告所用的跨 frame MathLive 消息并结案。

修复所体现的防御原则是：处理状态变更的 `postMessage` receiver 必须同时验证 `event.origin` 与获准通信的具体 `event.source`；跨窗口设置不能接受原始 HTML；只要动态文档内容可能受不可信 frame 影响，它就必须持续处于 sandbox 中；CSP 只能承担纵深防御，无法替代安全的消息认证和渲染路径。**真正需要审计的是跨功能组合形成的完整信任链**：Preview、图表、MathLive、frame 创建、第三方 CSP 白名单和公共分享单独看都很合理，但它们在同一页面相互连接后，使一个公开内容入口穿透了沙箱并获得登录账号的全部前端权限。
