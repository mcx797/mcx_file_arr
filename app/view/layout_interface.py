from .gallery_interface import GalleryInterface
from qfluentwidgets import FlowLayout, PushButton
from PyQt5.QtWidgets import QWidget

class LayoutInterface(GalleryInterface):
    def __init__(self, parent = None):
        super().__init__(
            title='流式布局',
            subtitle="layout view",
            parent=parent
        )

        self.addExampleCard(
            self.tr('Flow layout with animation'),
            self.createWidget(True),
            'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/flow_layout/demo.py',
            stretch=1
        )

    def createWidget(self, animation=False):
        texts = [
            self.tr('Star Platinum'), self.tr('Hierophant Green'),
            self.tr('Silver Chariot'), self.tr('Crazy diamond'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Heaven's Door"), self.tr('Killer Queen'),
            self.tr("Gold Experience"), self.tr('Sticky Fingers'),
            self.tr("Sex Pistols"), self.tr('Dirty Deeds Done Dirt Cheap'),
        ]

        widget = QWidget()
        layout = FlowLayout(widget, animation)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(20)

        for text in texts:
            layout.addWidget(PushButton(text))
        return widget
