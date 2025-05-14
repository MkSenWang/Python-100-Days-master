#教育机构 ：马士兵教育
#讲    师：杨淑娟

print('apple'>'app') #True
print('apple'>'banana') #False   ，相当于97>98 >False
print(ord('a'),ord('b'))
print(ord('杨'))

print(chr(97),chr(98))
print(chr(26472))

'''== 与is的区别
  == 比较的是 value
  is  比较的是id是否相等'''
a=b='Python'
c='Python'
print(a==b)  #True
print(b==c)  #True

print(a is b)  #True
print(a is c ) #True
print(id(a)) #2204259933168
print(id(b)) #2204259933168
print(id(c)) #2204259933168
