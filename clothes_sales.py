"""
    1.完成衣服销售数据的统计和分析
    1.1计算总销售额
    1.2计算平均每日销售数量
    1.3 计算每个种类月销售量占比

"""
import xlrd

# 打开工作簿
wb = xlrd.open_workbook("12月份衣服销售数据.xlsx", encoding_override=True)
st = wb.sheet_by_index(0)
rows = st.nrows  # 获取行数

# 1.计算销售总额
sum = 0
for i in range(1, rows):
    data1 = st.row_values(i)
    sum += data1[2] * data1[4]
print("12月份衣服销售总额为：%.2f元" % sum)
print("-" * 50)

# 2.计算平均每日销售数量
count = 0
avg = 0
for i in range(1, rows):
    data2 = st.row_values(i)
    count += data2[4]
avg = count/30
print("平均每日销售量为：%d件" % avg)
print("-" * 50)

# 3.计算每个种类月销售量占比
yrf_count = 0
nzk_count = 0
fy_count = 0
pc_count = 0
tx_count = 0
cs_count = 0
for r in range(1, rows):
    data = st.row_values(r)
    if data[1] == "羽绒服":
        yrf_count += data[4]
    elif data[1] == "牛仔裤":
        nzk_count += data[4]
    elif data[1] == "风衣":
        fy_count += data[4]
    elif data[1] == "皮草":
        pc_count += data[4]
    elif data[1] == "T血":
        tx_count += data[4]
    elif data[1] == "衬衫":
        cs_count += data[4]
print("每个种类月销售量占比如下：")
print("羽绒服月销售量占比为：%.2f" % (yrf_count/count))
print("牛仔裤月销售量占比为：%.2f" % (nzk_count/count))
print("风衣月销售量占比为：%.2f" % (fy_count/count))
print("皮草月销售量占比为：%.2f" % (pc_count/count))
print("T血月销售量占比为：%.2f" % (tx_count/count))
print("衬衫月销售量占比为：%.2f" % (cs_count/count))

