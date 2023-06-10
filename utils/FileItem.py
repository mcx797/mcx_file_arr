import os.path


class FileItem:
    def __init__(self, path, name):
        self._path = path
        self._name = name
        self._is_labeled = False
        self._suffix = os.path.splitext(name)[-1]
    def Name(self):
        return self._name

    def __str__(self):
        return 'Item name is\n' + str(self._name) + '\nItem Path is \n' + \
            str(self._path) + '\n-------------------------\n'
