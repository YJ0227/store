'''
车类：
    属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
    功能：跑（要求参数传入车的具体功能，比如越野，赛车）
    创建：法拉利，宝马，铃木，五菱，拖拉机对象
'''

class Car():
    __type = ""
    __wheel_num = 0
    __color = ""
    __weight = 0.0
    __oil_box_size = 0.0

    def settype(self, type):
        self.__type = type
    def gettype(self):
        return self.__type

    def setwheel_num(self, wheel_num):
        self.__wheel_num = wheel_num
    def getwheel_num(self):
        return self.__wheel_num

    def setcolor(self, color):
        self.__color = color
    def getcolor(self):
        return self.__color

    def setweight(self, weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def setoil_box_size(self, size):
        self.__oil_box_size = size
    def getoil_box_size(self):
        return self.__oil_box_size

    def run(self, value):
        print("%s车可以%s" % (self.__type, value))

    def show(self):
        print("我是%s，我有%s个轮子，我是%s颜色的，我有%s吨，油箱能存储%s升油。" % (self.__type, self.__wheel_num, self.__color, self.__weight, self.__oil_box_size))

#  创建：法拉利，宝马，铃木，五菱，拖拉机对象
car1 = Car()
car1.settype("法拉利")
car1.setwheel_num(4)
car1.setcolor("黑色")
car1.setweight(1)
car1.setoil_box_size(40)
car1.show()
car1.run("赛车")
print()

car2 = Car()
car2.settype("宝马")
car2.setwheel_num(4)
car2.setcolor("白色")
car2.setweight(1.5)
car2.setoil_box_size(55)
car2.show()
car2.run("越野")
print()

car3 = Car()
car3.settype("铃木")
car3.setwheel_num(3)
car3.setcolor("灰色")
car3.setweight(0.8)
car3.setoil_box_size(35)
car3.show()
car3.run("越野")
print()

car3 = Car()
car3.settype("五菱")
car3.setwheel_num(4)
car3.setcolor("灰色")
car3.setweight(1.2)
car3.setoil_box_size(60)
car3.show()
car3.run("赛车")
print()

car3 = Car()
car3.settype("拖拉机")
car3.setwheel_num(4)
car3.setcolor("黄色")
car3.setweight(3.6)
car3.setoil_box_size(75)
car3.show()
car3.run("赛车")

