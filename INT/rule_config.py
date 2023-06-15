from mxx_config.config import Config as mxxConfig
from mxx_config.item import ConfigItem as ConfigItem
from INT.intermediate_config import INTConfig
from INT.rule_gallery import RuleGallery

class RuleConfig(mxxConfig):
    def __init__(self, json_addr, INTcfg):
        super().__init__(json_addr)
        self.INTcfg = INTcfg
        rule_list = self.item('rule_list')
        print(self.item('rule_list'))
        self.rule = []
        for item in rule_list:
            if item['target'] not in INTcfg.INT_list:
                continue
            self.rule.append(RuleGallery(item))


    def match(self, path, suffix):
        for rule in self.rule:
            ans = rule.match(path, suffix)
            if ans != None:
                return ans
        return None


if __name__ == '__main__':
    INTcfg = INTConfig('Leading_INT.json')
    cfg = RuleConfig('Leading_rename_rule.json', INTcfg)