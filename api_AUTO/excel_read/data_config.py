'''
设置全局变量，获取Excel 中每列参数的列ID
'''

class global_var:
	id = 0 # ID
	request_name = 1 #名称
	url = 2  #url
	run = 3   #是否执行
	request_way = 4   #请求方法
	header = 5      #header 信息
	case_depend = 6   #依赖的case
	data_depend = 7    #依赖的case 参数
	field_depend = 8    #依赖的参数值
	data = 9         #参数data
	expect = 10    #接口期望结果
	result = 11     #接口实际结果
#获取caseid
def get_id():
	return global_var.id
def get_case_name():
	return global_var.request_name
#获取url
def get_url():
	return global_var.url

def get_run():
	return global_var.run

def get_run_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

# def get_header_value():
# 	return global_var.header
