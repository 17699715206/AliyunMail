from common.BrowserInit import browser
from selenium.webdriver import ActionChains
from common.logginginit import logger
import unittest
import time

# 登录函数
class loginPageFun:

    def getusername(self):
        username = browser.find_element_by_id("fm-login-id")
        return username
    def getpassword(self):
        password = browser.find_element_by_id("fm-login-password")
        return password
    def getloginbutton(self):
        loginbutton = browser.find_element_by_id("fm-login-submit")
        return loginbutton
    def getslide(self):
        slide = browser.find_element_by_id("nc_1_n1z")
        return slide


    def denglu(self, uname, pword):
        #try:
            # 定位到iframe
            iframe = browser.find_element_by_id("alibaba-login-box")
            # 切换到iframe
            browser.switch_to.frame(iframe)
            # 输入账号密码，点击登录按钮
            browser.find_element_by_id("fm-login-id").send_keys(uname)
            browser.find_element_by_id("fm-login-password").send_keys(pword)
            browser.find_element_by_id("fm-login-submit").click()
            time.sleep(3)
            # 滑动验证码
            action = ActionChains(browser)
            source = browser.find_element_by_xpath("//*[@id='nc_1_n1t']/span")  # 需要滑动的元素
            action.click_and_hold(source).perform()  # 鼠标左键按下不放
            # 这里每次移动的位置都一样的话，会被反爬虫机制限制滑不到最后
            action.move_by_offset(33, 0).perform()  # 需要滑动的坐标
            time.sleep(0.1)
            action.move_by_offset(43, 0).perform()
            time.sleep(0.3)
            action.move_by_offset(53, 0).perform()
            time.sleep(0.1)
            action.move_by_offset(103, 0).perform()
            time.sleep(0.2)
            #action.release().perform()  # 释放鼠标
            self.getloginbutton().click() #滑到最后还要再点一次登录
            time.sleep(5)
            # assert (browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[3]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span").text == "收件箱")
        # except:
        #     logger.info("登录失败~~~~~~~~~~~~"+"TestData:"+uname+","+pword)


if __name__ =="__main__":
    browser.get("https://mail.aliyun.com")
    time.sleep(3)
    loginPageFun().denglu("im.wangziyi","qwer1234...")
