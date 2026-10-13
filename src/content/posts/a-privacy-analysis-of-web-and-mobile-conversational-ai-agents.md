---
title: "A Privacy Analysis of Web and Mobile Conversational AI Agents"
date: 2026-10-13T07:10:00Z
category: reading
description: "研究发现对话式 AI 把广告追踪体系带入私人对话：提问、标题和会话链接常与持久身份标识一起流向第三方，部分会话链接还缺乏访问控制。"
source: "https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf"
author: "damaru2"
---

消费级 Conversational AI 已把广告追踪体系带进私人对话：用户的提问、自动生成的标题和会话链接会与持久身份标识一起流向第三方，拒绝非必要 cookies 或购买付费订阅都无法可靠阻止这种暴露。风险来自两条相互连接的路径：服务把对话衍生信息交给广告与分析平台，部分会话链接又缺乏访问控制，使获得链接的一方能够进一步读取完整内容。

研究团队在西班牙对 ChatGPT、Claude、Grok、DeepSeek、Perplexity、Gemini、MS Copilot、Mistral 的 Le Chat 和 Meta AI 进行测试，覆盖九个网页客户端和八个 Android 客户端。实验使用模拟医疗咨询的可复现提问，比较访客、免费与付费账户，以及忽略、拒绝和接受 cookie 横幅的状态；网页侧检查网络请求、cookies、存储与经过编码或哈希处理的标识，移动侧结合代码静态分析和运行时监测，再用未登录的独立会话检查链接权限。主要测量发生于 2026 年 5 月，企业和政府订阅不在研究范围内，Gemini 移动端的网络流量也未能成功提取。

所有受测服务都连接至少一家 Advertising and Tracking Service（ATS）。研究识别出 124 个第三方域名，归属于 44 家组织，其中 34 家属于 ATS；Google 产品最普遍，其后包括 Sentry、Meta、Datadog 和 Intercom。网页与移动端接入的基础设施并不相同：11 家 ATS 同时出现在两端，15 家仅见于网页，八家仅见于移动端。DeepSeek 还使用较少被追踪数据库记录的 Fengkong Cloud 与 ShuMei，涉及设备指纹和风险评分。移动应用也大量借助 WebView 引入网页追踪：移动客户端所连接的不同端点中，71% 来自 WebView，Grok 达到 98%，Perplexity 为 91%，ChatGPT 为 71%。Grok 因而能在原生应用内部加载 Google Ads、TikTok Analytics、Twitter Analytics 和 Meta Pixel。

第三方连接的存在本身不能证明对话泄露，研究进一步检查了实际传输的数据。结果发现，九个网页客户端中有六个、八个 Android 客户端中有三个向第三方发送对话衍生信息。五个网页客户端泄露会话 URL 或全局会话 ID，接收者涉及九家 ATS，其中三个客户端默认就会发送，另外两个在接受 cookies 后发送。ChatGPT 和 Claude 还会把会话 ID 作为独立参数交给 Datadog；即使请求没有直接携带完整 URL，这种 ID 也可能支持链接重建。三个网页客户端把自动生成的对话标题传给九家第三方，接收者包括 Meta、TikTok 和 DoubleClick，其中八家相关接收方的传输仅在接受 cookies 后出现。标题已经概括了对话主题，足以暴露健康问题、财务状况或工作活动，无须取得逐字聊天记录。

这种内容暴露与身份追踪结合后，能够形成跨会话、跨服务的个人画像。Grok 在正常聊天期间就向多家 Google 服务、TikTok 和 Twitter Analytics 发送会话 ID、URL 或标题；其一次 Meta Pixel 请求同时携带会话 ID、标题、完整会话 URL、分享 ID 和分享 URL，并附带用于身份关联的 _fbp cookie。Perplexity 向 Singular 发送用户邮箱哈希，另外四家提供商把用户名或账户 ID 与对话信息一起传输。**邮箱哈希并不自动构成匿名化**：只要接收方能用已有邮箱数据匹配哈希，或者能将它与广告标识、账户 ID 连接，对话信息就仍然可以归属于同一个人。

部分数据流通过第一方域名和服务端转发，降低了浏览器拦截与用户检查的有效性。Claude 经 `a-cdn.anthropic.com` 接入 Segment，再通过 Conversion API 将事件转发给 11 个广告平台，包括 Facebook、LinkedIn、TikTok、Reddit 和 Google Enhanced Conversions；事件携带共享标识，使不同平台的数据可以在同一会话中连接。Grok 则使用 server-side Google Tag Manager，把会话 URL 和标题转发给 Meta Conversions API 与 TikTok Events API，同时携带 Meta 的 `_fbp` 和 TikTok 的 `_ttp` cookies，搭起两个广告体系之间的身份桥梁。这些服务端链路无法仅凭浏览器端请求完整观察，也能绕过常规广告拦截器。研究还在所有提供商的脚本中发现与指纹识别相关的 JavaScript API，但这只能证明技术能力存在，不能证明每家都实际进行了指纹追踪。

