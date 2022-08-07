import unittest
import requests
import json,os
import sys
# sys.path.append(os.path.)
import pytest,allure
from api_AUTO.common.handle_requests import SendRequest
from api_AUTO.read_config  import ReadConfig
from api_AUTO.read_config  import report_path,result_path,excel_path
from api_AUTO.common.common_func import get_request_params
from api_AUTO.common.common_func import get_excel_path
import api_AUTO.common.common_func as common_func
from api_AUTO.common.readYaml import getYaml
# from common.Log import logger
from api_AUTO.excel_read.get_data import GetData
from api_AUTO.excel_read.operate_excel import OperateExcel
from api_AUTO.common.login import login
from api_AUTO.common .operation_json import  OperetionJson   #获取json文件
# from api_AUTO.common.dependent_data import DependdentData
from api_AUTO.common.other_depend  import DependdentData
# log=logger

#获取此类case使用的excel表格路径
# excel_path=get_excel_path('mgms')

datajson=OperetionJson()
headerjson=OperetionJson('header.json')

# print(headerjson.get_data('otherheader'))
class GetToken:  #获取token，绑定到全局变量类的类属性
    token =login()
# print(GetToken().token)
# @allure.MASTER_HELPER.feature('MGMS_login')
@allure.feature('场次管理')
class Test_round():
    '''测试退出接口'''

    # def __init__(self):
    #     self.sheet='Sheet2'  #Excel表sheet 名称
    #     # self.base_url=ReadConfig().get_base_url('base_url_for_mgms')#获取接口域名base URL
    #     self.run_request=SendRequest()
    # @classmethod
    # def setUpClass(cls):
    #     cls.run_request = SendRequest()

    run_request = SendRequest()

    def setup_class(self):
        print('测试开始了。。。。。。。')
        # self.token=GetToken.token
        yield
        print('测试结束了。。。。。。。')
        # self.token=login()   #  放置在方法级的前置方法中，绑定到当前用例对象的属性上

    # @allure.MASTER_HELPER.story('Login success')
    @allure.story('退出登录测试')
    @allure.testcase('https://www.baidu.com','test退出')
    @pytest.mark.case1



    # def test_logout_success(self):
    #
    #     case_name='退出接口'
    #     #首先根据case name 当前获取行号
    #     row_num=OperateExcel().get_row_by_case_name(case_name)
    #     # print(row_num)
    #     # url=self.base_url+GetData().get_request_url(row_num)
    #     #根据行号，获取接口对应的接口信息
    #     case_id=GetData().case_id(row_num)
    #     case_name=GetData().case_name(row_num)
    #     get_request_url=GetData().get_request_url(row_num)
    #     is_run=GetData().is_run(row_num)
    #     get_request_method=GetData().get_request_method(row_num)
    #     is_header=GetData().is_header(row_num)
    #     depend_id=GetData().depend_id(row_num)
    #     depend_data=GetData().depend_data(row_num)
    #     depend_value=GetData().depend_value(row_num)
    #     get_request_body=GetData().get_request_body(row_num)
    #     get_request_result=GetData().get_request_result(row_num)
    #     get_request_except=GetData().get_request_except(row_num)
    #     # print(case_id)
    #     # print(case_name)
    #     # print(get_request_url)
    #     # print(is_run)
    #     # print(get_request_method)
    #     # print(is_header)
    #     # print(depend_id)
    #     # print(depend_data)
    #     # print(depend_value)
    #     # print(depend_value)
    #     # print(get_request_body)
    #     # print(get_request_result)
    #     # print(get_request_except)
    #     #
    #     with allure.step('第一步：退出'):
    #         print('111111')
    #
    #     header = common_func.opera_json(headerjson.get_data(is_header))
    #     data = get_request_body + GetToken.token
    #     # print(data)
    #     # print(self.token)
    #     allure.attach.file('/Users/fumengjiao/work/bug/1.png',name='图片',attachment_type=allure.attachment_type.PNG)
    #     # res = self.run_request.request_main(method=get_request_method, request_url=get_request_url, data=data,headers=header)
    #     # res=requests.post(url=get_request_url,data=data,headers=header,verify=False)
    #     res = self.run_request.request_main(method=get_request_method, url=get_request_url, data=data, header=header,type='urlencoder')
    #
    #     # 判断是否存在依赖测试,存在就修改依赖测试用例的data
    #     self.assertEqual(int(res['code']), 200)
    #     self.assertIn(res['data'], get_request_except)
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize('testdata',getYaml('data.yaml').alldata()['round'])
    # @pytest.mark.parametrize('testdata', getYaml('data.yaml').alldata()['round'])
    # def test_data(self,testdata):
    #     print(testdata['data'])
    #     print(testdata['expect'])
    def test_round_num(self):
        case_name='获取场次总数'
        #首先根据case name 当前获取行号
        row_num=OperateExcel().get_row_by_case_name(case_name)
        # print(row_num)
        # url=self.base_url+GetData().get_request_url(row_num)
        #根据行号，获取接口对应的接口信息
        case_id=GetData().case_id(row_num)
        case_name=GetData().case_name(row_num)
        get_request_url=GetData().get_request_url(row_num)
        is_run=GetData().is_run(row_num)
        get_request_method=GetData().get_request_method(row_num)
        is_header=GetData().is_header(row_num)
        depend_id=GetData().depend_id(row_num)
        depend_data=GetData().depend_data(row_num)
        depend_value=GetData().depend_value(row_num)
        get_request_body=GetData().get_request_body(row_num)
        get_request_result=GetData().get_request_result(row_num)
        get_request_except=GetData().get_request_except(row_num)
        # print(case_id)
        # print(case_name)
        # print(get_request_url)
        # print(is_run)
        # print(get_request_method)
        # print(is_header)
        # print(depend_id)
        # print(depend_data)
        # print(depend_value)
        # print(depend_value)
        # print(get_request_body)
        # print(get_request_result)
        # print(get_request_except)
        #
        header = common_func.opera_json(headerjson.get_data(is_header))
        header['Souche-Security-Token']=GetToken().token
        

        # res = self.run_request.request_main(method=get_request_method, request_url=get_request_url, data=data,headers=header)
        # res=requests.post(url=get_request_url,headers=header,verify=False)
        res = self.run_request.request_main(method=get_request_method, url=get_request_url, data=get_request_body , header=header)
        # self.run_request.
        # 判断是否存在依赖测试,存在就修改依赖测试用例的data
        assert int(res['code'])==200
        # self.assertEqual(int(res['code']), 200)
        assert get_request_except  in  res['msg']
        # self.assertIn(res['msg'], get_request_except)

    @allure.title('场次列表筛选接口测试')
    @pytest.mark.parametrize('testdata', getYaml('data.yaml').alldata()['round'])
    def test_queryPage(self,testdata):


        case_name = '场次列表查询接口'
        # 首先根据case name 当前获取行号
        row_num = OperateExcel().get_row_by_case_name(case_name)
        # print(row_num)
        # url=self.base_url+GetData().get_request_url(row_num)
        # 根据行号，获取接口对应的接口信息
        case_id = GetData().case_id(row_num)
        case_name = GetData().case_name(row_num)
        get_request_url = GetData().get_request_url(row_num)
        is_run = GetData().is_run(row_num)
        get_request_method = GetData().get_request_method(row_num)
        is_header = GetData().is_header(row_num)
        depend_id = GetData().depend_id(row_num)
        depend_data = GetData().depend_data(row_num)
        depend_value = GetData().depend_value(row_num)
        get_request_body = GetData().get_request_body(row_num)
        get_request_result = GetData().get_request_result(row_num)
        get_request_except = GetData().get_request_except(row_num)
        request_data=testdata['data']
        expected=testdata['expect']
        header = GetData().get_header(row_num)
        header['Souche-Security-Token'] = GetToken().token


        res = self.run_request.request_main(method=get_request_method, url=get_request_url, data=request_data, header=header)

        # 判断是否存在依赖测试,存在就修改依赖测试用例的data
        assert int(res['code'])==200
        # self.assertEqual(int(res['code']), 200)
        assert expected in  res['msg']
    @allure.title('根据roundID获取场次详情')
    def test_round_xianchang(self):
        case_name='根据roundID获取场次详情'
        #首先根据case name 当前获取行号
        row_num=OperateExcel().get_row_by_case_name(case_name)
        # print(row_num)
        # url=self.base_url+GetData().get_request_url(row_num)
        #根据行号，获取接口对应的接口信息
        case_id=GetData().case_id(row_num)
        case_name=GetData().case_name(row_num)
        get_request_url=GetData().get_request_url(row_num)
        is_run=GetData().is_run(row_num)
        get_request_method=GetData().get_request_method(row_num)
        is_header=GetData().is_header(row_num)
        depend_id=GetData().depend_id(row_num)
        depend_data=GetData().depend_data(row_num)
        depend_value=GetData().depend_value(row_num)
        get_request_body=GetData().get_request_body(row_num)
        get_request_result=GetData().get_request_result(row_num)
        get_request_except=GetData().get_request_except(row_num)

        header = GetData().get_header(row_num)
        # print(header)
        data=GetData().get_request_json(row_num)
        # print(data)
        header['Souche-Security-Token']=self.token



        #首先判断是否执行
        if is_run=='yes':
            if depend_id !=None: #判断是否有依赖
                self.depend = DependdentData(depend_id)
                depend_response_data = self.depend.get_data_for_key(depend_data)  # 执行依赖case后，获取依赖value
                print(depend_response_data)
                #修改接口的data
                data[depend_value]=depend_response_data
                print('new data',data)
                res = self.run_request.request_main(get_request_method, get_request_url, data,header)
                print(res)
                self.assertEqual(int(res['code']), 200)
                self.assertIn(res['msg'], get_request_except)




if __name__=='__main__':
    # MGMS_Login().login_success()
    pytest.main(['-s', '-v','test_round.py'])
    # cmd = 'allure generate --clean ./testresult -o ./test_report'
    # os.system(cmd)
    # unittest.main()