---
title: "SwiftUI Scroll Performance: The 120FPS Challenge"
date: 2025-05-12T13:38:46Z
category: reading
author: "Jacob Bartlett"
description: "SwiftUI 在处理无限滚动列表时可能遇到性能瓶颈。文章通过对比 VStack、LazyVStack 和 List 在 iOS 18 上的表现，发现 List（基于 UICollectionView）在处理包含动态尺寸内容的无限滚动列表时，性能和稳定性均优于 LazyVStack。此外，文章还探讨了多种进一步优..."
source: "https://blog.jacobstechtavern.com/p/swiftui-scroll-performance-the-120fps"
---

## TL;DR
SwiftUI 在处理无限滚动列表时可能遇到性能瓶颈。文章通过对比 `VStack`、`LazyVStack` 和 `List` 在 iOS 18 上的表现，发现 `List`（基于 `UICollectionView`）在处理包含动态尺寸内容的无限滚动列表时，性能和稳定性均优于 `LazyVStack`。此外，文章还探讨了多种进一步优化滚动性能的技术，如图像缓存、分页加载、最小化重绘、后台处理和利用 Metal。
### 主题
#### 滚动架构对比
为了实现流畅的无限滚动视图（目标60fps，在低功耗模式下测试），文章对比了三种 SwiftUI 布局容器。
##### `VStack` 的性能问题
`VStack` 会一次性加载和渲染其包含的所有子视图。
- 在测试中，当 `VStack` 包含1000个单元格时，应用在加载时立即冻结，无法交互。
- 动画卡顿工具 (Animation Hitches instrument) 显示大量帧丢失，VSync 远超16.67ms。
- 内存使用出现巨大峰值且不会下降，因为所有视图都保留在内存中。
结论：`VStack` 不适用于包含大量项目的滚动列表。
##### `LazyVStack` 的按需加载与权衡
`LazyVStack` 会按需加载和渲染即将进入视口 (viewport) 的子视图，从而提升性能。它通过动态估算几何尺寸来实现，这可能牺牲一定的准确性。
- 初始加载和滚动性能远好于 `VStack`，VSync 显示帧率稳定在60fps（16.67ms每帧）。
- 滚动数百个项目时，仅出现少量轻微掉帧，无卡顿。
- 对于动态尺寸的单元格：性能出现可见下降，有数个掉帧和微小卡顿。在随机单元格高度的极端测试下，总体表现尚可。
- 内存使用：相对稳定，快速滚动时略有上升，视图离开视口后其数据会被逐出内存。
- 潜在问题：当使用动态尺寸单元格并快速拖动滚动指示器时，`LazyVStack` 的动态高度估算机制可能失效，导致滚动跳动和内存使用激增。
- 历史改进：与 iOS 16 相比，iOS 18 中的 `LazyVStack` 实现了双向懒加载（即视图离开视口上方或下方都会被卸载），而 iOS 16 中仅为单向懒加载（向上滚动时内存持续增长）。
##### `List` 的卓越性能与稳定性
`List` 底层使用 `UICollectionView`，包含了单元格复用 (cell recycling) 等优化机制。
- 格式化 `List` 可能比纯 SwiftUI 视图稍显繁琐，因其基于 UIKit 的默认设置。
- 性能表现：滚动体验非常流畅。Instruments 分析显示，在低功耗模式下也能轻松达到60fps，无卡顿或掉帧。
- 对于动态尺寸的单元格：快速滚动时出现极少量（一两帧）的卡顿，但少于 `LazyVStack`。
- 内存使用：初始加载时略有峰值，之后在滚动1000个项目的过程中保持非常稳定和平滑。
- 稳定性：在测试中未能使其出现故障。
结论：`List` 是渲染无限滚动列表的最高效方式，尤其在处理动态尺寸内容时表现更稳定。
#### 进一步优化滚动性能
即使选择了 `List`，仍有方法可以进一步提升滚动体验。
##### 图像缓存 (Image Caching)
SwiftUI 的 `AsyncImage` 组件在单元格每次出现时都会重新加载图像，即使图像之前已加载过，这会浪费网络 I/O。
- 解决方案：使用图像缓存库，如 Nuke、Kingfisher 或 CachedAsyncImage。
- 效果：图像（至少在第二次渲染时）能即时加载，使应用感觉更灵敏。
##### 分页加载 (Pagination)
一次性加载所有数据（即使是“无限”列表）是不现实且昂贵的。分页加载是指初始只加载一部分数据（如20、50或100项），当用户滚动到列表末尾附近时再加载更多数据。
- 效果：对于 `LazyVStack` 和 `List`，这能使初始内存分配和网络 I/O 更高效。较小的数据源也可能加快数据变化时的差异比较 (diffing) 速度。
##### 最小化重绘 (Minimise Redraws)
SwiftUI 在视图的依赖项（如 `@State` 属性或 `@Observable` ViewModel 的属性）发生变化时，会重新计算视图。它通过差异比较算法对比新旧视图结构和标识，若检测到差异则可能重新布局和绘制视图。
- 优化策略：
  1. 最小化视图依赖：视图应包含尽可能少的状态，以减少重计算和重绘的频率。
  2. 加快差异计算：使视图遵循 `Equatable` 协议，并应用 `equatable()` 修改器。如果视图的依赖项仅为原始类型 (primitive types)，SwiftUI 可能会执行（未公开文档的）类似 `memcmp` 的字节级比较，从而提高效率。
- 调试工具：可使用 `Self._printChanges` 来帮助调试视图的重计算。
##### 后台处理 (Background Processing)
为了保持主线程的流畅以响应用户交互，应将耗时操作（如长时间运行的处理、图像转换、数据解析）转移到后台线程。
- 注意：SwiftUI 视图的 `body` 默认在 `@MainActor` 上执行，这意味着视图计算（如字符串插值、数据过滤）发生在主线程，每次视图计算都会累积开销，影响应用响应性。
- 检查：调用 ViewModel 中的函数时，需确保异步工作不会意外地在主线程上执行。
##### 利用 Metal (Utilising Metal)
SwiftUI 提供了 `drawingGroup()` 修改器，它使用 Metal 将视图渲染为单个预渲染的纹理，然后再绘制到屏幕上。这利用 GPU 将复杂的视图层级扁平化为简单的图像。
- 适用场景：复杂的动画集合、深层嵌套的视图层级，或大量使用 CoreImage 混合模式 (blend modes) 的情况。
- 注意：将视图上传到 GPU 会产生开销。虽然此修改器有时能神奇地解决性能问题，但在某些情况下反而可能降低视图性能。应在响应性能问题时考虑使用，而非预先应用于所有视图。
##### 更详细的性能分析 (More Detailed Profiling)
建议使用 Instruments 中的多种工具（如 View Body, View Properties, Core Animation Commits, Hangs, 以及 Time Profiler）来分析应用，找出可能影响性能的计算瓶颈。
### 总结
截至 iOS 18，`List` 和 `LazyVStack` 在性能、内存使用和单元格回收方面均表现良好，但基于 `UICollectionView` 的 `List` 在处理动态尺寸内容时具有更佳的稳定性，是实现高性能无限滚动列表的首选，并可通过图像缓存、分页加载、最小化重绘、后台处理及审慎使用 Metal 等多种技术进一步优化。
