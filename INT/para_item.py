
class ParaItem():
    def __init__(self, para_dic):
        self.type = para_dic['type']
        self.value = para_dic['value']

    def __str__(self):
        ans = "type:{}\nvalue:{}".format(str(self.type), str(self.value))
        return ans


class ListParaItem(ParaItem):
    def __init__(self, para_dic):
        super().__init__(para_dic)
        self.list = para_dic['list']

    def __str__(self):
        ans = "type:{}\nlist:{}\nvalue:{}".format(str(self.type), str(self.list), str(self.value))
        return ans
