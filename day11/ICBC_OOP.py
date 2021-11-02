import random
import pymysql

# 定义数据库工具类
class DBUtils():
    # 全局增删改的方法
    def update(self,sql,param):
        con = pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor = con.cursor()
        cursor.execute(sql,param)
        con.commit()
        cursor.close()
        con.close()

    # 全局做查询的方法
    def select(self,sql,param):
        con = pymysql.connect(host="localhost",user="root",password="root",database="bank")
        cursor = con.cursor()
        cursor.execute(sql,param)
        con.commit()
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

class ICBC():
    # 银行的名称写死
    def __init__(self):
        self.bank_name = "中国工商银行的昌平支行"
        self.db = DBUtils()

    # 1.入口程序
    @staticmethod
    def welcome():
        print("*************************************")
        print("*      中国工商银行昌平支行           *")
        print("*************************************")
        print("*  1.开户                            *")
        print("*  2.存钱                            *")
        print("*  3.取钱                            *")
        print("*  4.转账                            *")
        print("*  5.查询                            *")
        print("*  6.Bye！                           *")
        print("**************************************")

    # 2.开户
    # 2.1银行的开户逻辑
    def bank_addUser(self, username):
        # 1.判断数据库是否已满
        sql_count = "select count(*) from user"
        param = []
        count = self.db.select(sql_count, param)
        if count[0][0] >= 100:
            return 3

        # 2.判断用户是否存在
        sql_username = "select username from user"
        param = []
        select_username = self.db.select(sql_username, param)
        for i in select_username:
            if username in i:
                return 2
        return 1

    # 2.2用户的开户的操作逻辑
    def addUser(self):
        username = input("请输入您的用户名：")
        password = input("请输入您的开户密码：")
        country = input("请输入您的国籍：")
        province = input("请输入您的居住省份：")
        street = input("请输入您的街道：")
        door = input("请输入您的门牌号：")
        money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型

        # 随机产生8为数字
        # 判断账号是否存在,存在则重新生成
        while True:
            account = random.randint(10000000, 99999999)
            sql_account = "select account from user"
            param = []
            select_account = self.db.select(sql_account, param)
            if account not in select_account:
                break

        status = self.bank_addUser(username)
        if status == 3:
            print("对不起，用户库已满，请携带证件到其他银行办理！")
        elif status == 2:
            print("对不起，该用户已存在！请勿重复开户！")
        elif status == 1:
            sql_insert = "insert into user value (%s, %s, %s, %s, %s, %s, %s, %s, now(), %s)"
            param = [account, username, password, country, province, street, door, money, self.bank_name]
            self.db.update(sql_insert, param)

            print("开户成功！以下是您的个人开户信息：")
            info = '''
                 -------------------个人信息-------------------
                 用户名：%s
                 密码：%s
                 账号：%s
                 地址信息
                     国家：%s
                     省份：%s
                     街道：%s
                     门牌号: %s
                 余额：%s
                 开户行地址：%s
                 ----------------------------------------------
             '''
            print(info % (username, password, account, country, province, street, door, money, self.bank_name))

    # 3.存钱
    def saveMoney(self):
        account = int(input("请输入账号："))
        sql_account = "select account from user"
        param = []
        select_account = self.db.select(sql_account, param)
        for i in select_account:
            if account in i:
                password = input("请输入密码：")
                sql_info = "select * from user where account = %s "
                param = [account]
                select_info = self.db.select(sql_info, param)
                if password == select_info[0][2]:
                    save_money = int(input("请输入存入的金额："))
                    sql_save = "update user set money = money + %s where account = %s "
                    param_mon_acc = [save_money, account]
                    self.db.update(sql_save, param_mon_acc)
                    print("存款成功！")
                    sql_new_info = "select * from user where account = %s"
                    param_mon_acc_new = [account]
                    new_info = self.db.select(sql_new_info, param_mon_acc_new)
                    print("您的余额为：%s元" % new_info[0][7])
                else:
                    print("密码错误！")
                break
        else:
            print("该账户不存在！")

    # 4.取钱
    def getMoney(self):
        account = int(input("请输入账号："))
        sql_account = "select account from user"
        param = []
        select_account = self.db.select(sql_account, param)
        for i in select_account:
            if account in i:
                password = input("请输入密码：")
                sql_info = "select * from user where account = %s "
                param_input_account = [account]
                select_info = self.db.select(sql_info, param_input_account)
                if password == select_info[0][2]:
                    get_money = int(input("请输入您要取出的金额："))
                    if get_money <= select_info[0][7]:
                        sql_get = "update user set money = money - %s where account = %s "
                        param_input_money = [get_money, account]
                        self.db.update(sql_get, param_input_money)
                        print("取款成功！")
                        print("成功取款%s元" % get_money)
                        sql_new_info = "select * from user where account = %s"
                        param_new_money = [account]
                        new_info = self.db.select(sql_new_info, param_new_money)
                        print("您的余额为：%s元" % new_info[0][7])
                    else:
                        self.Return(3)
                else:
                    self.Return(2)
                break
        else:
            self.Return(1)


    # 返回值
    def Return(self,num):
        if num == 1:
            print("您输入的账号不存在！")
        elif num == 2:
            print("您输入的密码错误!")
        elif num == 3:
            print("您的钱不够!")

    # 5.转账
    def transferMoney(self):
        out_account = int(input("请输入您的账号："))
        sql_account = "select account from user"
        param = []
        select_account = self.db.select(sql_account, param)
        for i in select_account:
            if out_account in i:
                password = input("请输入您的密码：")
                sql_info = "select * from user where account = %s"
                param_input_account = [out_account]
                select_info = self.db.select(sql_info, param_input_account)
                if password == select_info[0][2]:
                    in_account = int(input("请输入转入账号："))
                    if in_account != out_account:
                        for j in select_account:
                            if in_account in j:
                                out_money = int(input("请输入您要转出的金额："))
                                if out_money <= select_info[0][7]:
                                    sql_transfer_out = "update user set money = money - %s where account = %s "
                                    sql_transfer_in = "update user set money = money + %s where account = %s "
                                    param_out = [out_money, out_account]
                                    param_in = [out_money, in_account]
                                    self.db.update(sql_transfer_out, param_out)
                                    self.db.update(sql_transfer_in, param_in)
                                    print("转账成功！")
                                    sql_new_info = "select * from user where account = %s"
                                    param_out = [out_account]
                                    new_info = self.db.select(sql_new_info, param_out)
                                    print("您的余额为：%s元" % new_info[0][7])
                                else:
                                    self.Return(3)
                                break
                        else:
                            self.Return(1)
                    else:
                        print("转入账号与转出账号不能相同！")
                else:
                    self.Return(2)
                break
        else:
            self.Return(1)

    # 6.查询
    def select_userInfo(self):
        account = int(input("请输入查询账号："))
        sql_account = "select account from user"
        param = []
        select_account = self.db.select(sql_account, param)
        for i in select_account:
            if account in i:
                password = input("请输入密码：")
                sql_info = "select * from user where account = %s"
                param_input_account = [account]
                select_info = self.db.select(sql_info, param_input_account)
                if password == select_info[0][2]:
                    info = '''
                             ------------个人信息------------
                             账号：%s
                             用户名:%s
                             密码：%s
                             地址：%s%s%s%s
                             余额：%s
                             开户行名称：%s
                             --------------------------------
                             '''
                    print(info % (
                    select_info[0][0], select_info[0][1], select_info[0][2], select_info[0][3], select_info[0][4],
                    select_info[0][5], select_info[0][6], select_info[0][7], select_info[0][9]))

                else:
                    print("密码错误!")
                break
        else:
            print("账号不存在！")

class ICBCMain():
    def __init__(self):
        self.icbc = ICBC()

    def run(self):
        # 添加死循环，让程序入口重复显示
        while True:
            self.icbc.welcome()
            # 获取用户的输入选择,根据用户的输入选择进行判断
            chose = input("请输入您的业务：")
            if chose == "1":
                self.icbc.addUser()
            elif chose == "2":
                self.icbc.saveMoney()
            elif chose == "3":
                self.icbc.getMoney()
            elif chose == "4":
                self.icbc.transferMoney()
            elif chose == "5":
                self.icbc.select_userInfo()
            elif chose == "6":
                print("Bye! 欢迎下次光临！")
                break
            else:
                print("输入错误！请重新输入！")


# 程序启动
m = ICBCMain()
m.run()


