class INTItem():
    def __init__(self, item, idx):
        self.idx = idx
        self.type_list = item['type_list']
        self.out_path = item['out_path']
        self.para_list = item['para_list']

    def __str__(self):
        ans = "type_list:{}\nout_path:{}\npara_list{}\n".format(self.type_list, self.out_path, self.para_list)
        return ans