# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import time
from functools import wraps

def logger(func):
    @wraps(func)
    def write_logging(*args,**kwargs):
        print("[info] --时间是：%s"%time.strftime('%H:%M:%S',time.localtime()))
        func(*args,**kwargs)
    return  write_logging

@logger  # 使用装饰器来给所有的work增加记录日志的功能
def work():
    print("我在工作")

@logger
def work_2(name,name2): # 1、 当前word2 函数可能有多个参数 2、自定义日志文件的名字和位置，记录日志的级别
    print("%s 和 %s 在工作"%(name,name2))

# work()
work_2('张三','李四')