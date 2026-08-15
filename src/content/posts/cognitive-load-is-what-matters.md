---
title: "Cognitive load is what matters"
date: 2024-12-27T17:47:30Z
category: reading
description: "Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather a fundamental human constraint...."
source: "https://minds.md/zakirullin/cognitive"
---

Confusion costs time and money. Confusion is caused by high cognitive load. It's not some fancy abstract concept, but rather a fundamental human constraint. It's not imagined, it's there and we can feel it.
### Cognitive load
Cognitive load is how much a developer needs to think in order to complete a task.

When reading code, you put things like values of variables, control flow logic and call sequences into your head. The average person can hold roughly four such chunks in working memory. Once the cognitive load reaches this threshold, it becomes much harder to understand things.
### Types of cognitive load
- Intrinsic - caused by the inherent difficulty of a task. It can't be reduced, it's at the very heart of software development.
- Extraneous - created by the way the information is presented. Caused by factors not directly relevant to the task, such as smart author's quirks. Can be greatly reduced. We will focus on this type of cognitive load.
### Cognitive load in familiar projects
The more mental models there are to learn, the longer it takes for a new developer to deliver value.
### Conclusion
We should reduce any cognitive load above and beyond what is intrinsic to the work we do.
## TL;DR
这篇文章讨论的是Cognitive Load在软件设计中的体现。软件开发中的认知负荷（cognitive load）是开发者理解和完成任务所需的心智努力。过高的认知负荷，特别是外部认知负荷（extraneous cognitive load），会显著增加理解代码的难度、耗费时间和成本。应通过简化代码结构、选择恰当的抽象层次、避免不必要的复杂性和依赖，以及采用清晰直接的沟通方式（如使用自描述字符串而非数字代码）来主动最小化外部认知负荷，从而提升开发效率和代码可维护性。
### 主题
#### 认知负荷是核心问题
认知负荷是指开发者为完成任务需要思考的程度。人类工作记忆有限，大约只能同时处理四个信息块（chunks）。当认知负荷超过这个阈值时，理解代码会变得非常困难。由于阅读和理解代码的时间远超编写代码的时间，因此需要持续关注代码中是否嵌入了过多的认知负荷。
#### 认知负荷的类型
- 内在认知负荷 (Intrinsic cognitive load): 任务本身固有的难度，无法减少，是软件开发的核心部分。
- 外部认知负荷 (Extraneous cognitive load): 由信息呈现方式引起，与任务本身不直接相关，例如代码作者的“聪明”怪癖或不佳的设计选择。这是可以且应该被大幅减少的。本文主要关注减少外部认知负荷。
#### 导致高认知负荷的具体实践及改进建议
##### 复杂的条件语句 (Complex conditionals)
复杂的、多层嵌套的逻辑与 (&&) 和逻辑或 (||) 条件判断会迅速耗尽工作记忆。
- 改进方法: 引入具有描述性名称的中间变量来分解复杂条件，使 `if` 语句本身变得清晰易读。
##### 嵌套的 If 语句 (Nested ifs)
深层嵌套的 `if` 语句会增加理解代码路径所需的心智负担，需要记住每一层的条件。
- 改进方法: 使用“提前返回”(early returns) 的方式处理无效或不满足条件的情况，使主逻辑路径（happy path）保持线性，减少需要记忆的前提条件。
##### 继承带来的噩梦 (Inheritance nightmare)
深层或复杂的继承链条（如 `AdminController extends UserController extends GuestController extends BaseController`）迫使开发者需要追溯多个父类的实现细节，并且修改时还需考虑对子类的潜在影响，导致认知负荷急剧增加。
- 改进方法: 优先使用组合 (composition) 而非继承 (inheritance)。
##### 过多的小型模块、类或方法 (Too many small methods, classes or modules)
遵循诸如“方法不超过15行”或“类要小”的教条可能导致产生大量“浅模块”（shallow modules），即接口复杂度相对于其提供的功能来说过高。理解这些模块不仅需要了解每个模块的职责，还需要理解它们之间复杂的交互关系，隐藏的信息量少，增加了整体认知负荷。
- 对比: “深模块”（deep module）提供强大的功能，但接口简单。例如 UNIX I/O 接口只有五个基本调用 (`open`, `read`, `write`, `lseek`, `close`)，但其实现包含数十万行代码，隐藏了大量复杂性。
- 案例: 作者对比了两个约5000行代码的个人项目，一个有80个浅类，另一个只有7个深类。一年半后，前者难以理解，后者则容易上手。
- 观点: 最好的组件是功能强大但接口简单的。信息隐藏至关重要，浅模块隐藏的复杂性不足。
##### 对单一职责原则 (SRP) 的误解导致浅模块
将 SRP 误解为“一个模块只做一件事”（模糊的“一件事”），可能导致创建大量极其细碎的浅模块（如 `MetricsProviderFactoryFactory`）。这类模块的名称和接口可能比其实现更耗费心智。
- 正确理解 SRP: 一个模块应该只对一个用户或利益相关者负责。即，如果一个模块的修改会导致两个不同的业务方抱怨，那么 SRP 可能被违反了。关注点应是变更的原因和影响范围，而非模块执行的操作数量。
- 核心: 跳跃于大量浅模块之间会增加认知负荷，线性思维更自然。
##### 过多浅显的微服务 (Too many shallow microservices)
模块的深浅原则同样适用于微服务架构。过多的浅微服务（功能少、接口相对复杂）会导致所谓的“分布式单体”（distributed monolith），增加集成难度、诊断困难和整体认知负荷。
- 案例: 一个5人开发团队创建了17个微服务，导致进度严重落后，任何需求变更都涉及多个服务。
- 对比: Tanenbaum-Torvalds 关于 Linux (monolithic) 与微内核 (microkernel) 的争论，实践证明设计上看似更优的微内核并未普及，而单体内核 Linux 无处不在。
- 观点: 精心设计的、模块间真正隔离的单体通常比微服务更灵活，认知负荷更低。只有当独立部署需求（如扩展开发团队）变得至关重要时，才应考虑引入网络层（即微服务化）。应尽可能推迟做此类决策。

