---
title: "Static, Dynamic, Mergeable, oh, my!"
date: 2026-03-15T08:15:10Z
category: reading
description: "iOS 工程师大多知道\"用 static 还是 dynamic\"这个问题，但几乎没人能说清背后的机制。这篇文章的真正主张是：静态链接在编译期把所有目标文件物理拷贝进主 binary，动态链接只记一个路径，等启动时 dyld 才映射进来——这个\"拷贝 vs. 引用\"的区别，是所有 build time、launch..."
source: "https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my"
---

## TL;DR
iOS 工程师大多知道"用 static 还是 dynamic"这个问题，但几乎没人能说清背后的机制。这篇文章的真正主张是：**静态链接在编译期把所有目标文件物理拷贝进主 binary，动态链接只记一个路径，等启动时 dyld 才映射进来——这个"拷贝 vs. 引用"的区别，是所有 build time、launch time、bundle bloat 差异的根源，而不是什么平台魔法。**

## 核心机制拆解
链接本质上是把编译出的 `.o` 文件合并进可执行文件。静态链接在这步直接 copy 全部 object file 进主 binary——于是 build 慢（每次增量编译都要重走一遍拷贝），但 launch 快（OS 只需加载一个 Mach-O 文件）。

动态链接只把 `.dylib` 的文件夹路径写进 binary，真正的符号解析推迟到 app 启动前的 pre-main 阶段由 dyld 完成——于是增量 build 几乎是瞬时的，但 launch 慢，因为每个 dynamic framework 都要被 dyld 映射进进程内存地址空间。**关键纠正：dynamic library 不是按需 lazy 加载的，它们全部在 pre-main 启动，用太多就会拖慢冷启。**

**值得质疑的默认认知**：很多人以为"dynamic = 更小的包体积"，但这是错的。动态链接模块因为编译时无法做跨模块 dead-code stripping，反而可能更臃肿。文章举了 Factory 这个轻量依赖的反例：dynamic framework 200KB，换成 static library 只有 15KB。

系统 framework（Foundation、SwiftUI）也是 dynamic 的，但通过 dyld shared library cache 预链接，几乎零启动开销——这是第三方库没有的特权。

Mergeable Libraries（Xcode 15）本质是让 dynamic framework 在 debug build 保持动态（fast incremental build），在 release build 自动合并成静态（fast launch）。代价是 metadata 让库体积翻倍，且完全不解决多 target 间的资源复制问题——这是真正让包体积膨胀的主要原因，文章自己也坦率地指出这个盲区。

## 边缘判断
这篇文章最有价值的地方，不是给你一个"应该用 static 还是 dynamic"的答案，而是给了一个**从机制倒推性能特征**的思维方式：不要记结论，要理解那个"编译期拷贝 vs. 运行时映射"的分叉点，所有性能取舍都从那里展开。Mergeable Libraries 是个合理的工程妥协，但不是思考的终点——知道它帮你做了什么、没帮你做什么，才能在自己项目里做对选择。
