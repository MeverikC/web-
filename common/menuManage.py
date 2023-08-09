from Pms.src.common.driverCommon import drivercommon
from selenium.webdriver.common.by import By
import time
url='http://192.168.2.54:8080/Achievements-admin/longin'
class menuManage:
    def test_menuManage(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[3]/a').click()
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.XPATH,'//*[@id="form-menu-add"]/div[2]/div/label[1]').click()
        self.driver.find_element(By.XPATH,'//*[@id="menuName"]').send_keys('menu')
        self.driver.find_element(By.XPATH, '//*[@id="form-menu-add"]/div[7]/div/input').send_keys(7)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[2]').click()
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()