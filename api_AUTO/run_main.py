
import configparser as CP
import os,time
import unittest
from common.common_func import make_targz
from api_AUTO.read_config import base_path,report_path,testcase_dir
from api_AUTO.common.send_email import SendEmail
from api_AUTO.common.log import logger
import pytest,allure
log=logger
#指定测试报告压缩文件的名字
zip_report_name=time.strftime('%Y%m%d_%H%M%S')+'api_report.zip'

log.info('zip report name:'+zip_report_name)
html_report_path=os.path.join(base_path,'allure-report')
log.info('xml report path:'+html_report_path)

if __name__=='__main__':

    #pytest执行测试用例，并使用allure生成测试报告

    pytest.main(['-s', '-v','./test_cases','--alluredir', './testresult'])
    cmd='allure generate --clean ./testresult -o ./test_report'
    os.system(cmd)

    #获取测试报告生成压缩文件并发送
    # report_lists=os.listdir(report_path)
    # report_lists.sort(key=lambda fn:os.path.getmtime(report_path+'\\'+fn))
    # report_new=os.path.join(report_path,report_lists[-1])
    # make_targz(zip_report_name,html_report_path)
    #
    # #发送邮件
    # try:
    #     send_mail(zip_report_name)
    # except:
    #     logger.info('邮件发送失败，请检查邮件配置')
    #     raise
    #

