from  time import sleep
import  unittest,random,sys,os
from  UI2.test_case.models import screenshot,driver,readYaml
from  UI2.test_case.models.myunit import MyTest
from UI2.test_case.page_obj.loginPage import Login
import ddt
login_data=readYaml.getYaml('login_data.yaml').alldata()
#登录页面测试用例。使用ddt ,解析yaml测试数据，自动执行测试用例

@ddt.ddt
class loginTest(MyTest):
    # driver=
    def user_login_verfy(self,username='',password=''):
        Login(self.driver).user_login(username,password)

    # def test_login_success(self):
    #     self.user_login_verfy(username='13581708170',password='souche2020')
    #     sleep(3)
    @ddt.data(*login_data)
    def test_login(self,datayaml):
        '''
        登录测试，
        :param datayaml: 加载login_data获取登录测试数据
        :return:
        '''

        self.user_login_verfy(username=str(datayaml['data']['phone']),password=str(datayaml['data']['password']))
        po=Login(self.driver)
        if datayaml['detail']=='手机号或密码不匹配':
            msg=po.login_fail_text()
            sleep(3)
            self.assertEqual(msg,datayaml['check'])#获取测试结果和测试数据进行断言
            screenshot.insert_image(self.driver,datayaml['screenshot']+'.png')
        if datayaml['detail']=='登录成功':
            sleep(3)
            msg = po.login_success_text()
            po.close_xieyi()  # 关闭协议窗口
            self.assertEqual(msg, str(datayaml['check']))
            screenshot.insert_image(self.driver, datayaml['screenshot'] + '.png')




    # def test_username_error_verfy(self):
    #     '''密码错误'''
    #     self.user_login_verfy(username='13581708100',password='souche2020')
    #     po=Login(self.driver)
    #     msg=po.user_error_hint()
    #     print('-------')
    #     print(msg)
    #     sleep(3)
    #     self.assertEqual(msg,'用户名或密码错误')
    #     screenshot.insert_image(self.driver,'username_error.png')

if __name__=='__main__':
    unittest.main()
