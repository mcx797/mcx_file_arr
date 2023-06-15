import os.path


class FileItem:
    def __init__(self, path, name, ruleCfg):
        self.path = path
        if len(name) >= 2 and name[0:2] == '~$':
            name = name[2:]
        self.name = name
        self.path[len(self.path) - 1] = name
        self.suffix = os.path.splitext(name)[-1]
        target = ruleCfg.match(self.path, self.suffix)
        if target != None:
            self.is_labeled = True
            self.target = target
        else:
            self.is_labeled = False
            self.target = 'no target'
        print(self.is_labeled)
        print(self.target)

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