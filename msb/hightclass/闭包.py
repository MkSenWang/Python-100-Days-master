# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

#2、闭包的定义：
def func_a(number_a): # 高阶函数，返回一个函数

    def func_b(number_b):
        print('内嵌函数func_b的参数是:%s, 外部函数func_a的参数:%s'%(number_b,number_a))
        return number_b+number_a

    return func_b

result =  func_a(10) # 10传给函数func_a 的
# print(result(10))  # 10传给内嵌函数func_b的
# print(result(90))  # 10传给内嵌函数func_b的

#func_b就是闭包


#2、 闭包的应用

def create_line(a,b):

    def line(x):
        return a*x + b

    return line

# 得到一个一元线性函数
l1 =create_line(2,2)
l2 = create_line(1.5,-2)

# 计算在线1函数中，当x = 5 是对应的y
y = l2(5)
# print(y)



#3、 闭包里面修改外部变量的值
def test1():
    #c 其实不是局部变量，介于全局变量和局部变量之间的一种变量,nonlocal标识
    c = 1
    def add():
        nonlocal c
        print(c)
        c+=1
        return c
    return add

# print(test1()())

#4 、闭包的陷阱

def test3():
    func_list = []
    for i in  range(1,4):

        def test4(_i = i):
            return _i**2

        func_list.append(test4)
    return func_list

f1,f2,f3 =test3()
print(f1(),f2(),f3())


