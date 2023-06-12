class ConfigItem():
    def __init__(self, parent, name:str, value, default):
        self.__parent = parent
        self.__name = name
        self.__value = value
        if self.__value == None:
            print('config/Item.py: no such item {0}'.format(self.__name))
            self.__value = default

    def Name(self):
        return self.__name

    def set(self, value):
        self.__value = value

    def Value(self):
        return self.__value

    def __str__(self):
        return "Item name is {0}\nItem value is {1}\n----------------------"\
            .format(str(self.__name), str(self.__value))