import pytest,allure
from api_AUTO.common.handle_requests import SendRequest
from api_AUTO.read_config  import ReadConfig
from api_AUTO.read_config  import report_path,result_path,excel_path
from api_AUTO.common.common_func import get_request_params
from api_AUTO.common.common_func import get_excel_path
import api_AUTO.common.common_func as common_func
from api_AUTO.common.readYaml import getYaml
from ddt import ddt,data,unpack,file_data
import unittest
import pytest
import yaml
# @pytest.mark.parametrize(("a"))
def data_yaml():
    # print(getYaml('data.yaml').alldata()['rounddata'])
    return getYaml('data.yaml').alldata()['round']


# @ddt
# class Mytest(unittest.TestCase):
#     @data(*test_yaml())  #传入list，
#     # @unpack
#     def test(self,value):
#         print(value)
#
#
#
# if __name__=='__main__':
#    unittest.main()
class Test():
    @pytest.mark.parametrize('testdata',data_yaml())
    def test_data(self,testdata):
        print(testdata['data'])
        print(testdata['expect'])
if __name__=='__main__':
    pytest.main(['-s','-v','test_yanl.py'])