##### 功能过多的语言特性 (Feature-rich languages)
语言特性过多，开发者可能花费时间选择使用哪个特性，并且后续维护者需要重现这个思考过程，理解为何选择特定特性而非其他。这增加了额外的认知负荷。
- 观点 (引用 Rob Pike): 通过限制选择来减少认知负荷。语言特性只要彼此正交（orthogonal）即可。
- 案例 (来自 C++ 开发者): C++ 语言历史悠久，特性不断增加（如 `||` 在不同上下文有不同含义，对象生命周期规则变化，初始化方式增多），导致即使修复了旧问题，整体认知负荷仍在增长。开发者需要了解特性的历史、修复时间和旧行为。这种认知负荷并非来自业务本身，而是语言带来的外部认知负荷。开发者不得不制定规则避免使用过于晦涩的特性。

##### 业务逻辑与数字状态码 (Business logic and HTTP status codes)
使用数字状态码（如 HTTP 401, 403, 418）来传递具体的业务错误信息（如 token 过期、权限不足、用户被封禁）会给客户端（前端、QA）带来认知负荷，他们需要记住或查找这些数字与具体含义的映射关系。
- 改进方法: 在响应体中直接返回自描述的字符串错误码（如 `{"code": "jwt_has_expired"}`），消除记忆映射的需要。此原则适用于所有使用数字状态码表示业务含义的场景。
- 附加建议: 使用更简单的术语，如用 "login" 和 "permissions" 替代易混淆的 "authentication" 和 "authorization"。

##### 滥用 DRY 原则 (Abusing DRY principle)
过度追求“不要重复自己”（Don't Repeat Yourself）可能导致在不相关的组件间创建紧密耦合（tight coupling），使得修改一个部分可能意外影响其他部分。过早地基于表面相似性提取公共功能可能产生难以修改或扩展的不必要抽象。
- 观点 (引用 Rob Pike): “一点点复制代码胜过一点点依赖”（A little copying is better than a little dependency）。
- 警惕: 为了避免“重复造轮子”而引入大型、重型库来使用其中一小部分功能，可能得不偿失。所有依赖项都成为代码的一部分，调试深入到库的堆栈中会非常痛苦。

