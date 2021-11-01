'''
定义一个学生类：
    属性:
        学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
    行为：
        学习（要求参数传入学习的时间），玩游戏（要求参数传入游戏名），
        编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
'''

class Student():
    __stu_id = ""
    __name = ""
    __age = 0
    __sex = ""
    __hight = 0.0
    __weight = 0.0
    __grade = 0.0
    __address = ""
    __phone = 0

    def setid(self, id):
        self.__stu_id = id
    def getid(self):
        return self.__stu_id

    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name


    def setage(self, age):
        self.__age = age
    def getage(self):
        return self.__age

    def setsex(self, sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex

    def sethight(self, hight):
        self.__hight = hight
    def gethight(self):
        return self.__hight

    def setweight(self, weight):
        self.__weight = weight
    def getweight(self):
        return self.__weight

    def setgrade(self, grade):
        self.__grade = grade
    def getgrade(self):
        return self.__grade

    def setaddress(self, address):
        self.__address = address
    def getaddress(self):
        return self.__address

    def setphone(self,phone):
        self.__phone = phone
    def getphone(self):
        return self.__phone

    def study(self, time):
        print("学生%s学习了%s小时。" % (self.__name, time))

    def play_games(self, game_name):
        print("学生%s在玩%s游戏。" % (self.__name, game_name))

    def programming(self, rows):
        print("学生%s正在编程，已经写了%s行代码。" % (self.__name, rows))

    def sum(self, *num):
        sum = 0
        for i in num:
            sum = sum + i
        print("学生%s正在计算数的求和，求和结果为%s。" % (self.__name, sum))

    def show(self):
        print("学号：%s,  姓名：%s， 年龄：%s， 性别：%s，身高：%s， 体重：%s， 成绩：%s， 家庭地址：%s， 电话号码：%s。" % (self.__stu_id, self.__name, self.__age, self.__sex, self.__hight, self.__weight, self.__grade, self.__address, self.__phone))

student = Student()
student.setid("s001")
student.setname("张三")
student.setage("18")
student.setsex("男")
student.sethight(1.75)
student.setweight(60)
student.setgrade(88)
student.setaddress("北京市昌平区沙河镇")
student.setphone(18211112222)

student.show()
student.sum(1,2,3,4,5)
