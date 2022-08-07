'''配置全局变量'''
import os,time

#获取项目路径
project_path=os.path.dirname(os.path.dirname(__file__))
# print(project_path)
#测试用例路径
test_case_path=os.path.join(project_path,'test_case','cases')
# print(test_case_path)
#测试结果路径
test_result_path=os.path.join(project_path,'report','testReport')
#测试截图存放路径
image_path=os.path.join(project_path,'report','images')

#log
log_dir=os.path.join(project_path,'log')
#config.ini文件路径
config_path=os.path.join(project_path,'data','config.ini')
#元素定位yaml文件
yaml_path=os.path.join(project_path,'data')


