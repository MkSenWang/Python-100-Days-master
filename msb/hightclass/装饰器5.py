# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import time
from functools import wraps

def main_logger(log_file='out.log'):
    def logger(func):
        @wraps(func)
        def write_logging(*args,**kwargs):
            log = "[info] --时间是：%s"%time.strftime('%H:%M:%S',time.localtime())
            print(log)
            with open(log_file,'a') as f:
                f.write(log+'\n')
            func(*args,**kwargs)
        return  write_logging
    return logger

@main_logger()  # 使用装饰器来给所有的work增加记录日志的功能
def work():
    print("我在工作")

@main_logger('work2.log')
def work_2(name,name2): # 1、 当前word2 函数可能有多个参数 2、自定义日志文件的名字和位置，记录日志的级别
    print("%s 和 %s 在工作"%(name,name2))

work()
# work_2('张三','李四')