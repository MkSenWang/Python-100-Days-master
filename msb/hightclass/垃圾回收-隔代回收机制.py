# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import sys
import gc
import time

class TestObject(object):
    def __init__(self):
        print("当前对象已经被创建，占用的内存地址为:%s"%hex(id(self)))

    def __del__(self):
        print("当前对象马上被系统GC回收")
gc.disable() # 不启用GC，python3默认是启用
while True:
    a = TestObject()
    b = TestObject()
    a.pro = b
    b.pro = a
    del a
    del b
    print(gc.get_threshold()) # 打印隔代回收的阈值
    print(gc.get_count()) # 打印GC需要回收的对象的数量
    time.sleep(0.2)



