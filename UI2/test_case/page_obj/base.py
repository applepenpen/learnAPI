from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base(object):
    '''
    页面基础类：用于所以页面的继承
    '''

    base_url='https://pm-sso.cheyipai.com/login.html?s=aHR0cHM6Ly9wYWltYWkuY2hleWlwYWkuY29t' #系统登录页面

    def __init__(self,selenium_driver,base_url=base_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30
        self.parent=parent

    def _open(self,url=None):
        url=self.base_url+url
        self.driver.get(url)
        # print('----------')
        # print(self.driver.current_url)
        # print(url)
        assert self.driver.current_url==(url) ,'did not land on %s' % url
    # def on_page(self):
    #     return self.driver.current_url()==(self.base_url+self.url)

    def open(self,url):
        self._open(url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)



    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    #封装执行JS的方法
    def scrip(self,src):
        return  self.driver.execute_script(src)
    #操作日期控件,使用js去除日期控件的可读属性，使其可输入
    def data_input(self,loc):
        '''

        :param loc: 日期控件的xpath路径
        :return:
        '''
        js="document.getElementByXpath('{}').removeAttribute('readonly')".format(loc)
        self.scrip(js)
    #日期控件中输入日期
#封装浏览器基本操作
    def set_windows_size(self):
        self.driver.set_windows_size(480,600)
    #浏览器刷新当前页面
    def refresh_driver(self):
        self.driver.refresh()
    #浏览器浏览时，模拟后退或前进到上一页
    def back_to(self):
        self.driver.back()
    def forward_to(self):
        self.driver.forward()
    #打印当前页面title:
    def print_title(self):
        return self.driver.title
    #打印当前页面url:
    def print_url(self):
        return self.driver.current_url
#封装基本元素操作
    #获取输入框尺寸
    def get_size(self,*loc):
        return self.find_element(*loc).size
    #获取元素text
    def get_text(self,*loc):
        return self.find_element(*loc).text
    #获取元素属性值
    def get_att(self,*loc,att):
        return self.find_element(*loc).get_attribute(att)
    #返回元素是否可见
    def get_isdisplay(self, *loc):
        return self.find_element(*loc).is_displayed()

#鼠标事件，右击，双击，拖动，悬停
    def action_right_click(self,*loc):
        right_click=self.find_element(*loc)
        AC(self.driver).context_click(right_click).perform()
#设置元素等待事件
    #显式等待
    def wait(self,*loc):
        element=WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(*loc))
        return element
#浏览器切换iframe
    def switch_iframe(self):
        pass
#多窗口切换
    def switch_windows(self):
        current_handle=self.driver.current_window_handle
        #一些操作后，打开多个页面
        all_handles=self.driver.windows_handles
        for handle in all_handles:
            if handle==current_handle:
                self.driver.switch_to.windows(handle)
#JS警告框处理，alert/confirm/prompt()   ,accept/text/dismiss
    def alert_handle(self):
        self.driver.switch_to.alert().accept #接受弹窗
        self.driver.switch_to.alert().text  # 获取警告框内文字
        self.driver.switch_to.alert().dismiss#解散警告框
        self.driver.switch_to.alert().send_keys()#发送文本到警告框



    #输入框清空
    def action_clear(self,*loc):
        self.find_element(*loc).clear()

    # 输入框输入文字内容
    def action_sendkeys(self,value,*loc):
        self.find_element(*loc).send_keys(value)

    # 按钮点击按钮
    def action_click(self,*loc):
        self.find_element(*loc).click()
    # 输入框输入内容的组合操作
    def action(self,*loc,value):
        self.action_clear(*loc)
        self.action_click(*loc)
        self.action_sendkeys(value,*loc)