移动端暴露的数据有所不同：研究未观察到会话 URL 和标题传输，却发现邮箱、账户标识、广告 ID 与 SDK 标识的组合。Perplexity 把邮箱交给 RevenueCat，Grok 把邮箱及其哈希交给 TikTok 和 Twitter Analytics；Copilot、Grok、Perplexity 分别向 Adjust、AppsFlyer、Singular 发送 Android Advertising ID（AAID）。Grok 和 Perplexity 还将 AAID 与用户或安装标识一起发送，削弱了重置广告 ID 切断追踪的作用。Claude 向 Datadog 发送会话 ID，同时附带 Datadog 生成的标识和账户关联标识，并向 Sift Science 发送地理位置与 Android ID；Meta AI 则向自己的服务器发送 Android ID。

cookie 选择能够减少部分数据流，但保护范围有限。接受非必要 cookies 会在 Claude、Perplexity 和 Grok 中启用更多广告服务；拒绝后，Perplexity、DeepSeek、Gemini、Copilot、ChatGPT 和 Claude 仍连接 Google Ads。研究发现，拒绝 cookies 后仍有 80.8% 的第三方追踪服务保持活跃，九家服务中有四家仍存在数据收集；这个数字描述的是追踪方活动，不能直接理解为同等比例的聊天正文继续外泄。拒绝确实能切断部分 Meta Pixel、Datadog 遥测以及 Claude 向 11 个广告平台的转发，但免费与付费账户整体上呈现近乎相同的第三方交互。Claude 移动端免费账户出现、付费账户未出现 Intercom 和 Sentry，是少数例外，也可能来自动态代码路径差异。移动应用通常仅要求接受服务条款和隐私政策，没有对应网页 cookie 横幅的独立选择机制。

链接权限进一步决定了元数据泄露是否会升级为完整对话暴露。Grok 的免费和付费会话链接默认可以在未登录状态下访问，用户需要主动退出这种公开设置；Perplexity 的访客会话始终公开，不过它已于 2026 年 4 月 3 日停止向 Meta 追踪器传递相关 URL。所有受测服务都提供分享链接，分享后无需认证即可读取会话，研究发现这些链接会让九家第三方获得查看完整内容的机会。Grok 的分享流程还直接暴露逐字内容：TikTok 收集会话截图，Meta 和 TikTok 均收集最新一条 prompt。这里必须区分用户主动分享与默认公开，后者让用户在没有明确分享动作的情况下承担同类访问风险。

为了检验链接暴露后是否真的有人访问，研究者在对话和文档中嵌入 canary URLs。Grok 出现最明确的后续外部访问证据：提交后数小时至数天内，诱饵链接被触发 70 次，来自 70 个 IP，跨越 48 个 Autonomous Systems、14 个国家和四个大陆；65.7% 的连接来自美国，尽管测试在欧盟进行。这证明嵌入对话的资源随后被分布式基础设施访问，但不能仅凭访问记录确定每个访问者的身份或用途。DeepSeek、Copilot、Mistral 和 Claude 的部分诱饵只在提交时由云基础设施访问一次；Perplexity 的 Perplexity-User crawler 则在用户明确要求不要访问后仍反复请求链接，所用 AWS 基础设施位于美国。

这些行为涉及独立的同意、透明度与处理合法性问题。ePrivacy Directive 第 5(3) 条对广告、分析和画像用途的 cookies 要求事先知情同意，EDPB 的解释还覆盖像素、URL 追踪、持久标识及相关客户端数据传输。GDPR 下，提供商向第三方披露聊天信息，以及第三方随后读取会话，是各自需要法律依据的处理活动。研究者检查的政策虽然使用"用户内容""对话""交互信息"等宽泛类别，却未具体说明测量到的第三方分享方式；他们据此认为，这些披露难以满足按处理活动说明数据类别、目的和法律依据的透明度要求。将聊天标题、URL 和身份标识送入广告技术体系，也难以仅靠"履行合同所必需"来解释；医疗对话还可能涉及特殊类别个人数据。对于擅长整合多源数据的 Meta、Google，哈希化或假名化不足以直接排除重新识别风险。这些是论文提出的法律分析，并非监管机关已经作出的违法认定。

研究的结论有明确边界：它记录的是有限服务、有限会话和特定时间点的可观察行为，没有测量多年对话记忆积累后的画像风险，也未覆盖桌面客户端、语音优先产品或行业专用工具；支付、故障诊断等第三方 SDK 也不能一概视为广告追踪。尽管如此，同类像素、SDK、服务端转发和公开链接机制可以延伸到采用这些基础设施的 LLM 应用与第三方包装产品。Google 和 Meta 同时拥有广告追踪体系与竞争性 AI 产品，使模型回答的暴露还涉及潜在的竞争情报风险。研究团队于 2026 年 4 月通知欧洲及英国数据保护机构和 xAI，5 月公开部分结果；截至 9 月 10 日，Grok 仍使用可公开访问的会话链接，xAI 尚未正式回应披露。

用户拒绝非必要 cookies、关闭可关闭的会话分享、使用追踪拦截和重置广告 ID，能够削减部分暴露，却无法覆盖第一方域名转发、服务端追踪和默认公开链接。提供商可以直接取消会话默认公开，并停止向第三方传递标题、会话链接及关联标识。**对话隐私取决于整条数据链路**：只要高度敏感的内容摘要仍与可关联身份一起进入广告基础设施，界面上的隐私选项和付费身份就不足以建立可靠的保密边界。
