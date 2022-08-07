#coding:utf-8
import json
import os.path
'''从json 文件中，根据关键字提取具体value
   获取接口的对应的data
'''
from api_AUTO.read_config import excel_path

class OperetionJson:

	def __init__(self,json_file=None):
		if json_file == None:
			self.file_path = os.path.join(excel_path,'jsondatas.json')
		else:
			# json_file='header.json'
			self.file_path = os.path.join(excel_path,json_file)
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path) as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		return self.data[id]

#写json  ?需要重写封装
	def write_data(self,data):
		with open('../dataconfig/cookie.json','w') as fp:
			fp.write(json.dumps(data))



if __name__ == '__main__':
	opjson = OperetionJson('header.json')
	print(opjson.get_data('otherheader'))
