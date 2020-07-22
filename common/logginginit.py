import yaml
import logging.config

# 工具类
# 读取logging配置文件
# 配置全局logger
class readlogConf:
    logingCongifPath = r"D:\Desktop\202006\AliyunMail\config\loggingconf.yaml"

    def __init__(self):
        with open(self.logingCongifPath, encoding="utf8") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    def loginit(self):
        #print(self.cfg)
        logging.config.dictConfig(self.cfg)
        logger = logging.getLogger(__name__)
        return logger

logger = readlogConf().loginit()

# if __name__ == "__main__":
#     logger = readlogConf().loginit()
#     logger.info("aaaa")