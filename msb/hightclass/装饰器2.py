# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
from functools import wraps

def test1(func): #定义一个额外功能（装饰器）
    @wraps(func) #使用func来包装test2
    def test2():
        print("帮你把饭做好")
        func()
        print("洗碗")
    return test2

@test1 #装饰器
def eat():
    print("我正在吃饭")


# eat = test1(eat)

eat()
print(eat.__name__)