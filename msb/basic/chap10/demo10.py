#教育机构 ：马士兵教育
#讲    师：杨淑娟

def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1)
        return  res

print(fac(6))
