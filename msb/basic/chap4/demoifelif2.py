#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/5/15 15:52
'''多分支结构，多选一执行
 从键盘录入一个整数 成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于0或大于100 为非法数据（不是成绩的有效范围）
'''
score=int(input('请输入一个成绩:'))
#判断
if  90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=69:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')
