import unittest

from BeautifulReport import BeautifulReport
from testcases.TeatCase1 import TestCase_login1
from testcases.TeatCase2 import TestCase_login2
from common.HTMLTestRunner import HTMLTestRunner


class runner():

    # 构造测试套件
    def selecttestcase(self):
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase_login1))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase_login2))

        # 使用BeautifulReport输出html测试报告
        # BeautifulReport_runner = BeautifulReport(suite)
        # BeautifulReport_runner.report(filename="阿里邮箱UI自动化测试报告(BeautifulReport)",description="阿里邮箱自动化登录测试", report_dir=r'.\report', theme='theme_default')


        # 使用HTMLTestRunner输出HTMl测试报告   
        with open(r".\report\阿里邮箱UI自动化测试报告(HTMLTestRunner).html", 'wb') as fp:
            HTMLTestRunner_runner = HTMLTestRunner(stream=fp, title='阿里邮箱自动化登录测试', description='测试用例', verbosity=2)
            HTMLTestRunner_runner.run(suite)
            fp.close()
                




if __name__ == '__main__':
    # 运行测试套件
    runner().selecttestcase()
