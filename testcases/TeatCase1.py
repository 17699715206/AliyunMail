import unittest
from ddt import ddt,file_data,unpack
from pages.login import loginPageFun
from common.BrowserInit import browser
import time
from common.logginginit import logger




@ddt()
class TestCase_login1(unittest.TestCase):

    # FAILURE_REPEAT_RUN_FLAG = True

    def setUp(self) -> None:
        browser.get("https://mail.aliyun.com")
        time.sleep(3)

    @file_data(r"D:\Desktop\202006\AliyunMail\config\data.yaml")
    @unpack
    def testLoginmail_correct(self, **kwargs):
        try:
            loginPageFun().denglu(kwargs["data"]["user"], kwargs["data"]["pasw"])
            self.assertEqual(browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[3]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span"), "收件箱")
        except:
            logger.info("用例执行失败~~~~~~~~~~~~"+"TestData:"+kwargs["data"]["user"]+","+kwargs["data"]["pasw"])


    def tearDown(self) -> None:
        browser.delete_all_cookies()






if __name__ == '__main__':
    unittest.main()