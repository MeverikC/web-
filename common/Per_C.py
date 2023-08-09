from Pms.src.common.driverCommon import drivercommon
from selenium.webdriver.common.by import By
import time

url='http://192.168.2.54:8080/Achievements-admin/login'
class Per_C:
    def test_Per_C(self):
        self.driver=drivercommon().getDriver(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[1]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//*[@id="signupForm"]/input[2]').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[1]/div/a/div[2]/img').click()
        time.sleep(2)
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.XPATH,'/html/body/section/div/div[1]/div/div[2]/div/p[2]/a').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        time.sleep(2)
        # print(os.getcwd())
        self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div/input').send_keys(r'C:\Users\YM1231\PycharmProjects\pythonProject\Pms\src\pictures\cat.jpg')
        self.driver.switch_to.default_content()
        time.sleep(2)
        #self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT,'关闭').click()
        now_url = self.driver.current_url
        print(now_url)
        if 'http://192.168.2.54:8080/Achievements-admin/index' == now_url:
            return True
        else:
            return False

    drivercommon().driver.close()