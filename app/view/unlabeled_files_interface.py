from .gallery_interface import GalleryInterface

from PyQt5.QtCore import Qt, pyqtSignal

from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QTreeWidgetItem, \
    QTreeWidgetItemIterator, QApplication

from qfluentwidgets import SmoothScrollArea, SearchLineEdit, IconWidget, FlowLayout, TreeWidget, FluentIcon, TextWrap

from qfluentwidgets import FluentIcon as FIF

from app.common.style_sheet import StyleSheet

from utils.FileFactory import FileFactory
from utils.FileItem import FileItem
from app.common.trie import Trie


class LineEdit(SearchLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(self.tr('搜索未分类文件'))
        self.setFixedWidth(304)
        self.textChanged.connect(self.search)

class FileCard(QFrame):

    file_card_clicked_signal = pyqtSignal(FileItem)

    def __init__(self, file:FileItem, parent=None):
        super().__init__(parent=parent)
        self.file = file
        self.name = self.file.Name()
        self.icon = FIF.FOLDER
        self.isSelected = False
        self.nameLabel = QLabel(self)
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setText(TextWrap.wrap(file.Name(), 45, False)[0])
        self.hBoxLayout = QHBoxLayout(self)
        self.setFixedSize(192, 126)
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(8, 28, 8, 0)
        self.hBoxLayout.setAlignment(Qt.AlignTop)
        self.hBoxLayout.addSpacing(8)
        self.hBoxLayout.addWidget(self.nameLabel, 0, Qt.AlignHCenter)

    def mouseReleaseEvent(self, e):
        if self.isSelected:
            return
        self.file_card_clicked_signal.emit(self.file)

    def setSelected(self, isSelected:bool, force=False):
        if isSelected == self.isSelected and not force:
            return
        self.isSelected = isSelected

        self.setProperty('isSelected', isSelected)
        self.setStyle(QApplication.style())

class MesPanel(QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)
        #self.iconWidget = IconWidget(FIF.FOLDER, self)
        self.fileNameLabel = QLabel(self.tr('文件名字.txt'))
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(15, 5, 5, 5)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.addWidget(self.fileNameLabel)
        self.setFixedWidth(600)
        self.fileNameLabel.setObjectName('fileNameLabel')
        self.frame = TreeFrame(self, False)
        self.vBoxLayout.addWidget(self.frame)


    def setMes(self, file:FileItem):
        self.fileNameLabel.setText(file.Name())
        self.frame.refresh(file)

class FileCardView(QWidget):
    def __init__(self, parent, fileFactory:FileFactory):
        super().__init__(parent=parent)
        self.trie = Trie()
        self.fileFactory = fileFactory
        self.fileCardViewLabel = QLabel(self.tr('未分类文件列表'), self)
        self.searchLineEdit = LineEdit(self)

        self.view = QFrame(self)
        self.scrollArea = SmoothScrollArea(self.view)
        self.scrollWidget = QWidget(self.scrollArea)
        self.fileMesPanel = MesPanel(self)

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout(self.view)
        self.flowLayout = FlowLayout(self.scrollWidget, isTight=True)
        self.files = fileFactory.files
        self.cards = []
        self.currentIndex = -1

        self.__initWidget()

    def __initWidget(self):
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.setViewportMargins(0, 5, 0, 5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.addWidget(self.fileCardViewLabel)
        self.vBoxLayout.addSpacing(10)
        self.vBoxLayout.addWidget(self.searchLineEdit)
        self.vBoxLayout.addWidget(self.view)

        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.scrollArea)
        self.hBoxLayout.addWidget(self.fileMesPanel, 0, Qt.AlignRight)

        self.flowLayout.setVerticalSpacing(8)
        self.flowLayout.setHorizontalSpacing(8)
        self.flowLayout.setContentsMargins(8, 3, 8, 8)
        self.__setQss()


        self.flowLayout.removeAllWidgets()
        self.search('')



        for item in self.files:
            self.addCard(item)


        #self.showAllFiles()
        self.searchLineEdit.searchSignal.connect(self.search)
        self.searchLineEdit.clearSignal.connect(self.showAllFiles)
        '''
        self.setSelectedFile(self.files[0])

        
        

        self.showAllFiles()
        '''

    def search(self, keyWord:str):
        self.flowLayout.removeAllWidgets()

        for i, card in enumerate(self.cards):
            if keyWord in card.name:
                isVisible = True
            else:
                isVisible = False
            card.setVisible(isVisible)
            if isVisible:
                self.flowLayout.addWidget(card)

    def showAllFiles(self):
        self.flowLayout.removeAllWidgets()
        for card in self.cards:
            card.show()
            card.setVisible(True)
            card.show()
            self.flowLayout.addWidget(card)

    def setSelectedFile(self, file:FileItem):
        index = self.fileFactory.files.index(file)
        if self.currentIndex >= 0:
            self.cards[self.currentIndex].setSelected(False)

        self.currentIndex = index
        self.cards[index].setSelected(True)
        self.fileMesPanel.setMes(file)

    def addCard(self, file):
        card = FileCard(file, self)
        card.setVisible(True)
        card.file_card_clicked_signal.connect(self.setSelectedFile)
        self.flowLayout.addWidget(card)
        self.cards.append(card)


    def __setQss(self):
        self.view.setObjectName('fileView')
        self.scrollWidget.setObjectName('scrollWidget')
        self.fileCardViewLabel.setObjectName('fileCardViewLabel')

        StyleSheet.UNLABELED_FILES_INTERFACE.apply(self)

class Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 8, 0, 0)
        self.setObjectName('frame')

    def addWidget(self, widget):
        self._widget = widget
        self.hBoxLayout.addWidget(widget)

    def clear(self):
        self._widget.clear()
        self.hBoxLayout.removeWidget(self._widget)

