from mxx_config.config import Config as mxxConfig
from mxx_config.item import ConfigItem as ConfigItem
class RuleConfig(mxxConfig):
    def __init__(self, json_addr):
        super().__init__(json_addr)
        self.target_list = ConfigItem(self, 'target_list', self.item('target_list'), [])
        self.rule_list = ConfigItem(self, 'rule_list', self.item('rule_list'), [])