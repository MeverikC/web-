import time
from selenium.webdriver.common.by import By
from Pms.src.common.driverCommon import drivercommon
url='http://192.168.2.54:8080/Achievements-admin/login'
class user_login:
    def test_login(self,username,password):
        #获取驱动
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        #定位元素
        self.driver.find_element(By.NAME,'username').clear()
        self.driver.find_element(By.NAME,'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME,'password').send_keys(password)
        self.driver.find_element(By.ID,'btnSubmit').click()
        time.sleep(3)
        sj_url=self.driver.current_url
        print(sj_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index'==sj_url:

            return True
        else:
            return False
    drivercommon().driver.close()
        # sele.driver=drivercommon.quiteDriver()