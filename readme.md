## 本项目为阿里邮箱个人版WEB端UI自动化测试模板

## 环境安装
1. 开发语言：Python
2. UI自动化测试框架：selenium
3. 用例组织框架：unittest
4. 数据驱动：ddt
5. 日志模块：logging
6. 测试报告HTMLTestRunner&BeautifulReport



## 项目结构

### common
1. 浏览器初始化(全局Browser配置)
2. logging初始化(全局logger配置)
### config
1. 测试数据.yaml
2. logging配置.yaml
3. 项目配置,Browser配置.yaml
### drivers
1. UI自动化浏览器驱动，如：Chrome，Firefox，Edge
### logs
1. 存储logger日志文件
2. 存储selenium日志文件
### pages
自动化页面对象管理(po模式)
### reports
1.存放UI可视化html测试报告(HTMLTestRunner,BeautifulReport)
### teatcases
存放测试用例
### main.py
执行UI自动化测试用例入口
