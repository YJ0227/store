import xlrd
import pymysql

wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx', encoding_override='utf-8')

db = pymysql.connect(host='localhost', user='root', password='root', database='clothes', charset='utf8')
cursor = db.cursor()

sheet_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

for st in range(12):
    print("st:",st)
    sheet = wb.sheet_by_index(st)
    nrow = sheet.nrows
    nclo = sheet.ncols

    for i in range(1, nrow):
        list = []
        for j in range(0, nclo):
            data = sheet.cell_value(i, j)
            list.append(data)
        print(list)
        sql = 'insert  into '+sheet_names[st]+' values (%s,%s,%s,%s,%s)'
        cursor.execute(sql, list)
        db.commit()
cursor.close()
db.close()
