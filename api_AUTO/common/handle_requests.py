'''封装get/post 方法'''
import requests
import json
from api_AUTO.common.log import Logger
# import chardet

# requests.packages.urllib3.disable_warnings()
log=Logger().get_logger()
class SendRequest:
    def post_main(self, url, data=None, header=None):
        res = None
        if data != None and header!=None:
            res = requests.post(url=url, json=data, headers=header, verify=False)
        elif data==None and header!=None:
            res = requests.post(url=url, headers=header, verify=False)
        elif data!=None and header==None:
            res = requests.post(url=url, json=data, verify=False)
        else:
            res = requests.post(url=url,  verify=False)
        return res.json()

    def post_urlencoder(self, url, data=None, header=None):
        res = None
        if data != None and header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
            print(res)
        return res.json()
    def get_main(self, url, data=None, header=None):
        res = None
        if data != None and header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        elif data == None and header != None:
            res = requests.get(url=url, headers=header, verify=False)
        elif data != None and header == None:
            res = requests.get(url=url, params=data, verify=False)
        else:
            res = requests.get(url=url, verify=False)
        return res.json()



    def request_main(self, method, url, data=None, header=None,type=None):
        res = None
        if method == 'Post' or method=='post' or method=='POST':
            if type==None:
                res = self.post_main(url, data, header)
            elif type!=None:
                res=self.post_urlencoder(url,data,header)
        # elif method == 'put':
        #     res = self.put_main(url, data, header)
        # elif method == 'delete':
        #     res = self.delete_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
    # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
