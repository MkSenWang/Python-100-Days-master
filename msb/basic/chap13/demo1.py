#教育机构 ：马士兵教育
#讲    师：杨淑娟

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')


car=Car('宝马X5')
car.start()
print(car.brand)