# coding:utf-8
from enum import Enum
from string import Template
from typing import Union
import weakref

from PySide6.QtCore import QFile, QObject
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

from .config import qconfig, Theme, isDarkTheme
from .color import mixColor
from .material_color.utils.color_utils import argbFromRgb, redFromArgb, greenFromArgb, blueFromArgb
from .material_color.utils.theme_utils import themeFromSourceColor
from .material_color.scheme.scheme import Scheme


class StyleSheetManager(QObject):
    """ Style sheet manager """

    def __init__(self):
        self.widgets = weakref.WeakKeyDictionary()

    def register(self, file: str, widget: QWidget):
        """ register widget to manager

        Parameters
        ----------
        file: str
            qss file path

        widget: QWidget
            the widget to set style sheet
        """
        if widget not in self.widgets:
            widget.destroyed.connect(self.deregister)

        self.widgets[widget] = file

    def deregister(self, widget: QWidget):
        """ deregister widget from manager """
        if widget not in self.widgets:
            return

        self.widgets.pop(widget)

    def items(self):
        return self.widgets.items()


styleSheetManager = StyleSheetManager()


class QssTemplate(Template):
    """ style sheet template """

    delimiter = '--'


def applyThemeColor(qss: str):
    """ apply theme color to style sheet

    Parameters
    ----------
    qss: str
        the style sheet string to apply theme color, the substituted variable
        should be equal to the value of `ThemeColor` and starts width `--`, i.e `--ThemeColorPrimary`
    """
    template = QssTemplate(qss)
    mappings = {c.value: c.name() for c in ThemeColor._member_map_.values()}
    mappings.update({n: c.name() for n, c in palette.colors().items()})
    return template.safe_substitute(mappings)


class StyleSheetBase:
    """ Style sheet base class """

    def path(self, theme=Theme.AUTO):
        """ get the path of style sheet """
        raise NotImplementedError

    def content(self, theme=Theme.AUTO):
        """ get the content of style sheet """
        return getStyleSheet(self, theme)

    def apply(self, widget: QWidget, theme=Theme.AUTO):
        """ apply style sheet to widget """
        setStyleSheet(widget, self, theme)


class MaterialStyleSheet(StyleSheetBase, Enum):
    """ Material style sheet """

    MENU = "menu"
    BUTTON = "button"
    INFO_BAR = "info_bar"
    TOOL_TIP = "tool_tip"
    CHECK_BOX = "check_box"
    INFO_BADGE = "info_badge"
    MESSAGE_BOX = "message_box"
    TEACHING_TIP = "teaching_tip"
    SWITCH_BUTTON = "switch_button"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/qmaterialwidgets/qss/{theme.value.lower()}/{self.value}.qss"


def getStyleSheet(file: Union[str, StyleSheetBase], theme=Theme.AUTO):
    """ get style sheet

    Parameters
    ----------
    file: str | StyleSheetBase
        qss file

    theme: Theme
        the theme of style sheet
    """
    if isinstance(file, StyleSheetBase):
        file = file.path(theme)

    f = QFile(file)
    f.open(QFile.OpenModeFlag.ReadOnly)
    qss = str(f.readAll(), encoding='utf-8')
    f.close()

    return applyThemeColor(qss)


def setStyleSheet(widget, file: Union[str, StyleSheetBase], theme=Theme.AUTO, register=True):
    """ set the style sheet of widget

    Parameters
    ----------
    widget: QWidget
        the widget to set style sheet

    file: str | StyleSheetBase
        qss file

    theme: Theme
        the theme of style sheet

    register: bool
        whether to register the widget to the style manager. If `register=True`, the style of
        the widget will be updated automatically when the theme changes
    """
    if register:
        styleSheetManager.register(file, widget)

    widget.setStyleSheet(getStyleSheet(file, theme))


def updateStyleSheet():
    """ update the style sheet of all fluent widgets """
    removes = []
    for widget, file in styleSheetManager.items():
        try:
            setStyleSheet(widget, file, qconfig.theme)
        except RuntimeError:
            removes.append(widget)

    for widget in removes:
        styleSheetManager.deregister(widget)


def setTheme(theme: Theme, save=False):
    """ set the theme of application

    Parameters
    ----------
    theme: Theme
        theme mode

    save: bool
        whether to save the change to config file
    """
    qconfig.set(qconfig.themeMode, theme, save)
    updateStyleSheet()


class ThemeColor(Enum):
    """ Theme color type """

    PRIMARY = "ThemeColorPrimary"
    DARK_1 = "ThemeColorDark1"
    DARK_2 = "ThemeColorDark2"
    DARK_3 = "ThemeColorDark3"
    LIGHT_1 = "ThemeColorLight1"
    LIGHT_2 = "ThemeColorLight2"
    LIGHT_3 = "ThemeColorLight3"

    def name(self):
        return self.color().name()

    def color(self):
        color = qconfig.get(qconfig.themeColor)  # type:QColor

        # transform color into hsv space
        h, s, v, _ = color.getHsvF()

        if isDarkTheme():
            s *= 0.84
            v = 1
            if self == self.DARK_1:
                v *= 0.9
            elif self == self.DARK_2:
                s *= 0.977
                v *= 0.82
            elif self == self.DARK_3:
                s *= 0.95
                v *= 0.7
            elif self == self.LIGHT_1:
                s *= 0.92
            elif self == self.LIGHT_2:
                s *= 0.78
            elif self == self.LIGHT_3:
                s *= 0.65
        else:
            if self == self.DARK_1:
                v *= 0.75
            elif self == self.DARK_2:
                s *= 1.05
                v *= 0.5
            elif self == self.DARK_3:
                s *= 1.1
                v *= 0.4
            elif self == self.LIGHT_1:
                v *= 1.05
            elif self == self.LIGHT_2:
                s *= 0.75
                v *= 1.05
            elif self == self.LIGHT_3:
                s *= 0.65
                v *= 1.05

        return QColor.fromHsvF(h, min(s, 1), min(v, 1))


