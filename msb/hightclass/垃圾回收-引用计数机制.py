# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import sys

class TestObject(object):
    def __init__(self):
        print("当前对象已经被创建，占用的内存地址为:%s"%hex(id(self)))

a = TestObject()
print("当前对象的引用计数为:%s"%sys.getrefcount(a))
b =a
print("当前对象的引用计数为:%s"%sys.getrefcount(a))
list1 = []
list1.append(a)
print("当前对象的引用计数为:%s"%sys.getrefcount(a))

# 减少
del a
# list1.remove(a)
print("当前对象的引用计数为:%s"%sys.getrefcount(b))


