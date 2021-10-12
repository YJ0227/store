'''
任务一：
    字典判断
'''

# dict = {"地球":{
#     "中国":{
#         "北京":{
#             "昌平区":{
#                 "沙河":["沙阳路", "老牛湾路"], "龙泽":[ "龙泽地铁站", "龙泽公交站"]
#             },
#             "海淀区":{
#                 "公主坟":['军事博物馆','中华世纪园'], "科普场馆":['中国科技馆','北京天文馆']
#             }
#         },
#
#         "上海":{
#             "宝山区":{
#                 "宝杨路":["宝山滨江公园"], "友谊路":["上海淞沪抗战纪念公园"]
#             },
#             "闵行区":{
#                 "东川路":["上海交通大学（闵行校区）"], "浦星公路":["上海浦江郊野公园"]
#             }
#         }
#     }
#   }
# }
#
# def print_place(choice):
#     for i in choice:
#         print('\t\t', i)
#
# for a in dict:
#     print(a)
#
# while True:
#         name = input("请输入地点名称：")
#         if name == 'q':
#             break
#         if name in dict:
#             print_place(dict[name])
#             country = input("请输入国家名称：")
#             if country == 'q':
#                 break
#             if country in dict[name]:
#                 print_place(dict[name][country])
#                 city = input("请输入城市名称：")
#                 if city == 'q':
#                     break
#                 if city in dict[name][country]:
#                     print_place(dict[name][country][city])
#                     area = input("请输入地区名称：")
#                     if area in dict[name][country][city]:
#                         print_place(dict[name][country][city][area])
#                         place = input("请输入详细地点：")
#                         if place in dict[name][country][city][area]:
#                             print_place(dict[name][country][city][area][place])


'''
任务二：
    有下列人员数据库，请按要求实现
    # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
    names = [
        ["曹操","56","男","106","IBM", 500 ,"50"],
        ["大乔","19","女","230","微软", 501 ,"60"],
        ["小乔", "19", "女", "210", "Oracle", 600, "60"],
        ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
    ]
        1.统计每个人的平均薪资
        2.统计每个人的平均年龄
        3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
        4.统计公司男女人数
        5.每个部门的人数
'''
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# print("-------------------人员信息表-----------------------")
# for a in names:
#     print(a)
# print("----------------------------------------------------")
#
# #  1.统计每个人的平均薪资
# salary_list = []
# for i in names:
#     salary_list.append(i[5])
# avg_salary = sum(salary_list)/len(salary_list)
# print("平均薪资为：%.2f" % avg_salary)
# print("----------------------------------------------------")
#
# # 2.统计每个人的平均年龄
# age_list = []
# for j in names:
#     age_list.append(int(j[1]))
# avg_age = sum(age_list)/len(age_list)
# print("平均年龄为：%.2f" % avg_age)
# print()
#
# # 3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# names.append( ["刘备", "45", "男", "220", "alibaba", 500 , "30"])
# print("-------------------人员信息表-----------------------")
# for b in names:
#     print(b)
# print("----------------------------------------------------")
#
# # 4.统计公司男女人数
# man = 0
# woman = 0
# for k in names:
#     if k[2] == "男":
#         man += 1
#     elif k[2] == "女":
#         woman += 1
# print("男生人数为：", man)
# print("女生人数为：", woman)
# print("----------------------------------------------------")
#
# # 5.每个部门的人数
# person_50, person_60, person_10, person_30 = 0,0,0,0
# for r in names:
#     if r[6] == '50':
#         person_50 +=1
#     elif r[6] == '60':
#         person_60 +=1
#     elif r[6] == '10':
#         person_10 +=1
#     elif r[6] == '30':
#         person_30 +=1
# print("部门编号为10的人数有：", person_10, "人")
# print("部门编号为30的人数有：", person_30, "人")
# print("部门编号为50的人数有：", person_50, "人")
# print("部门编号为60的人数有：", person_60, "人")


'''
任务三：
    现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
    [罗恩, 23 ,35 ,44]
    [哈利 ,60, 77 ,68 ,88, 90]
    [赫敏, 97 ,99 ,89 ,91, 95, 90]
    [马尔福 ,100, 85 ,90]
    求每个人的总成绩？
'''
#
# list1 = ['罗恩', 23 ,35 ,44]
# list2 = ['哈利' ,60, 77 ,68 ,88, 90]
# list3 = ['赫敏', 97 ,99 ,89 ,91, 95, 90]
# list4 = ['马尔福' ,100, 85 ,90]
#
# sum1, sum2, sum3, sum4 = 0,0,0,0
# list1.pop(0)
# for a in list1:
#     sum1 += a
# print("罗恩的总成绩为：", sum1, "分")
#
# list2.pop(0)
# for b in list2:
#     sum2 += b
# print("哈利的总成绩为：", sum2, "分")
#
# list3.pop(0)
# for c in list3:
#     sum3 += c
# print("赫敏的总成绩为：", sum3, "分")
#
# list4.pop(0)
# for d in list4:
#     sum4 += d
# print("马尔福的总成绩为：", sum4, "分")


'''
任务四：
    阅读程序并回答问题
    输入54321，写出执行结果
'''
#
# num = int(input("请输入一个数："))
# while num !=0:
#     print(num % 10)
#     num = num // 10
#
# # 执行结果为：1   2    3    4    5


'''
任务五：
    请对下列列表进行冒泡排序（网易测试开发笔试题）
    a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
'''
#
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# for i in range(1, len(a)):    # i：表示第几轮冒泡
#     for j in range(len(a)-i):   # j：走访到的元素的索引
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print("冒泡排序结果：", a)

