import sys
import json
from api_AUTO.read_config import ReadConfig,base_path
from api_AUTO.excel_read.operate_excel import OperateExcel
from api_AUTO.excel_read import  data_config
from api_AUTO.common.readexcel import ExcelUtil   #读取Excel，返回list,key：value形式返回全部接口信息
from api_AUTO.common.handle_requests import SendRequest
# from common.Log import logger
from api_AUTO.common .operation_json import  OperetionJson   #获取json文件
from api_AUTO.excel_read.get_data import  GetData
from api_AUTO.common.login import login
from jsonpath_rw  import jsonpath,parse

class GetToken:  #获取token，绑定到全局变量类的类属性
    token =login()

class DependdentData:  #获取依赖case信息
    def  __init__(self,case_id):#传入依赖caseID
        self.case_id = case_id
        self.opera_excel = OperateExcel()
        self.data = GetData()
        self.row_num=self.get_row()
    def get_row(self):
        row_num = self.opera_excel.get_row_num(self.case_id)  # 根据依赖的case ID ,获取行号，
        return row_num
# 执行依赖case,获取response ,目前处理逻辑和这个不一致，这个是先执行依赖case,
    def run_dependent(self):
        run_method = SendRequest()
        row_num = self.opera_excel.get_row_num(self.case_id)  # 根据依赖的case ID ,获取行号，
        request_data = self.data.get_request_json(self.row_num)
        # print(type(request_data),request_data)

        # 根据行号，然后获取当前用例的json data
        # header = self.data.is_header(row_num)

        header_data=self.data.get_header(row_num)
        print(type(header_data),header_data)
        # header = common_func.opera_json(headerjson.get_data(is_header))
        header_data['Souche-Security-Token'] = GetToken().token
        method = self.data.get_request_method(self.row_num)
        # print(method)
        url = self.data.get_request_url(self.row_num)
        # print(url)
        res = run_method.request_main(method, url, request_data,header_data)
        return res


    #执行依赖后，根据data.items[0]:roundId  ,解析depend_data  获取实际依赖值
    def get_data_for_key(self,depend_key):
        # depend_key=self.data.depend_data(self.row_num)

        res=self.run_dependent()
        print(res)
        json_exe=parse(depend_key)
        madle=json_exe.find(res)
        return [math.value for math in madle][0]

if __name__=='__main__':
    de=DependdentData('Test3')
    res=de.run_dependent()
    print(res)
    print(de.get_data_for_key('data.items[0].roundId'))