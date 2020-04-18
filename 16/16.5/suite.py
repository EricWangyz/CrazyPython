import unittest

from test_fk_math import TestFKMath
from tet_hello import TestHello

test_cases = (TestHello, TestFKMath)


def whole_suite():
	# 创建测试加载器
	loader = unittest.TestLoader()
	# 创建测试包
	suite = unittest.TestSuite()
	# 遍历所有的测试类
	for test_class in test_cases:
		# 从测试类中加载测试用例
		tests = loader.loadTestFromTestCase(test_class)
		# 将测试用例添加到测试包中
		suite.addTests(tests)
	return suite


if __name__ == '__main__':
	# 创建测试运行器TestRunner
	with open ('fk_test_report.txt','a') as f:
		# 创建测试运行器，将测试报告输出到文件中
		runner = unittest.TextTestRunner(verbosity=2, stream = f)
		runner.run(whole_suite())
