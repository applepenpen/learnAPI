

import requests
import urllib3
# requests.packages.urllib3.
from bs4 import BeautifulSoup
urllib3.disable_warnings()
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
def login():
    url = "https://pm-sso.cheyipai.com/loginAction/login.do"

    payload = 'username=13581708170&password=souche2020'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'acw_tc=3ccdc14916584977853378593e576d57394a158a1407689d127a113910b7b7; loginType=account; _security_token=19_NHPv_MgwHhiAIKk; JSESSIONID=7CF18152D0F2FE5EEF383AB94AC0BD7D'
    }
    s=requests.session()
    response = s.post( url, headers=headers, data=payload, verify=False)
    # soup=BeautifulSoup(response.text,'html.parser')
    # token_result=soup.find(id='ssoHideFrame').attrs['src']
    # print(token_result.split('=')[-1])
    # return '19_ySFc_MgwHhiAIKk'
    # print(response.content)
    # print(response.text)
    # print(response.cookies)
    return s.cookies['_security_token']

# print(login())

