#教育机构 ：马士兵教育
#讲    师：杨淑娟

#print(10/0)
import  traceback
try:
    print('---------------------')
    print(1/0)
except:
    traceback.print_exc()