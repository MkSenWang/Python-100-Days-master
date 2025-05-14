#教育机构 ：马士兵教育
#讲    师：杨淑娟

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#斐波那契数列第6位上的数字
print(fib(6))

print('------------------------------')
#输出这个数列的前6位上的数字
for i in range(1,7):
    print(fib(i))