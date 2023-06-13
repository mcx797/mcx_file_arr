from PyQt5.QtCore import Qt, pyqtSignal, QEasingCurve
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QFrame, QWidget, QLabel

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, PopUpAniStackedWidget, qrouter)
#from qframelesswindow import FramelessWindow

from qfluentwidgets import FluentIcon as FIF
from app.components.frameless_window import FramelessWindow

from ..common.style_sheet import StyleSheet
from .title_bar import CustomTitleBar
from .setting_interface import SettingInterface
from .layout_interface import LayoutInterface
from .labeled_files_interface import LabeledFilesInterface
from .unlabeled_files_interface import UnlabeledFilesInterface
from utils.FileFactory import FileFactory

from ..common.path import LOGO_ICON_PATH

from app.common.config import cfg


class StackedWidget(QFrame):
    """ Stacked widget """

    currentWidgetChanged = pyqtSignal(QWidget)
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.view = PopUpAniStackedWidget(self)

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.view)

        self.view.currentChanged.connect(
            lambda i: self.currentWidgetChanged.emit(self.view.widget(i)))
    def addWidget(self, widget):
        """ add widget to view """
        self.view.addWidget(widget)
    def setCurrentWidget(self, widget, popOut=True):
        widget.verticalScrollBar().setValue(0)
        if not popOut:
            self.view.setCurrentWidget(widget, duration=300)
        else:
            self.view.setCurrentWidget(
                widget, True, False, 200, QEasingCurve.InQuad)
    def setCurrentIndex(self, index, popOut=False):
        self.setCurrentWidget(self.view.widget(index), popOut)

class MainWindow(FramelessWindow):
    def __init__(self):
        #open_word('\"C:\\Users\\77902\\Desktop\\1124.docx\"')
        super().__init__()
        self.setTitleBar(CustomTitleBar(self))
        self.hBoxLayout = QHBoxLayout(self)
        self.widgetLayout = QHBoxLayout()

        self.stackWidget = StackedWidget(self)
        self.navigationInterface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True)

        self.initFile()

        self.settingInterface = SettingInterface(self)
        self.layoutInterface = LayoutInterface(self)
        self.labeledFilesInterface = LabeledFilesInterface(self)
        self.unlabeledFilesInterface = UnlabeledFilesInterface(self, self.fileFactory)

        self.initLayout()

        self.initNavigation()

        self.initWindow()



    def initFile(self):
        root_path = cfg.get(cfg.sourceFolder)
        print(root_path)
        self.fileFactory = FileFactory(root_path)

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addLayout(self.widgetLayout)
        self.hBoxLayout.setStretchFactor(self.widgetLayout, 1)
        self.widgetLayout.addWidget(self.stackWidget)
        self.widgetLayout.setContentsMargins(0, 48, 0, 0)

        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)
        self.titleBar.raise_()

    def initNavigation(self):

        self.addSubInterface(
            self.labeledFilesInterface, 'labeledFilesInterface', FIF.HOME, self.tr('已分类文件'),
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.unlabeledFilesInterface, 'unlabeledFilesInterface', FIF.PASTE, self.tr('未分类文件'),
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.layoutInterface, 'layoutInterface', FIF.LAYOUT, self.tr('Layouts'),
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.settingInterface, 'settingInterface', FIF.SETTING, self.tr('Settings'),
            NavigationItemPosition.BOTTOM)

        qrouter.setDefaultRouteKey(self.stackWidget, self.labeledFilesInterface.objectName())

        self.stackWidget.currentWidgetChanged.connect(self.onCurrentWidgetChanged)
        self.navigationInterface.setCurrentItem(
            self.labeledFilesInterface.objectName())
        self.stackWidget.setCurrentIndex(0)

    def addSubInterface(self, interface: QWidget, objectName: str, icon, text: str, position=NavigationItemPosition.SCROLL):
        """ add sub interface """
        interface.setObjectName(objectName)
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=objectName,
            icon=icon,
            text=text,
            onClick=lambda t: self.switchTo(interface, t),
            position=position,
            tooltip=text
        )

    def initWindow(self):

        self.setMinimumWidth(1330)
        self.setMinimumHeight(700)
        self.resize(1330, 780)
        self.setWindowIcon(QIcon(LOGO_ICON_PATH))
        self.setWindowTitle('File Transfer')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(100, 50)

        StyleSheet.MAIN_WINDOW.apply(self)

    def switchTo(self, widget, triggerByUser=True):
        self.stackWidget.setCurrentWidget(widget, not triggerByUser)

    def onCurrentWidgetChanged(self, widget: QWidget):
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackWidget, widget.objectName())

    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width()-46, self.titleBar.height())

    def refreshConfig(self):
        self.settingInterface.refreshConfigContent()
        self.layoutInterface.refreshConfigContent()
        self.signal1.emit()