<p align="center">
  <img width="18%" align="center" src="source/_static/logo.png" alt="logo">
</p>
  <h1 align="center">
  PySide6-Material-Widgets
</h1>
<p align="center">
  基于 PySide6 的 Material Design 风格组件库
</p>

<p align="center">
  <a href="https://pypi.org/project/PySide6-Material-Widgets" target="_blank">
    <img src="https://img.shields.io/pypi/v/pyside6-material-widgets?color=%2334D058&label=Version" alt="Version">
  </a>

  <a style="text-decoration:none">
    <img src="https://static.pepy.tech/personalized-badge/pyside6-material-widgets?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Download"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-GPLv3-blue?color=#4ec820" alt="GPLv3"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"/>
  </a>
</p>

<p align="center">
<a href="../README.md">English</a> | 简体中文
</p>

![Interface](./source/_static/Interface.jpg)

## 安装📥
安装社区版：
```shell
pip install PySide6-Material-Widgets -i https://pypi.org/simple/
```

社区版只提供了基本的组件，[高级版](https://afdian.net/a/zhiyiYo?tab=shop)中内置了更多复杂的组件，开箱即用，快速开发。

> **Warning**
> 请勿同时安装 PySide2-Material-Widgets 和 PySide6-Material-Widgets，因为他们的包名都是 `qmaterialwidgets`


## 运行示例▶️
使用 pip 安装好 PySide6-Material-Widgets 包并下载好此仓库的代码之后，就可以运行 examples 目录下的示例程序，比如：
```python
cd examples/button
python demo.py
```

如果遇到 `ImportError: cannot import name 'XXX' from 'qmaterialwidgets'`，这表明 demo 中导入的组件只在高级版可用.

## 在线文档📕
想要了解 PySide6-Material-Widgets 的正确使用姿势？请仔细阅读 [帮助文档](https://qmaterilwidgets.readthedocs.io/zh_CN/latest/) 👈

## 支持💖
如果这个组件库帮助了您，或者是想支持作者继续开发和维护这个组件库，可以在 [爱发电](https://afdian.net/a/zhiyiYo) 或者 [ko-fi](https://ko-fi.com/zhiyiYo) 上请作者喝一杯奶茶。您的支持就是作者开发和维护的动力 🥰。

## 演示视频📽️
请查收哔哩哔哩上的 [视频合集](https://www.bilibili.com/video/BV1k14y1z74o)，它展示了 PySide6-Material-Widgets 的全部组件和特性 🎉

## 搭配 QtDesigner🚀
运行 `python ./tools/designer.py` 启动安装了 PySide6-Material-Widgets 插件的 QtDesigner。如果操作成功，QtDesigner 的侧边栏中将会显示 PySide6-Material-Widgets 的组件。对于旧项目的改造，推荐使用 [视频教程](https://www.bilibili.com/video/BV1na4y1V7jH) 中介绍的 `提升为...`。


## 参考
* [**Figma/Material 3 Design Kit**: Provides an introduction to the material design system](https://www.figma.com/community/file/1035203688168086460/Material-3-Design-Kit)
* [**Google/Material Design**: A website demonstrates the controls available in Material Design 3 System](https://m3.material.io/get-started)

## 许可证
PySide6-Material-Widgets 使用双许可证。非商业用途使用 [GPLv3](../LICENSE) 许可证进行授权，商用请在 [爱发电](https://afdian.net/a/zhiyiYo?tab=shop) 上进行购买以支持作者的开发。

Copyright © 2023 by zhiyiYo.
