---
title: "The Next Scaling Problem — Tetral"
date: 2026-10-03T03:13:50Z
category: reading
description: "云端 agent 的下一轮扩展瓶颈是围绕智能运行的整套系统：身份、权限、状态恢复、执行环境、存储与验证都需要独立扩展。Tetral 把 agent 做成可替换 runtime，历史与身份留在持久化系统中，电脑降为按需调用的执行资源。"
source: "https://tetral.ai/blog/the-next-scaling-problem/"
author: "Yang Li — building Tetral"
---

云端 agent 的下一轮扩展瓶颈，是围绕智能运行的整套系统：模型能力越强、任务越长、并行路径越多，身份、权限、状态恢复、执行环境、存储与验证就越需要独立扩展。Tetral 的核心设计是把 agent 做成可替换的计算 runtime，让历史与身份留在持久化系统中，把电脑降为按需调用的执行资源，同时在外部动作发生前建立可审计的授权边界。

Yang Li 最初开发 Anoma 时，把 Claude Code、Codex CLI 式的本地 agent 循环搬进 E2B，沿用了 Manus 以虚拟机文件系统保存可恢复上下文的思路。这使 sandbox 成为 agent 容量的单位：用户增加，就要创建、复用和回收更多 sandbox；历史与 traces 留在环境内部，调试需要接触包含用户私有数据的机器；要把 API key 隔离出去，又得另建代理模型请求的 Gateway。最终架构叠成 sandbox 内的完整 agent、管理容量和模型流量的 control plane、产品界面三层，外围职责不断增加，每个 sandbox 仍背着整个 agent。

开发第二个产品 Tetral 时，他希望提供开发者可以嵌入自有产品的通用 SDK，因此必须重新划分托管边界。Kubernetes 可以承载稳定服务，但高频创建与销毁 sandbox 会撞上串行调度和 pod 生命周期协调的瓶颈；EC2、Firecracker 加 microVM control plane 则会把团队带向 sandbox provider 的建设。两条路线都没有改变 agent 容量受电脑供应量约束的问题。关键拆分依据是两者的扩展曲线：agent runtime 是可跨任务复用的稳定服务，sandbox 是隔离、突发、可丢弃的资源。拆开后，Kubernetes 负责 runtime 副本与并发 session，独立服务负责电脑的生命周期，Linux、Windows、macOS 都成为 agent 可以调用的执行资源。

**Runtime 的边界由所有权、生命周期和扩展方式决定**。Gateway 接管 provider 格式、凭据、连接与流式协议，为 runtime 提供统一请求契约；PostgreSQL 保存已接受输入、执行进度和结果；Bridge 检查所有权与顺序，提交状态转换，使 runtime 无须直接绑定数据库 schema、事务和重试协议；Queue 管理顺序、租约、重试、取消与 dead-lettering；Sandbox Service 管理电脑并执行命令。Public API 接收 SDK 请求，Event Stream 暴露数据库中的有序记录，这两个服务都不执行 agent。runtime 剩下的职责，是读取 session 和 thread 的已提交状态，计算下一步。

Session 是绑定 agent version 与选定资源的一项持续任务，thread 是其中独立排序的执行路径，主 agent 从 root thread 开始，subagent 使用 child thread。每个 thread 的 pure reducer 根据已提交输入与结果，决定调用模型、路由工具、等待或结束，自身不做数据库或网络 I/O。runtime pod 可以同时保温多个 session 与 thread，但不拥有它们，任何外部操作都必须先获得提交确认。Cursor 使用 Temporal 重放 workflow Event History 恢复控制流，并另存 conversation；Tetral 则把转换、conversation 和 projections 放在 PostgreSQL，由替代 runtime 重建 checkpoint，再交给 reducer 决定当前状态与下一步，让 alpha 的持久化控制状态服从同一个事务数据库。

可替换 runtime 最困难的地方，是进程消失后如何分清操作尚未开始、仍在执行或已经完成。Tetral 借用 WAL 的先记录后执行规则：runtime 先向 Bridge 提交带稳定身份的不可变 declaration，Bridge 验证所有权和顺序，在一个事务中写入转换与 receipt，确认后才能 dispatch。稳定身份充当 idempotency key，重试返回原 receipt，同一身份配上不同内容会被拒绝。这个协议无法让任意外部系统获得事务性，但能为每项 effect 建立已提交身份和责任归属，避免用猜测推进 thread。

一次模型生成 Bash 调用的过程展示了这条规则如何贯穿执行。用户输入先进入持久化记录，span.model_request_start 固定模型实际读取的上下文边界；模型返回工具调用后，agent.tool_use 必须先提交。Bridge 随后把 sandbox execution 与 Queue job 一起登记，worker 执行命令，保存“完成但未消费”的原始结果。runtime 再声明 agent.tool_result，Bridge 在同一事务中追加结果事件、更新 session_messages、标记结果已消费并保存 receipt，确认后 reducer 才能依赖结果继续。下一次模型请求还必须等待 span.model_request_end 和所需工具结果全部提交。

