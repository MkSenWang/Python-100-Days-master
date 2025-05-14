#教育机构 ：马士兵教育
#讲    师：杨淑娟
#创建星座的列表
constellation=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
#创建性格列表
nature=['积极乐观','固执内向','圆滑世故','多愁善感','迷之自信','精明计较','犹豫不决','阴暗消极','放荡不羁','务实本分','作天作地','安于现状']

#将两个列表转成集合
d=dict(zip(constellation,nature))
'''for item in d:
    print(item,d[item])'''
print(d)
key=input('请输入您的星座名称:')
flag=True
for item in d:
    if key==item:
        flag=True
        print(key,'的性格特点为:',d.get(key))
        break
    else:
        #print('对不起，您输入的星座有误')
        flag=False

if not flag:
    print('对不起，您输入的星座有误')
