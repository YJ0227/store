'''
随机生成一个处罚遍数
有一个列表里面有人名
优化代码：一个输入进行判断，判断为1 开始选人，判断为2开始生成数字  判断为q Q，退出
'''
import random
list=["陆梓言","郭洪波","方则属","签","千纸鹤","EXO"]
print("============欢迎来到处罚系统===============")
while 1==1:
    index = input("请输入您的选择[1.选人  2.处罚遍数  q/Q:退出系统]：")
    if index == "1":
        ran = random.randint(0, len(list)-1)#len==6  范围是0-6全部可以取到
        print("选择的人是：", list[ran])
    elif index == "2":
        num = random.randint(0, 90)
        print("处罚", num, "遍")
    elif index == "q" or index == "Q":
        print("退出系统！")
        break
    else:
        print("输入错误！ 请核对后重新输入！")