这套 session log 包含不同用途的记录：session_events 保存输入、请求边界、工具调用、结果、中断与结束等执行历史；session_messages 是模型上下文 projection；session_bridge_operations 保存幂等 receipt。Compaction 改变后续模型从哪个摘要 checkpoint 开始加载，早期事件仍然保留，未来可成为可搜索的上下文。系统不保存可变的 state machine snapshot，冷启动时从已提交消息、请求和工具边界、未解决工作重建状态。丢失 commit acknowledgement 可以用原身份重试；丢失 runtime pod 则不能恢复原 provider stream，Bridge 将开放请求关闭为 runtime_pod_lost，已提交工作继续归相应服务负责，未知的部分响应不会被当成完整结果。

持久化状态还需要持久化投递。用户消息到达时，即使没有可用 runtime，Public API 也能在一个 PostgreSQL 事务中写入输入事件、目标 thread 的 Inbox entry 与 Queue job，提交后返回 200。pg_notify 只负责唤醒 Job Runner，不携带消息、不承担投递状态，通知丢失后仍可由 polling 找回 job。同一 thread 的普通输入保持顺序，其他 thread 可以并行；session 级修改形成跨路径 barrier，interrupt 使用独立路径避免被普通输入堵住。Inbox 的 accepted 表示 runtime 已接收，processed_at 要等输入真正提交进 thread 才设置，因此投递完成与 agent 开始处理有明确区分。

Inbox 同时封住重复投递和旧进程继续运行的故障窗口。RPC 响应丢失时，runner 使用同一 input identity 重试；Queue acknowledgement 丢失时，下一位 runner 可以看到既有 acceptance，直接关闭 job。超时本身不足以证明旧 runtime 已停止，binding generation 与 pod UID 构成 fencing token，只有 Kubernetes 确认原 pod 身份消失后，Bridge 才把已接受投递交回 Queue，允许替代 runtime 接续同一个持久化义务。

凭据与连接也沿独立边界管理。模型请求不带 API key 或 OAuth token，Gateway 验证 Kubernetes workload identity，以及证明 runtime 仍拥有该 session、thread 的短期 Bridge token；被替换 pod 无法续签并继续调用。Gateway 读取 session 指定凭据，遇到缺失、撤销、归档或无法解密时直接拒绝，只有没有指定凭据的 session 才能使用平台 key pool。OAuth refresh 通过锁定凭据行、保存替换 token 后注入 outbound request 完成，明文不会进入 runtime、Bridge、session log 或 sandbox。Gateway 使用 Vercel AI SDK 转换请求，通过 gRPC 返回统一 ProviderStreamEvent，自身不选择模型，也不保留 session 状态。MCP connector 使用相同原则：工具目录先版本化保存，runtime 只获得名称、描述和 schema，调用声明先提交，connector 再验证权限、注入凭据并处理连接，结果经 Bridge 后进入上下文。

电脑只在 shell 或 filesystem 工具确实需要时分配。Bash declaration 与 Queue job 可以先存在，Sandbox Service worker 再检查当前电脑是否兼容、资源是否准备就绪；不满足条件时启动 activation，按状态复用、启动、创建或替换电脑，再通过 materialization 准备文件、helper state 和 session access。多个调用可以共享一次 activation，逻辑执行暂存为 waiting_activation，准备完成后以新一代 job 回到 Queue。提交命令前还要绑定确切电脑，防止旧 worker 在电脑被释放或替换后误把命令送进新环境；runtime 故障不会取消已登记电脑操作，也不要求 Bash 重跑。目前实现为每个 session 懒分配一台 Daytona-backed computer，但文件访问未来可以走 virtual filesystem，轻任务可以使用 container，平台专属工作再选择相应机器。

并行扩展需要两种不同边界：thread 在同一任务内创建独立执行路径，session 在同一 workspace 的选定资源上创建独立任务。多个模型请求不能同时推进同一个有序上下文，否则会从同一边界生成竞争状态。Tetral 借鉴 Codex 的 subagent 控制方式，让 parent 创建、发送消息、等待或中断 child；fork_turns 明确选择不继承历史、继承全部保留上下文或最近若干轮，并固定为不可变初始 context。Bridge 在一个事务中建立 parent-child 关系、保存上下文与指令、创建 Inbox 和 delivery job，重试返回同一 child ID。后续 parent 消息不会自动进入 child，通信与完成结果都通过有序输入返回。实现、文档、审计和知识维护若需要各自的 agent version、凭据和生命周期，则应使用独立 session，共享 workspace 资源而保持执行历史隔离。

