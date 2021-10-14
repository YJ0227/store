'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
任务：优惠券加上随机获得一张优惠券（9折10，5折3，免费的1：单个商品打折9折10，5折3，免费的1）
'''
import random

# 准备商品
shop=[
    ["戴尔",19999],
    ["电磁炉",199],
    ["A4纸",9.9],
    ["华为P50 4G",5000],
    ["劳力士手表", 200000],
    ["Iphone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["Mac PC", 15000],
    ["卫龙辣条", 2.5],
    ["老干妈", 13]
]

# 初始化余额
money = input("请输入您的余额：")
money = int(money)

# 准备一个购物车
mycart = []

# 正常购买
def buy():
    global chose, money
    if money < shop[chose][1]:
        print("gun！")
    else:
        mycart.append(shop[chose])
        money = money - shop[chose][1]
        print("恭喜，成功添加购物车!您的余额为：￥%.2f" % money)

# 优惠券购买
def you_buy(zhe):
    global chose, money
    # 金钱是否足够
    zmoney = shop[chose][1] * zhe
    if money > zmoney:
        mycart.append(shop[chose])
        money = money - zmoney
        print("恭喜，成功添加购物车!优惠券已使用！您的余额为：￥%.2f" % money)
    else:
        print("gun！")

# 打印购物小条
def shoping_list():
    global mycart
    mylist = []
    for i in mycart:
        if i not in mylist:
            mylist.append(i)
        else:
            i[2] = i[2] + 1
    print("以下是您的购物小条，请拿好：")
    print("--------------Frank的商城------------------")
    for key, value in enumerate(mylist):
        print(key, value)
    print("您的钱包余额还剩：￥%.2f" % money)
    print("-------------------------------------------")
    print("欢迎下次光临！")

while True:
#展示商品
    for index,value in enumerate(shop):
        print(index,":",value)
    # 抽优惠券
    print("欢迎光临!请抽取您的优惠券，购买结算时享受折扣优惠！")
    youhui = input("输入Y即可抽取您的优惠券！,输入其他则不抽取优惠！")
    if youhui == "Y":
        num = random.randint(1, 28)
        if 0 < num <= 10:
            print("恭喜您获得通用9折优惠券，任意商品均可享受9折优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品！")
                else:
                    you_buy(0.9)
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！")
        elif 10 < num <= 13:
            print("恭喜您获得通用5折优惠券，任意商品均可享受5折优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品！")
                else:
                    you_buy(0.5)
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！")
        elif 13 < num <= 14:
            print("恭喜您获得通用免费优惠券，任意商品均可享受免费优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品！")
                else:
                    you_buy(0)
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！")
        elif 14 < num <= 24:
            print("恭喜您获得戴尔9折优惠券，可享受9折优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品!")
                if chose == 0:
                    you_buy(0.9)
                else:
                    buy()   # 正常购买
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！")
        elif 24 < num <= 27:
            print("恭喜您获得电磁炉优惠券，可享受5折优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品！")
                if chose == 1:
                    you_buy(0.5)
                else:
                    buy()  # 正常购买
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！别瞎弄！")
        else:
            print("恭喜您获得劳力士手表免费优惠券，可享受免费优惠！")
            chose = input("请输入商品编号：")
            if chose.isdigit():  # "5" --> 5     isdigit检测字符串是否只由数字组成
                chose = int(chose)
                if chose > len(shop):
                    print("这里没有您需要的商品！")
                if chose == 4:
                    you_buy(0)
                else:
                    buy()  # 正常购买
            elif chose == 'q' or chose == 'Q':
                shoping_list()
                break
            else:
                print("对不起，输入非法，请重新输入！")
    else:
        chose = input("请输入商品编号：")
        if chose.isdigit():  # "5" --> 5     isdigit检测字符串是否只由数字组成
            chose = int(chose)
            if chose > len(shop):
                print("这里没有您需要的商品！")
            else:
                buy()
        elif chose == 'q' or chose == 'Q':
            shoping_list()
            break
        else:
            print("对不起，输入非法，请重新输入！")
