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

from jsonpath_rw  import jsonpath,parse
class DependdentData:  #获取依赖case信息
    def  __init__(self,case_id):#传入依赖caseID
        self.case_id = case_id
        self.opera_excel = OperateExcel()
        self.data = GetData()

    # 根据caseID获取依赖用例的行num
    # def get_row_of_depend_case(self):
    #     depend_case_row_num = self.opera_excel.get_row_num(str(self.case_id))  # 根据case ID获取行号
    #     return depend_case_row_num
    # 根据行号获取整行数据
    def get_case_line_data(self):#先获取行号，在获取行内容
        # self.row_ID =self.get_row_of_depend_case
        rows_data = self.opera_excel.get_row_data_by_caseID(self.case_id)
        return rows_data

    #获取依赖case的json 格式data ,老值
    def  get_json_data(self):
        row_num = self.opera_excel.get_row_num(self.case_id)  # 根据依赖的case ID ,获取行号，
        request_data = self.data.get_request_json(row_num)
        return request_data





    def yilai_value(self,depend_key,res):
        json_exe = parse(depend_key)
        madle = json_exe.find(res)
        return [math.value for math in madle][0]


if __name__=='__main__':
    dep=DependdentData('Test4')
    print(dep.get_case_line_data())
