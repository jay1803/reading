---
title: "Key, in sight"
date: 2026-06-17T08:03:59Z
category: reading
description: "键盘定制失败的根因是从现有快捷键里抢地盘。作者的策略是先划出一块无冲突的空地：买一块 macropad 全部映射到 F1–F20，或用 Caps Lock 变 Hyper 键。从空地出发，不用和 macOS 与各应用的现有约定缠斗，电机记忆才能生长。"
source: "https://aresluna.org/key-in-sight"
---

## 先占地，再填功能

键盘定制失败的根因是从现有快捷键里抢地盘。作者的策略是先划出一块无冲突的空地：买一块 macropad 全部映射到 F1–F20，或用 Caps Lock 变 Hyper 键。从空地出发，不用和 macOS 与各应用的现有约定缠斗，电机记忆才能生长。

## 一次击键经过的七层软件

作者给出了一个完整的分层模型，按击键传播顺序排列：

1. *键盘固件*（VIA/Chrysalis）：灯光、按键映射、层切换
2. *USB 层*（Karabiner）：识别击键来源键盘，拦截 media/system 键，跨设备统一修饰键
3. *菜单快捷键层*（CustomShortcuts）：改变应用菜单快捷键，修改后菜单中可见
4. *Player piano 层*（Keyboard Maestro）：模拟按键与鼠标点击，只写不读
5. *命令与逻辑层*（Keyboard Maestro 高级功能）：与应用 API 对话，读状态、做条件分支
6. *命令面板*（Raycast/Alfred）：单一可见入口
7. *文本展开*（Espanso/macOS Text Replacements）

Karabiner 是唯一能区分"哪块键盘发出的击键"的节点，也是唯一能处理 media/system 键的层。

## Player piano 与命令逻辑的实质区别

Player piano 是"只写不读"：模拟按键，但不知道按到了什么，不会失败报错，适合无 API 的应用，但脆。命令逻辑层能读系统状态与按钮名，失败有反馈，支持条件分支——代价是只对提供 API 的应用有效。实践中两者混用：逻辑层判断当前应用，player piano 执行操作。

## 25 个用法里最不显然的五个

- *截图用单键而非 Shift 组合*：Shift 会改变鼠标光标外观，可能打断需要截图的 tooltip；单键操作消除这个副作用。
- *⇧⇧Space 作为插入分隔线快捷键*：同时按住左右两个 Shift，刻意违反人体工学，只为自己设计，且物理"重量感"与分隔线语义匹配。
- *长按 ⌘V 弹出剪贴板历史*：将手机"长按展开更多"移植到 Mac；需要 Karabiner 截获后传给 Keyboard Maestro，并先执行 undo，避免干扰正常的首次粘贴。
- *同一动作绑多个触发键*：大街机按钮和 Fn 键都触发扫描，方便在不同体态（握书扫描 vs 坐在键盘前）下都能操作。
- *"Print the legend" 键*：用 macropad 上的一个键作新修饰键，按住后再按 ↓/Esc/Return 等，输出对应键位符号（⌘ ⇧ 等），比文本替换覆盖场景更广，且不会干扰正常输入"Command"。

## 隐藏限制

- 单键绑多功能造成场景互斥（在 Zoom 里无法同时用大按钮扫描）。
- Player piano 依赖屏幕布局，按钮移位即失效。
- Keyboard Maestro 安装后默认替换 ⌘Tab 切换器，需手动关掉（取消 Switcher Group）。
- 键盘固件层只能传输标准键码，不能直接发 Unicode；所有符号插入必须在更高层完成。
