#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  os
print(os.getcwd())

lst=os.listdir('../chap15')
print(lst)

#os.mkdir('newdir2')
#os.makedirs('A/B/C')
#os.rmdir('newdir2')
#os.removedirs('A/B/C')
os.chdir('E:\\vippython\\chap15')
print(os.getcwd())