class TreeFrame(Frame):
    def __init__(self, parent = None, enableCheck=False):
        super().__init__(parent)
        self.tree = TreeWidget(self)
        self.addWidget(self.tree)
        item1 = QTreeWidgetItem([self.tr('井')])
        item1.addChildren([
            QTreeWidgetItem([self.tr('测井评价资料')])
        ])
        self.tree.addTopLevelItem(item1)
        item2 = QTreeWidgetItem([self.tr('1')])
        item3 = QTreeWidgetItem([self.tr('2')])
        item4 = QTreeWidgetItem([self.tr('3')])
        item2.addChild(item3)
        item3.addChild(item4)
        self.tree.addTopLevelItem(item2)
        self.tree.expandAll()
        self.tree.setHeaderHidden(True)
        self.setFixedSize(550, 600)

        if enableCheck:
            it = QTreeWidgetItemIterator(self.tree)
            while(it.value()):
                it.value().setCheckState(0, Qt.Unchecked)
                it += 1

    def refresh(self, file:FileItem):
        self.tree.clear()
        if len(file.Path()) != 0:
            itemTop = QTreeWidgetItem([self.tr(file.Path()[0])])
            itemTemp = itemTop
            for i in range(1, len(file.Path())):
                item1 = QTreeWidgetItem([self.tr(file.Path()[i])])
                itemTemp.addChild(item1)
                itemTemp = item1
            item1 = QTreeWidgetItem([self.tr(file.Name())])
            itemTemp.addChild(item1)
            self.tree.addTopLevelItem(itemTop)
            self.tree.expandAll()

class UnlabeledFilesInterface(GalleryInterface):
    def __init__(self, parent=None, fileFactory:FileFactory =None):
        super().__init__(
            title='未分类文件',
            subtitle='untitled files',
            parent=parent
        )
        self.fileFactory = fileFactory
        self.fileView = FileCardView(self, self.fileFactory)
        self.vBoxLayout.addWidget(self.fileView)
