import json as json
from config.item import ConfigItem

class Config():
    def __init__(self, json_addr):
        self.__json_addr = json_addr
        self.load(json_addr)


    def load(self, json_addr):
        try:
            with open(json_addr, encoding="utf-8") as f:
                self.__config = json.load(f)
        except:
            self._config = {}
            print('config/Config.py: no such file')
        print('load json file {0}'.format(self.__json_addr))
    def item(self, name):
        try:
            item = self.__config[name]
        except:
            item = None
        return item

    def set(self, configItem, value):
        print(self.__json_addr)
        print(self.__config)
        print(configItem.Name())
        if self.__config.get(configItem.Name()) == None:
            print('no such item')
            return
        configItem.set(value)
        self.__config[configItem.Name()] = value
        with open(self.__json_addr, "w", encoding="utf-8") as f:
            json.dump(self.__config, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    cfg = Config('log_items.json')