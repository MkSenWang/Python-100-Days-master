#教育机构 ：马士兵教育
#讲    师：杨淑娟
try:
    score=int(input('请输入分数:'))
    if 0<=score<=100:
             print('分数为:',score)
except ValueError as e:
    print(e)
