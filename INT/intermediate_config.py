import json

from mxx_config.config import Config as Config
from mxx_config.item import ConfigItem as ConfigItem
from INT.para_item import ParaItem
from INT.para_item import ListParaItem as ListItem
from INT.INT_item import INTItem as INTItem
class INTConfig(Config):
    def __init__(self, json_addr):
        super().__init__(json_addr)
        self.description = self.item('description')
        para_dic = self.item('para')
        self.para = {}
        for item in para_dic:
            content = para_dic[item]
            if content['type'] == 'str':
                self.para[item] = ParaItem(content)
            elif content['type'] == 'options':
                self.para[item] = ListItem(content)

        self.INT = {}
        self.INT_list = []
        INT_dic = self.item('INT')
        idx = 0
        for item in INT_dic:
            self.INT_list.append(item['name'])
            self.INT[item['name']] = INTItem(item, idx)
            idx = idx + 1

    def __str__(self):
        ans = ""
        ans = ans +  str(self.description) + '\n'
        ans = ans +  str(self.para) + '\n'
        ans = ans + str(self.INT_list) + '\n'
        ans = ans +  str(self.INT) + '\n'
        return ans

if __name__ == '__main__':
    cfg = INTConfig('Leading_INT.json')
    print(cfg)