def themeColor():
    """ get theme color """
    return palette.primary


def setThemeColor(color, save=False):
    """ set theme color

    Parameters
    ----------
    color: QColor | Qt.GlobalColor | str
        theme color

    save: bool
        whether to save to change to config file
    """
    color = QColor(color)
    qconfig.set(qconfig.themeColor, color, save=save)
    updateStyleSheet()


def qcolorToArgb(color: QColor):
    return argbFromRgb(color.red(), color.green(), color.blue())


def argbToQColor(argb: int):
    return QColor(redFromArgb(argb), greenFromArgb(argb), blueFromArgb(argb))


class Palette(QObject):
    """ Palette """

    def __init__(self, color: QColor):
        super().__init__()
        self.setThemeColor(color)

    def setThemeColor(self, color: QColor):
        self.palette = themeFromSourceColor(qcolorToArgb(color))['schemes']

    @property
    def primary(self):
        return argbToQColor(self.scheme.primary)

    @property
    def onPrimary(self):
        return argbToQColor(self.scheme.onPrimary)

    @property
    def primaryContainer(self):
        return argbToQColor(self.scheme.primaryContainer)

    @property
    def onPrimaryContainer(self):
        return argbToQColor(self.scheme.onPrimaryContainer)

    @property
    def secondary(self):
        return argbToQColor(self.scheme.secondary)

    @property
    def secondaryContainer(self):
        return argbToQColor(self.scheme.secondaryContainer)

    @property
    def onSecondary(self):
        return argbToQColor(self.scheme.onSecondary)

    @property
    def onSecondaryContainer(self):
        return argbToQColor(self.scheme.onSecondaryContainer)

    @property
    def tertiary(self):
        return argbToQColor(self.scheme.tertiary)

    @property
    def onTertiary(self):
        return argbToQColor(self.scheme.onTertiary)

    @property
    def tertiaryContainer(self):
        return argbToQColor(self.scheme.tertiaryContainer)

    @property
    def onTertiaryContainer(self):
        return argbToQColor(self.scheme.onTertiaryContainer)

    @property
    def error(self):
        return argbToQColor(self.scheme.error)

    @property
    def onError(self):
        return argbToQColor(self.scheme.onError)

    @property
    def errorContainer(self):
        return argbToQColor(self.scheme.errorContainer)

    @property
    def onErrorContainer(self):
        return argbToQColor(self.scheme.onErrorContainer)

    @property
    def background(self):
        return argbToQColor(self.scheme.background)

    @property
    def onBackground(self):
        return argbToQColor(self.scheme.onBackground)

    @property
    def surface(self):
        return argbToQColor(self.scheme.surface)

    @property
    def onSurface(self):
        return argbToQColor(self.scheme.onSurface)

    @property
    def surfaceContainer(self):
        return argbToQColor(self.scheme.surfaceContainer)

    @property
    def surfaceContainerLow(self):
        return argbToQColor(self.scheme.surfaceContainerLow)

    @property
    def surfaceContainerHigh(self):
        return argbToQColor(self.scheme.surfaceContainerHigh)

    @property
    def surfaceContainerHighest(self):
        return argbToQColor(self.scheme.surfaceContainerHighest)

    @property
    def surfaceVariant(self):
        return argbToQColor(self.scheme.surfaceVariant)

    @property
    def surfaceBright(self):
        return argbToQColor(self.scheme.surfaceBright)

    @property
    def onSurfaceVariant(self):
        return argbToQColor(self.scheme.onSurfaceVariant)

    @property
    def outline(self):
        return argbToQColor(self.scheme.outline)

    @property
    def outlineVariant(self):
        return argbToQColor(self.scheme.outlineVariant)

    @property
    def shadow(self):
        return argbToQColor(self.scheme.shadow)

    @property
    def inverseSurface(self):
        return argbToQColor(self.scheme.inverseSurface)

    @property
    def inverseOnSurface(self):
        return argbToQColor(self.scheme.inverseOnSurface)

    @property
    def inversePrimary(self):
        return argbToQColor(self.scheme.inversePrimary)

    @property
    def scheme(self) -> Scheme:
        return self.darkScheme if isDarkTheme() else self.lightScheme

    @property
    def reverseScheme(self) -> Scheme:
        return self.lightScheme if isDarkTheme() else self.darkScheme

    @property
    def darkScheme(self) -> Scheme:
        return self.palette['dark']

    @property
    def lightScheme(self) -> Scheme:
        return self.palette['light']

    def colors(self):
        return {n: argbToQColor(argb) for n, argb in self.scheme.props.items()}


class ThemePalette(Palette):

    def __init__(self):
        super().__init__(qconfig.get(qconfig.themeColor))
        qconfig.themeColorChanged.connect(self.setThemeColor)


palette = ThemePalette()


def mixPrimary(color: QColor, weight: float):
    """ mix color with primary color

    Parameters
    ----------
    color: QColor
        the color to be mixed

    weight: float
        the weight of primary color
    """
    return mixColor(themeColor(), color, weight)


def hoverMixPrimary(color: QColor):
    """ mix color with primary color on hover state """
    return mixPrimary(color, 0.08)


def pressedMixPrimary(color: QColor):
    """ mix color with primary color on pressed state """
    return mixPrimary(color, 0.12)