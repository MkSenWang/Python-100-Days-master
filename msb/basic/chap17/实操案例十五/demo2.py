#教育机构 ：马士兵教育
#讲    师：杨淑娟
def find_answer(question):
    with open('replay.txt','r',encoding='gbk') as file:
        while True:
            line=file.readline()
            if not line: #if line==''到文件末尾退出
                break
            #字符串的分割
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return  reply
    return  False

if __name__ == '__main__':

    question=input('Hi,您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧')
    while True:
        if question=='bye':
            break
        #开始在文件中查找
        replay=find_answer(question)
        if not replay :  #如果回复的是False ，  not False-->True
            question=input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题,（退出请输入bye）')
        else:
            print(replay)
            question=input('小主，你还可以继续问一些关于订单、物流、账户、支付等问题（退出请输bye）')
    print('小主再见')