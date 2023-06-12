import json

from config.Config import Config as Config
from config.item import ConfigItem as ConfigItem
class INTConfig(Config):
    def __init__(self, json_addr):
        super().__init__(json_addr)
        self.Description = ConfigItem(self, 'Description', self.item('Description'), 'no_Description')
        self.Para_list = ConfigItem(self, 'Para_list', self.item('Para_list'), [])
        self.Para_dic = {}
        for item in self.Para_list.Value():
            self.Para_dic[item] = ConfigItem(self, item, self.item(item), "no_para")

if __name__ == '__main__':
    cfg = INTConfig('log_items.json')
    cfg.set(cfg.Description, 'test description of log items!')