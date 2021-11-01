class Chef():
    __name = ""
    __age = ""

    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age

    # 蒸饭
    def steam_rice(self):
        print("%s在蒸饭..." % self.__name)

class Chef_son(Chef):
    # 炒菜
    def stir_fry(self):
        print("%s在炒菜..." % self.getname)

class Chef_grand_son(Chef_son):
    def steam_rice(self):
        print("蒸饭")
    def stir_fry(self):
        print("炒菜")

chef = Chef_grand_son()
chef.setname("李四")
chef.setage(25)
print("姓名：%s   年龄：%s" % (chef.getname(), chef.getage()))
chef.steam_rice()
chef.stir_fry()
