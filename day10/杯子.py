'''
分析一个水杯的属性和功能，使用类描述并创建对象
    高度，容积，颜色，材质
    能存放液体
'''

class Cup:
    __high = ''
    __v = 0
    __color = ''
    __cai = ''

    def sethigh(self, high):
        if high > 0:
            self.__high = high
        else:
            print("高度不能为0cm")
    def gethigh(self):
        return self.__high

    def setcolor(self, color):
        self.__color = color

    def getcolor(self):
        return self.__color

    def setv(self, v):
        if v <= 0:
            print("体积不能为0L或小于0升")
        else:
            self.__v = v
    def getv(self):
        return self.__v

    def setcai(self, cai):
        self.__cai = cai
    def getcai(self):
        return self.__cai

    def cun(self,p,m):
        if str(m).isdigit() is False:
            print('请输入正确的格式')
        elif int(m) > self.__v:
            print("放多了，杯子装不完")

        else:
            print("该杯子存放了%s%s升" % (p, m))

    def show_cup(self):
        print("此杯子体积为%s升， 材质为%s,  颜色为%s,  高为%scm " % (self.__v,self.__cai,self.__color,self.__high))

cup = Cup()
cup.setcai("玻璃")
cup.setv(1)
cup.sethigh(20)
cup.setcolor('绿色')
cup.show_cup()
cup.cun('普洱茶', '1')