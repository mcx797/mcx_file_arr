import os.path


class FileItem:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.is_labeled = False
        self.suffix = os.path.splitext(name)[-1]
    def Name(self):
        return self.name

    def Path(self):
        return self.path

    def __str__(self):
        ans = ''
        for item in self.path:
            ans = ans + item + '/'
        ans = ans + self.name
        return ans