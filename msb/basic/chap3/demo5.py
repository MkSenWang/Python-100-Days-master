#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/5/14 16:11
#比较运算符  ,比较运算符的结果为bool类型
a,b=10,20
print('a>b吗?',a>b)  #False
print('a<b吗?',a<b) #True
print('a<=b吗?',a<=b) #True
print('a>=b吗?',a>=b) #False
print('a==b吗?',a==b) #False
print('a!=b吗?',a!=b) #True

''' 一个  = 称为赋值运算符  , ==称为比较运算符
  一个变量由三部分组成，标识，类型，值 
   == 比较的是值还是标识呢?  比较的是值
  比较对象的标识使用  is 
'''
a=10
b=10
print(a==b)  #True  说明，a与b的value 相等
print(a is b ) #True 说明,a与b的id标识 ，相等
#以下代码没学过，后面会给大家讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)  #value   -->True
print(lst1 is lst2) #id   -->False
print(id(lst1))
print(id(lst2))
print(a is not b ) #False  a的id与b的id是不相等的
print(lst1 is not lst2) #True


