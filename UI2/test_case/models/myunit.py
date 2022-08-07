from selenium import webdriver
from UI2.test_case.models.driver import browser
import unittest
import os
class MyTest(unittest.TestCase):
    '''
    继承unittest,初始化setup,teardown
    '''

    def setUp(self):
        self.driver=browser()#启动浏览器
        self.driver.implicitly_wait(10)#显示等待时间
        self.driver.maximize_window()#窗口最大化

    def  tearDown(self):
        self.driver.quit()



