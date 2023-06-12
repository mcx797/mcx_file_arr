from .gallery_interface import GalleryInterface

from PyQt5.QtWidgets import QWidget, QLabel, QFrame

from qfluentwidgets import SmoothScrollArea, SearchLineEdit


class LineEdit(SearchLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(self.tr('搜索未分类文件'))
        self.setFixedWidth(304)
        self.textChanged.connect(self.search)


class FileCardView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.FileCardViewLabel = QLabel(self.tr('未分类文件列表'), self)
        self.searchLineEdit = LineEdit(self)
        self.view = QFrame(self)
        self.scrollArea = SmoothScrollArea(self.view)
        self.scrollWidget = QWidget(self.scrollArea)

class UnlabeledFilesInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(
            title='未分类文件',
            subtitle='untitled files',
            parent=parent
        )

        self.fileView = FileCardView(self)
        self.vBoxLayout.addWidget(self.fileView)