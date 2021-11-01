class Person():
    __age = 0
    __sex = ""
    __name = ""

    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    def setSex(self, sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

class Worker(Person):
    def work(self):
        print("工人%s正在干活..." % self.getName())

    def worker_introduce(self):
        print("我是工人%s，性别为%s，年龄为%s岁" % (self.getName(), self.getSex(), self.getAge()))

class Student(Worker, Person):
    __stu_id = ""

    def setStu_id(self, id):
        self.__stu_id = id
    def getStu_id(self):
        return self.__stu_id

    def study(self):
        print("学生%s正在学习..." % self.getName())

    def sing(self):
        print("学生%s正在唱歌..." % self.getName())

    def student_introduce(self):
        print("我是学生%s，学号是%s，性别为%s，今年%s岁。" % (self.getName(), self.__stu_id, self.getSex(), self.getAge()))

worker = Worker()
worker.setName("张三")
worker.setSex("男")
worker.setAge(44)
worker.work()
worker.worker_introduce()
print()

student = Student()
student.setName("李四")
student.setStu_id("stu001")
student.setAge(18)
student.setSex("女")
student.study()
student.sing()
student.student_introduce()
