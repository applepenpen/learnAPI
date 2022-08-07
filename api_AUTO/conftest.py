import pytest

from api_AUTO.common.handle_requests import SendRequest
from api_AUTO.common.login import login
@pytest.fixture(scope='class',autouse=True)
def get_token():
    print('测试开始了。。。。。。。')
    # self.token=GetToken.token
    yield
    print('测试结束了。。。。。。。')
    # self.run_request = SendRequest()
    # # self.token=GetToken.token
    # self.token = login()  # 放置在方法级的前置方法中，绑定到当前用例对象的属性上
