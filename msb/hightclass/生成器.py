# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import  time

#列表生成式
# list1 = [1,2,3,4,5,10]
list1 = [ x for x in range(1,10) ]

print(list1)

#引出生成器：对象，保存了产生元素的算法，同时会记录游标的位置
# 创建一个生成器： 1、通过列表生成式来创建
#                 2、通过函数来创建生成器（yield）
# 遍历生成器中元素内容：
#       1、通过next(g) ，当已经遍历到生成器的结尾抛异常 ：StopIteration
#       2、通过for来遍历
#       3、object内置的__next__ ：当已经遍历到生成器的结尾抛异常 ：StopIteration
#       4、send 函数  ,但是生成器的第一个值必须使用send(None)，后面的值就没有限制
g = (x for x in range(1,10) )
print(g)


# print(next(g))
# print(next(g))
# print(next(g))
# time.sleep(5)
# print(next(g))
# print(next(g))
# next(g)
# for i in g:
#     print(i,'-----')

# g2 = (x for x in range(10) if x%2==0)
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(next(g2))  # 第六次next时候，生成器中已经没有数据
# print(next(g2))


def test1(times):
    #初始化
    a,b =0,1
    n =0

    while n< times:  # yield一般用于创建生成器：工作返回后面变量值给生成器
        yield  b #print(b)  b 就是斐波拉契数列中的一个元素
        a,b = b,(a+b)
        n+=1
    return "done"

# print(test1(6))
g3 = test1(6)
print(g3)
print(next(g3))

def test2():
    #初始化
    a,b =0,1
    while True:  # yield一般用于创建生成器：工作返回后面变量值给生成器
        temp = yield  b #print(b)  b 就是斐波拉契数列中的一个元素
        a,b = b,(a+b)
        print(temp) # 输出None
    return "done"


def test3():
    print('hello')


g4 = test2()
print(g4)
# print(next(g4))
# print(next(g4))
# print(next(g4))
# print(g4.__next__())
# print(g4.__next__())
# print(g4.__next__())
# print(g4.__next__())

print(g4.send(None))
print(g4.send(''))
print(g4.send(''))
print(g4.send(''))
print(g4.send(''))