import os.path

import xlrd
from api_AUTO.read_config import excel_path
# 非框架中的
# 读取测试用例的Excel表格文件,并生成一个list .每条记录存为dict,key：value
#一行为一条测试用例

class ExcelUtil():
    def __init__(self,excel_path,sheet_name='login'):
        self.data=xlrd.open_workbook(excel_path)
        self.table=self.data.sheet_by_name(sheet_name)
        #获取第一行作为key值
        self.keys=self.table.row_values(0)

        self.rowNum=self.table.nrows#获取行数
        self.colNum=self.table.ncols#获取列数


    def get_dict_data(self):
        if self.rowNum<=1:
            print('总行数小于1')
        else:
            # print(self.rowNum)
            self.dict_data=[]
            j=1
            for i in list(range(self.rowNum-1)):
                s={}
                s['rowNum']=i+2
                values=self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]]=values[x]
                j = j + 1
                self.dict_data.append(s)
            # print(self.dict_data)
            return self.dict_data




if __name__=='__main__':
    path= os.path.join(excel_path,'cases.xls')
    execl_data=ExcelUtil(path,'Sheet2')
    datas=execl_data.get_dict_data()
    # print(datas)
    #
    for i in datas:
        print(i)


