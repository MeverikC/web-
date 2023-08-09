from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class drivercommon():
    #加载驱动的方法
    def getDriver(self,url):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        return self.driver
    #关闭
    def quiteDriver(self):
        return self.driver.quit()