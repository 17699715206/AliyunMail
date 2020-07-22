from selenium import webdriver
import yaml
from common.logginginit import logger
import time
# 浏览器初始化
class BrowserInit:

    # 先读取配置文件内容
    def __init__(self):
        with open(r'D:\Desktop\202006\AliyunMail\config\config.yaml', 'r', encoding="utf8") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


    # get浏览器名称
    def getBrowserName(self):
        return self.cfg['browser']['name']
    #get浏览器模式
    def getBrowserMode(self):
        return self.cfg['browser']['mode']
    #getie浏览器path
    def getiebrowserpath(self):
        return self.cfg['ie_browser_path']
    # get360浏览器path
    def get360browserpath(self):
        return self.cfg['360_browser_path']
    # getqq浏览器path
    def getqqbrowserpath(self):
        return self.cfg['qq_browser_path']
    # get百度浏览器path
    def getbaidubrowserpath(self):
        return self.cfg['baidu_browser_path']
    # get搜狗浏览器path
    def getsougoubrowserpath(self):
        return self.cfg['sougou_browser_path']
    # getuc浏览器path
    def getucbrowserpath(self):
        return self.cfg['uc_browser_path']
    # getchrome浏览器path
    def getchromebrowserpath(self):
        return self.cfg['chrome_browser_path']
    # getfirefox浏览器path
    def getfirefoxbrowserpath(self):
        return self.cfg['firefox_browser_path']
    # getedge浏览器path
    def getedgebrowserpath(self):
        return self.cfg['edge_browser_path']

    # 浏览器初始化函数
    def browserinit(self):
        if self.getBrowserName() is None:
            logger.info("浏览器类型不能为空")
        if self.getBrowserName() == 'ie':
            browser = webdriver.Ie(executable_path='.\drivers\msedgedriver',)
            return browser
        elif self.getBrowserName() == 'firefox':
            options = webdriver.FirefoxOptions()
            options.binary_location = self.getfirefoxbrowserpath()
            browser = webdriver.Firefox(options=options,executable_path='.\drivers\geckodriver')
            return browser
        elif self.getBrowserName() == 'chrome':
            options = webdriver.ChromeOptions()
            '''谷歌的headless模式'''
            if self.getBrowserMode() == 'headless':
                options.add_argument("headless")
                options.binary_location = self.getchromebrowserpath()
            options.add_argument("start-maximized")
            browser = webdriver.Chrome(options=options, executable_path=r'D:\Desktop\202006\AliyunMail\drivers\chromedriver.exe', service_log_path=r'D:\Desktop\202006\AliyunMail\logs\geckodriver.log')
            return browser
        elif self.getBrowserName() == 'edge':
            options = webdriver.ChromeOptions()
            '''谷歌的headless模式'''
            if self.getBrowserMode() == 'headless':
                options.add_argument("headless")
                options.binary_location = self.getedgebrowserpath()
            options.add_argument("start-maximized")
            browser = webdriver.Chrome(options=options, executable_path='.\drivers\chromedriver')
            return browser
        else:
            logger.info("暂无支持%s浏览器类型", self.getBrowserName())



browser = BrowserInit().browserinit()


# if __name__ =="__main__":
#     bor = BrowserInit().browserinit()
#     bor.get("https://baidu.com")
#     time.sleep(3)
#     bor.quit()
