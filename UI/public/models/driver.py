from selenium.webdriver import  Remote
from selenium import webdriver

def browser():
    '''
    启动浏览器驱动
    :return  返回浏览器驱动url
    '''
    try:
        # host='127.0.0.0.1:4444'
        # dc={'browserName':'chrome'}
        # driver=Remote(command_executor='http://'+host+'/wd/hub',
        #               desired_capabilities=dc)
        driver=webdriver.Chrome()
        driver.get('https://www.baidu.com')
        return  driver
    except Exception as msg:
        print('驱动异常-》{0}'.format(msg))


browser()