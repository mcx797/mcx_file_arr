import sys
import os
from utils.FileItem import FileItem

class FileFactory:
    """文件管理器"""
    def __init__(self, root_path, ruleCfg):
        self.root_path = root_path
        self.ruleCfg = ruleCfg
        self.files = []
        self.LoadFiles(root_path, [])


    def LoadFiles(self, path, path_list):
        dir_or_files = os.listdir(path)
        for file_name in dir_or_files:
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_path):
                path_list.append(file_name)
                self.LoadFiles(file_path, path_list)
                path_list.pop(len(path_list) - 1)
            else:
                if len(file_name) >= 2 and file_name[0:2] == '~$':
                    continue
                path_list.append(file_name)
                new_file = FileItem(path_list.copy(), file_name, self.ruleCfg)
                path_list.pop(len(path_list) - 1)
                self.files.append(new_file)

    def AllPath(self):
        return self.files

    def __str__(self):
        ans = 'the number of the file item is ' + str(len(self.files))
        for i in range(len(self.files)):
            ans += '\nitem '
            ans += str(i)
            ans += '\n-----------------------------------\n'
            ans += str(self.files[i])
            ans += '-------------------------------------'
        return ans

