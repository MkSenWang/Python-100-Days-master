#教育机构 ：马士兵教育
#讲    师：杨淑娟

'''元组的遍历'''
t=('Python','world',98)
'''第一种获取元组元组的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
#print(t[3]) #IndexError: tuple index out of range
'''遍历元组'''
for item in t:
    print(item)
