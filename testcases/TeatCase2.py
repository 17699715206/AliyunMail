import unittest
from ddt import ddt,file_data,unpack
from pages.login import loginPageFun
from common.BrowserInit import browser
import time
from common.logginginit import logger




@ddt()
class TestCase_login2(unittest.TestCase):

    # FAILURE_REPEAT_RUN_FLAG = True

    def setUp(self) -> None:
        browser.get("https://mail.aliyun.com")
        time.sleep(3)


    @file_data(r"D:\Desktop\202006\AliyunMail\config\data.yaml")
    @unpack
    def testLoginmail_wrong(self, **kwargs):
        try:
            loginPageFun().denglu(kwargs["wrongdata"]["user"], kwargs["wrongdata"]["pasw"])
            self.assertEqual(browser.find_element_by_class_name("notice-descript").text, "登录名或登录密码不正确")
        except:
            logger.info("用例执行失败~~~~~~~~~~~~" + "TestData:" + kwargs["wrongdata"]["user"] + "," + kwargs["wrongdata"]["pasw"])


    def tearDown(self) -> None:
        browser.quit()


if __name__ == '__main__':
    unittest.main()