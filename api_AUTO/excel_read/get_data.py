'''获取excel 单元格内容:根据行号，获取每个接口的参数值'''
import os.path

from api_AUTO.read_config import excel_path
from api_AUTO.excel_read import data_config
from api_AUTO.excel_read.operate_excel import OperateExcel
from api_AUTO.common .operation_json import  OperetionJson   #获取json文件
import xlrd

class GetData:
    def __init__(self,file_name=None,sheet_name=None):
        if file_name==None:
            self.file_name = os.path.join(excel_path,'cases.xls')
            self.sheet_name = 'Sheet2'
        self.opera_excel=OperateExcel(file_name,sheet_name)

    #获取Excel 中测试接口的总行数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #根据行号，获取接口对应的参数信息
    def case_id(self,row):
        col = int(data_config.get_id())  # 获取header 参数列ID
        id = self.opera_excel.get_cell_value(row, col)
        return  id

    # 根据行号，获取接口对应的参数信息
    def case_name(self, row):
        col = int(data_config.get_case_name())  # 获取header 参数列ID
        case_name = self.opera_excel.get_cell_value(row, col)
        return case_name

       # 获取url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        request_url = self.opera_excel.get_cell_value(row, col)
        if request_url != '':
            return request_url
        else:
            return None

    def is_run(self,row):
       col = int(data_config.get_run())  # 获取header 参数列ID
       is_run= self.opera_excel.get_cell_value(row, col)
       return  is_run

    #获取请求方法：
    def get_request_method(self,row):
       col=int(data_config.get_run_way())
       # print(col)
       request_method=self.opera_excel.get_cell_value(row,col)
       return request_method

   #根据行号，获取接口是否携带headers
    def is_header(self,row):
       col=int(data_config.get_header()) #获取header 参数列ID
       header=self.opera_excel.get_cell_value(row,col)  #获取 对应的单元格内容
       if header!='':
           return header
       else:
           return None
   #获取依赖case id

    def depend_id(self,row):
       col=int(data_config.get_case_depend()) #获取header 参数列ID
       case_depend=self.opera_excel.get_cell_value(row,col)  #获取 对应的单元格内容
       if case_depend!='':
           return case_depend
       else:
           return None

       # 获取依赖的字段
    def depend_data(self, row):
       col = int(data_config.get_data_depend())  # 获取header 参数列ID
       data_depend = self.opera_excel.get_cell_value(row, col)  # 获取 对应的单元格内容
       if data_depend  != '':
           return data_depend
       else:
           return None

    # 获取依赖的参数值
    def depend_value(self, row):
       col = int(data_config.get_field_depend())  # 获取header 参数列ID
       value_depend = self.opera_excel.get_cell_value(row, col)  # 获取 对应的单元格内容
       if value_depend  != '':
           return value_depend
       else:
           return None

    # 获取请求body,因为data 是json格式，很长，放置在json文件，所以需要进一步读取
    def get_request_body(self, row):  #data非Json格式时使用
       col = int(data_config.get_data())
       request_body = self.opera_excel.get_cell_value(row, col)
       if request_body != '':
           return request_body
       else:
           return None

    def get_request_json(self,row):#获取request json
        json_data=OperetionJson()
        # print(self.get_request_body(row))
        col = int(data_config.get_data())
        request_body = self.opera_excel.get_cell_value(row, col)
        if request_body != '':
            data=json_data.get_data(self.get_request_body(row))
            return data
        else:
            return None


    def get_header(self,row):  #获取实际header 值
        json_data = OperetionJson('header.json')
        col = int(data_config.get_header())  # 获取header 参数列ID
        header = self.opera_excel.get_cell_value(row, col)  # 获取 对应的单元格内容
        if header != '':
            header_data=json_data.get_data(header)
            return header_data
        else:
            return None


    # 获取实际结果
    def get_request_result(self, row):
       col = int(data_config.get_result())
       request_result = self.opera_excel.get_cell_value(row, col)
       if request_result!= '':
           return request_result
       else:
           return None
    # 获取期望结果
    def get_request_except(self, row):
       col = int(data_config.get_expect())
       request_result = self.opera_excel.get_cell_value(row, col)
       if request_result!= '':
           return request_result
       else:
           return None
   #  # 获取用例参数方式
   # def get_case_params_type(self, row):
   #     col = int(data_config.get_case_params_type())
   #     case_params_type = self.opera_excel.get_cell_value(row, col)
   #     if case_params_type!= '':
   #         return case_params_type

    #
    # # 获取用例参数
    # def get_request_params(self, row):
    #    col = int(data_config.get_parameters())
    #    request_params= self.opera_excel.get_cell_value(row, col)
    #    if request_params!= '':
    #        return request_params
    #    else:
    #        return None
    #
    # #获取case ID
    # def get_case_id(self,row):
    #    col=int(data_config.get_id()) #获取列号
    #    case_id=self.opera_excel.get_cell_value(row,col)
    #    return case_id
    #
    # def get_depend_case(self,row):
    #    col = int(data_config.get_depend_case())
    #    depend_case_id = self.opera_excel.get_cell_value(row, col)
    #    if depend_case_id!='':
    #        return depend_case_id
    #    else:
    #        return  None

if __name__=='__main__':
    # path = os.path.join(excel_path,'cases.xls')
    # sheet_name='Sheet2'
    get_data=GetData()
    lines=get_data.is_header(1)
    print(lines)
    print(get_data.get_header(5))

    # print(get_data.get_request_method(2))
