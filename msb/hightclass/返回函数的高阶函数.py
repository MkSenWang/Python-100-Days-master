# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

def get_sum(*args):

    def tt(): #定义函数
        s = 0
        for n in args:
            s+=n
        return s

    return tt # 返回函数

f1 = get_sum(1,2,3,4,5,6)()
# print(f1)


# 需求： 得到所有的质数, 打印小于100的所有质数
#1、质数：最小的质数是2
#2、偶数（2,0除外）都不是质数，只有1后奇数才有可能是质数
#3、思路：先得到所有大于的奇数  ---> 生成器 ,再把生成器中的所有元素过滤去掉：那些可以被小于元素本身的质数整除的

def odd_num(): # 得到所有大于1 奇数的生成器
    n = 1
    while True:
        n+=2
        yield n #n大于1 的所有奇数
g1  =odd_num()
# print(next(g1))
# print(next(g1))
# print(next(g1))

def my_filter(n):  # 判断是否能够整除的函数, n代表从一个生成器拿的的一个数字（质数）
    return lambda x: x % n >0  # x 是某一个奇数，n小于当前x的一个质数


#创建一个质数的生成器,最小的质数是2
def tt():
    yield 2
    g = odd_num() #得到所有大于的奇数
    while True:
        x = next(g) # 从生成器中拿到一个奇数
        g = filter(my_filter(x),g)  # 过滤之后再赋值给g
        yield  x

for n in  tt():
    if n<100:
        print(n)
    else:
        break