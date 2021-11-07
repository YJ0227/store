from HTMLTestRunner import HTMLTestRunner
import unittest

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"F:\Python学习\day13【单元测试】\代码\任务", pattern="Test*.py")

# 2.创建运行器并执行用例
with open("计算器测试报告.html", "wb") as f:
    HTMLTestRunner(stream=f, verbosity=2, title="计算器测试报告").run(tests)