##### 与框架的紧密耦合 (Tight coupling with a framework)
框架通常包含“魔法”（magic），过度依赖框架会迫使所有开发者首先学习这些魔法，耗时可能数月。虽然框架能快速启动 MVP，但长期看可能增加不必要的复杂性和认知负荷。当需求与框架设计冲突时，可能导致需要 fork 并维护自定义版本的框架，进一步加剧认知负荷。
- 改进方法: 编写框架无关（framework-agnostic）的代码。业务逻辑不应驻留在框架内，而应使用框架作为库。将框架置于核心逻辑之外，允许新成员在不深入了解框架复杂性的情况下贡献价值。

##### 分层架构的代价 (Layered architecture)
诸如六边形架构（Hexagonal Architecture）或洋葱架构（Onion Architecture）等分层架构虽然在理论上看似清晰，但在实践中可能导致文件数量翻倍、大量胶水代码、跨多层修改的繁琐，以及调试时需要在多个抽象层之间跳转，显著增加认知负荷。抽象本应隐藏复杂性，此处却增加了间接性（indirection）。
- 观点: 这些架构并非基础原则，而是对更基本原则（如依赖倒置 DIP、单一事实来源 SoT、认知负荷、信息隐藏）的主观解释。应遵循基本原则，而非强制套用特定架构模式。
- 误区: 认为分层能轻易替换数据库等依赖。实际替换存储的困难主要在于数据模型不兼容、通信协议、分布式挑战和隐式接口（Hyrum's Law），而非数据访问层的抽象本身。抽象层节省的时间可能微乎其微（如案例中存储迁移耗时10个月，适配器编码仅几小时）。
- 建议: 不要为了架构而添加抽象层，仅在有实际扩展需求时添加。抽象层是有成本的，它们占据有限的工作记忆。

##### 对领域驱动设计 (DDD) 的误解
DDD 的核心价值在于问题空间（problem space），如通用语言（Ubiquitous Language）、领域（domain）、限界上下文（Bounded Context）、事件风暴（Event Storming），旨在促进开发者、领域专家和业务人员之间的有效沟通和理解。然而，人们常将其误解为特定的解决方案空间（solution space）技术，如特定的文件夹结构、服务、仓库模式等。这种主观解释可能导致独特的、难以理解的代码实现，增加外部认知负荷。
- 对比: Team Topologies 提供了一个更易理解的框架来划分团队认知负荷。DDD 的解释可能因人而异，导致争论而非共识。

##### 简单架构的价值
成功的系统往往采用简单、易于理解的架构。
- 案例: 标准 CRUD 应用架构（如 Python monolith + Postgres）、Instagram 早期仅用3名工程师扩展到1400万用户、许多看似“聪明绝顶”的初创公司反而失败了、用一个函数连接整个系统的简单设计。
- 建议: 让初级开发者参与架构评审，他们能帮助识别认知负荷高的区域。

##### 熟悉项目中的认知负荷 (Cognitive load in familiar projects)
熟悉度不等于简单性。对于长期参与项目的开发者来说，代码可能感觉简单，因为他们已经内化了其复杂性（形成了长期记忆）。但对于新人来说，这些“聪明”的、非惯用的技巧会带来学习成本。代码库的复杂性是逐渐累积的，需要有意识地进行简化。
- 识别方法: 观察新成员的困惑程度（如结对编程）。如果他们连续困惑超过约40分钟，说明代码有改进空间。
- 目标: 保持低认知负荷，使新成员能在加入几小时内开始贡献。

### 总结
软件开发的核心挑战之一是管理认知负荷，应优先减少由代码结构、抽象选择和呈现方式引入的外部认知负荷，以构建更易于理解、维护和协作的系统。
