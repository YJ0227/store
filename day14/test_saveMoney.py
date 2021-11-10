from 工商银行完整版 import bank_saveMoney
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook(r'F:\Python学习\day14【参数化测试】\代码\任务\bank.xlsx', encoding_override=True)
r_sheet = rb.sheet_by_index(1)
rows = r_sheet.nrows
da = []
for i in range(1, rows):
    value = r_sheet.row_values(i)
    value.pop()
    da.append(value)

wb = copy(rb)
w_sheet = wb.get_sheet(1)

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testSaveMoney(self, ac, money, excepted_result):
        result = bank_saveMoney(ac, money)
        r = str(result)
        for i in range(1, rows):
            if r == excepted_result:
                w_sheet.write(i, 3, "通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果2.xlsx')
            else:
                w_sheet.write(i, 3, "不通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果2.xlsx')

        # 断言
        self.assertEqual(r, excepted_result)



