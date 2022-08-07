from selenium.webdriver.common.action_chains import  ActionChains #鼠标操作
import os ,sys
from  selenium.webdriver.common.by  import By
base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(base_path)
sys.path.append(base_path)
from UI2.test_case.page_obj.base import Base
from time import sleep
from UI2.test_case.models import driver,myunit
from UI2.test_case.models.readYaml import getYaml
loc_value=getYaml('loginPage.yaml')
class Login(Base):
    '''
    登录页面
    '''
    URL='/'
    login_user_loc=(By.XPATH,loc_value.get_elementinfo('login_user_loc'))
    login_password_loc=(By.XPATH,loc_value.get_elementinfo('login_password_loc'))
    login_loc = (By.XPATH, loc_value.get_elementinfo('login_loc'))

    def login_username(self,username):
        # self.find_element(*self.login_user_loc).clear()
        # self.find_element(*self.login_user_loc).click()
        # self.find_element(*self.login_user_loc).send_keys(username)
        self.action(*self.login_user_loc,value=username)

    def login_password(self,password):
        # self.find_element(*self.login_password_loc).clear()
        # self.find_element(*self.login_password_loc).click()
        # self.find_element(*self.login_password_loc).send_keys(password)
        self.action(*self.login_password_loc, value=password)

    def login_button(self):
        self.action_click(*self.login_loc)

    #定义统一的登录入口
    def user_login(self,username='13581708170',password='souche2020'):
        '''登录操作'''
        self.open(self.URL)
        sleep(3)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
    #用户名，密码错误元素定位
    error_loc=(By.XPATH,loc_value.get_elementinfo('error_loc'))
   #登录成功
    success_loc=(By.XPATH,loc_value.get_elementinfo('success_loc'))

    def login_fail_text(self):
        return self.find_element(*self.error_loc).text
    def login_success_text(self):
        return self.find_element(*self.success_loc).text

    #店铺入住协议窗口操作
    checkbox_loc=(By.XPATH,loc_value.get_elementinfo('checkbox_loc'))
    confirm_button_loc=(By.XPATH,loc_value.get_elementinfo('confirm_button_loc'))
    close_windows_loc=(By.XPATH,loc_value.get_elementinfo('close_button'))

    def close_xieyi(self):
        self.action_click(*self.checkbox_loc)
        self.action_click(*self.confirm_button_loc)
        self.action_click(*self.close_windows_loc)
        sleep(3)
if __name__=='__main__':
    dr=driver.browser()
    test=Login(dr)
    test.user_login()
    test.close_xieyi()