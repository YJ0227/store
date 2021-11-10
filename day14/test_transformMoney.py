from 工商银行完整版 import bank_transformMoney
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook(r'F:\Python学习\day14【参数化测试】\代码\任务\bank.xlsx', encoding_override=True)
r_sheet = rb.sheet_by_index(4)
rows = r_sheet.nrows
da = []
for i in range(1, rows):
    value = r_sheet.row_values(i)
    value.pop()
    da.append(value)

wb = copy(rb)
w_sheet = wb.get_sheet(4)

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testTransformMoney(self,outputaccount,inputaccount,outputpassword,outputmoney,excepted_result):
        result = bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney)
        r = str(result)
        for i in range(1, rows):
            if r == excepted_result:
                w_sheet.write(i, 5, "通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果5.xlsx')
            else:
                w_sheet.write(i, 5, "不通过")
                wb.save(r'F:\Python学习\day14【参数化测试】\代码\任务\测试结果5.xlsx')

        # 断言
        self.assertEqual(r, excepted_result)



