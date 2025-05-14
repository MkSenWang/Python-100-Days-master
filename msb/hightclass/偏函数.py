# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import functools

print(int('123')) # 默认是按照10进制

print(int('123',base=16))
# print(int('123',16))

def int_2(num,base=2):
    return int(num,base)

print(int_2('1001'))

int_2 = functools.partial(int,base=2) #偏函数
print(int_2('1000000'))