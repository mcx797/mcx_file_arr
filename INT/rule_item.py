
class RuleItem():
    def __init__(self, rule_in):
        self.type = rule_in['type']
        self.content = rule_in['content']
        self.start = rule_in['start']
        self.end = rule_in['end']
        self.suffix = rule_in['suffix']
        if 'vars' in rule_in.keys():
            self.isVar = True
            self.vars = rule_in['vars']
        else:
            self.isVar = False


    def match(self, path, vars, suffix):
        start, end = self.getRange(path, vars)
        for i in range(start, end + 1):
            print(path[i])
            if self.matched(path[i], suffix):
                self.setVar(vars, i, path)
                return True
        return False

    def setVar(self, vars, num, path):
        if self.isVar:
            vars[self.vars] = len(path) - num - 1

    def matched(self, path, suffix):
        if self.type == 'in':
            if self.content in path and self.suffix == suffix:
                return True
            else:
                return False

    def getRange(self, path, vars):
        start = len(path) - int(self.end) - 1
        end = len(path) - int(self.start) - 1
        return start, end



