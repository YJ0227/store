class Air_conditioner:
    __name = ''
    __price = 0

    def setname(self, value):
        self.__name = value
    def getname(self):
        return self.__name

    def setprice(self, value):
        self.__price = value
    def getprice(self):
        return self.__price

    def power_on(self):
        print("空调开机了...")

    def power_off(self, value):
        print("空调将在%s分钟之后自动关闭..." % value)

    def show(self):
        print("空调品牌名称为%s；价格为%s￥" % (self.__name, self.__price))

air=Air_conditioner()

air.setname('格力空调')
air.setprice(2889)

air.power_on()
air.power_off(10)

air.show()

