#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''一，使用print方式进行输出（输出的目地地是文件)'''
fp=open('h:/test.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

'''第二种方式，使用文件读写操作'''
with open('h:/test1.txt','w') as file:
    file.write('奋斗成就更好的你')

