from .gallery_interface import GalleryInterface

class LabeledFilesInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(
            title='已分类文件',
            subtitle='labeled files',
            parent=parent
        )