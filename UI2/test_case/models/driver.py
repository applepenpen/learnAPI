from selenium.webdriver import Remote
from selenium import webdriver
#定义驱动文件
def browser():
    '''
    启动浏览器驱动:使用grid 分布式测试，配置不同的主机和浏览器
    :return  返回浏览器驱动url
    '''
    try:

        host='http://127.0.0.1:4444'
        dc={'browserName':'chrome'}
        driver=Remote(command_executor=host+'/wd/hub',desired_capabilities=dc)
        # driver=webdriver.firefox
        #driver.get('https://www.baidu.com')
        return  driver
    except Exception as msg:
        print('驱动异常-》{0}'.format(msg))

if __name__=='__main__':
    dc=browser()
    dc.get('https://www.baidu.com')
    dc.quit()

