# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import time
from functools import wraps

def logger(func):
    @wraps(func)
    def write_logging():
        print("[info] --时间是：%s"%time.strftime('%H:%M:%S',time.localtime()))
        func()
    return  write_logging

@logger  # 使用装饰器来给所有的work增加记录日志的功能
def work():
    print("我在工作")

@logger
def work_2(name): # 1、 当前word2 函数可能有多个参数 2、自定义日志文件的名字和位置，记录日志的级别
    print("%s 在工作"%name)

# work()
work_2('张三')