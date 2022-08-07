from selenium import webdriver
import  os

#封装截图函数

def insert_image(driver,file_name):
    '''

    :param driver:
    :param file_name: 截图文件名称，png文件
    :return:
    '''
    base_dir=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    base_dir=str(base_dir)
    print(base_dir)
    file_path=base_dir+'/report/images/'+file_name#截图存放路径
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_image(driver,'baidu.png')
    driver.quit()

