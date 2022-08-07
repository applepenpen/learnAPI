from hashlib import md5
import json,os
import tarfile
from api_AUTO.read_config import ReadConfig,base_path
from api_AUTO.excel_read.operate_excel import OperateExcel
from api_AUTO.excel_read import  data_config
from api_AUTO.common.readexcel import ExcelUtil   #读取Excel，返回list,key：value形式返回全部接口信息
# from common.Log import logger
from api_AUTO.common .operation_json import  OperetionJson   #获取json文件
# log=logger

#获取参数的MD5加密后的值
def md5_decode(value):
    m2=md5()
    m2.update(value.encode('utf-8'))
    return m2.hexdigest()


#对json 格式的响应结果进行处理
def opera_json(value):
    if type(value)==str:
        data_value=json.loads(value)
    elif type(value)==dict:
        data_value=value
    return data_value

#找到依赖的测试用例，将指定内容写入excel 表格的此用例的单元格





#根据用例的row，col 获取cell 的gd_case(excel_path,sheet_name,row,col):
#     opera_excel = OperateExcel(excel_path, sheet_name)
#     value=opera_excel.get_cell_value(row,col)
#     return value

#获取依赖case的body参数值，并进行处理，用来方便的生成新的值
# def get_param_value_of_depend_case(table,row,col=None):
#
#     if col==None:
#         col= int(data_config.get_data())    #获取依赖case 的header
#     # else:
#     #     col=int(global_var.case_headers)
#     body_value=table.get_cell_value(row,col)  #str：这里格式还是原来的
#     # body_value=body_value.split
#     return body_value

#modify old value of depend case，之前前测试用例后，修改依赖case的body
# def modify_the_data_value(data_value,new_value,key):
#     # logger.info('the old value of this cell is %s ' % data_value)
#
#     # if type(data_value)==str:
#     #     data_value=json.loads(data_value)
#     # elif type(data_value)==dict:
#     #     data_value=data_value
#     data_value=OperetionJson.get_data(data_value)
#     for i in range(len(key)):
#         if key[i]=='jsonObject':
#
#             value=json.loads(data_value[key[i]])
#             value['reportCode']=str(new_value[i])
#             data_value['jsonObject']=json.dumps(value,ensure_ascii=False)
#         else:
#             data_value[key[i]] = str(new_value[i])
#     # logger.info('After modify:the new value of this cell is %s ' % data_value)
#     print(data_value)
#     return data_value

#修改完成，写入excel
# def write_excel_body(excel_path,sheet_name,new_value,depend_case_row_num,col=None):
#
#     #excel表格中‘body’字段的行
#     if col==None:
#         col = int(global_var.case_headers)
#     table_excel = OperateExcel(excel_path,sheet_name)
#     # row_num = opera_excel.get_row_by_case_name(case_name)#根据case name 获取对应行号
#     # logger.info('Need to modify the cell of sheet:%s'%sheet_name)
#     table_excel.write_values(depend_case_row_num,col, new_value,sheet_name=sheet_name)#excel中找到sheet表格，向表格的某个单元格写入数据
#     logger.info('修改完毕')

#修改完成，写入excel
# def write_excel_body(excel_path,sheet_name,new_value,depend_case_id,keys,col=None):
#
#     #excel表格中‘header’字段的行
#     if col==None:
#         col = int(global_var.case_headers)
#     else:
#         col = int(global_var.body)
#
#     table_excel = OperateExcel(excel_path,sheet_name)
#
#     # 根据case id 获取依赖用例的row num
#     depend_case_row_num = get_row_of_depend_case(table_excel, depend_case_id=depend_case_id)
#     # 获取依赖用例修改前的参数值
#     old_data_value = get_param_value_of_depend_case(table_excel, depend_case_row_num,col)
#     # 修改值
#     new = modify_the_data_value(old_data_value, new_value=new_value, key=keys)
#     # 修改完毕，写入excel中
#     table_excel.write_values(depend_case_row_num,col,value=new,sheet_name=sheet_name)#excel中找到sheet表格，向表格的某个单元格写入数据
#     # logger.info('修改完毕')




#  #获取需要的excel 表格文件的路径
def get_excel_path(name=None):
    if name!=None:
        excel_name=ReadConfig().get_excel_name(name)
        excel_path=os.path.join(base_path,'testFile',excel_name)
    else:
        excel_path=os.path.join(base_path,'testFile','test cases.xls')
    return excel_path


# #根据case name 从Excel表格中获取到对应行的参数内容，即每条测试用例的
def get_request_params(excel_path,case_name,sheet_name):
    #取出excel表格中用例信息，dict格式
    datas = ExcelUtil(excel_path=excel_path, sheet_name=sheet_name).get_dict_data()
    #取出某条case 的具体信息
    for requests_datas in datas:
        if requests_datas['case_name']==case_name:
            # logger.info('接口的request data:'+requests_datas['body'])
            return requests_datas




#一次性打包压缩pytest生成的测试报告
def make_targz(out_filename,source_dir):
    with tarfile.open(out_filename,'w:gz') as tar:
        tar.add(source_dir,arcname=os.path.basename(source_dir))

#逐个添加文件打包
# def make_targz_one_by_one(out_filename,source_dir):
#     tar=tarfile.open(output_filename,'w:gz')
#     for root,dir,files in os.walk(source_dir):
#         for file in files:
#             pathfile=os.path.join(root,file)
#             tar.add(pathfile)
#     tar.close()


if __name__=='__main__':
    # value=md5_decode('123456')
    # print(value)
    # path=get_excel_path('268v')
    # print(path)
    # output_filename=os.path.join(base_path,'report.zip')
    # source_dir=os.path.join(base_path,'allure-report')
    # # make_tcargz(output_filename,source_dir)
    # data_value={'a':123,'b':345,'c':324}
    # new_value=['222','333']
    key='e2e'
    # modify_the_data_value(data_value=data_value,new_value=new_value,key=key)
    print(md5_decode(key))
    # get_vin_license_info()