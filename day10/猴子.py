'''
猴子类：
    属性：类别，性别，身体颜色，体重。
    行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
'''

class Monkey():
    __type = ""
    __sex = ""
    __color = ""
    __weight = ""

    def settype(self, type):
        self.__type = type
    def gettype(self):
        return self.__type

    def setsex(self, sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex

    def setcolor(self, color):
        self.__color = color
    def getcolor(self):
        return self.__color()

    def setweight(self, weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def make_fire(self, value):
        print("%s可以使用%s造火" % (self.__type, value))

    def study(self, *value):
        print("%s可以学习：" % self.__type, end=" ")
        for i in value:
            print(i, end=" ")

    def show(self):
        print("我是一只%s, 我的性别是%s, 我是%s的， 我体重%sKG。" % (self.__type, self.__sex, self.__color, self.__weight))

monkey = Monkey()
monkey.settype("金丝猴")
monkey.setsex("男")
monkey.setcolor("金色")
monkey.setweight(30)
monkey.show()
monkey.make_fire("木棍")
monkey.study("骑自行车", "跳绳", "穿衣服")



