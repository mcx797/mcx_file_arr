class ConfigItem():
    def __init__(self, parent, name, value, default):
        self.__parent = parent
        self.name = name
        self.value = value

    def set(self, value):
        self.__value = value


    def __str__(self):
        return str(self.value)
