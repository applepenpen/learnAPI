#读取ini配置文件 获取文件中参数

import os
import configparser as CP

from UI2.data import globalparam

class ReadConfig:
    def __init__(self):
        self.cf=CP.ConfigParser()
        self.cf.read(globalparam.config_path,encoding='utf-8')

    def get_mail(self,name):
        value=self.cf.get('EMAIL',name)
        return value


if __name__=='__main__':
    readconfig=ReadConfig()
    print(type(readconfig.get_mail('content')))