---
title: "Nix Derivation Madness"
date: 2025-11-04T11:14:00Z
category: reading
description: "Nix 中\"一个 /nix/store 输出路径可以对应多个完全不同的 .drv 文件\"——这不是 bug，而是固定输出 derivation（FOD）的设计必然结果；nix-store --query --deriver 和 nix derivation show 返回不同 .drv 哈希，两者都没错。"
source: "https://fzakaria.com/2025/10/29/nix-derivation-madness"
---

## TL;DR
Nix 中"一个 /nix/store 输出路径可以对应多个完全不同的 .drv 文件"——这不是 bug，而是固定输出 derivation（FOD）的设计必然结果；`nix-store --query --deriver` 和 `nix derivation show` 返回不同 .drv 哈希，两者都没错。

## 核心洞见
FOD 的输出路径由输出内容的哈希决定，而非 .drv 本身的哈希。修改 FOD 中任意非输出属性（如加入 `garbage = 123`）会产生一个全新的 .drv，但 /nix/store 输出路径完全不变。这个不变性向上传播：所有依赖该 FOD 的上层 derivation 也会得到全新的 .drv，却产出相同的输出路径。nixpkgs 规模下，FOD 的微小变动会刷新整个 .drv 树，产生大量无法从二进制缓存 realize 的"孤儿 .drv"。

## 具体机制
`nix-store --query --deriver` 查的是本地 SQLite 数据库的 deriver 字段——二进制缓存在下载输出时不强求本地保存对应的 .drv，因此本地 DB 可能记录一个本地和远程缓存都不存在的 .drv 哈希。`nix derivation show` 则从当前 nixpkgs 求值结果推导，两者天然可能指向不同 .drv。

## 更大意义
这个性质还允许更极端的操作：若两个不同 FOD 恰好产出相同内容（相同哈希），它们在父 derivation 的 inputDrvs 中可以互相替代——手工删除其中一个输入、用 `nix derivation add` 导入修改后的 .drv，仍能构建出完全相同的输出路径。输出路径与"参与构建的 .drv 集合"之间不存在一一对应，可以多对一，也可以在输入集合被修改后依然成立。

## 边缘事实
Nix 的纯粹性依赖"相同内容 = 相同哈希"，但这把钥匙也意味着"这个输出到底是由哪个 .drv 构建的"在实践中可能永远无法精确溯源。
