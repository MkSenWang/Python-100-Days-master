#教育机构 ：马士兵教育
#讲    师：杨淑娟

s='hello world Python'
lst=s.split()
print(lst)
s1='hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))
print('-------------------------------')
'''rsplit()从右侧开始劈分'''
print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))