from INT.rule_item import RuleItem
class RuleGallery():
    def __init__(self, rule_in):
        self.target = rule_in['target']
        self.rules = []
        self.vars = {}
        for item in rule_in['rules']:
            self.rules.append(RuleItem(item))

        if 'vars' in item.keys():
            self.vars[item['vars']] = -1


    def match(self, path, suffix):
        for rule in self.rules:
            ans = rule.match(path, self.vars, suffix)
            if ans == False:
                return None
        return self.target
