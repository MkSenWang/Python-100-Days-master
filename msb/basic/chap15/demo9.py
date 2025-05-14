#教育机构 ：马士兵教育
#讲    师：杨淑娟

file=open('c.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()





