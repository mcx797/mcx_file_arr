from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog

from qfluentwidgets import IconWidget, TextWrap, FlowLayout
from ..common.style_sheet import StyleSheet

from app.common.config import cfg
from ..common.path import FILE_ICON_PATH


class FileCard(QFrame):
    def __init__(self, parent=None, icon = None, title='文件', index = -1, folder=cfg.sourceFolder):
        super().__init__(parent=parent)
        self.index = index
        self.iconWidget = IconWidget(icon, self)
        self.titleLabel = QLabel(title, self)
        self._folder = folder
        self._parent = parent
        self.contentLabel = QLabel(TextWrap.wrap(cfg.get(self._folder), 45, False)[0], self)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout(self)
        self.setFixedSize(360, 90)
        self.iconWidget.setFixedSize(48, 48)

        self.hBoxLayout.setSpacing(28)
        self.hBoxLayout.setContentsMargins(20, 0, 0, 0)
        self.vBoxLayout.setSpacing(2)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)

        self.hBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addWidget(self.iconWidget)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addWidget(self.contentLabel)
        self.vBoxLayout.addStretch(1)

        self.titleLabel.setObjectName('titleLabel')
        self.contentLabel.setObjectName('contentLabel')

        #self.setAcceptDrops(True)



    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        folder = QFileDialog.getExistingDirectory(
            self, self.tr('Choose folder'), cfg.get(self._folder)
        )
        if not folder or cfg.get(self._folder) == folder:
            return
        cfg.set(self._folder, folder)
        self.refreshConfig()

    def clearLayout(self, target):
        item_list = list(range(target))
        item_list.reverse()
        for i in item_list:
            item = target.itemAt(i)
            target.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

    def refreshConfig(self):
        self._parent.refreshConfig()

class FileCardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._cards = []
        self._parent = parent
        self.vBoxLayout = QVBoxLayout(self)
        self.flowLayout = FlowLayout()
        self.vBoxLayout.setContentsMargins(36, 0, 36, 0)
        self.vBoxLayout.setSpacing(10)
        self.flowLayout.setContentsMargins(0, 0, 0, 0)
        self.flowLayout.setHorizontalSpacing(12)
        self.flowLayout.setVerticalSpacing(12)


        self.vBoxLayout.addLayout(self.flowLayout)
        StyleSheet.FILE_CARD.apply(self)
        #StyleSheet.HOME_INTERFACE.apply(self)

    def addFileCard(self, icon, title, index, folder):
        card = FileCard(self, icon, title, index, folder)
        self.flowLayout.addWidget(card)
        self._cards.append(card)

    def refreshConfig(self):
        self._parent.refreshConfig()

    def clearCards(self):
        self.flowLayout.removeAllWidgets()
        for item in self._cards:
            item.deleteLater()
        self._cards = []

    def refreshConfigContent(self):
        self.clearCards()
        self.flowLayout = FlowLayout()
        self.flowLayout.setContentsMargins(0, 0, 0, 0)
        self.flowLayout.setHorizontalSpacing(12)
        self.flowLayout.setVerticalSpacing(12)
        self.vBoxLayout.addLayout(self.flowLayout)
        self.addFileCard(
            icon = FILE_ICON_PATH,
            title='源文件夹',
            index=0,
            folder=cfg.sourceFolder
        )
        self.addFileCard(
            icon=FILE_ICON_PATH,
            title='目标文件夹',
            index=5,
            folder=cfg.targetFolder)