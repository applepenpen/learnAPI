import os
import logging
from logging.handlers import TimedRotatingFileHandler
from api_AUTO.read_config import log_dir
#日志收集器
#日志级别：debug,info ,warning,error,critical
#输出渠道:控制台，文件
#日志内容：时间，那个文件，哪行代码，暑促内容
class Logger(object):
    def __init__(self,logger_name='logs...'):
        self.logger=logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name='logs'#日志文件的名称
        self.backup_count=5#最多存放日志的数量
        #日志输出级别
        self.console_output_level='INFO'
        self.file_output_level='DEBUG'
        #日志输出格式
        self.formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


    def get_logger(self):
        '''在logger中添加日志句柄并返回，如果logger已有句柄，直接返回'''
        if not self.logger.handlers:#避免重复日志
            console_handle=logging.StreamHandler()
            console_handle.setFormatter(self.formatter)
            console_handle.setLevel(self.console_output_level)
            self.logger.addHandler(console_handle)
            #每天重新创建日志文件，最多保留backup_count份
            file_handler=TimedRotatingFileHandler(filename=os.path.join(log_dir,self.log_file_name),
                                                  when='D',interval=1,backupCount=self.backup_count,
                                                  delay=True,encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return  self.logger

logger=Logger().get_logger()
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

