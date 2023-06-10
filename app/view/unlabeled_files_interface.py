from .gallery_interface import GalleryInterface

from PyQt5.QtWidgets import QWidget

class IconCardView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        print('hh')

class UnlabeledFilesInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(
            title='未分类文件',
            subtitle='untitled files',
            parent=parent
        )

        self.fileView = IconCardView(self)
        self.vBoxLayout.addWidget(self.fileView)