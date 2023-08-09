from Pms.src.common.driverCommon import drivercommon
import time
from selenium.webdriver.common.by import By
# from selenium import webdriver
# from login import user_login
url='http://192.168.2.54:8080/Achievements-admin/login'

class roles_add:

    def roles_add_test(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,'//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH,'//*[@id="btnSubmit"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]').click()
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()
        time.sleep(2)
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'//*[@id="roleName"]').send_keys('123456')
        self.driver.find_element(By.XPATH,'//*[@id="roleKey"]').send_keys(99999)
        self.driver.find_element(By.XPATH,'//*[@id="roleSort"]').send_keys(15)
        self.driver.find_element(By.XPATH,'//*[@id="menuTrees_90_check"]').click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]').click()
        time.sleep(1)
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()