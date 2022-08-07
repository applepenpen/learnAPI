'''
description:配置全局变量
配置文件路径
配置用例目录路径
配置报告路径
配置日志路径
配置元素控制路径
配置测试数据
'''
import time,os,sys

#获取项目路径UI
BASE_DIR =os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)#加入环境变量
#配置文件路径
CONFIG_DIR=os.path.join(BASE_DIR,'database','user.ini')
#测试用例路径
TEST_DIR=os.path.join(BASE_DIR,'testcase')
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata")
# 元素定位控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")


