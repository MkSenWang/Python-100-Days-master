#教育机构 ：马士兵教育
#讲    师：杨淑娟
lst=[]
for i in range(0,5):
    goods=input('请输入商品编写和商品名称进入商品的入库，每次只能输入一件商品:\n')
    lst.append(goods)
for item in lst:
    print(item)

cart=[]
while True:
    num=input('请输入要购买的商品编号:')
    for item in lst:
        if item.find(num)!=-1:
            cart.append(item)
            break #退出for
    if num=='q':
        break #退出while循环
print('您购物车里已经选好的商品为:')
'''for m in cart:
    print(m)'''
for i in range(len(cart)-1,-1,-1):
    print(cart[i])
