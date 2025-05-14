# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

#map: 把一个可迭代对象中的每个元素转换成一个新的对象，最后返回一个迭代器
list1 = [1,2,3,4,5,10,6,8,20,4]

it1 = map(lambda x:x**2,list1 ) # x 是列表中的每个原始。

# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1))

print(list(it1))

#2 、reduce 把一个可迭代对象中每个元素做聚会处理，最后返回一个聚会之后的值
from functools import reduce

print(reduce(lambda x,y :x+y ,list1 ))  #累加的需求

def getMax(x,y):
    if x>y:
        return x
    else:
        return y


print(reduce(getMax,list1)) #当前列表中的最大值


# 3、filter 把一个可迭代对象中的元素做过滤操作，如果func返回值为True则留下。否则过滤掉

emps = [  # 员工的列表
    {'name':'zhangsan','age':18,'salary':3000},
    {'name':'lisi','age':38,'salary':1000},
    {'name':'王五','age':28,'salary':2000}
]

#需求，过滤留下大于18岁的员工,返回一个迭代器
print(list(filter(lambda x:x['age']>18,emps)))


# 4、max 和 min
#计算薪资最高的员工
print( max(emps,key=lambda x:x['salary']) )
#计算新增最少的员工
print( min(emps,key=lambda x:x['salary']) )

# 5 、sorted  把一个可迭代对象里面的每个元素做排序，返回一个列表

#根据员工的年龄降序排序
print(sorted(emps,key=lambda x:x['age'],reverse=True))



