'''
统计：
    全年的销售总额
    每件衣服的销售（件数）占比
    每件衣服的月销售占比
    每件衣服的销售额占比
    最畅销的衣服是那种
    每个季度最畅销的衣服
    全年销量最低的衣服
'''
import xlrd

# 打开工作簿
wb = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)

# 存储每个月每种衣服的月销售量和月销售额
data = {}
for i in range(12):
    st = wb.sheet_by_index(i)
    nrows = st.nrows
    data.update({i+1:{}})
    for j in range(1, nrows):
        value = st.row_values(j)
        if value[1] in data[i+1]:
            data[i+1][value[1]] = {
                "money":round(data[i+1][value[1]]["money"] + value[2] * value[4],2),
                "count":int(data[i+1][value[1]]["count"] + value[4])
            }
        else:
            data[i+1][value[1]] = {
                "money":round(value[2] * value[4],2),
                "count":int(value[4])
            }

# 统计全年总销售额、总销售量
sum_money, sum_count = 0, 0
for a in data:
    for b in data[a]:
        sum_money += data[a][b]["money"]        # 总销售额
        sum_count += data[a][b]["count"]      # 总销售量
print("全年的销售总额：￥", round(sum_money, 2))
print("-"*50)

# 每种衣服的月销售量占比、月销售额占比
for c in data:
    for d in data[c]:
        mon_count = round(data[c][d]["count"]/sum_count * 100,2)
        mon_money = round(data[c][d]["money"] / sum_money * 100, 2)
        print(d,"的",c,"月销售量占比为：", mon_count, "%")
        print(d, "的",c,"月销售额占比为：", mon_money, "%")
        print()
    print("-"*50)

# 每种衣服的年销售量占比、年销售额占比
# 存储每种衣服的年销售量、销售额
year_data = {}
for i in range(12):
    st = wb.sheet_by_index(i)
    nrows = st.nrows
    for j in range(1, nrows):
        value = st.row_values(j)
        if value[1] in year_data:
            year_data[value[1]] = {
                "year_money":round(year_data[value[1]]["year_money"] + value[2] * value[4],2),
                "year_count":int(year_data[value[1]]["year_count"] + value[4])
            }
        else:
            year_data[value[1]] = {
                "year_money":round(value[2] * value[4],2),
                "year_count":int(value[4])
            }

# 每种衣服的销售量占比
for clothes in year_data:
    print(clothes, "的年销售量占比为：", round(year_data[clothes]["year_count"]/sum_count * 100,2),"%")
    print(clothes, "的年销售额占比为：", round(year_data[clothes]["year_money"] / sum_money * 100,2),"%")
    print()
print("-"*50)

# 全年最畅销的衣服
count={}
for i in year_data:
    count.update({i: year_data[i]["year_count"]})
max_count = max(count, key=count.get)
print("全年最畅销的衣服为：",max_count)
print("-"*50)

# 全年销量最低的衣服
max_count = min(count, key=count.get)
print("全年销量最低的衣服为：",max_count)
print("-"*50)

# 每个季度最畅销的衣服
season_clothes = {"春季":{},"夏季":{},"秋季":{},"冬季":{}}
def season(month, season):
    for i in data:
        if i in month:
            for j in data[i]:
                if j in season_clothes[season]:
                    season_clothes[season][j] = {
                        "season_count": int(season_clothes[season][j]["season_count"] + data[i][j]["count"])
                    }
                else:
                    season_clothes[season][j] = {
                        "season_count": int(data[i][j]["count"])
                    }


season((11, 0, 1), "春季")
season((2, 3, 4), "夏季")
season((5, 6, 7), "秋季")
season((8, 9, 10), "冬季")

def season_max(season):
    count = {}
    for i in season_clothes:
        if i == season:
            for j in season_clothes[i]:
                count.update({j:season_clothes[i][j]["season_count"]})
    count_max = max(count, key=count.get)
    print("%s最畅销的衣服为：%s" % (season, count_max))

season_max("春季")
season_max("夏季")
season_max("秋季")
season_max("冬季")