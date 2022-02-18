import unittest2

from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 找到所有需要执行的测试用例
    suite = unittest2.defaultTestLoader.discover("./test_case/", "*Test.py")
    # 执行找到的测试用例集
    # unittest2.TextTestRunner().run(suite)
    # 使用HTMLTestRunner打印测试报告
    path = "report/ReportRunner.html"
    # 使用写（w）的方式打开文件，并且使用二进制（b）的方式进行写入
    file = open(path, "wb")
    HTMLTestRunner(stream=file, verbosity=1, title="测试内容：注册和登录验证", description="Ray").run(suite)
