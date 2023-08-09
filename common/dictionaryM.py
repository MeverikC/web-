from Pms.src.common.driverCommon import drivercommon
from selenium.webdriver.common.by import By
from time import sleep
url='http://192.168.2.54:8080/Achievements-admin/login'
class dictionaryM:
    def test_dictionaryM(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[5]/a').click()
        sleep(2)
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'//*[@id="dictName"]').send_keys('king')
        self.driver.find_element(By.XPATH,'//*[@id="dictType"]').send_keys('asjbc')
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]').click()
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()