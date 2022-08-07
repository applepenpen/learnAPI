import os.path

import xlrd
import json
from api_AUTO.read_config import excel_path,ReadConfig

from xlutils.copy import copy
from api_AUTO.excel_read.data_config import global_var
# from common.Log import logger
# log=logger
# col_num=int(global_var.body)
# print(col_num)

class OperateExcel:
    '''读取Excel中接口信息'''

    def __init__(self,file_name=None,sheet_name=None):
        if file_name==None:
            self.file_name = os.path.join(excel_path,'cases.xls')
            self.sheet_name = 'Sheet2'
        else:
            self.file_name = os.path.join(excel_path,file_name)
            self.sheet_name = sheet_name
        self.data = self.get_data_contents()


    # 获取指定sheet内容
    def get_data_contents(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheet_by_name(self.sheet_name)
        return table

    # 获取单元格行数
    def get_lines(self):
        tables = self.get_data_contents()
        return tables.nrows

    # 获取某个单元格内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #往excel的表格 的某个单元格写入数据
    def write_values(self,row,col,value,sheet_name):
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_id=read_data.sheet_names().index(sheet_name)#根据sheet name 获取sheet id
        sheet_data=write_data.get_sheet(sheet_id)
        if type(value)==str:
            sheet_data.write(row,col,value)
        elif type(value)==dict:
            sheet_data.write(row, col, json.dumps(value,ensure_ascii=False))
        write_data.save(self.file_name)


    #根据行号获取该行内容
    def get_row_values_by_row(self,row):
        row_data=self.data.row_values(row)
        return row_data

    #根据列号获取某一列内容
    def get_cols_data(self,col_id):
        cols=self.data.col_values(col_id)
        # print(cols)
        return cols

    #根据caseID 获取行号
    def get_row_num(self,case_id):
        num=0
        # case_id_col_num=
        #case id 在第一列，行号为0
        cols_data=self.get_cols_data(0)
        # print(cols_data)
        for col_data in cols_data:
            if case_id in str(col_data):
                return num
            num=num+1

    # 根据case name 获取对应的行号
    def get_row_by_case_name(self, case_name):
        num = 0
        col = int(global_var.request_name)
        # print('the col of case name:',col)
        cols_data = self.get_cols_data(col)
        # print(cols_data)
        for col_data in cols_data:
            if case_name in str(col_data):
                # logger.info('根据case name 获取到case的行号是：' + str(num))
                return num
            num = num + 1



    #根据cese id 获取对应内容
    def get_row_data_by_caseID(self,case_id):
        row_num=self.get_row_num(case_id)
        row_data=self.get_row_values_by_row(row_num)
        return  row_data



if __name__=='__main__':
    # path='/Users/fumengjiao/work/cheyipai/API_AUTO/cyp_api_test/testFile/cases.xls'
    excel_data=ReadConfig().get_excel_name('round')
    path=os.path.join(excel_path,excel_data)
    print(path)
    excel_data=OperateExcel(path,sheet_name='Sheet2')
    # print(excel_data.get_data_contents())
    print(excel_data.get_row_values_by_row(1))  #根据行号获取行内容
    print(excel_data.get_row_values_by_row(2))
    print(excel_data.get_cols_data(0))  #根据列号获取列内容
    # print(excel_data.get_row_num('Test1'))   #根据case ID ，获取当前的行号
    # print(excel_data.get_row_by_case_name('退出接口'))
    # row_data=excel_data.get_row_values_by_row(0)
    # print(row_data)
    # col_data=excel_data.get_cols_data(0)
    # print(col_data,type(col_data))
    # row_num=excel_data.get_row_num("8")
    # print(row_num)
    # row_num=excel_data.get_row_by_case_name('成功获得Fast信息配置数据')
    # print(row_num)
    # data={'asd':113,'qqe':1313}
    # excel_data.write_values(7,7,data,sheet_name='Sheet1')
    # row=excel_data.get_row_by_case_name('成功提交')
    # print(excel_data.get_cell_value(row,4))