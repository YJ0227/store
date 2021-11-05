from threading import Thread
import time

basket = 0
cash_register = 0
cus = 6

class Cook(Thread):
    chef = ""
    salay = 0.0

    def run(self):
        global basket, cash_register, cus
        while True:
            if basket < 600:
                basket += 1
                print("%s造了1个蛋挞" % self.chef)
                self.salay += 1.5
            else:
                time.sleep(3)
                continue
            if cus == 0:
                break
        print("%s的工资为：%s" % (self.chef, self.salay))
        cash_register -= self.salay
        print("收银机剩余：%s元" % cash_register)

class customer(Thread):
    username = ""
    money = 3000

    def run(self):
        global basket, cash_register, cus
        while True:
            if self.money > 0:
                if basket > 0:
                    basket -= 1
                    self.money -= 3
                    cash_register += 3
                    print("%s买了1个蛋挞，还剩%s元。" % (self.username, self.money))
                else:
                    time.sleep(2)
                    continue
            else:
                cus -= 1
                print("钱不够了！")
                break
        print("一共收银：%s元" % cash_register)

c1 = Cook()
c2 = Cook()
c3 = Cook()
c1.chef = "一"
c2.chef = "二"
c3.chef = "三"

cus1 = customer()
cus2 = customer()
cus3 = customer()
cus4 = customer()
cus5 = customer()
cus6 = customer()
cus1.username = "张"
cus2.username = "刘"
cus3.username = "杨"
cus4.username = "李"
cus5.username = "王"
cus6.username = "陈"

c1.start()
c2.start()
c3.start()
cus1.start()
cus2.start()
cus3.start()
cus4.start()
cus5.start()
cus6.start()
