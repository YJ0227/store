# 中国农业银行昌平支行
# 实现功能：开户、存钱、取钱、转账、查询、Bye
import random

# 1.准备一个数据库 和 银行名称
bank = {}
bank_name = "中国农业银行昌平支行"  # 银行名称写死的

# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国农业银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")

# 3.开户
# 3.1银行的开户逻辑
def bank_addUser(account, username, password, account_type, country, province, street, door, money):
    # 1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if account in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "account_type":account_type,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1

# 判断账户类型
def type():
    while True:
        account_type = input("请输入账户类型[1.金卡  2.普通卡]：")
        if account_type == "1":
            return "【金卡】"
            break
        elif account_type == "2":
            return "【普通卡】"
            break
        elif len(account_type) == 0:
            print("该项不能为空！请重新输入！")
            continue
        else:
            print("输入错误！！！   请重新输入！！！")


# 3.2用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    account_type = type()
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    door = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))
    # 随机产生8位数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password,account_type, country, province, street, door, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            账户类型：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, account_type, country, province, street, door, money, bank_name))

# 4.存钱
def saveMoney():
    save_account = int(input("请输入您的账号："))
    if save_account in bank:
        save_password = input("请输入您的密码：")
        # 判断密码是否正确
        if save_password == bank[save_account]["password"]:
            save_money = int(input("请输入存入的金额："))
            bank[save_account]["money"] += save_money
            print("您的余额为：", bank[save_account]["money"])
        else:
            print("密码错误！")
    else:
        print("该账户不存在！")

# 5.取钱
def getMoney():
    get_account = input("请输入您的账号：")
    get_account = int(get_account)
    if get_account in bank:
        get_password = input("请输入您的密码：")
        if get_password == bank[get_account]["password"]:
            get_money = int(input("请输入您要取出的金额："))
            bank[get_account]["money"] = int(bank[get_account]["money"])
            if get_money <= bank[get_account]["money"]:
                bank[get_account]["money"] -= get_money
                print("成功取款%s元" % get_money)
                print("您的余额为：",bank[get_account]["money"])
            else:
                Return(3)
        else:
            Return(2)
    else:
        Return(1)

#返回值
def Return(num):
    if num == 1:
        print("您输入的账号不存在！")
    elif num == 2:
        print("您输入的密码错误!")
    elif num == 3:
        print("您的钱不够!")

# 6.转账
def transferMoney():
    in_account = int(input("请输入转入的账号："))
    out_account = int(input("请输入转出的账号："))
    if in_account == out_account:
        print("转出账号与转入账号不能相同！")
    else:
        if in_account and out_account in bank:
            out_password = input("请输入转出账号的密码：")
            if out_password == bank[out_account]["password"]:
                if bank[out_account]["account_type"] == "【金卡】":
                    print("您的账户最大转账额为5万元！")
                    out_money = int(input("请输入您要转出的金额："))
                    bank[out_account]["money"] = int(bank[out_account]["money"])
                    bank[in_account]["money"] = int(bank[in_account]["money"])
                    if out_money <= 50000:
                        if out_money <= bank[out_account]["money"]:
                            bank[out_account]["money"] -= out_money
                            bank[in_account]["money"] += out_money
                            print("转账成功！")
                            print("转出金额%s元,转出账户的余额为%s元！" % (out_money, bank[out_account]["money"]))
                            print("转入金额%s元,转入账户的余额为%s元！" % (out_money, bank[in_account]["money"]))
                        else:
                            Return(3)
                    else:
                        print("转账金额超出限制！")
                elif bank[out_account]["account_type"] == "【普通卡】":
                    print("您的账户最大转账额为2万元！")
                    out_money = int(input("请输入您要转出的金额："))
                    bank[out_account]["money"] = int(bank[out_account]["money"])
                    bank[in_account]["money"] = int(bank[in_account]["money"])
                    if out_money <= 20000:
                        if out_money <= bank[out_account]["money"]:
                            bank[out_account]["money"] -= out_money
                            bank[in_account]["money"] += out_money
                            print("转账成功！")
                            print("转出金额%s元,转出账户的余额为%s元！" % (out_money, bank[out_account]["money"]))
                            print("转入金额%s元,转入账户的余额为%s元！" % (out_money, bank[in_account]["money"]))
                        else:
                            Return(3)
                    else:
                        print("转账金额超出限制！")
            else:
                Return(2)
        else:
            Return(1)


# 7.查询
def select():
    select_account = input("请输入账号：")
    select_account = int(select_account)
    if select_account in bank:
        select_password = input("请输入密码：")
        if select_password == bank[select_account]["password"]:
            info = '''
                    ------------个人信息------------
                    账号：%s
                    用户名:%s
                    密码：%s
                    账户类型：%s
                    地址：%s%s%s%s
                    余额：%s
                    开户行名称：%s
                    --------------------------------
                    '''
            print(info % (select_account,
                          bank[select_account]['username'],
                          bank[select_account]['password'],
                          bank[select_account]['account_type'],
                          bank[select_account]['country'],
                          bank[select_account]['province'],
                          bank[select_account]['street'],
                          bank[select_account]['door'],
                          bank[select_account]["money"],
                          bank[select_account]['bank_name']))

        else:
            print("密码错误!")
    else:
        print("账号不存在！")


# 添加死循环，让程序入口重复显示
while True:
    welcome()
    # 获取用户的输入选择,根据用户的输入选择进行判断
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoney()
    elif chose == "3":
        getMoney()
    elif chose == "4":
        transferMoney()
    elif chose == "5":
        select()
    elif chose == "6":
        print("Bye! 欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
