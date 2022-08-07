#读取配置文件config.ini :获取接口域名，数据库，email相关信息， Excel 表格名称

import os
import configparser as CP

#获取项目的根目录路径
base_path=os.path.abspath(os.path.dirname(__file__))
# base_path=base_path.replace('\\','/')
# print(base_path)
#获取config文件绝对路径
cfg_path=os.path.join(base_path,'config.ini')
# print(cfg_path)
# #获取test case 的Excel表格路径
excel_path=os.path.join(base_path,'test_data')
# print(excel_path)
#获取测试报告存放路径
report_path=os.path.join(base_path,'test_report')
result_path=os.path.join(base_path,'testresult')
#测试用例存放路径
testcase_dir=os.path.join(base_path,'test_cases')
#log存放路径
log_dir=os.path.join(base_path,'log')


class ReadConfig:
    '''
    解析ini配置文件，获取信息
    '''
    def __init__(self):
        self.cf = CP.ConfigParser()
        self.cf.read(cfg_path, encoding='utf-8')

    def get_mail(self,name):#获取email中信息
        value=self.cf.get('EMAIL',name)
        return value


    def get_db(self,name):
        value=self.cf.get('DATABASE',name)
        return value

    def get_base_url(self,name): #获取域名
        value=self.cf.get('HTTP',name)
        return value

    def get_excel_name(self,name): #获取Excel名称
        value=self.cf.get('EXCEL',name)
        return value
if __name__=='__main__':
    readconfig=ReadConfig()
    print(readconfig.get_excel_name('round'))

