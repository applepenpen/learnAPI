#封装查找最新测试报告方法，从测试报告路径中，按照生成时间排序，获取最新生成测试报告
import os
from UI2.test_case.models import readConfig
from UI2.data.globalparam import test_result_path
#
def new_report(test_report=None):
    if test_report==None:
        test_report=test_result_path
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_result_path+'/'+fn))
    file_new=test_result_path+'/'+lists[-1]
    # print(file_new)
    return file_new

print(new_report())
