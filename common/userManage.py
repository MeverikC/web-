from selenium.webdriver.common.by import By
from Pms.src.common.driverCommon import drivercommon
import time
url='http://192.168.2.54:8080/Achievements-admin/login'

class userManage:
    def test_Manage(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'//*[@id="form-user-add"]/div[1]/div[1]/div/div/input').send_keys('king')
        self.driver.find_element(By.XPATH,'//*[@id="loginName"]').send_keys('king6')
        self.driver.find_element(By.XPATH,'//*[@id="form-user-add"]/div[7]/div/div/div/textarea').send_keys('------')
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/button[2]').click()
        self.driver.switch_to.default_content()
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()