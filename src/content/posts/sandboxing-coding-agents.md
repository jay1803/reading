---
title: "Sandboxing coding agents"
date: 2026-09-04T17:49:13Z
category: reading
description: "如何用独立签名密钥、GitHub fine-grained PAT 和 Docker Sandbox 把 coding agent 的权限限制到单个仓库，同时让 AI 生成的提交在 Git 历史中可审计、可辨识。"
source: "https://micahflee.com/sandboxing-coding-agents/"
author: "Micah Lee"
---

安全使用 coding agents 的核心，是把身份、代码访问权和运行环境拆成彼此独立、权限最小化的边界：agent 只接触单个 GitHub 仓库，以专用身份创建并签署提交，同时运行在与主机凭据隔离的 Docker Sandbox 中。Micah Lee 的方案由三部分组成：仅用于签名的 SSH key、仅授权指定仓库的 GitHub fine-grained PAT，以及每个工作副本独享的 sandbox。这样即使 agent 执行恶意代码、遭遇 prompt injection 或误用凭据，它能够影响的范围也被限制在预先选定的仓库内，而提交历史仍能明确显示哪些代码由 AI 生成。

第一步是为 agents 创建独立的 Ed25519 SSH key，例如保存在 `~/.ssh/agent-signing-key`，并用 passphrase 加密私钥。随后把公钥添加到 GitHub 账户，但必须将其登记为 **signing key**，不能登记为 authentication key；签名权限只让 GitHub 验证提交来源，认证权限则可能让持钥者访问该账户能够访问的全部仓库。Lee 还建议让 agent 使用明确可识别的作者名，例如 "Micah Lee (agent)"，从提交作者字段和 GitHub 的 Verified 标记两个维度公开 AI 的参与，而人的常用 SSH key 继续留在 YubiKey 或正常 SSH agent 中。

Docker Sandboxes 支持把主机的 SSH agent 转发进容器，以便 agent 签署提交，但直接转发日常使用的 SSH agent 会把其中所有已加载密钥一并暴露给 sandbox。Lee 因而编写了 `start-isolated-ssh.sh`：脚本必须通过 source 在当前 shell 中加载，先保存原有的 `SSH_AUTH_SOCK` 和 `SSH_AGENT_PID`，再启动一个新的 `ssh-agent`，其中只加入 `agent-signing-key`。随后脚本重启 `sbx daemon`，让 daemon 继承这个隔离后的 agent socket；配套的 `stop_isolated_ssh` 函数会停止 sandbox daemon、杀掉临时 SSH agent，并恢复原先的环境变量。脚本还会拒绝重复启动、检查 signing key 与 `sbx` 是否存在，并在加载密钥或重启 daemon 失败时自动清理状态。进入 sandbox 后运行 `ssh-add -L`，应当只能看到专用签名公钥；出现其他密钥就说明隔离没有成功。

GitHub 仓库访问则通过 **fine-grained personal access token** 单独控制。Lee 为测试仓库 `micahflee/sandbox-test` 创建短期 PAT，将 Repository access 设为 Only select repositories，只选择该仓库，并授予 Contents、Issues、Pull requests 的读写权限，Actions 和 Commit statuses 的只读权限，以及 GitHub 强制要求的 Metadata 只读权限。如果仓库属于 organization，resource owner 必须选该组织，而且可能需要管理员批准。这个 token 应按 sandbox 注入，例如使用 `sbx secret set github --sandbox sandbox-test-1`，不能设置成全局 `github` secret；全局 secret 会让所有 sandboxes 共用更广泛的 GitHub 身份，破坏每个项目独立授权的边界。

为了并行运行多个 agents，Lee 把同一个 HTTPS 仓库克隆为 `sandbox-test-1` 和 `sandbox-test-2` 两个工作副本，再为每个目录创建同名 Docker Sandbox，并使用 `--no-share-skills` 避免共享宿主机 skills。多个 agents 因此拥有各自的文件系统工作区，不会同时修改同一份 working tree。由于 sandbox 没有认证用 SSH key，仓库必须通过 HTTPS clone，并预先在主机上安装、登录 GitHub CLI，运行 `gh auth setup-git`。首次创建 sandbox 可能需要下载镜像；进入容器后还应更新其中可能过期的 coding-agent 客户端，并用 `gh auth status` 确认 GitHub 身份来自注入的 `GH_TOKEN`，Git 操作协议为 HTTPS。

每个 sandbox 还要单独配置 Git 提交身份：作者名带 "(agent)" 标识，邮箱使用作者自己的地址，`gpg.format` 设为 `ssh`，`user.signingkey` 从隔离环境中 `ssh-add -L` 返回的第一把公钥取得，同时开启 `commit.gpgsign` 和 `tag.gpgSign`。这里写入 Git 配置的是公钥内容，实际签名操作仍由转发进来的隔离 SSH agent 完成，受 passphrase 解锁和临时 agent 生命周期约束。项目需要的 Claude plugins 或其他开发工具也可以在这一阶段安装，但都局限于对应 sandbox。

Lee 用一次完整操作验证了整个权限链：Claude 在约 30 秒内修改 README、建立独立分支、创建签名提交并打开 `micahflee/sandbox-test` 的第一个 PR，全程没有请求额外权限。PR 合并后，GitHub 将提交显示为由专用 agent signing key 验证，`git log` 则显示作者为 "Micah Lee (agent)"，并保留 `Co-Authored-By: Claude Opus 5 (1M context)`。这同时证明 PAT 足以完成 branch、push 和 PR 工作，也证明 sandbox 只需签名公钥对应的临时 SSH agent，无需获得主账户的认证密钥。

实际使用时，每个新项目只需一次性创建受限 PAT、准备一个或多个独立 clone、创建对应 sandboxes、注入项目级 secret，并配置提交身份与签名；每次开工前则 source 隔离脚本、输入 agent signing key 的 passphrase、启动 sandbox，结束后调用清理函数恢复原 SSH agent。Lee 还建议把这套环境放在家用服务器的 tmux 会话中运行，让多个 agents 在笔记本合盖后继续工作；涉及敏感代码时，家用服务器也比云服务器减少了一层第三方基础设施暴露。整套设计的关键在于把 agent 视为需要审计的独立软件主体：它获得完成任务所需的仓库权限和签名能力，却无法借此继承操作者的完整 GitHub 身份。
