from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog

from qfluentwidgets import IconWidget, TextWrap, FlowLayout
from ..common.style_sheet import StyleSheet

from app.common.config import cfg
from ..common.path import FILE_ICON_PATH
import os
from app.common.signal_bus import signalBus


class FileCard(QFrame):

    def __init__(self, parent=None, icon = None, title='文件', index = -1, folder=cfg.sourceFolder, signal = None):
        super().__init__(parent=parent)
        self.folder_changed_signal = signal
        self.index = index
        self.iconWidget = IconWidget(icon, self)
        self.titleLabel = QLabel(title, self)
        self._folder = folder
        self.__parent = parent
        self.contentLabel = QLabel(TextWrap.wrap(cfg.get(self._folder), 45, False)[0], self)
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout(self)
        self.setFixedSize(360, 90)
        self.iconWidget.setFixedSize(48, 48)
        self.contentLabel.setFixedSize(220, 45)

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
        self.setAcceptDrops(True)
        self.initSignal()

    def initSignal(self):
        self.folder_changed_signal.connect(self.refreshContent)

    def allSignals(self):
        ans = {}
        ans['folder_changed_signal'] = self.folder_changed_signal
        return ans

    def refreshContent(self):
        print('refreshContent done!')
        self.contentLabel.setText(TextWrap.wrap(cfg.get(self._folder), 45, False)[0])
        self.repaint()

    def dragEnterEvent(self, e):
        #print(e.minData())
        # print(evn.minData().text())
        # 鼠标放开函数事件
        e.accept()
    def dropEvent(self, e):
        file_path = e.mimeData().text()
        file_path = file_path[8:]
        print(file_path)
        if os.path.isdir(file_path):
            self.folderChanged(file_path)
        e.accept()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        folder = QFileDialog.getExistingDirectory(
            self, self.tr('Choose folder'), cfg.get(self._folder)
        )
        self.folderChanged(folder)

    def folderChanged(self, folder):
        if not folder or cfg.get(self._folder) == folder:
            return
        cfg.set(self._folder, folder)
        self.folder_changed_signal.emit()

class FileCardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._cards = []
        self.__parent = parent
        self.vBoxLayout = QVBoxLayout(self)
        self.flowLayout = FlowLayout()
        self.vBoxLayout.setContentsMargins(36, 0, 36, 0)
        self.vBoxLayout.setSpacing(10)
        self.flowLayout.setContentsMargins(0, 0, 0, 0)
        self.flowLayout.setHorizontalSpacing(12)
        self.flowLayout.setVerticalSpacing(12)


        self.vBoxLayout.addLayout(self.flowLayout)
        StyleSheet.FILE_CARD.apply(self)

    def addFileCard(self, icon, title, index, folder, signal):
        card = FileCard(self, icon, title, index, folder, signal)
        self.flowLayout.addWidget(card)
        self._cards.append(card)