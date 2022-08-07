from UI2.package.HTMLTestRunner import HTMLTestRunner
from UI2.test_case.models.get_new_report import new_report
import time ,os,unittest
from UI2.data import globalparam
from UI2.test_case.models.send_mail import  send_mail



def add_case():
    '''
    构造测试集合
    :return:
    '''
    discover=unittest.defaultTestLoader.discover(globalparam.test_case_path,pattern='*_sta.py')
    return discover

def run_case():
    '''执行测试用例'''
    #按照当前时间生成html 测试报告文件名称
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = globalparam.test_result_path + '/' + now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='店铺后台管理系统自动测试报告', description='环境：MAC OS，浏览器：chrome')
    cases=add_case()
    runner.run(cases)
    fp.close()
    report=new_report()
    send_mail(report)
if __name__=='__main__':
    run_case()



