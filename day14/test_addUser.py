from 工商银行完整版 import bank_addUser
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook(r'F:\Python学习\day14【参数化测试】\代码\任务\bank.xlsx', encoding_override=True)
r_sheet = rb.sheet_by_index(0)
rows = r_sheet.nrows
da = []
for i in range(1, rows):
    value = r_sheet.row_values(i)
    value.pop()
    da.append(value)

wb = copy(rb)
w_sheet = wb.get_sheet(0)

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testAddUser(self,username,password,country,province,street,door,money,excepted_result):
        result = bank_addUser(username,password,country,province,street,door,money)

        for i in range(1, rows):
            if result == excepted_result:
                w_sheet.write(i, 8, "通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果.xlsx')
            else:
                w_sheet.write(i, 8, "不通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果.xlsx')

        # 断言
        self.assertEqual(result, excepted_result)




















