'''
    测试用例
'''
from Calc import Calc
from unittest import TestCase

class TestCalc(TestCase):
    # 加法测试
    def testAdd1(self):
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    def testAdd2(self):
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    def testAdd3(self):
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    def testAdd4(self):
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(s,sum)

    # 减法测试
    def testMinus1(self):
        a = 6
        b = 5
        c = 1

        calc = Calc()
        sum = calc.minus(a, b)
        self.assertEqual(c, sum)

    def testMinus2(self):
        a = -6
        b = 5
        c = 1

        calc = Calc()
        sum = calc.minus(a, b)
        self.assertEqual(c, sum)

    # 乘法测试
    def testMulti1(self):
        a = 3
        b = 3
        c = 9

        calc = Calc()
        sum = calc.multi(a, b)
        self.assertEqual(c, sum)

    def testMulti12(self):
        a = -3
        b = 3
        c = 9

        calc = Calc()
        sum = calc.multi(a, b)
        self.assertEqual(c, sum)

    # 除法测试
    def testDevision1(self):
        a = 8
        b = 2
        c = 4

        calc = Calc()
        sum = calc.devision(a, b)
        self.assertEqual(c, sum)

    def testDevision2(self):
        a = -8
        b = 2
        c = 4

        calc = Calc()
        sum = calc.devision(a, b)
        self.assertEqual(c, sum)

