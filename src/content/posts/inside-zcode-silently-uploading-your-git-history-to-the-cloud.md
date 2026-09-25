---
title: "Inside ZCode: Silently uploading your Git history to the cloud"
date: 2026-09-25T08:42:39Z
category: reading
description: "ZCode 在用户登录后会后台打包工作区并尝试上传，范围包括完整的 Git 历史；作者发现的一个商业项目快照达 313 MB，且界面上的两个相关开关都不能阻止这一流程。作者清理磁盘时发现 ~/.zcode 占用超过 700 MB，其中 v2/checkpoints/ 约占 303 MB。元数据表明，"
source: "https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/"
author: "csmantle"
---

ZCode 在用户登录后会后台打包工作区并尝试上传，范围包括完整的 Git 历史；作者发现的一个商业项目快照达 313 MB，且界面上的两个相关开关都不能阻止这一流程。作者清理磁盘时发现 ~/.zcode 占用超过 700 MB，其中 v2/checkpoints/ 约占 303 MB。元数据表明，客户端从该项目收集了约 345 MB 内容，生成 313 MB 的加密 **baseline** 快照；上传已失败 564 次，文件仍留在 pending 目录等待重试。这个仓库总计约 10 GB，排除依赖后的快照主要涉及项目自身内容。失败记录也意味着，这个本地样本不能单独证明上传已经成功。

日志没有直接给出上传地址，作者于是拆解 ZCode 的 app.asar，还原出流程：客户端先向 zcode.z.ai 请求 snapshot_id、大小限制、RSA 公钥和 Aliyun OSS 表单凭证，再把工作区压成 tar.gz，用 AES-256-CTR 加密内容，并以服务器下发的 RSA 公钥封装对称密钥，最后将 tar.gz.enc 直接 POST 至 OSS，由 OSS 回调 Zhipu 后端登记快照。运行中的网络连接也指向 zcode.z.ai 和两个 Aliyun OSS 节点。作者尝试用本机私钥解开存于磁盘的密文，均告失败；结合密钥分发方式，他判断相应私钥由服务端持有，本地客户端无法自行解密这份快照。

加密文件旁的明文 manifest 揭示了收集范围。在一份包含 42,411 个文件的快照中，.git/lfs/ 占 196.1 MB、.git/objects/ 占 102.2 MB、.git/logs/ 占 0.6 MB，三者合计占载荷的 86.6%；源码和文档约 46.2 MB，仅占 13.4%。因此快照带走的不止当前工作树，还可能包含旧提交中后来删除的密钥、未推送分支的操作痕迹，以及 .git/config 中的内部仓库地址。另一个 repo_snapshot_extra_manifest 还会记录全局 ZCode 配置文件的哈希，并随各工作区快照一起打包。

作者对照界面选项与代码发现，“Optimize Experience”控制的是数据能否用于模型训练，“Repo Snapshot Indexing”控制的是服务端是否为已上传快照建立索引；两者都不阻止本地打包和上传。快照组件在启动时无条件实例化，只要 tokenProvider 能提供有效 JWT，流程便可运行；触发点包括每次提问前的 captureBeforePrompt，以及标记为 repo-wiki-update 的任务完成时，单次活跃会话的日志最多记录了 62 次捕获。作者查阅的隐私政策提到收集对话中提交的文本、文件和代码，却未明确说明会在后台上传整个工作区及 Git 历史。

删除 pending 文件也不能持久阻止捕获：作者半小时内又看到新生成的 313 MB 归档，重试计数从 564 增至 565。他提出清空并锁定 ~/.zcode/v2/checkpoints/，在 macOS 用 chflags uchg、在 Linux 用 chattr +i，使客户端无法写入待上传快照；代价是 checkpoint rollback／timeline 功能失效，而他观察到普通聊天、补全和工具执行仍可使用。整条证据链指向一个关键边界：完成当前任务所需的代码上下文，与持续收集完整仓库历史并交由服务端掌握解密能力，是范围明显不同的数据处理。
