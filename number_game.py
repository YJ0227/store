'''
需求：
    10-90这个范围里面
    如果猜大了打印”猜大了“ 猜小了
    最多猜3次 锁屏 time.sleep(10)
'''

import random
import time

# 让系统产生一个10-90的随机数
data = random.randint(10, 90)

count = 0  # 记录所猜次数
while True:
    count = count + 1
    if count <= 3:
        num = int(input("请输入您要猜的数字："))
        if num > data:
            print("大了！")
        elif num < data:
            print("小了！")
        elif num == data:
            print("恭喜，猜中了！本次幸运数字为：", data)
            break  # 终止循环
    else:
        print("猜数超过3次，被锁定了，请10秒后再试！")
        time.sleep(10)
        count = 0