**凭据隔离限制能力的持有，授权决定具体动作能否使用能力**。Tetral 的 approve_for_me 在执行前先运行 deterministic Tool Gate，结合 session approval mode、tool catalog 和工具 policy 决定是否需要独立审查。always_ask 的 Bash 此时仍是 proposal，没有公开 agent.tool_use、sandbox job 或外部 effect。Review identity 绑定 workspace、session、thread、model request、tool call、tool name、canonical action 与 policy，修改命令或 policy 就产生新 identity。Reviewer 使用内部 thread，读取 proposal、相关上下文、当前输出和同轮其他调用，但这些材料只作为证据，平台 policy 与可能含 prompt injection 的内容分开；输出必须包含风险、上下文中可见的用户授权、allow 或 deny 和理由，格式错误视为失败。

审查意见提交 PostgreSQL 后，Tool Gate 才进行第二次判断：允许才形成可执行 tool use，拒绝则记录 rejected result，审查失败必须先记录失败才能转交用户审批；提交失败或 runtime 失去权限，调用不能推进。并行 review 使用从持久 reviewer 最新已提交状态复制的临时 thread，避免上下文交错。Parent 取消后，迟到 decision 只能留作审计；runtime 若在 proposal 产生后、授权完成前消失，alpha 关闭请求且不重建 proposal，主动放弃这段恢复能力，防止孤立 decision 变成执行许可。这条边界保障的是决定必须被记录、绑定确切提议、先于调度发生，无法保证 reviewer 的判断永远正确。

这些基础设施让 agent 成为跨 terminal、browser、phone、GitHub 和团队产品持续存在的可寻址参与者。Tetral fork 了 Managed Agents SDK，采用 versioned agents、固定版本的 session、per-session overrides，以及 files、memory stores、vaults、skills、environments 等独立资源，兼容已经实现的接口并登记差异。关闭客户端不会结束 session，外部动作可以追溯到 agent version、session、thread、policy 与 review，部署者继续承担责任。RoboBun 的公开 GitHub 身份、Raft 的命名 stateful agents、Claude Tag 的异步 Slack 参与者体现了这一方向；支付等能力则可通过 merchant-、amount-bound credential 授予有限权限。CLI 继续服务操作系统、仓库、编译器和 debugger 工作，云端原生能力优先走 MCP；计划中的 Code Mode 将允许受限 JavaScript 发现、组合获准工具并并行调用，目前仍属规划。

多 agent 的长期价值取决于怎样接受成果。共享聊天和增加参与者不会自动提高效率，协调 swarm 与独立并行 agent 可能消耗相近 tokens，大型 coding swarm 的成果合并比例还可能更低。Tetral 押注先进行 adversarial review：其他 agent 主动挑战结论与证据，再由人决定哪些成果进入共享 workspace，防止未经检查的错误成为后续工作的前提。Workspace 保存被接受的成果及其推理、证据，session log 保存候选成果的生产过程；不同 agent version 运行同一任务后，其轨迹可以比较，被拒工具调用、推翻的 review、验证失败与人工纠正可以转成 evaluation 和 alignment data。用于未来评测和训练的前提是保留 provenance、移除私有数据、让人判断成败，训练改进也不能撤掉外部执行的 policy、验证、审查与升级机制。

模型进步会把压力传导到每个外围容量。Tetral 在开发服务器上的一条 integration path 需要七到八分钟，完整 validation 约半小时，编译和测试已经可能先于 inference 成为瓶颈；TypeScript 的 native Go port 早期构建约快十倍，Bun 转向 Rust 则改善内存、吞吐、稳定性与内存安全。执行环境还要承受突发创建、挂载、暂停、恢复、释放和回收，短启动时间无法单独解决高 churn 的 control-plane 协调问题。轻量、可休眠唤醒的 actor compute 提供另一种选择，如何映射到 Tetral 的 session、thread 或 worker 尚未确定。可丢弃环境的产物必须回到 repository、object store 或 workspace files；更多 agent 还会放大事件写入、Git 操作、PR 和 test run 的压力，推动 PostgreSQL 采用 replicas、pooling、caching、workload isolation，甚至推动 Git-compatible host 改用 object-storage WAL 与可替换本地仓库。产品配置也开始围绕 effort、tools、skills、context、policy 与 orchestration 展开，交付单位逐渐扩大到包含模型的 agent system。

Tetral 目前是运行在个人 k3s cluster 上、采用 MIT license 开源的 alpha，尚未获得生产规模证明。Runtime placement 不感知容量，admission、Queue pressure 与 scaling 尚未连成 backpressure，持续多节点恢复未经验证，rollout 也会因缺少 graceful draining 而打断运行中的 turn。接下来需要容量感知 placement、跨节点恢复、由队列压力控制接入与 worker 供给、更快的电脑 activation 和资源准备、更轻的文件访问、自托管 provider，以及一个 agent 协调多台电脑的能力；小部署还应允许合并逻辑服务，生产部署再独立扩展。Bridge、Queue、数据库拆分、Bun runtime 和 Kubernetes topology 都可以随真实负载变化，稳定的设计原则是让 agent 保持计算中心，让外围系统承载连续性与控制：智能能够扩展到多远，最终取决于整条执行链中最先耗尽的容量，以及权限与历史能否在故障和并行中继续成立。
