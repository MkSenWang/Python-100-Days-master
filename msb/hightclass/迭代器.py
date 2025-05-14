# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
# Iterable: 可迭代对象，能够通过for循环来遍历里面的元素的对象。
from collections.abc import Iterable
from collections.abc import Iterator

a = (1,)
b = [1,2]
c= {}

def test1(arg):
    if isinstance(arg,Iterable):
        print("arg对象是可迭代对象")
    else:
        print('arg对象不是可迭代对象')


def test2(arg):
    if isinstance(arg,Iterator):
        print("arg对象是迭代器")
    else:
        print('arg对象不是迭代器')

test2( ( 1 for x in  range(5)) )

#把list ，dict, str变成迭代器

test2(iter(b))

