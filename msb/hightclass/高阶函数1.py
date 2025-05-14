# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

# 定义一个函数，传入一个列表[1,2,3,4,5,6,7], 返回一个新的列表 [每个数字的阶乘] [1! ,2!]
# 已经存在一个阶乘函数，

def test1(num): #计算一个数字的阶乘
    if num==1:
        return 1
    else:
        return num * test1(num-1) # n! = n * (n-1)!


#test2就是高阶函数 ，它的参数其中，第二个参数是函数本身
def test2(list,func):
    new_list=[]
    for x in list:
        new_list.append(func(x))
    return new_list

list1 = [1,2,3,4,5,6,7]
print(test2(list1,test1))