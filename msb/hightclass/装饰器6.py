# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import time
from functools import wraps

#不适用函数，而是用类来做装饰器
class Logs(object):

    def __init__(self,log_file='out.log',level='INFO'):
        self.log_file =log_file
        self.level =level

    def __call__(self, func): # 定义装饰器，需要有一个接受函数
        @wraps(func)
        def write_logging(*args, **kwargs):
            log = "[%s] --时间是：%s" %(self.level, time.strftime('%H:%M:%S', time.localtime()))
            print(log)
            with open(self.log_file, 'a') as f:
                f.write(log + '\n')
            func(*args, **kwargs)

        return write_logging


@Logs()  # 使用装饰器来给所有的work增加记录日志的功能
def work():
    print("我在工作")

@Logs(log_file='work2.log',level="WARNING")
def work_2(name,name2): # 1、 当前word2 函数可能有多个参数 2、自定义日志文件的名字和位置，记录日志的级别
    print("%s 和 %s 在工作"%(name,name2))

# work()
work_2('张三','李四')