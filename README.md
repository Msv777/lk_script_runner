# LK Script Runner
## 来源
原始插件来自 [Blender Artists 论坛](https://blenderartists.org/t/script-runner-addon/1481368)，由 Ludvik Koutny 创建,由于其Artstation 和 Gumroad似乎不可用了,这里这个版本修复了一些问题.

## 简介
LK Script Runner 是一个 Blender 插件，允许您从便捷的菜单中运行文本编辑器脚本。通过简单的快捷键 Ctrl+R，您可以访问所有可用脚本并快速执行它们。

## 特点
- 使用 Ctrl+R 快速访问脚本菜单
- 自动识别并列出文本编辑器中的 Python 脚本
- 支持全局脚本文件夹，使脚本在任何 Blender 文件中都可用
- 修复了嵌套函数不执行和 `if __name__ == '__main__'` 块不执行的问题

## 安装
1. 下载 ZIP 文件
2. 在 Blender 中，转到 编辑 > 首选项 > 插件
3. 点击 "安装..." 并选择下载的 ZIP 文件
4. 启用插件

## 使用方法
1. 在 Blender 中按 Ctrl+R 打开脚本菜单
2. 选择要运行的脚本
3. 脚本将立即执行

## 全局脚本
您可以在插件首选项中设置全局脚本文件夹。放置在此文件夹中的所有 .py 文件将在任何 Blender 文件中都可用。

**警告：** 全局脚本文件夹中的脚本将在没有任何安全检查的情况下执行。请不要放置任何您不完全信任的脚本。

## 兼容性
- 在 Blender 3.6 中测试过
- 应该可以在 Blender 4.0 中工作，但尚未完全测试


---

# LK Script Runner
## Source
Original addon from [Blender Artists forum](https://blenderartists.org/t/script-runner-addon/1481368), created by Ludvik Koutny.Due to the apparent unavailability of the original Artstation and Gumroad, this version has fixed some issues and uploaded to github.
## Introduction
LK Script Runner is a Blender addon that allows you to run Text Editor scripts from a convenient menu. With a simple shortcut Ctrl+R, you can access all available scripts and execute them quickly.

## Features
- Quick access to scripts menu with Ctrl+R
- Automatically identifies and lists Python scripts in the Text Editor
- Support for a global scripts folder that makes scripts available in any Blender file
- Fixed issues with nested functions not executing and `if __name__ == '__main__'` blocks not executing

## Installation
1. Download the ZIP file
2. In Blender, go to Edit > Preferences > Add-ons
3. Click "Install..." and select the downloaded ZIP file
4. Enable the addon

## Usage
1. Press Ctrl+R in Blender to open the scripts menu
2. Select the script you want to run
3. The script will execute immediately

## Global Scripts
You can set a global scripts folder in the addon preferences. All .py files placed in this folder will be available in any Blender file.

**WARNING:** Scripts in the global folder will be executed without any safety checks. Do not put any scripts you do not 100% trust in this folder.

## Compatibility
- Tested in Blender 3.6
- Should work in Blender 4.0, but not fully tested


