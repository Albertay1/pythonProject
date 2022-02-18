import unittest2

from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 通过defaultTestLoader方法找到需要执行的测试用例，用例的地址在：./test_casse3下面，以Test.py结尾的所有测试用例；并赋值给测试用例集（suite）
    suite = unittest2.defaultTestLoader.discover("../test_case3", "*Test.py")
    # 执行找到的测试用例：通过文本测试用例运行器去执行找到的suite测试用例集
    # unittest2.TextTestRunner().run(suite)
    # 生成测试报告
    path = "../report/ReportRunner1.html"
    # w是写方法，b是二进制方法；wb就是以二进制的方式写入文件中
    file = open(path, "wb")
    HTMLTestRunner(stream=file, verbosity=1, title="自动化测试", description="Ray").run(suite)
