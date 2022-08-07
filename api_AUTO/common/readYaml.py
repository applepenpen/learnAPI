import os
import yaml
from time import sleep

from api_AUTO.read_config  import excel_path
#读取yaml文件，

class getYaml:
    def __init__(self,filename):
        self.path=os.path.join(excel_path,filename)
        print('-----',self.path)
    def ReadYaml(self):
        '''加载yaml
        :param path :传入参数yaml名称
        '''
        try:
            f=open(self.path,'r',encoding='utf-8')
            datas=f.read()
            f.close()
            values=yaml.load(datas,Loader=yaml.FullLoader)
            return values
        except  Exception as msg:
            print(msg)

    def alldata(self):#返回全部yaml数据,返回dict
        datas=self.ReadYaml()
        return datas

    def get_elementinfo(self,locType):#获取元素的定位
        datas=self.alldata()
        return datas[locType][0]['element_info']

    def get_find_type(self, locType):#获取元素的定位方式
        datas = self.alldata()
        print(datas[locType])
        return datas[locType][0]['find_type']

    def get_element_info(self, locType):
        datas = self.alldata()
        return datas[locType][0]['info']
    def get_test_data(self):
        return self.alldata()[0]
if __name__=='__main__':
    # getyaml=getYaml('loginPage.yaml')
    # print(type(getyaml.get_find_type('login_user_loc')))
    # print(type(getyaml.get_elementinfo('login_user_loc')))
    data=getYaml('data.yaml')
    print(data.alldata()['round'])
