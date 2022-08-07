import os ,sys
from  selenium.webdriver.common.by  import By
base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(base_path)
sys.path.append(base_path)
from UI2.test_case.page_obj.base import Base
from UI2.test_case.page_obj.loginPage import Login
from time import sleep
from UI2.test_case.models import driver,myunit
from UI2.test_case.models.readYaml import getYaml
loc_value=getYaml('roundPage.yaml')

class RoundManagePage(Base):
    round_loc=(By.XPATH,loc_value.get_elementinfo('round_loc'))
    round_type_loc = (By.XPATH, loc_value.get_elementinfo('round_type_loc'))
    round_type_list_loc=(By.XPATH, loc_value.get_elementinfo('round_type_list_loc'))#指定选中场次类型，暗拍
    roundlist_loc = (By.XPATH, loc_value.get_elementinfo('roundlist_loc'))

    def goto_roundpage(self):
        self.action_click(*self.round_loc)

    #成功进入场次页面
    round_page=(By.XPATH,)
    def verfy_round_page(self):
        msg=self.find_element(*self.round_page).text

    def filter_by_anpai(self):
        self.action_click(*self.round_type_loc)
        sleep(2)
        self.action_click(*self.round_type_list_loc)

    def filter_by_round_type(self):
        self.action_click(*self.round_type_loc)
        return self.find_elements(*self.roundlist_loc)


