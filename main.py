from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

ele=driver.find_element(By.ID,'kw')

print(ele)


driver.quit()
