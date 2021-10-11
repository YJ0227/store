'''
任务1：惩罚系统代码优化
    随机生成一个处罚遍数
    有一个列表里面有人名
    优化代码：一个输入进行判断，判断为1 开始选人，判断为2开始生成数字  判断为q Q，退出
'''
# import random
# list=["陆梓言","郭洪波","方则属","签","千纸鹤","EXO"]
# print("============欢迎来到处罚系统===============")
# while 1==1:
#     index = input("请输入您的选择[1.选人  2.处罚遍数  q/Q:退出系统]：")
#     if index == "1":
#         ran = random.randint(0, len(list)-1)#len==6  范围是0-6全部可以取到
#         print("选择的人是：", list[ran])
#     elif index == "2":
#         num = random.randint(0, 90)
#         print("处罚", num, "遍")
#     elif index == "q" or index == "Q":
#         print("退出系统！")
#         break
#     else:
#         print("输入错误！ 请核对后重新输入！")



# '''
# 任务2：
#     1、实现输入10个数字，并打印10个数的求和结果
#     2、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# '''
# # 输入10个数字
# list = []   # 存放输入的10个数
# i = 1
# while i <= 10:
#     num = float(input("请输入第%s个数字：" % i))
#     list.append(num)
#     i += 1
# # 打印10个数的和
# print("输入的10个数字的和为：%.2f" % sum(list))
#
# # 打印最大的数
# m = list[0]
# for j in list:
#     if j > m:
#         m = j
# print("最大值为：", m)
#
# # 打印平均数
# avg = sum(list)/len(list)
# print("平均数为：", avg)



# '''
# 任务3：
#     使用random模块，如何产生 50~150之间的数？
# '''
# import random
# num = random.randint(50, 150)
# print(num)



# '''
# 任务4：
#     从键盘输入任意三边，判断是否能形成三角形
#     若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# '''
# a = float(input("请输入a边的边长："))
# b = float(input("请输入b边的边长："))
# c = float(input("请输入c边的边长："))
# if a>0 and b>0 and c>0:
#     if a+b>c and a+c>b and b+c>a:
#         if a==b and b==c:
#             print("构成等边三角形")
#         elif a==b or a==c or b==c:
#             print("构成等腰三角形")
#         elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
#             print("构成直角三角形")
#         else:
#             print("构成普通三角形")
#     else:
#         print("无法构成三角形！")
# else:
#     print("请输入大于0的数字！")



# '''
# 任务5：
#     有以下两个数，使用+，-号实现两个数的调换。
#     A=56
#     B=78
#     实现效果：
#     A=78
#     B=56
# '''
# A = 56
# B = 78
#
# A = A+B
# B = A-B
# A = A-B
#
# print("A=", A)
# print("B=", B)



# '''
# 任务6：
#     实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# '''
# while True:
#     username = input("请输入用户名：")
#     if username == "root":
#         password = input("请输入密码：")
#         if password == "admin":
#             print("登录成功！")
#             break
#         else:
#             for i in range(1, 3):
#                 print("密码输入错误！请核对后重新输入！")
#                 password = input("请输入密码：")
#             print("输入密码错误超过3次，账号已被锁定！")
#             break
#     else:
#         print("用户名输入错误！请核对后重新输入！")



# '''
# 任务7：
#     编程实现下列图形的打印：
#            *
#           * *
#          * * *
#         * * * *
#        * * * * *
#       * * * * * *
#      * * * * * * *
# '''
# for i in range(7):
#     print(" " * (7-i), end=" ")
#     print("* " * (i+1))



# '''
# 任务8：
#     1.使用while循环实现99乘法表的打印。
#     2.编程实现99乘法表的倒叙打印
# '''
# # 99乘法表打印
# i = 1
# while i < 10:
#     j = 1
#     while j < i+1:
#         print("%d*%d=%d" % (j, i, (j*i)), end=' ')
#         j += 1
#     print()
#     i += 1
# print("-"*60)
#
# # 99乘法表倒序打印
# for m in range(9, 0, -1):
#     for n in range(1, m+1):
#         print("%d*%d=%d" % (n, m, (n*m)), end=' ')
#     print()



# '''
# 任务9：
#     一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# '''
# high = 20
# i = 0
# while True:
#     high -= 3
#     if high < 0:
#         print("青蛙出井花了%s天" % i)
#         break
#     high += 2
#     i += 1
#     if high < 0:
#         print("青蛙出井花了%s天" % i)
#         break



# '''
# 任务10：
#     继续完成上午的猜数字游戏的需求功能。
#     1.添加计数打印功能
#     2.添加次数金币功能和锁定系统功能。
# '''
#
# # 游戏规则说明：
# # 拥有初始金币2000个，每猜一次扣除金币200个，猜对奖励金币1000个,金币不足200将不能继续游戏
# # 一次游戏只有5次猜数机会，超过5次则猜数失败，系统将会锁定10秒，10秒后可选择是否继续游戏
#
# import random
# import time
#
# count = 0  # 记录所猜次数
# money = 2000
# def num_game():
#     global count, money
#     # 让系统产生一个10-90的随机数
#     data = random.randint(10, 90)
#     print(data)
#     while True:
#         count = count + 1
#         if money >= 200:
#             if count <= 3:
#                 num = int(input("请输入您要猜的数字："))
#                 if num > data:
#                     money = money - 200
#                     print("大了！")
#                     print("剩余金币为：%s个" % money)
#                 elif num < data:
#                     money = money - 200
#                     print("小了！")
#                     print("剩余金币为：%s个" % money)
#                 elif num == data:
#                     money = money - 200 + 1000
#                     print("恭喜，猜中了！ 本次幸运数字为：%s，本次猜了%s次！" % (data, count))
#                     print("恭喜获得1000金币奖励！剩余金币为：%s个" % money)
#                     break  # 终止循环
#             else:
#                 print("只有%s次猜数机会，本次猜数失败！" % (count-1))
#                 print("系统锁定10秒钟，10秒后可选择是否继续猜数游戏！")
#                 time.sleep(10)
#                 count = 0
#                 print("-" * 60)
#                 print("您是否要继续游戏？ [1.是    0.否]")
#                 op = input("请输入您的选择：")
#                 if op == "1":
#                     num_game()
#                 elif op == "0":
#                     print("游戏结束！欢迎下次再来！")
#                 else:
#                     print("输入错误，请核对后重新输入！")
#                 break  # 终止循环
#         else:
#             print("金币不足！游戏结束！")
#             break
#
# num_game()



# '''
# 任务11：
#     用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# '''
# num = 1
# sum = 0
# for i in range(1, 21):
#     num *= i
#     sum += num
# print("阶乘之和为：%s" % sum)













