��          �               �   B  �      0     6  
   B  f   M     �     �  �   �  M   �  �   �  �   g  >   �  �  <  3  �     �  	   �       c        v     �  J   �  L   �  c   G	  q   �	  U   
   If you want to automatically switch the interface style when the theme changes, you can inherit StyleSheetBase and override the path() method. Suppose you have a MainWindow class and its qss file paths are app/resource/qss/light/main_window.qss and app/resource/qss/dark/main_window.qss, the code can be written like this: Theme Theme color Theme mode Theme.AUTO: Follow system theme. If the system theme cannot be detected, the light theme will be used. Theme.DARK: Dark theme Theme.LIGHT: Light theme When the theme changes, the config instance managed by qconfig (i.e., the config object passed in using the qconfig.load() method) will emit the themeChanged signal. When the theme color changes, qconfig will emit the themeColorChanged signal. You can use setThemeColor() method to change the theme color of QMaterialWidgets. This method accepts the following three types of parameters: You can use the setTheme() method to switch the light/dark theme of QMaterialWidgets. The parameter of setTheme() accepts the following three values: str: Hex color strings or color names, such as #0065d5 or red. Project-Id-Version: QMaterialWidgets 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2023-07-25 14:00+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_CN
Language-Team: zh_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0;
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.11.0
 如果想在主题发生改变时，自动切换界面的样式，可以继承 `StyleSheetBase` 类并重写 `path()` 方法。假设有一个 `MainWindow` 类，它的 qss 文件路径为 `app/resource/qss/light/main_window.qss` 和  `app/resource/qss/dark/main_window.qss`，那么代码可以这么写： 主题 主题色 主题模式 `Theme.AUTO`：跟随系统主题。如果无法检测到系统的主题，将使用浅色主题。 `Theme.DARK`：深色主题 `Theme.LIGHT`：浅色主题 当主题发生改变时，`qconfig` 将会发出 `themeChanged` 信号。 当主题发生改变时，`qconfig` 会发出 `themeColorChanged` 信号。 `setThemeColor()` 函数用于修改全部组件的主题色。该函数接受三种类型的值： `setTheme()` 函数用于切换 PySide-Material-Widgets 全部组件的亮暗主题。该函数接受下述值： `str`：十六进制颜色字符串或者颜色名字，比如 `#0065d5` 或者 `red` 