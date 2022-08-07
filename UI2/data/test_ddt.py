import json
import os

import ddt
import  requests
# import  json
# datas={
#     "auctionScreenListQuery": "",
# 	"lastAuctionId": "0",
# 	"pageIndex": 1,
# 	"pageSize": 10,
# 	"pageType": 3}
# header= {'Content-Type':'application/json'}
# print(type(datas))
# print(type(json.loads(json.dumps(datas))))
# res=requests.post('https://npi.cheyipai.com/auction/biz/auctionListController/getAuctionCarList.json',data=json.dumps(datas),headers=header)
# print(res.json())
# print(res.status_code)
# print(requests.utils.dict_from_cookiejar(res.cookies))
# #
# datas=[{'username':'mm','password':'123'},{'username':'jj','password':'9090'}]
# datas=[{'username':'mm','password':'123'}]
# # data=[[1.2.3]]
#
# a={'a':'11','b':'23'}
# @ddt.ddt
# class Test:
#     @ddt.data(*datas)
#     # @ddt.unpack
#     def test_ddt(self,data):
#         print(data)
#         # a['a']=data['username']
#         # a['b']=data['password']
#         # print('---')
#         # print(username)
#         # print(password)
#         # print(a)
#
#
# #
# if __name__=='__main__':
#     test=Test().test_ddt_1()
# import  math
# def fun(a,b,c):
#     x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
#     y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
#     return x, y
#
# print(fun(1,3,-4))
  #递归函数，在函数内部调用函数本身
  #汉诺塔
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '__>', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
# move(3,'a','b','c')

#闭包

# def inc():
#     x=1
#     def fn():
#         nonlocal x#闭包中对外层局部变量赋值，使用nonlocal 声明变量是外层的
#         x=x+1
#         return x
#     return fn
#闭包返回计数器函数
# def creatcount():
#     x=0
#     def count():
#         nonlocal  x
#         x=x+1
#         print(x)
#     return count
#
# A=creatcount()
# A()
# A()
# A()
# A()

#冒泡排序,从小到大
# L=[2,1,4,8]
# def fun():
#     for i in range(len(L)-1,0,-1):
#         for j in range(i):
#             if L[j]>L[j+1]:
#                 L[j],L[j+1]=L[j+1],L[j]
#     return L
#
# print(fun())

# import yaml
# import os
# path=os.path.dirname(__file__)
# print(path)
# # path=os.path.abspath(__file__)
# yaml_file=os.path.join(path+'/test.yaml')
# def get_data():
#     with open(yaml_file) as f:
#         # datas=yaml.load(f,Loader=yaml.FullLoader)
#         datas=yaml.safe_load(f)['add_params']
#         return datas
# print(get_data())
# import pytest
# def add(a,b):
#     return a+b
# l=[['1','2','3'],[]]
# @pytest.mark.parametrize('a,b,c',get_data()['argvalues'])
# def test_add(a,b,c):
#     # print(a,b,c)
#     assert c==add(a,b)
# # ll=['xx','效率']
# # @pytest.mark.parametrize('name',ll)
# # def test_name(name):
# #     print(name)
# if __name__=='__main__':
#     pytest.main(['-s','-v','test_ddt.py'])

#99乘法
# for i  in range(1,10):
#     for j in range(1,i+1):
#         print('%s * %s= %s'%(j,i,i*j),end=' ')
#     print('')
import unittest

def test():
    return 'aaa'
def test1():
    return  'bbb'
class EnvData:
    d=None
class Test(unittest.TestCase):
    name='mj'
    @classmethod
    def setUpClass(cls) -> None:
        data=test()
        # EnvData.d=data
        # cls.data=data #放置当前类的类属性中


        __class__.data=data
        os.environ['testToken']=data #放置在系统环境变量
        setattr(EnvData,'d',data) #放置在全局变量类的属性

    def setUp(self) -> None:
        data1=test1()
        self.data1=data1

    def test_data(self):
        print('开始测试')
        # print(os.environ.get('testToken'))
        # print(EnvData.d)
        # print(getattr(EnvData,'d'))
        print(self.__class__.data)
        print(self.data1)


    def test_2(self):
        print(self.__class__.id)


if __name__=='__main__':
    unittest.main()
    # print(Test().data)